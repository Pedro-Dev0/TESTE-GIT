num1 = int(input("Digite um numero:"))
num2 = int(input("Digite um numero:"))

operacao = input("Digite a operação que deseja (+, -, *, /)")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1-num2)
elif operacao == '*':
    print(num1*num2)
else:
    print(num1/num2)