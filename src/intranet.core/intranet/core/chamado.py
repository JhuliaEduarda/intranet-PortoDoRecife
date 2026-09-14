from plone.supermodel import model
from zope import schema

class IChamado(model.Schema):
    solicitante = schema.TextLine(
        title="Solicitante",
        required=True,
    )
    descricao = schema.Text(
        title="Descrição da Solicitação",
        required=True,
    )
    prioridade = schema.Choice(
        title="Prioridade",
        values=["Baixa", "Média", "Alta"],
        default="Média",
        required=True,
    )
