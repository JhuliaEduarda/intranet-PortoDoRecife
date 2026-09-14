from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema

class INoticia(model.Schema):

    categoria = schema.Choice(
        title=u"Categoria",
        values=[u"Geral", u"Comunicado", u"Evento", u"Urgente"],
        required=True,
    )

    imagem = NamedBlobImage(
        title=u"Imagem de Capa",
        required=False,
    )

    texto = RichText(
        title=u"Texto da Notícia",
        required=False,
    )
