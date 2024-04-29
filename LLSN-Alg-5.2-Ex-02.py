TARIFA_INICIAL = 4.00  
PRECO_POR_QUILOMETRO = 0.25 / 0.14  

def main():
    try:
        distancia_km = float(input("Digite a distância percorrida em quilômetros: "))
        if distancia_km >= 0:
            valor_corrida = TARIFA_INICIAL + (PRECO_POR_QUILOMETRO * distancia_km)
            print(f"O valor total da corrida é: R${valor_corrida:.2f}")
        else:
            print("Você digitou um valor menor que zero.")
    except ValueError:
        print("Por favor, insira uma distância válida.")

if __name__ == "__main__":
    main()
