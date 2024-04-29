def validade(escolha):
        if len(escolha)<8:
            return False
        if not any(c.isupper() for c in escolha):
            return False
        if not any(c.islower() for c in escolha):
            return False
        if not any(c.isnumeric() for c in escolha):
            return False
        return True

def main():
    escolha=input("SENHA: ")
    if validade(escolha):
        print("SENHA SEGURA.")
    else:
        print("ESSA SENHA NÃO É SEGURA.")
if __name__=='__main__':
    main()