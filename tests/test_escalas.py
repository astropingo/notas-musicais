from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    tonica = "c"
    tonalidade = "maior"

    assert escala(tonica, tonalidade)


def test_retornar_erro_se_nota_nao_existe():
    tonica = "z"
    tonalidade = "maior"

    mensagem_de_erro = f"Nota não existe, utilize uma das seguintes notas: {NOTAS}"

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


def test_retornar_erro_se_tonica_nao_existe():
    tonica = "c"
    tonalidade = "tonalidade"

    mensagem_de_erro = f"Escala não existe ou não implementada. Utilize uma entre {list(ESCALAS.keys())}"

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    "tonica,esperado",
    [
        ("C", ["C", "D", "E", "F", "G", "A", "B"]),
        ("C#", ["C#", "D#", "F", "F#", "G#", "A#", "C"]),
        ("F", ["F", "G", "A", "A#", "C", "D", "E"]),
    ],
)
def test_retorna_notas_corretas(tonica, esperado):
    resultado = escala(tonica, "maior")
    assert resultado["notas"] == esperado


def test_deve_retornar_os_sete_graus():
    tonica = "C"
    tonalidade = "maior"
    esperado = ["I", "II", "III", "IV", "V", "VI", "VII"]
    resultado = escala(tonica, tonalidade)
    assert resultado["graus"] == ["I", "II", "III", "IV", "V", "VI", "VII"]
