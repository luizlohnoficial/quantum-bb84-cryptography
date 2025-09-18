# QuantumBB84Cryptography

Este projeto demonstra o protocolo BB84 escrito em Q# integrado a scripts
Python para gerar chaves de uso único (One-Time Pad).

## Requisitos

- Python 3.10+
- Pacote [`qsharp`](https://pypi.org/project/qsharp/)

Instale as dependências executando:

```bash
pip install -r requirements.txt
```

## Utilização

Para executar um exemplo de geração de chave, criptografia e
 descriptografia de uma mensagem, rode:

```bash
python start.py
```

Siga as instruções em tela para informar a mensagem a ser criptografada.

## Testes

Os testes unitários utilizam `pytest` e verificam se o processo de
criptografia e descriptografia preserva a mensagem original.
Execute:

```bash
pytest -q
```

**Observação:** se o pacote `qsharp` não estiver instalado os testes serão
automaticamente ignorados.