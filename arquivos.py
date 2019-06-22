# -*- coding:utf-8 -*-
'''
Manipulação de arquivos

Modos:
r       somente leitura
w       escrita (caso o arquivo já exista, ele será apagado e outro criado em seu lugar)
a       leitura e escrita (adiciona novo conteúdo no fim do arquivo)
r+      leitura e escrita
w+      escrita (w+ assim como w também apagará o conteúdo anterior)
a+      leitura e escrita (abre o arquivo para atualização)
'''

pasta = "./arquivos/"
arquivo = open(pasta + "arquivo.txt")
linhas = arquivo.readlines()

for linha in linhas:
    print(linha)

arquivo.close()

# criando um arquivo
arquivo2 = open(pasta + "arquivo2.txt", "w")
arquivo2.encoding

arquivo2.write("Esse é o meu arquivo numero 2\n")

arquivo2.close()

arquivo2 = open(pasta + "arquivo2.txt", "a")

for linha in linhas:
    arquivo2.write(linha)

arquivo2.close()


