def centralizar(string,largura):
    texto_centralizado=string.center(largura)
    print(texto_centralizado)
def main():
    mensagem=input("Texto: ")
    widht=int(input("Largura: "))
    centralizar(string=mensagem, largura=widht)
if __name__=="__main__":
    main()