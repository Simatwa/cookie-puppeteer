from pathlib import Path
from json import load
from json import dump
from json import dumps
from typing import Any
from typing import NewType
from importlib import metadata

__prog__ = "cookie-puppeteer"
__description__ = (
    " Retrieve cookies exported by Export cookie JSON File Puppeteer extension "
)

try:
    __version__ = metadata.version(__prog__)
except metadata.PackageNotFoundError:
    ___version__ = "0.0.0"

NoneType = NewType("noneType", None)


class CookieFileNotFoundError(FileNotFoundError):
    pass


class CookieValueNotFoundError(KeyError):
    pass


class Puppeteer:

    def __init__(self, path: str):
        """Constructor

        Args:
            path (str): Path to subdomain.domain.cookies.json file.
        """
        self.path: Path = Path(path)
        if not self.path.is_file():
            raise CookieFileNotFoundError(f"{self.path} is not a valid file path")

    def read(self, raw: bool = False, indent: int = 4) -> dict | str:
        """Load cookies from file

        Args:
            raw (bool, optional): Return as str. Defaults to False.
            indent (int, optional): Indentation level (str). Defaults to 4.

        Returns:
            dict|str: Cookies
        """
        with self.path.open() as fh:
            contents = load(fh)
        return dumps(contents, indent=indent) if raw else contents

    def cookies(self, sorted: bool = True) -> dict:
        """Dict cookies
        Args:
            sorted: Format the cookies to dict only. Defaults to True.
        Returns:
            dict: cookies
        """
        cookies = self.read()
        if sorted:
            resp = {}
            for entry in cookies:
                resp[entry["name"]] = entry["value"]
            return resp
        return cookies

    def get(self, key: str, default: Any = NoneType(None)) -> Any:
        """Retrieve just a specific cookie value

        Args:
            key (str): Key
            default (Any): Return this incase not found. Defaults to noneType.

        Returns:
            Any: Corresponding cookie value
        """
        cookie_value = self.cookies().get(key, default)

        if cookie_value == NoneType(None):
            raise CookieValueNotFoundError(f"No cookie value of key '{key}'")

        return cookie_value

    def update(self, key: str, value: Any, indent=4) -> None:
        """Insert new or update existing ones.

        Args:
            key (str): Cookie key.
            value (Any): Cookie value.
            indent (int, optional): Indentation level. Defaults to 4.
        """
        cookies = self.cookies(sorted=False)
        cookies.update({key: value})
        with self.path.open("w") as fh:
            dump(cookies, fh, indent=indent)
