import pandas as pd
import openpyxl
from funcoes_de_apoio import normalizar_email as ne
from funcoes_de_apoio import validar_email as ve

tabela = pd.read_excel(fr'C:\Users\lungu\Documents\Python\github\Repositorio-De-Testes-Diversos-De-Python\bases\bases_emails.xlsx')

df = pd.DataFrame()

for linha in tabela.index:
    
    emails = tabela.loc[linha, "E-mail"]
    
    lista_emails_normalizados = ne.normalize_email(emails)
    lista_emails_validados = ve.valide_email(lista_emails_normalizados)
    emails_tratados = ";".join(lista_emails_validados)

    if emails_tratados != "":
        df = df._append({'Email': emails_tratados}, ignore_index=True)
    else:
        continue

df.to_excel(fr'C:\Users\lungu\Documents\Python\github\Repositorio-De-Testes-Diversos-De-Python\bases\emails_tratados.xlsx', sheet_name='e-mail', header=True, index=False)