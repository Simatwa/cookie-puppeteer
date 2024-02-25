# cookie-puppeteer

Retrieve cookies exported by Export cookie JSON File Puppeteer extension

# Installation

```sh
pip install cookie-puppeteer
```

# Usage

```python
from cookie_puppeteer import Puppeteer

cookies = Puppeteer("/home/smartwa/Downloads/gemini.google.com.cookies.json")

print(cookies.get("AEC"))
# Ae3NU9ORz35qy6ucvgm9D3U161kwUayh0dj*********
```

<details>

<summary>
Console
</summary>

`$ cookie-puppeteer --help` or `$ cpt -h`

```
usage: cookie-puppeteer [-h] [-v] [-k [KEY ...]] [-d [DEFAULT ...]]
                        [-i INDENT] [--whole]
                        PATH

Retrieve cookies exported by Export cookie JSON File Puppeteer extension

positional arguments:
  PATH                  Path to cookie file

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -k [KEY ...], --key [KEY ...]
                        Set cookie value of this key
  -d [DEFAULT ...], --default [DEFAULT ...]
                        Default cookie value incase of None
  -i INDENT, --indent INDENT
                        Stdout all cookies with this indentation - 4
  --whole               Stdout whole cookie contents

```

</details>