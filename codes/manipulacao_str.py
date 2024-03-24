# emails = 'test0.test@test.com; test1.test@test.com;test2.test@test.com;test2.test@test.com'
emails = 'test0.test@test.com,test1.test@test.com;test2.test@test.com'
emails.strip()
print(emails)
emails = emails.replace(',',';')
print(emails)
lista_emails = emails.split(';')
lista_emails_sem_espaco = [email.strip() for email in lista_emails]

print(lista_emails_sem_espaco)
print(len(lista_emails_sem_espaco))

lista_emails_unico = set(lista_emails_sem_espaco)

print(lista_emails_unico)
print(len(lista_emails_unico))

lista_vazia = []
for elemento in lista_emails_unico:
    if (lista_emails_sem_espaco.count(elemento) > 1):
        lista_vazia.append(elemento)

print(lista_vazia)

emails_tratado = ";".join(lista_emails_unico)

print(emails_tratado)