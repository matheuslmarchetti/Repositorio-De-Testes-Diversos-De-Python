from funcoes_de_apoio import validar_email as ve
from funcoes_de_apoio import normalizar_email as ne


#---------------------------------ANÁLISE PADRÃO----------------------------------------------------

lista_emails_normalizados_do_sistema = ne.normalize_email('assuncão@energisa.com.br;assunção@energisa.com.br;mãtheus marchetti@gmail.com;lunguinhomarchetti@gmail.com; lunguinhomarchetti@gmail.com ; matheus.marchetti@energisa.com.br;Assunção@energisa.com.br;matheus.marchetti@en-;lunguuinho@gmail; lungui')
lista_emails_normalizados_do_input = ne.normalize_email('lunguinhomarchetti@gmail.com;matheus.marchetti@energisa.com.br;marchetti@gmail.com;marchetti2@gmail.com')
lista_emails_validados_do_sistema = ve.valide_email(lista_emails_normalizados_do_sistema)
lista_emails_validados_do_sistema_absoluto = ve.valide_email(lista_emails_normalizados_do_sistema)
lista_emails_validados_do_input = ve.valide_email(lista_emails_normalizados_do_input)

emails_tratados_do_sistema = ";".join(lista_emails_validados_do_sistema)
emails_tratados_do_input = ";".join(lista_emails_validados_do_input)

# print('################NORMALIZADOS ABAIXO DA LINHA######################')

# print(type(lista_emails_normalizados_do_input))
# print(len(lista_emails_normalizados_do_input))
# print(lista_emails_normalizados_do_input)

# print('################VALIDADOS ABAIXO DA LINHA######################')

# print(type(lista_emails_validados_do_input))
# print((lista_emails_validados_do_input))
# print(len(lista_emails_validados_do_sistema))
# print(lista_emails_validados_do_sistema)
# print(emails_tratados_do_input)

# print('################VALIDADOS ACIMA DA LINHA######################')

#---------------------------------ANÁLISE PADRÃO----------------------------------------------------

#SIATT OPÇÕES
#REMOCÃO TOTAL E-MAIL
#REMOÇÃO PARCIAL DE E-MAIL
#INCLUSÃO TOTAL

#DEF ANALISE DE INCLUSÃO
max_email_adicionar = 0
lista_emails_novo = []








# for i in range(len(lista_emails_validados)):
#      for j in range(len(lista_emails_adicionar)):
#         if lista_emails_validados[i] == lista_emails_adicionar[j]:
#             print(lista_emails_validados[i] + ' igual a ' + lista_emails_adicionar[j])
#         else:
#             print(lista_emails_validados[i] + ' não igual a ' + lista_emails_adicionar[j])


# print('######################################')
# for i in range(len(lista_emails_adicionar)):
#     print(lista_emails_adicionar[i] in lista_emails_validados)


# print('######################################')
# for i in range(len(lista_emails_adicionar)):
#     if lista_emails_adicionar[i] in lista_emails_validados and len(lista_emails_validados) <= 3:
#         print(lista_emails_adicionar[i] + ' não adicionado')
#     elif len(lista_emails_validados) <= 3:
#         print(lista_emails_adicionar[i]  + ' adicionado')
        
#     else:
#         print(lista_emails_adicionar[i] + ' caiu no else')


# print('######################################')
for i in range(len(lista_emails_validados_do_input)):
    print(len(lista_emails_validados_do_sistema))
    if lista_emails_validados_do_input[i] in lista_emails_validados_do_sistema:
        print(lista_emails_validados_do_input[i] + ' não adicionado')
    elif max_email_adicionar < 2 and len(lista_emails_validados_do_sistema_absoluto) == 3:
        
        if max_email_adicionar < 1:
            lista_emails_novo = lista_emails_validados_do_sistema
            lista_emails_novo.append(lista_emails_validados_do_input[i])
            emails_novos = ';'.join(lista_emails_novo)
            print(emails_novos)
        else:
            lista_emails_novo = lista_emails_novo
            lista_emails_novo.append(lista_emails_validados_do_input[i])
            emails_novos = ';'.join(lista_emails_novo)
            print(emails_novos)
        max_email_adicionar =+ 1
        print(max_email_adicionar)

        # print(lista_emails_validados_do_input[i]  + ' adicionado')
        # max_email_adicionar =+ 1
    else:
        print(lista_emails_validados_do_input[i] + ' caiu no else')


# for i in range(len(lista_emails_validados_do_input)):
#     if lista_emails_validados_do_input[i] == lista_emails_validados_do_input[-1]:
#         print('parou')
#     else:
#         print('caiu no else')