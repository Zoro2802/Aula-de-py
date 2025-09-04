from Sub import sub
from Mult import mult
from Div import div

def soma(a, b):
    return a + b

def main():
    while True:
       
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        
        operacao = input("Digite a operação (+, -, *, /): ")

       
        if operacao == '+':
            resultado = soma(num1, num2)
        elif operacao == '-':
            resultado = sub(num1, num2)
        elif operacao == '*':
            resultado = mult(num1, num2)
        elif operacao == '/':
            resultado = div(num1, num2)
        else:
            print("Operação inválida!")
            break  

       
        print("O resultado é:", resultado)

       
        repetir = input("Quer fazer outra conta? (s/n): ")
        if repetir.lower() != 's':
            print("Já que não quer mais contas... TOMA CARNE! 🍖🍗🥩")
            break  
    
    return 0
main()