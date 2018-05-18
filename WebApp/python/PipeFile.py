class PipeFile():
    '''
    A layer of abstraction between python
    and the 'pipe' file
    '''
    Name = 'pipe'
    
    def write(htmlText):
        f = open(PipeFile.Name, "w")
        f.write(htmlText)
        f.close()
    
    def append(htmlText):
        f = open(PipeFile.Name, "a")
        f.write(htmlText)
        f.close()
    
    def clear():
        f = open(PipeFile.Name, "w")
        f.close()

    def read():
        f = open(PipeFile.Name, "r")
        return f.read()

class PipeFile2():
    '''
    A layer of abstraction between python
    and the 'pipe2' file
    '''
    Name = 'pipe2'
    
    def write(htmlText):
        f = open(PipeFile2.Name, "w")
        f.write(htmlText)
        f.close()
    
    def append(htmlText):
        f = open(PipeFile2.Name, "a")
        f.write(htmlText)
        f.close()
    
    def clear():
        f = open(PipeFile2.Name, "w")
        f.close()

    def read():
        f = open(PipeFile2.Name, "r")
        return f.read()