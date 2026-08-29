import ada_url
from pywhatwgurl import URLSearchParams

__all__ = ["URL"]


class URL(ada_url.URL):
    """``ada_url.URL`` with the accessors the rest of zapros relies on."""

    @property
    def search_params(self) -> URLSearchParams:
        """The query string as URLSearchParams."""
        return URLSearchParams(self.search)

    def to_string(self) -> str:
        return self.href
