from setuptools import setup, find_packages
from os import path
from io import open

def get_readme():
    """
        Get the long description from the README file
        :return:
        """
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        return f.read()


here = path.abspath(path.dirname(__file__))

setup(
    name = "nautapy",
    version = "1.0",
    description = "Librería sencilla para acceder al Portal Nauta",
    long_description = get_readme(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/SamuelDev00/nautapy",
    author = "SamuelDev",
    author_email = "samuel.falconpc@gmail.com",
    license = "GNU General Public License v3",
    platforms=["Unix"],
    classifiers=[
        "Topic :: Internet",
        "License :: OSI Approved :: GNU General Public License v3 or later "
        "(GPLv3+)",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Operating System :: Unix"
    ],
    keywords = "Portal Nauta Librería",
    packages=find_packages(),
    install_requires=["requests~=2.27.1", "beautifulsoup4~=4.10.0"],
)