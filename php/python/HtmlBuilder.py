from PipeFile import PipeFile
import sys


# Future implementation:
#
# Send in a dict of all input names
# HtmlBuilder will parse the input names from sys.argv[i]
#

s = "<h1>The name you sent was: " + sys.argv[1] + "<br>" + "</h1>This variable is accessible through the python backend (albeit in a very rough implementation).<br>" + "This implementation is held together only by elmers glue and bits of tape, but at least it works.<br>"

PipeFile.write(s)
