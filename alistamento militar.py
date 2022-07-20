from datetime import date
atual = date.today().year
nasc = int(input('qual o ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos de idade em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Deve se alistar \033[33mIMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda falta {} anos para o alistamento.'.format(saldo,))
    print('seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você devia ter se alistado a {} anos.'.format(saldo))
    print('seu alistamento foi em {}.'.format(ano))

