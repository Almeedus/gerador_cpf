import os, time
numero_corrigidos = 0
soma_numeros = 0
primeiro_digito = 0
segundo_digito = 0
numero_decrescente1 = [10, 9, 8, 7, 6, 5, 4 ,3, 2]
numero_decrescente2 = [11, 10, 9, 8, 7, 6, 5, 4 ,3, 2]
cpf = []

try:
    while True:
        numeros_brutos = input('Informe os 9 primeiros digitos do CPF: ').strip()
    
        if len(numeros_brutos) == 9:
            if numeros_brutos.isnumeric():
                numero_corrigidos = [int(numeros_brutos)]
                numero_corrigidos = [int(digito) for digito in numeros_brutos]

                for digito in range(9):
                    soma_numeros = (numero_corrigidos[digito] * numero_decrescente1[digito]) + soma_numeros 

                primeiro_digito = (soma_numeros * 10) % 11 
                primeiro_digito = (primeiro_digito if (soma_numeros * 10) % 11 < 9 else 0)
                numero_corrigidos.append(primeiro_digito)

                soma_numeros = 0
                for digito in range(10):
                    soma_numeros = (numero_corrigidos[digito] * numero_decrescente2[digito]) + soma_numeros 
                   
                segundo_digito = (soma_numeros * 10) % 11
                segundo_digito = (segundo_digito if ((soma_numeros * 10) % 11) < 9 else 0)
                numero_corrigidos.append(segundo_digito)


                for i in range(0, 9, 3):
                    sub_lista = numero_corrigidos[i:i+3]
                    sub_string = ''.join(str(num) for num in sub_lista)
                    print(sub_string,end='')
                    if i < 6:
                        print(end='.')
                    else:
                        print(end='-')
                print(primeiro_digito,segundo_digito, sep='')
                break

            else:
                print('Digite APENAS números')
                time.sleep(2)
                os.system('cls')
                continue

        else:
            print('Informe 9 números')
            time.sleep(2)
            os.system('cls')
            continue

except Exception as error:
    print(error)