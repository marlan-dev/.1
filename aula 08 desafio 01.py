import sys




def calculadora(num1, num2, op):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2

    return result

def main():
    print("calculadora simples")
    print("1- SOMA")
    print("2- SUBTRAÇÃO")
    print("3- MULTIPLICAÇÃO")
    print("4- DIVISÃO")

    escolha = input("Escolha a operação (1,2,3,4): ")
    if escolha in [1, 2, 3, 4]:
        num1=input("Digite o primeiro número")
        num2=input("Digite o segundo número")
    if escolha == '1':
        print(f"resultado= ")

     
if __name__ == "__main__":

    argumentos=sys.argv [1:]
    num1=float(argumentos[0])
    num2=float(argumentos[1])
    operacao=argumentos[2]

    resultado=calculadora(num1,num2,operacao)
    print(resultado)
