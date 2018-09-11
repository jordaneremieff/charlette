from setuptools import find_packages, setup

from charlette.__version__ import __version__

setup(
    name="charlette",
    version=__version__,
    packages=find_packages(),
    install_requires=["Django", "channels", "starlette", "innate"],
    license="MIT License",
    entry_points={"console_scripts": ["charlette = charlette.__main__:innate.cli"]},
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
)
