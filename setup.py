"""bum - setup.py"""
import setuptools

try:
    import bum
except (ImportError, SyntaxError):
    print("error: bum requires Python 3.6 or greater.")
    quit(1)


try:
    import pypandoc
    LONG_DESC = pypandoc.convert("README.md", "rst")
except(IOError, ImportError):
    LONG_DESC = open('README.md').read()


VERSION = bum.__version__
DOWNLOAD = "https://github.com/dylanaraps/bum/archive/%s.tar.gz" % VERSION


setuptools.setup(
    name="bum",
    version=VERSION,
    author="Dylan Araps",
    author_email="dylan.araps@gmail.com",
    description="Download and display album art for mopidy-spotify tracks.",
    long_description=LONG_DESC,
    license="MIT",
    url="https://github.com/dylanaraps/bum",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["bum"],
    entry_points={
        "console_scripts": ["bum=bum.__main__:main"]
    },
    python_requires=">=3.6",
    test_suite="tests",
    include_package_data=True
)