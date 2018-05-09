from py_html.HtmlElement import HtmlElement

def buildCardWithLink(title, text, link_url, link_text):
    outerWrapper = HtmlElement(
        tag='div', 
        attrs={'class' : '"card margin10"'}
    )
    cardBody = HtmlElement(
        tag='div',
        attrs={'class' : 'card-body'}
    )
    cardTitle = HtmlElement(
        tag='h5',
        content= title,
        attrs={'class' : 'card-subtitle mb-2 text-muted'}
    )
    cardText = HtmlElement(
        tag='p',
        content= text,
        attrs={'class' : 'card-text'}
    )
    cardLink = HtmlElement(
        tag='a',
        content= link_text,
        attrs={'href' : link_url, 'class' : 'card-link'}
    )

    cardBody.addContent(cardTitle)
    cardBody.addContent(cardText)
    cardBody.addContent(cardLink)
    outerWrapper.addContent(cardBody)
    return str(outerWrapper)

def buildCard(title, text):
    outerWrapper = HtmlElement(
        tag='div', 
        attrs={'class' : '"card margin10"'}
    )
    cardBody = HtmlElement(
        tag='div',
        attrs={'class' : 'card-body'}
    )
    cardTitle = HtmlElement(
        tag='h5',
        content= title,
        attrs={'class' : 'card-subtitle mb-2 text-muted'}
    )
    cardText = HtmlElement(
        tag='p',
        content= text,
        attrs={'class' : 'card-text'}
    )

    cardBody.addContent(cardTitle)
    cardBody.addContent(cardText)
    outerWrapper.addContent(cardBody)
    return str(outerWrapper)