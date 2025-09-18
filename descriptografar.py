
"""Rotinas para descriptografar mensagens cifradas com One-Time Pad."""


def descriptografa_caracter(c: str, key: str) -> str:
    """Descriptografa um caractere binário usando a chave fornecida."""
    valor = (int(c, 2) - int(key, 2)) % 255
    return chr(valor)


def descriptografa_mensagem(msgs, keys) -> str:
    """Descriptografa uma lista de caracteres binários usando as chaves."""
    resultado = []
    for i in range(len(msgs)):
        resultado.append(descriptografa_caracter(msgs[i], keys[i]))
    return "".join(resultado)
