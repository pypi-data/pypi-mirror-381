import functools
import io
import re
import warnings
from typing import Iterable, Iterator, Optional

import requests
from mcap.reader import McapReader, make_reader
from packaging import version
from packaging.specifiers import SpecifierSet

from owa.core.utils.typing import PathLike

from .. import __version__
from ..decoder import DecoderFactory
from ..types import DecodeArgs
from .mcap_msg import McapMessage


class OWAMcapReader:
    """
    Reader for OWA MCAP files that supports both local file paths and network URLs.

    This class provides functionality to read, parse, and iterate through messages
    in an MCAP file, with support for both local filesystem paths and remote HTTP/HTTPS URLs.
    """

    def __init__(self, file_path: PathLike, *, decode_args: DecodeArgs = {}):
        """
        Initialize an OWA MCAP reader.

        :param file_path: Path to the MCAP file. Can be either:
                          - A local file path (string or Path object)
                          - A network URL (http:// or https:// protocol)
                          e.g., "https://huggingface.co/datasets/.../example.mcap"
        :param decode_args: Dictionary controlling message decoding behavior. Available options:
                           - 'return_dict' (bool, default=False): If True, always decode messages
                             as dictionaries (EasyDict objects) instead of typed OWA message objects.
                             Use this when you want simple dictionary access to message fields.
                           - 'return_dict_on_failure' (bool, default=False): If True, fall back to
                             dictionary decoding when typed decoding fails. Use this for robust
                             reading of files that may contain unknown or malformed message types.

                           Common usage patterns:
                           - {} or {"return_dict": False}: Default typed decoding (recommended)
                           - {"return_dict": True}: Always use dictionary decoding
                           - {"return_dict_on_failure": True}: Typed with fallback (robust)
                           - {"return_dict": True, "return_dict_on_failure": True}: Always dict (redundant)
        """
        self.file_path = file_path

        # Check if the path is a URL or local file
        if isinstance(file_path, str) and (file_path.startswith("http://") or file_path.startswith("https://")):
            # Handle network path (URL)
            response = requests.get(file_path, stream=True)
            response.raise_for_status()  # Raise exception for HTTP errors
            self._file = io.BytesIO(response.content)
            self._is_network_path = True
        else:
            # Handle local file path
            self._file = open(file_path, "rb")
            self._is_network_path = False

        self.reader: McapReader = make_reader(self._file, decoder_factories=[DecoderFactory(decode_args=decode_args)])
        self.decode_args = decode_args  # TODO: merge with decoded_message in McapReader.iter_decoded_messages
        self.__finished = False

        # Check profile of mcap file
        header = self.reader.get_header()
        assert header.profile == "owa", f"MCAP file is not an OWA file (profile={header.profile})"

        # Check version compatibility
        libversion = header.library
        m = re.match(
            r"mcap-owa-support (?P<version>[\d\.]+[a-zA-Z0-9\-]*)\s*;\s*mcap (?P<mcap_version>[\d\.]+[a-zA-Z0-9\-]*)",
            libversion,
        )

        # Use packaging.version instead of semantic_version for PEP 440 compliance
        self._file_version_str = m["version"] if m else "unknown"
        self._mcap_version_str = m["mcap_version"] if m else "unknown"
        current_version = version.Version(__version__)

        # ~=X.Y.Z is equivalent to >=X.Y.Z, ==X.Y.* (allows patch-level changes)
        if m:
            specifier = SpecifierSet(f"~={self._file_version_str}")
            if current_version not in specifier:
                warnings.warn(
                    f"Reader version {__version__} may not be compatible with writer version {self._file_version_str}"
                )

    def finish(self):
        """Close the file and release resources."""
        if not self.__finished:
            self.__finished = True
            self._file.close()

    @functools.cached_property
    def topics(self) -> list[str]:
        """Get a list of topics in the MCAP file."""
        summary = self.reader.get_summary()
        return [channel.topic for channel_id, channel in summary.channels.items()]

    @functools.cached_property
    def message_count(self) -> int:
        """Get the number of messages in the MCAP file."""
        summary = self.reader.get_summary()
        return summary.statistics.message_count

    @functools.cached_property
    def start_time(self) -> int:
        """Get the start time of the MCAP file in nanoseconds."""
        summary = self.reader.get_summary()
        return summary.statistics.message_start_time

    @functools.cached_property
    def end_time(self) -> int:
        """Get the end time of the MCAP file in nanoseconds."""
        summary = self.reader.get_summary()
        return summary.statistics.message_end_time

    @functools.cached_property
    def duration(self) -> int:
        """Get the duration of the MCAP file in nanoseconds."""
        return self.end_time - self.start_time

    @property
    def file_version(self) -> str:
        """Get the mcap-owa-support version that created this file."""
        return self._file_version_str

    @property
    def mcap_version(self) -> str:
        """Get the mcap library version that created this file."""
        return self._mcap_version_str

    @functools.cached_property
    def schemas(self) -> list[str]:
        """Get all schemas in the MCAP file."""
        return [schema.name for schema_id, schema in self.reader.get_summary().schemas.items()]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.finish()

    def iter_messages(
        self,
        topics: Optional[Iterable[str]] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        log_time_order: bool = True,
        reverse: bool = False,
    ) -> Iterator[McapMessage]:
        """Iterates through the messages in an MCAP, returning rich message objects.

        :param topics: if not None, only messages from these topics will be returned.
        :param start_time: an integer nanosecond timestamp. if provided, messages logged before this
            timestamp are not included.
        :param end_time: an integer nanosecond timestamp. if provided, messages logged at or after
            this timestamp are not included.
        :param log_time_order: if True, messages will be yielded in ascending log time order. If
            False, messages will be yielded in the order they appear in the MCAP file.
        :param reverse: if both ``log_time_order`` and ``reverse`` are True, messages will be
            yielded in descending log time order.
        :returns: Iterator yielding McapMessage objects with lazy-evaluated properties
        """
        for schema, channel, message in self.reader.iter_messages(
            topics=topics,
            start_time=start_time,
            end_time=end_time,
            log_time_order=log_time_order,
            reverse=reverse,
        ):
            yield McapMessage.from_mcap_primitives(schema, channel, message, decode_args=self.decode_args)

    def iter_attachments(self):
        yield from self.reader.iter_attachments()

    def iter_metadata(self):
        yield from self.reader.iter_metadata()
