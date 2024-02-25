from pathlib import Path

from setuptools import setup


setup(
    name="cookie-puppeteer",
    version="0.0.1",
    license="MIT",
    author="Smartwa",
    maintainer="Smartwa",
    author_email="simatwacaleb@proton.me",
    description=" Retrieve cookies exported by Export cookie JSON File Puppeteer extension ",
    packages=["cookie_puppeteer"],
    url="https://github.com/Simatwa/cookie-puppeteer",
    project_urls={
        "Bug Report": "https://github.com/Simatwa/cookie-puppeteer/issues/new",
        "Homepage": "https://github.com/Simatwa/cookie-puppeteer",
        "Source Code": "https://github.com/Simatwa/cookie-puppeteer",
        "Issue Tracker": "https://github.com/Simatwa/cookie-puppeteer/issues",
        "Download": "https://github.com/Simatwa/cookie-puppeteer/releases",
        "Documentation": "https://github.com/Simatwa/cookie-puppeteer/blob/main/docs",
    },
    entry_points={
        "console_scripts": [
            "cookie-puppeteer = cookie_puppeteer.console:main",
            "cpt = cookie_puppeteer.console:main",
        ],
    },
    python_requires=">=3.10",
    keywords=[
        "cookies",
        "cookies-puppeteer",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
