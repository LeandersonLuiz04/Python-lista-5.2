

def magic_data(dia,mes,ano):
    if dia*mes==ano%100:
        return True
    else:
        return False

def main():
    d=int(input("DIA: "))
    m=int(input("MÊS: "))
    a=int(input("ANO: "))
    if magic_data(dia=d,mes=m,ano=a):
        print(magic_data(dia=d,mes=m,ano=a))
if __name__=="__main__":
    main()