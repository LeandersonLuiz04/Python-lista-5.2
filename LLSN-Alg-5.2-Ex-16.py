import os
#PEÇO DESCULPAS POR O CÓDIGO TER FICADO GRANDE 
print("Digite 1 para converter de -HEXADECIMAL PARA BINARIO--\n"
"Digite 2 para converter de -INTEIRO PARA HEXADECIMAL--\n"
"Digite 3 para converter de -BINÁRIO PARA DECIMAL--\n"
"Digite 4 para converter de -DECIMAL PARA BINÁRIO--\n"
"Digite 5 para converter de -DECIMAL PARA BASE ARBITRARIA--\n"
"Digite 6 para converter de -BASE ARBITRARIA PARA DECIMAL--\n")

escolha=int(input("Sua escolha: "))
os.system("cls") or None
if escolha==1:
    def hex2int(hex):
        """Converte um único dígito hexadecimal em um inteiro de base 10"""
        hexa_valores = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        if hex in hexa_valores:
            return hexa_valores[hex]
        else:
            raise ValueError("O que você digitou não pode ser convertido.")
    h=input("STRING: ").upper()
    print(f"RESULTADO: {hex2int(hex=h)}")
    hex2int(hex=h)

if escolha==2:
    def int2hex(inteiro):
        """Converte um inteiro entre 0 e 15 em um único dígito hexadecimal."""
        hexa_valores = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        if inteiro >= 0 and inteiro <= 15:
            return hexa_valores[inteiro]
        else:
            raise ValueError("O número que você digitou não pode ser convertido.")
    I=int(input("INTEIRO: "))
    print(f"RESULTADO: {int2hex(inteiro=I)}")    

if escolha==3:
    def binario_decimal():
        numero_binario = input("Digite um número binário para converter para decimal: ")
        numero_decimal = 0
        for i in range(len(numero_binario)):
            digito = int(numero_binario[i])
            valor = digito * (2 ** (len(numero_binario) - 1 - i))
            numero_decimal += valor
        return numero_decimal
    def main():
        print(f"EM DECIMAL: {binario_decimal()}")
    if __name__=="__main__":
        main()

if escolha==4:
    def decimal_binario(n_decimal):
        """Converte um número decimal para binário."""
        if n_decimal == 0:
            return "0"
        result = ""
        q = n_decimal
        while q != 0:
            r = q % 2
            result = str(r) + result
            q //= 2
        return result
    def main():
        numero_decimal=int(input("NÚMERO DECIMAL: "))
        print(f"EM BINÁRIO: {decimal_binario(n_decimal=numero_decimal)}")
    if __name__=="__main__":
        main()

if escolha==5:
    def decimal_para_base(numero_decimal, base):
        digitos_hexadecimais = "0123456789ABCDEF"
        resultado = ""

        while numero_decimal > 0:
            resto = numero_decimal % base
            resultado = digitos_hexadecimais[resto] + resultado
            numero_decimal //= base

        return resultado

    def main():
        try:
            numero_decimal = int(input("Digite o número decimal: "))
            base = int(input("Digite a base para conversão (2 a 16): "))

            resultado = decimal_para_base(numero_decimal, base)
            print(f'O número decimal {numero_decimal} é equivalente a {resultado} na base {base}.')
        except ValueError as e:
            print("Erro:", e)

    if __name__ == "__main__":
        main()

if escolha==6:
    def base_para_decimal(numero, base):
            if not 2 <= base <= 16:
                raise ValueError("A base deve estar entre 2 e 16.")

            digitos_hexadecimais = "0123456789ABCDEF"
            numero = numero.upper()
            resultado = 0

            for digito in numero:
                if digito not in digitos_hexadecimais[:base]:
                    raise ValueError(f"Dígito inválido na base {base}: {digito}")
                resultado = resultado * base + digitos_hexadecimais.index(digito)

                return resultado

            def main():
            
                numero = input("Digite o número na base desejada: ")
                base = int(input("Digite a base do número (2 a 16): "))
                print(f"RESULTADO: {base_para_decimal(numero, base)}")

            if __name__ == "__main__":
                main()
