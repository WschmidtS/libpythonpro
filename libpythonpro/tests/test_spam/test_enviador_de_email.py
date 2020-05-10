from libpythonpro.spam.enviador_de_email import Enviador

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'walter@python.pro.br',
        'renzo@python.pro.br',
        'Curso PyTools',
        'Codando as aulas do curso do PyTools'
    )
    assert 'walter@python.pro.br' in resultado