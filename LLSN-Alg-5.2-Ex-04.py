def mediana(x,z):
   if x>z:
       return
   else:
       y=(x+z)/2
       return y

def main():
    primeiro_valor=int(input("Digite o primeiro valor: "))
    terceiro_valor=int(input("Digite o terceiro e ultimo valor: "))
    if mediana(x=primeiro_valor, z=terceiro_valor):
        print(f"MEDIANA: {mediana(x=primeiro_valor, z=terceiro_valor)}")
if __name__=="__main__":
    main()