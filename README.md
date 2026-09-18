\# Intranet Porto do Recife



Projeto de desenvolvimento da Intranet do Porto do Recife.



\## Equipe



\- Jhulia — Backend

\- Matheus — Backend

\- Lucas — Frontend



\## Estrutura



O projeto será dividido em:



\- `backend/` — Backend desenvolvido com Plone.

\- `frontend/` — Frontend desenvolvido com Volto.



\## Tecnologias



\### Backend

\- Plone

\- Python

\- Zope

\- ZODB

\- Docker

\- REST API



\### Frontend

\- Volto

\- React

\- JavaScript

\- Docker



\## Desenvolvimento



Cada desenvolvedor utilizará seu próprio ambiente local.



O GitHub será utilizado para versionamento e compartilhamento do código.



A branch `main` deverá permanecer estável.



Novas funcionalidades serão desenvolvidas em branches próprias e integradas à `main` após revisão.



\## Comunicação



O frontend Volto consumirá os dados e funcionalidades do backend Plone através da REST API.



```text

Volto

&#x20; |

&#x20; | REST API

&#x20; v

Plone

&#x20; |

&#x20; v

ZODB

