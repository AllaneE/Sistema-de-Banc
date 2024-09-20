# Sistema Bancário em Python

## Descrição do Projeto

Este projeto é um simples **sistema bancário** desenvolvido em Python que permite ao usuário realizar operações básicas de movimentação financeira, como depósitos, saques e consulta de extrato. O sistema opera com um saldo inicial de R$0,00 e possui um limite máximo de saques e valor por saque, garantindo controle sobre as transações.

## Funcionalidades

O sistema apresenta um menu de opções para o usuário realizar as seguintes operações:

1. **Depositar [d]:**
   - Permite o depósito de um valor escolhido pelo usuário. O valor deve ser positivo, caso contrário, o sistema informará que o depósito é inválido.
   - O valor depositado é adicionado ao saldo e registrado no extrato.

2. **Sacar [s]:**
   - Permite o saque de um valor escolhido, respeitando as seguintes condições:
     - O valor não pode ser maior que o saldo disponível.
     - O valor não pode exceder o limite de R$500,00 por saque.
     - O número de saques diários é limitado a 3.
   - Se todas as condições forem atendidas, o valor será subtraído do saldo e registrado no extrato.

3. **Consultar Extrato [e]:**
   - Exibe o extrato das movimentações realizadas (depósitos e saques).
   - Se não houver movimentações, será exibida a mensagem "Não há movimentações.".

4. **Sair [q]:**
   - Encerra o programa.

## Regras do Sistema

- **Saldo Inicial**: O saldo começa em R$0,00.
- **Limite de Saque**: O valor máximo por saque é de R$500,00.
- **Número de Saques Diários**: O número máximo de saques por dia é de 3.
- **Validação de Valores**: Tanto os valores de depósito quanto de saque devem ser positivos.

## Exemplo de Funcionamento

Ao iniciar o sistema, o usuário verá o seguinte menu:

Dependendo da escolha do usuário, o sistema solicitará um valor para depósito ou saque, atualizará o saldo e registrará a transação no extrato.

### Exemplo de Depósito:

Resultado: 
- Saldo atualizado: R$100,00
- Extrato: `Deposito de R$ 100,00`

### Exemplo de Saque:

Resultado: 
- Saldo atualizado: R$50,00
- Extrato: `Saque de R$ 50,00`

## Como Executar o Sistema

1. Certifique-se de ter o Python instalado em seu computador.
2. Copie o código do projeto para um arquivo `.py`.
3. Execute o arquivo com o comando:
   ```bash
   python banco.py


