valores={
   1:"Primeiro",
   2:"Segundo",
   3:"Terceiro",
   4:"Quarto",
   5:"Quinto",
   6:"Sexto",
   7:"Setimo",
   8:"Oitavo",
   9:"Nono",
   10:"Decimo",
   11:"Decimo primeiro",
   12:"Decimo segundo",
}


def ordinal(n):
   if n>12:
     return "O valor deve ser menor ou igual a 12"
   return valores[n]   

def main():
   numero=int(input("NÚMERO: "))
   if ordinal(n=numero):
      print(ordinal(n=numero))
if __name__=="__main__":
   main()