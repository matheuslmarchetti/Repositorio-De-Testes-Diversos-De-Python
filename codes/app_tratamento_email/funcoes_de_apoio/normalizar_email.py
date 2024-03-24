import unidecode

def normalize_email(emails):
    lista_emails_normalizados = []
    lista_emails = []
    lista_emails_sem_espaco = []

    emails.strip()
    lista_emails = emails.split(';')
    lista_emails_sem_espaco = [email.strip() for email in lista_emails]

    for i in range(len(lista_emails_sem_espaco)):
        #lower
        lista_emails_sem_espaco[i] = lista_emails_sem_espaco[i].lower()
        # remove ascents
        lista_emails_sem_espaco[i] = unidecode.unidecode(lista_emails_sem_espaco[i])

    set_emails_unico = set(lista_emails_sem_espaco)

    lista_emails_normalizados = list(set_emails_unico)

    return lista_emails_normalizados