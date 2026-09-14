from plone.supermodel import model
from zope import schema

class ISetor(model.Schema):
    nome_setor = schema.TextLine(
        title="Nome do Setor",
        required=True,
    )
    responsavel = schema.TextLine(
        title="Responsável pelo Setor",
        required=False,
    )
    descricao = schema.Text(
        title="Descrição das Atividades",
        required=False,
    )
