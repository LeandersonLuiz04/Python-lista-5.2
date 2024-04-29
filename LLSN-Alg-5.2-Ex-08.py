
def maiusculo(texto):
    texto_corrigido = ""
    deixar_maiuscula = True

    for caractere in texto:
        if deixar_maiuscula and caractere.isalpha():
            caractere = caractere.upper()
            deixar_maiuscula = False
        elif caractere in ".!?":
            deixar_maiuscula = True

        texto_corrigido += caractere

    return texto_corrigido

def main():
    texto = input("Texto: ")
    corrigido = maiusculo(texto)
    print(f"Frase Corrigida: {corrigido}")

if __name__ == "__main__":
    main()

