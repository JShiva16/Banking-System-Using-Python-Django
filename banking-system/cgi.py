# Minimal shim for stdlib `cgi` to allow running Django management
# This is a temporary compatibility shim used only for local development
# when running under Python versions that may not include the `cgi` module.

from typing import Tuple

class FieldStorage:
    def __init__(self, *args, **kwargs):
        # minimal placeholder; Django only imports this during startup
        pass

def parse_header(value: str) -> Tuple[str, dict]:
    # return the header and empty params
    return value, {}

# Provide commonly looked-up names to avoid AttributeError elsewhere
escape = lambda s: s

__all__ = ["FieldStorage", "parse_header", "escape"]
