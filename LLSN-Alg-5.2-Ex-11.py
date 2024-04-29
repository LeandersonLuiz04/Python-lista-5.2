import random

def senha_aleatoria():
    intervalo=random.randint(7,10)
    senha=""
    while len(senha)!=intervalo:
        aleatorio=chr(random.randint(33,126))
        senha+=aleatorio
    return senha


def main():
    if senha_aleatoria():
        print(f"SUA SENHA: {senha_aleatoria()}")
if __name__=="__main__":
    main()