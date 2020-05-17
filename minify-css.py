#!/usr/bin/env python
import sys
from pathlib import Path

from csscompressor import compress

folder = Path(__file__).parent.joinpath("sphinx_panels/css")
min_file = folder.joinpath("panels-bootstrap.min.css")
css_string = ""
for path in sorted(folder.glob("bs-*.css")):
    css_string += path.read_text() + "\n"

css_string = compress(css_string).rstrip() + "\n"

if not min_file.exists() or (min_file.read_text() != css_string):
    min_file.write_text(css_string)
    sys.exit(1)

sys.exit(0)
