import random
def main():
    numAle = random.randint(1 , 75)

    num = 0

    tentativas =0
    while num != numAle:
        num = int (input("Digete um número: "))
        
        if num > numAle:
            print("O número é maior que ", num)
        elif num < numAle:
            print("O número é maior que ", num)
        print("")
        tentativas += 1
        print("Você acertou com ", tentativas, "tentativas")
        return 0
    main()