import re



def valide_email(lista_de_emails):
    lista_emails_validados = []
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    for emails in lista_de_emails:
        if re.match(pattern, emails):
            # return True
            lista_emails_validados.append(emails)
        else: 
            continue
    return lista_emails_validados
    