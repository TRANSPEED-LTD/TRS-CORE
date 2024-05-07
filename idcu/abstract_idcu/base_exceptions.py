"""Base exceptions module for `idcu` project."""


class WebHttpException(Exception):
    """
    Base class for web http exceptions.

    Subclasses should provide `status_code` and `default_detail` properties.
    """

    status_code = 500
    default_detail = "A server error occurred."
    default_code = "error"

    def __init__(self, detail: str | None = None, code: str | None = None) -> None:
        self.detail: str = self.default_detail if detail is None else detail
        self.error_code: str = self.default_code if code is None else code

        super().__init__(self.detail, self.error_code)
