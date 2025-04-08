class Errors:
    class VersionsError(Exception):
        pass

    class InvalidStringToParse(VersionsError):
        pass


__all__ = ("Errors",)
