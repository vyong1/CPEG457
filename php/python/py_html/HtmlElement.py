class HtmlElement():
    def __init__(self, tag, content='', attrs={}):
        self.tag = tag
        self.content = str(content)
        self.attrs = attrs
    
    def addContent(self, newContent):
        self.content = self.content + str(newContent)
    
    ## TODO
    # def addAttrs(self, attrs):
    #     self.attrs.appe

    def __str__(self):
        # Start tag
        s = "<" + self.tag
        # Add attributes
        for k, v in self.attrs.items():
            s += " " + k + "=" + v
        s += ">" + str(self.content) + "</" + self.tag + ">"
        return s
