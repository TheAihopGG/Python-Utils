from __future__ import annotations
import re
from typing import (
    SupportsInt,
    Final,
    Any,
)
from .errors import (
    VersionsError,
    InvalidStringToParse,
)


version_pattern = re.compile(
    "^(?P<major>([0-9]+))[.]{1}(?P<minor>([0-9]+))[.]{1}(?P<patch>([0-9]+))(?P<string_part>([a-zA-Z]*))"
)


class Version:
    """docstring for Version."""

    # constructors
    def __init__(
        self,
        major: SupportsInt = 0,
        minor: SupportsInt = 0,
        patch: SupportsInt = 0,
        string_part: str = str(),
    ):
        self.__major = int(major)
        self.__minor = int(minor)
        self.__patch = int(patch)
        self.__string_part = string_part

    @staticmethod
    def from_string(string: str) -> Version:
        if parsed_string := version_pattern.search(string):
            return Version(
                major=int(parsed_string.group("major")),
                minor=int(parsed_string.group("minor")),
                patch=int(parsed_string.group("patch")),
                string_part=parsed_string.group("string_part"),
            )
        else:
            raise InvalidStringToParse(f"failed to parse {string}")

    @property
    def major(self):
        """The major property."""
        return self.__major

    @property
    def minor(self):
        """The minor property."""
        return self.__minor

    @property
    def patch(self):
        """The patch property."""
        return self.__patch

    @property
    def string_part(self):
        """The string_part property."""
        return self.__string_part

    # operator overrides
    def __eq__(self, version: Any | Version) -> bool:
        if isinstance(version, Version):
            return (
                self.major == version.major
                and self.minor == version.minor
                and self.patch == version.patch
            )
        else:
            raise TypeError(f"invalid type {type(version)}")

    def __ge__(self, version: Any | Version) -> bool:
        if isinstance(version, Version):
            return any(
                (
                    self.major >= version.major,
                    self.minor >= version.minor,
                    self.patch >= version.patch,
                )
            )
        else:
            raise TypeError(f"invalid type {type(version)}")

    def __gt__(self, version: Any | Version) -> bool:
        if isinstance(version, Version):
            return any(
                (
                    self.major > version.major,
                    self.minor > version.minor,
                    self.patch > version.patch,
                )
            )
        else:
            raise TypeError(f"invalid type {type(version)}")

    def __le__(self, version: Any | Version) -> bool:
        if isinstance(version, Version):
            return any(
                (
                    self.major <= version.major,
                    self.minor <= version.minor,
                    self.patch <= version.patch,
                )
            )
        else:
            raise TypeError(f"invalid type {type(version)}")

    def __lt__(self, version: Any | Version) -> bool:
        if isinstance(version, Version):
            return any(
                (
                    self.major < version.major,
                    self.minor < version.minor,
                    self.patch < version.patch,
                )
            )
        else:
            raise TypeError(f"invalid type {type(version)}")

    def __repr__(self):
        return f"{self.__qualname__}(major={self.major}, minor={self.minor}, patch={self.patch}, string_part={self.string_part})"

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}{self.string_part}"

    def to_json(self) -> str:
        return str(self)


class StringParts:
    DEV: Final = "dev"
    RELEASE: Final = "release"
    PRERELEASE: Final = "prerelease"
    BETA: Final = "beta"
    DEMO: Final = "demo"
    ALPHA: Final = "alpha"
    BUILD: Final = "build"


__all__ = (
    "Version",
    "StringParts",
    "VersionsError",
    "InvalidStringToParse",
)
