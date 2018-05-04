class PipeFile():
    '''
    A layer of abstraction between python
    and the 'pipe' file
    '''
    Name = 'pipe'
    
    def write(htmlText):
        f = open(HtmlFile.Name, "w")
        f.write(htmlText)
        f.close()
    
    def append(htmlText):
        f = open(HtmlFile.Name, "a")
        f.write(htmlText)
        f.close()
    
    def clear():
        f = open(HtmlFile.Name, "w")
        f.close()

    def read():
        f = open(HtmlFile.Name, "r")
        return f.read()

# Sample Usage:
#
# PipeFile.write("Dank\n")
# PipeFile.append("Memes")
#