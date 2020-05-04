from pathlib import Path
from setuptools import setup, find_packages

version = [
    line
    for line in Path("sphinx_panels/__init__.py").read_text().split("\n")
    if "__version__" in line
]
version = version[0].split(" = ")[-1].strip('"')

with open("./README.md", "r") as ff:
    readme_text = ff.read()

setup(
    name="sphinx-panels",
    version=version,
    description="A sphinx extension for creating panels in a grid layout.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Chris Sewell",
    author_email="chrisj_sewell@hotmail.com",
    url="https://github.com/executablebooks/sphinx-panels",
    project_urls={"Documentation": "https://sphinx-panels.readthedocs.io"},
    license="MIT",
    packages=find_packages(),
    package_data={
        "sphinx_panels": ["css/bs-cards.css", "css/bs-grids.css", "css/bs-borders.css"]
    },
    install_requires=["docutils", "sphinx"],
    extras_require={
        "rtd": ["sphinx-rtd-theme"],
        "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
        "testing": ["pytest>=3.6,<4"],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Sphinx :: Extension",
    ],
    keywords="sphinx html bootstrap grid card",
)
