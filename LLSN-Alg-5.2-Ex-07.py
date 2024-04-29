def validade(c1,c2,c3):
   if c1>=c2+c3 or c2>=c1+c3 or c3>=c2+c1:
       return "Não é possível formar um triângulo!!!"
   return "É possível formar um triângulo."



def main():
    x=int(input("COMPRIMENTO DO PRIMEIRO CANUDO: "))
    y=int(input("COMPRIMENTO DO SEGUNDO CANUDO: "))
    z=int(input("COMPRIMENTO DO TERCEIRO CANUDO: "))
    if validade(c1=x,c2=y,c3=z):
        print(validade(c1=x,c2=y,c3=z))
if __name__=="__main__":
    main()