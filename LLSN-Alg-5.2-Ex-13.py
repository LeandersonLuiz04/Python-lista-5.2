
meses={
    1:"Janeiro",
    2:"Fevereiro",
    3:"Março",
    4:"Abril",
    5:"Maio",
    6:"Junho",
    7:"Julho",
    8:"Agosto",
    9:"Setembro",
    10:"Outubro",
    11:"Nevembro",
    12:"Dezembro",
}

def dias(mes,ano):
    nome_do_mes=meses[mes]
    if nome_do_mes=='Janeiro' or nome_do_mes=='Março' or nome_do_mes=='Maio' or nome_do_mes=='Julho' or nome_do_mes=='Agosto' or nome_do_mes=='Outubro' or nome_do_mes=='Dezembro':
        print(f'{nome_do_mes}: 31 dias. ')
    elif nome_do_mes=="Fevereiro":
        if ano%400==0 or (ano % 4 == 0 and ano % 100 != 0):
            print(f"{nome_do_mes}: 29 dias. ")
        else:
            print(f"{nome_do_mes}: 28 dias. ")
    else:
        print(f"{nome_do_mes}: 30 dias. ")



def main():
    m=int(input("MÊS: "))
    a=int(input("ANO: "))
    dias(mes=m, ano=a)
if __name__=="__main__":
    main()
