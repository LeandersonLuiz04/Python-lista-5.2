


def primo(inteiro):
    if inteiro<=1:
        return False
    for i in range(2, int(inteiro**0.5)+1):
        if inteiro%1==0:
            return False
    return True

def main():
    inteiro=int(input("NÚMERO INTEIRO: "))
    if primo(inteiro):
        print(f"O número {inteiro} é primo.")
    else:
        print(f"O número {inteiro} não é primo.")
if __name__=="__main__":
    main()