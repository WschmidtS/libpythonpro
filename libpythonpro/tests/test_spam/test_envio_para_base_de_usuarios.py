from unittest.mock import Mock

import pytest

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'w.schmidt@uol.com.br',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'w.schmidt@uol.com.br',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )

    enviador.enviar.assert_called_once_with(
        'w.schmidt@uol.com.br',
        'renzo@python.pro.br',
        'Curso Python Pro,',
        'Confira os módulos fantásticos'
    )
