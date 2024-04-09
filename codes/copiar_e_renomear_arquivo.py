import os
import shutil
from datetime import datetime

nome_arquivo = 'Novo Documento de Texto'
renome_do_arquivo = fr'{nome_arquivo}_{datetime.today().strftime("%d_%m_%Y_%H_%M_%S")}.txt'
caminho_atual_do_arquivo = fr'C:\Users\lungu\Downloads\{nome_arquivo}.txt'
caminho_destino_temporario = fr'C:\Users\lungu\Downloads\pasta_temporaria_de_transferencia'
caminho_destino = fr'C:\Users\lungu\Downloads\historico'



try:
    caminho_para_mkdirs = os.path.join(caminho_destino_temporario)
    os.makedirs(caminho_para_mkdirs)
    print('Diretório Criado')
except FileExistsError as e:
    print('Diretório Existente')
    pass

# shutil.copy(caminho_atual_do_arquivo, caminho_destino_temporario)
shutil.copy2(caminho_atual_do_arquivo, caminho_destino_temporario)

# for arquivo in os.listdir(caminho_destino_temporario):
    
#     if ".txt" in arquivo:
#         nome_antigo = fr'{caminho_destino_temporario}\{arquivo}'
#         print(nome_antigo)
#         nome_novo = fr'{caminho_destino_temporario}\{renome_do_arquivo}'
#         print(nome_novo)
#         os.rename(nome_antigo, nome_novo)