import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", encoding="utf8") as f:
    readme = f.read()

with io.open("src/index_parser/data.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="index_parser",
    version=version,
    url="https://github.com/ndtfy/index_parser",
    project_urls={
        "Code": "https://gitflic.ru/project/stan/index_parser",
        "Issue tracker": "https://github.com/ndtfy/index_parser/issues",
    },
    license="MIT",
    author="Stan Ovchinnikov",
    author_email="lishnih@gmail.com",
    description="An index parser tool",
    long_description=readme,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    install_requires=[
        "Flask",
    ],
)
