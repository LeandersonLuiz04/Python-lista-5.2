def calculadora_ecommerce(q):
   return 10.95 + (2.95 * (q - 1))

def main():
      quantidade = int(input("Número de pedidos: "))   
      valor_total = calculadora_ecommerce(q=quantidade)
      print(f"Valor total: {valor_total:.2f}")
if __name__ == "__main__":
      main()
