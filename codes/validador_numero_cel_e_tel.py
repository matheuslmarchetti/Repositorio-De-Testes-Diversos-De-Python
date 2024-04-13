import re
import unidecode

lista_de_ddd = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 46, 47, 49, 51, 53, 54, 55, 61, 62, 64, 63, 65, 66, 69, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 87, 82, 83, 84, 85, 88, 86, 89, 91, 93, 94, 92, 97, 95, 96, 98, 99]
lista_de_digito_inicial_tel_fixo = [2, 3, 4, 5]
lsita_de_sequencia_repetida = [0000, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
lista_numero_normalizado = []

#Normalizar telefone REMOVER ESPAÇOS E CARACTERES ESPECIAIS
def normalize_numero(numero):
    lista_numero_normalizado = numero.split()
    lista_numero_normalizado = [numero.strip() for numero in lista_numero_normalizado]
    
    for i in range(len(lista_numero_normalizado)):
        # remove ascents
        lista_numero_normalizado[i] = unidecode.unidecode(lista_numero_normalizado[i])
    
    # remove caracteres
    numero = "".join(lista_numero_normalizado)
    numero = re.sub(r'[\WA-Za-z]', '', numero)
    
    i = 0

    while numero[i] == '0' and int(numero[i]) <= len(numero):
        numero = numero.replace('0','',1)
        i+1

    return numero

def validate_cel_e_tel(numero):

    numero = normalize_numero(numero)
    #CEL PADRÃO: DDD 9XXXX-XXXX
    if len(numero) == 11 and int(numero[:2]) in lista_de_ddd and int(numero[2]) == 9 and (int(numero[3:7]) in lsita_de_sequencia_repetida) == False and (int(numero[7:]) in lsita_de_sequencia_repetida) == False and numero.isdigit:
        return numero
    #TEL PADRÃO: DDD 2XXX-XXXX; 3XXX-XXXX; 4XXX-XXXX; 5XXX-XXXX
    elif len(numero) == 10 and int(numero[:2]) in lista_de_ddd and int(numero[2]) in lista_de_digito_inicial_tel_fixo and (int(numero[2:6]) in lsita_de_sequencia_repetida) == False and (int(numero[6:]) in lsita_de_sequencia_repetida) == False and numero.isdigit:
        return numero
    else:
        return 'numero inválido'


numero = '11 9 0000 1000'

print(validate_cel_e_tel(numero))

print(type(validate_cel_e_tel(numero)))