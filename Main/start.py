# File: Startup.py
# Author: vyong
# Summary: Call a series of python scripts to start things up
# 
#========================================================
from subprocess import call
SERVER_PORT = "8008"

def startServer():
    call(["php","-S", "localhost:" + SERVER_PORT])

def openChrome():
    call(["chrome", "http://localhost:" + SERVER_PORT])


openChrome()
startServer()
