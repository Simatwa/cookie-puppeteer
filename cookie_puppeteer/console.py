import argparse
from cookie_puppeteer import __version__
from cookie_puppeteer import __description__
from cookie_puppeteer import __prog__

from cookie_puppeteer import Puppeteer


def main():
    parser = argparse.ArgumentParser(__prog__, description=__description__)
    parser.add_argument(
        "-v", "--version", action="version", version=f"{__prog__} v{__version__}"
    )
    parser.add_argument("file", help="Path to cookie file", metavar="PATH")
    parser.add_argument("-k", "--key", nargs="*", help="Set cookie value of this key")
    parser.add_argument(
        "-d",
        "--default",
        nargs="*",
        help="Default cookie value incase of None",
    )
    parser.add_argument(
        "-i",
        "--indent",
        help="Stdout all cookies with this indentation - %(default)s",
        default=4,
    )
    parser.add_argument(
        "--whole", action="store_true", help="Stdout whole cookie contents"
    )

    args = parser.parse_args()

    try:
        cookies = Puppeteer(args.file)
        if args.key:
            for index, key in enumerate(args.key):
                print(
                    cookies.get(
                        key,
                        (
                            args.default[index]
                            if args.default and len(args.default) >= index + 1
                            else None
                        ),
                    )
                )
        elif args.whole:
            print(cookies.read(raw=True, indent=args.indent))
        else:
            from json import dumps

            print(dumps(cookies.cookies(), indent=args.indent))
    except Exception as e:
        print("ERROR :", e.args[1] if len(e.args) > 1 else e)
        exit(1)
