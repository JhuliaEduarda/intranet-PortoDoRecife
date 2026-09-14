from plone.supermodel import model
from zope import schema

class IRamal(model.Schema):
    nome = schema.TextLine(
        title="Nome do Colaborador",
        required=True,
    )
    setor = schema.TextLine(
        title="Setor",
        required=True,
    )
    numero = schema.TextLine(
        title="Numero do Ramal",
        required=True,
    )
    email = schema.TextLine(
        title="E-mail",
        required=False,
    )
