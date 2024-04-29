import math
def hipotenusa(a,b):
   hipotenusa=math.sqrt(a**2+b**2)
   print(f"HIPOTENUSA: {hipotenusa:.1f}")

def main():
   A=int(input("CATETO:"))
   B=int(input("CATETO:"))
   if hipotenusa(a=A,b=B):
      print(f"HIPOTENUSA: {hipotenusa:.1f}")
if __name__=="__main__":
   main()