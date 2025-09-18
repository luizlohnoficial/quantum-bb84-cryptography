"""Rotinas de criptografia usando chaves geradas pelo protocolo BB84."""

import random


try:
    import qsharp  # noqa: F401
    from CriptBB84 import KeyBB84, RandomBit
    QSHARP_AVAILABLE = True
except Exception:  # pragma: no cover - only executed when qsharp missing
    QSHARP_AVAILABLE = False
    KeyBB84 = None  # type: ignore[assignment]
    RandomBit = None  # type: ignore[assignment]


def generate_random_bits(n):
    """Retorna uma lista de ``n`` bits aleatórios (0 ou 1)."""
    return [random.randint(0, 1) for _ in range(n)]

def qubits_random_bits(n):
    """Gera ``n`` bits aleatórios utilizando a operação ``RandomBit`` em Q#."""
    if not QSHARP_AVAILABLE:
        raise ImportError("qsharp não está disponível")
    return [RandomBit.simulate() for _ in range(n)]

def gera_chave_compartilhada():
    """Executa o protocolo BB84 até gerar ao menos 8 bits de chave."""
    if not QSHARP_AVAILABLE:
        raise ImportError("qsharp não está disponível")
    key = []
    while len(key) <= 8:
        tam = 16
        user_origen = qubits_random_bits(tam)
        user_origen_base = qubits_random_bits(tam)
        user_destino_base = qubits_random_bits(tam)

        key = KeyBB84.simulate(
            AliceBits=user_origen,
            AliceBase=user_origen_base,
            BobBase=user_destino_base,
            n=tam,
        )

    return "".join(str(bit) for bit in key)


def criptografa_caracter(c: str, key: str) -> str:
    """Criptografa um único caractere usando a chave binária fornecida."""
    valor = (ord(c) + int(key, 2)) % 255
    return bin(valor)


def criptografa_mensagem(texto: str):
    """Criptografa cada caractere da mensagem utilizando uma chave única."""
    msg_cript = []
    keys = []
    for char in texto:
        key = gera_chave_compartilhada()
        keys.append(key)
        msg_cript.append(criptografa_caracter(char, key))
    return msg_cript, keys
