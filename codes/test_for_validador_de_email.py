import validador_email as ve
import re
import unidecode

#SIATT OPÇÕES
#REMOCÃO TOTAL E-MAIL
#REMOÇÃO PARCIAL DE E-MAIL
#INCLUSÃO
max_email_adicionar = 0
lista_emails_adicionar = ['lunguinhomarchetti@gmail.com', 'matheus.marchetti@energisa.com.br', 'marchetti@gmail.com', 'marchetti2@gmail.com']
emails = 'assuncão@energisa.com.br;assunção@energisa.com.br;mãtheus marchetti@gmail.com;lunguinhomarchetti@gmail.com; lunguinhomarchetti@gmail.com ; matheus.marchetti@energisa.com.br;Assunção@energisa.com.br;matheus.marchetti@en-;lunguuinho@gmail; lungui'
lista_emails_validados = []

emails.strip()
lista_emails = emails.split(';')
lista_emails_sem_espaco = [email.strip() for email in lista_emails]

# print(lista_emails_sem_espaco)
# print(len(lista_emails_sem_espaco))

for i in range(len(lista_emails_sem_espaco)):
    #lower
    lista_emails_sem_espaco[i] = lista_emails_sem_espaco[i].lower()
    # remove ascents
    lista_emails_sem_espaco[i] = unidecode.unidecode(lista_emails_sem_espaco[i])

lista_emails_unico = set(lista_emails_sem_espaco)



# print(lista_emails_unico)
# print(len(lista_emails_unico))

lista_emails_unico = list(lista_emails_unico)


for i in range(len(lista_emails_unico)):
    # remove ascents
    lista_emails_unico[i] = unidecode.unidecode(lista_emails_unico[i])
    #lower
    # lista_emails_unico[i] = lista_emails_unico[i].lower()

print(lista_emails_unico)

# print(type(lista_emails_unico))



for emails_unico in lista_emails_unico:
    print(emails_unico)
    print(ve.validate_email(emails_unico))
    if ve.validate_email(emails_unico) == True:
        lista_emails_validados.append(emails_unico)
    else:
        continue

emails_tratado = ";".join(lista_emails_validados)
print(len(lista_emails))
print(emails)
print('######################################')
print(len(lista_emails_validados))
print(emails_tratado)
print('######################################')
for i in range(len(lista_emails_validados)):
     for j in range(len(lista_emails_adicionar)):
        if lista_emails_validados[i] == lista_emails_adicionar[j]:
            print(lista_emails_validados[i] + ' igual a ' + lista_emails_adicionar[j])
        else:
            print(lista_emails_validados[i] + ' não igual a ' + lista_emails_adicionar[j])


# print('######################################')
# for i in range(len(lista_emails_adicionar)):
#     print(lista_emails_adicionar[i] in lista_emails_validados)


print('######################################')
for i in range(len(lista_emails_adicionar)):
    if lista_emails_adicionar[i] in lista_emails_validados and len(lista_emails_validados) <= 3:
        print(lista_emails_adicionar[i] + ' não adicionado')
    elif len(lista_emails_validados) <= 3:
        print(lista_emails_adicionar[i]  + ' adicionado')
        
    else:
        print(lista_emails_adicionar[i] + ' caiu no else')


print('######################################')
for i in range(len(lista_emails_adicionar)):
    if lista_emails_adicionar[i] in lista_emails_validados:
        print(lista_emails_adicionar[i] + ' não adicionado')
    elif max_email_adicionar < 1 and len(lista_emails_validados) <= 3:
        print(lista_emails_adicionar[i]  + ' adicionado')
        max_email_adicionar =+ 1
    else:
        print(lista_emails_adicionar[i] + ' caiu no else')