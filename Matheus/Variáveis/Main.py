def main():
    altura = float (input ("digete a sua altura: "))
    idade = int (input ("digete a sua idade: "))
    isCasado = input("vc é casado? ")
    sexo = input ("digete seu sexo: ")
    nome = input("digete seu nome: ")
    peso = float( input("digete seu peso: "))
    cpf = input("digete seu cpf: ")

    print("O",nome,"mede",altura,"m de altura, tem", idade,"anos de idade")
    print("È do sexo", sexo,",pesa",peso,"e seu CPF é:", cpf)

    if isCasado == "S" or isCasado == "s":    
      print("O ", nome, " é casado")
    elif isCasado == "Sou" or isCasado == "sou":
        print("ele é casado")
    else:
        print("O ", nome,"não é casado")
    return 0
main()