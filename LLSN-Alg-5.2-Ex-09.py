

def isinteger(mensagem):
    mensagem=mensagem.strip()
    if mensagem and mensagem[0] in ["+","-"]:
        mensagem=mensagem[1:]
        if mensagem.isnumeric():
            return True
        else:
            return False
    elif mensagem.isnumeric() and len(mensagem)>=1 :
        return True
    else:
        return False
def main():
    mensagem = input("TEXTO: ")
    if isinteger(mensagem):
        print("Representa inteiro")
    else:
        print("Não representa inteiro")
if __name__=="__main__":
    main()



