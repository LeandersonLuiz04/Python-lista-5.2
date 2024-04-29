
hexa_valores = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
escolha=input("Digite 1 para converter uma string em um inteiro de base 10, ou, digite 2 para converter um inteiro em um dígito Hexadecimal: ")

if escolha=="1":
    def hex2int(hex):
        """"é responsável por converter uma string contendo um único dígito hexadecimal em um inteiro de base 10"""
        if hex in hexa_valores:
            return hexa_valores[hex]
        else:
            print("O que você digitou não pode ser convertido ")
    h=input("STRING: ").upper()
    print(f"RESULTADO: {hex2int(hex=h)}")

elif escolha=="2":
    def int2hex(inteiro):
        """"é responsável por converter um inteiro entre 0 e 15 em um único dígito hexadecimal."""
        #if inteiro>=0 and inteiro<=9:
        #    return hexa_valores[inteiro]
        if inteiro>=0 and inteiro<=15:
            hexa_valores = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8:'8', 9:'9',10:'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}                    
            return hexa_valores[inteiro]
        else:
            print("O número que você digitou não pode ser convertido")
    I=int(input("INTEIRO: "))
    print(f"RESULTADO: {int2hex(inteiro=I)}")

else:
    print("Você deve esolher uma das alternativas. ")

