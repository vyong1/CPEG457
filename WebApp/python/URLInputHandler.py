from PipeFile import PipeFile
import POSTParser
import sys

# Parse the POST and extract the URL
POST = POSTParser.parse()
url = POST['url_input']

# TODO Extract the name of the author

# TODO Enter the author's name into the Aylien-Api

PipeFile.clear()
PipeFile.write(url)