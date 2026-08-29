from pywhatwgurl import URLSearchParams

try:
    from ada_url import URL as _BaseURL
except ImportError:
    # Pyodide/Emscripten has no compiled ada-url wheel, so fall back to the
    # pure-Python parser. Both expose the same WHATWG URL interface.
    from pywhatwgurl import URL as _BaseURL

__all__ = ["URL"]


class URL(_BaseURL):
    """``ada_url.URL`` with the accessors the rest of zapros relies on."""

    @property
    def search_params(self) -> URLSearchParams:
        """The query string as URLSearchParams."""
        return URLSearchParams(self.search)

    def to_string(self) -> str:
        return self.href
