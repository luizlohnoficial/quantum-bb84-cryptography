# Importando bibliotecas necessárias
import qsharp
import random

from CriptBB84 import KeyBB84,  RandomBit


def GenerateRandonBits(n):
    vetor = []
    for i in range(n):
        vetor.append(random.randint(0, 1))
    return vetor


# Retorna vetor de n bits aleatórios com Q#
# range: retorna uma sequência de números *
# simulate irá simular a execução da função GenerateRandonBits
def QubitsRandonBits(n):
    vetor = []
    for i in range(n):
        vetor.append(RandomBit.simulate())
    return vetor


def GeraChaveCompartilhada():
    key = []  # vetor inicial
    while len(key) <= 8:  # necessário 8 bits para representar qualquer valor da ASCII
        # numero n de bits/qubits que serão utilizados
        tam = 16  # Cria vetores de bits de tamanho n aleatórios
        # Origien gera n bits aleatórios de mensagem
        UserOrigen = QubitsRandonBits(tam)
        # Usuário Origen gera uma base de bits aleatórios onde serão aplicados a H
        UserOrigenBase = QubitsRandonBits(tam)
        # Usuário Destino  gera uma base de bits aleatórios onde serão aplicados a H
        UserDestinoBase = QubitsRandonBits(tam)
        # Faz a simulação com as bases aleatórias definidas e cria uma chave compartilhada

        print(f"UserOrigen     : {UserOrigen}")
        print(f"UserOrigenBase : {UserOrigenBase}")
        print(f"UserDestinoBase: {UserDestinoBase}")

        key = KeyBB84.simulate(
            AliceBits=UserOrigen, AliceBase=UserOrigenBase, BobBase=UserDestinoBase, n=tam)
        print(f"key sendo unida: {key}")

    # converte a lista de inteiros para uma string binária
    for i in range(len(key)):
        key[i] = str(key[i])
    key = "".join(key)
    print(f"key apenas converter lista: {key}")
    return key


def CriptografaCaracter(c, key):
    print(f"C ORD: {ord(c)}")
    print(f"int(key, 2)) % 255: {int(key, 2) % 255}")

    c = (ord(c) + int(key, 2)) % 255
    print(f"criptografa caractere: {c}")
    print(f"bin: {bin(c)}")

    return bin(c)


# Usar qualquer método de criptografia de chave única
def CriptografaMensagem(SenhaFornecida):
    Msg_Cript = []
    Keys = []
    for i in SenhaFornecida:
        key = GeraChaveCompartilhada()
        Keys.append(key)
        Msg_Cript.append(CriptografaCaracter(i, key))
        print(f"CriptografaMensagemKey: {key}")
        print(f"CriptografaMensagemMSG: {Msg_Cript}")
    return (Msg_Cript, Keys)
