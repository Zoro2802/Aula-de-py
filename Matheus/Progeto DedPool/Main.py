def main():
    idade = int(input("Me diga a sua idade?"))

    if idade >= 18:
        print("Entrada permitida")  
    elif idade >= 16:
        acom =input("Você está acompanhada?")
        if acom == "S":
            print("Entrada liberada")
            
            
            
            return 0
        main()

