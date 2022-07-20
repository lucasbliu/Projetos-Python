código = int(input('digite o codigo de entrada:'))
if código == 2430:
    print('BOM DIA \033[33mSENHOR\033[m, SEJA BEM VINDO.')
elif código == 4062:
    print('\033[33mENTRADA PERMITIDA\033[m')
    print('ACESSO VIP')
else:
    print('\033[31mENTRADA NEGADA\033[m')
    print('codigo inválido.')



