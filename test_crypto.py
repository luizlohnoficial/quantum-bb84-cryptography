import pytest

import criptografar
import descriptografar


@pytest.mark.skipif(not criptografar.QSHARP_AVAILABLE, reason="qsharp not installed")
def test_encrypt_decrypt_roundtrip():
    mensagem = "abc"
    cript, chaves = criptografar.criptografa_mensagem(mensagem)
    resultado = descriptografar.descriptografa_mensagem(cript, chaves)
    assert resultado == mensagem
