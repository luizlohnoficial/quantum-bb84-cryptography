# Importando bibliotecas necessárias
import criptografar
import descriptografar


SenhaFornecida = list(input("Digite uma palavra para enviar: "))
print(f"Mensagem: {SenhaFornecida}")

# Criptografa usando OTP para cada caracter
Msg_Cript, keys = criptografar.CriptografaMensagem(SenhaFornecida)
print(f"Chaves: {keys}")
print(f"Msg Criptografada: {Msg_Cript}")

# Descriptografa usando chave única
Msg_Descript = descriptografar.DescriptografaMensagem(Msg_Cript, keys)
print(f"Msg Descriptografada: {Msg_Descript}")
