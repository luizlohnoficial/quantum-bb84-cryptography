#!/usr/bin/env python3
"""Exemplo de uso das rotinas de criptografia e descriptografia."""

import criptografar
import descriptografar


SenhaFornecida = input("Digite uma palavra para enviar: ")
print(f"Mensagem: {SenhaFornecida}")

# Criptografa usando OTP para cada caracter
Msg_Cript, keys = criptografar.criptografa_mensagem(SenhaFornecida)

logger.info("Iniciando processo de criptografia")
if password:
    logger.info("Senha obtida da variável de ambiente")
else:
    if sys.stdin.isatty():
        logger.info("Solicitando senha ao usuário")
        try:
            password = HardCode
        except EOFError:
            logger.error("Nenhuma senha fornecida")
            raise SystemExit("Nenhuma senha fornecida")
    else:
        logger.error("Variável PASSWORD não definida e sem entrada interativa")
        raise SystemExit("Nenhuma senha fornecida")

# remove aspas extras e quebras de linha caso venham de variáveis de ambiente
password = password.strip().strip('"').strip("'")

logger.info("Mensagem recebida: %s", password)

# Criptografa usando OTP para cada caracter
Msg_Cript, keys = criptografar.CriptografaMensagem(password)
print(f"Chaves: {keys}")
print(f"Msg Criptografada: {Msg_Cript}")

# Descriptografa usando chave única
Msg_Descript = descriptografar.descriptografa_mensagem(Msg_Cript, keys)
print(f"Msg Descriptografada: {Msg_Descript}")
