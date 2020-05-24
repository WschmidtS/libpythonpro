import pytest

from libpythonpro.spam.enviador_de_email import Enviador

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Walter', email='w.schmidt@uol.com.br'),
            Usuario(nome='Renzo', email='renzo@python.pro.br')
        ],
        [
            Usuario(nome='Walter', email='w.schmidt@uol.com.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'w.schmidt@uol.com.br',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.paramentros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.paramentros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'w.schmidt@uol.com.br',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )

    assert enviador.paramentros_de_envio == (
        'w.schmidt@uol.com.br',
        'renzo@python.pro.br',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )
