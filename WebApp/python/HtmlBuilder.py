from PipeFile import PipeFile
import sys

def parsePOSTFromPipe():
    '''
    Parses PHP Pipelined POST data into a python dict
    '''
    POST = {}
    # Parse the post string into a dict
    raw = PipeFile.read()
    raw = raw.strip()
    raw = raw.split('\n')

    # Process each kvp
    for kvp in raw:
        i = kvp.find(':')
        key = kvp[0:i]
        val = kvp[i + 1:]
        POST[key] = val

    return POST

POST = parsePOSTFromPipe()
PipeFile.clear()
for k,v in POST.items():
    PipeFile.append(k + " : " + v + "<br>")