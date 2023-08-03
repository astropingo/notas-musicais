NOTAS = "C C# D D# E F F# G G# A A# B".split()
ESCALAS = {
    "maior": (0, 2, 4, 5, 7, 9, 11),
}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Retorna uma escala com notas e graus de uma escala a partir da tônica.

    Parameters:
        tonica: A tônica da escala.
        tonalidade: A tonalidade da escala.

    Returns:
        Um dicionário com as notas e graus da escala e os graus.

    Raises:
        ValueError: Nota fornecida inválida.
        KeyError: Escala fornecida inválida.

    Examples:
        >>> escala("C", "maior")
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala("a", "maior")
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
    except KeyError:
        raise KeyError(
            f"Escala não existe ou não implementada. Utilize uma entre {list(ESCALAS.keys())}"
        )
    try:
        tonica_position = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f"Nota não existe, utilize uma das seguintes notas: {NOTAS}")

    temp = []

    for intervalo in intervalos:
        nota = (tonica_position + intervalo) % 12
        temp.append(NOTAS[nota])

    return {"notas": temp, "graus": ["I", "II", "III", "IV", "V", "VI", "VII"]}
