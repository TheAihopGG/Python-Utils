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

__doc__ = """
Core module contains base classes for versions module
"""
version_pattern = re.compile(
    "^(?P<major>([0-9]+))[.]{1}(?P<minor>([0-9]+))[.]{1}(?P<patch>([0-9]+))(?P<string_part>([a-zA-Z]*))"
)


class Version:
    """
    Base class for versions

    Args:
        major (int): the first number in version
        minor (int): the second number in version
        patch (int): the third number in version
        string_part (str): a string after numbers in version

    Example:
        >>> v = Version(1, 0, 0, "dev")
        Version(major=1, minor=0, patch=0, string_part="dev")
        >>> # version supports >, >=, <, <=, == operators
    """

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
        """
        Parse string to version

        Args:
            string (str): string

        Returns:
            - Version instance
            - raises InvalidStringToParse if string has invalid format

        String version regular expression contains in version_pattern
        """
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
        """The first number in version"""
        return self.__major

    @property
    def minor(self):
        """The second number in version"""
        return self.__minor

    @property
    def patch(self):
        """The third number in version"""
        return self.__patch

    @property
    def string_part(self):
        """The string part in version"""
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
            raise TypeError(
                f"'==' not supported between instances of '{type(self)}' and '{type(version)}'"
            )

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
            raise TypeError(
                f"'>=' not supported between instances of '{type(self)}' and '{type(version)}'"
            )

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
            raise TypeError(
                f"'>' not supported between instances of '{type(self)}' and '{type(version)}'"
            )

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
            raise TypeError(
                f"'<=' not supported between instances of '{type(self)}' and '{type(version)}'"
            )

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
            raise TypeError(
                f"'<' not supported between instances of '{type(self)}' and '{type(version)}'"
            )

    def __repr__(self):
        return f"{self.__qualname__}(major={self.major}, minor={self.minor}, patch={self.patch}, string_part={self.string_part})"

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}{self.string_part}"

    def to_json(self) -> str:
        """Returns string version"""
        return str(self)


class StringParts:
    """
    Class contains string parts for version, such like "dev", "beta", "demo"...
    """

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
    "version_pattern",
)
