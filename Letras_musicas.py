from selenium import webdriver
from docx import Document
import time

nome_musica = input("Digite o nome da música: ")
navegador = webdriver.Edge(r'C:\Users\wesle\OneDrive\Área de Trabalho\Wesley\Python\MeusProjetos\Letras_musicas\Letras_musicas\msedgedriver.exe')

#busca a letra
navegador.get("https://www.letras.mus.br/")
navegador.find_element("id", "main_suggest").click()
navegador.find_element("xpath",'//*[@id="main_suggest"]').send_keys(nome_musica)
navegador.find_element("xpath",'/html/body/div[1]/header/div[1]/form/button').click()
time.sleep(4)
navegador.find_element("xpath",'//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div/a').click()
letra_elemento = navegador.find_element("xpath",'//*[@id="js-lyric-cnt"]/article/div[2]/div[1]')
letra = letra_elemento.text
print()
print(letra)
# Cria um novo documento do Word
doc = Document()
# Adiciona o conteúdo da variável 'letra' ao documento
doc.add_paragraph(letra)
# Define o nome do arquivo de saída
nome_arquivo = "letra_musica.docx"
# Salva o documento no arquivo
doc.save(nome_arquivo)
print(f"O arquivo {nome_arquivo} foi criado com sucesso!")