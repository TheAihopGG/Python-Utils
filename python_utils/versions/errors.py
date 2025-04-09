class VersionsError(Exception):
    pass


class InvalidStringToParse(VersionsError):
    pass


__all__ = (
    "VersionsError",
    "InvalidStringToParse",
)
