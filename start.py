# Importando bibliotecas necessárias
import os
from criptografar import CriptografaMensagem
from descriptografar import DescriptografaMensagem

# Tenta ler a senha da variável de ambiente
senha = os.environ.get("PASSWORD")

if not senha:
    # Fallback para execução local
    senha = input("MINHASENHA")

SenhaFornecida = senha

# NÃO imprimir a senha em texto puro em logs se for sensível
print("Mensagem recebida (comprimento):", len(SenhaFornecida))

# Criptografa usando OTP para cada caracter
Msg_Cript, keys = criptografar.CriptografaMensagem(SenhaFornecida)
print(f"Chaves: {keys}")
print(f"Msg Criptografada: {Msg_Cript}")

# Descriptografa usando chave única
Msg_Descript = descriptografar.DescriptografaMensagem(Msg_Cript, keys)
print(f"Msg Descriptografada: {Msg_Descript}")
