from py_html.HtmlElement import HtmlElement

a1 = HtmlElement(
    tag='a', 
    content='this is a link', 
    attrs={'href' : 'https://stackoverflow.com/questions/8930915/append-dictionary-to-a-dictionary'}
)
a2 = HtmlElement(
    tag='a', 
    content='this is also a link', 
    attrs={'href' : 'https://stackoverflow.com/questions/43462624/use-function-without-calling-module'}
)

div1 = HtmlElement(
    tag='div',
    content=a1,
    attrs={}
)
div1.addContent(a2)

print(div1)