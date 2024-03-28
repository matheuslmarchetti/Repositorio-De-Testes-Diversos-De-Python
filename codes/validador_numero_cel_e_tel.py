import re
import unidecode


#06733223322
#067988778877
#"[0-9]{2}[0-9]{4,5}[0-9]{4}"
#r"[\d]{10,11}"

#CEL
#11 a 19 9XXXX-XXXX

#TEL
#11 a 19 2XXX-XXXX; 3XXX-XXXX; 4XXX-XXXX; 5XXX-XXXX

# DDD 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 46, 47, 49, 51, 53, 54, 55, 61, 62, 64, 63, 65, 66, 69, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 87, 82, 83, 84, 85, 88, 86, 89, 91, 93, 94, 92, 97, 95, 96, 98, 99


lista = []
#Normalizar telefone REMOVER ESPAÇOS E CARACTERES ESPECIAIS
def normalize_numero(numero):
    lista = numero.split()
    lista = [numero.strip() for numero in lista]
    for i in range(len(lista)):
        # remove ascents
        lista[i] = unidecode.unidecode(lista[i])
    # remove caracteres
    numero = "".join(lista)
    numero = re.sub(r'[\WA-Za-z]', '', numero)
    if numero[0] == '0':
        numero = numero.replace('0','',1)
    return numero

#Classifica telefone MOVEL OU FIXO
def classifica_numero(numero):
    return numero, numero    


def validate_cel_e_tel(numero):
    numero = normalize_numero(numero)
    pattern = re.compile(r"[\d]{2}[\d]{4,5}[\d]{4}")
    if re.fullmatch(pattern, numero):
        numero = classifica_numero(numero)
        return numero
    return False

numero = '0 679887 78877@A'

print(normalize_numero(numero))
print(validate_cel_e_tel(numero))
print(type(validate_cel_e_tel(numero)))
# print(len(validate_cel_e_tel(numero)))
# print(validate_cel_e_tel(numero)[0])


