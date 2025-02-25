import os as os
def criar():
    html = input("Qual o nome que gostaria de colocar no seu html?")
    css = input("Qual o nome que você gostaria de usar em seu css?")
    js = input("Qual nome você dará a seu js?")
    contenthtml= """
    <!DOCTYPE html>
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="">
</head>
<body>
    <script src=""></script>
</body>
</html>
    """
    contentcss = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior:smooth;
    overflow-x: hidden;
}
"""
    contentjs = """
"""
    with open(html + '.html', 'w') as htm:
        htm.write(contenthtml)
    with open(css + '.css', 'w') as csss:
        csss.write(contentcss)
    with open(js + '.js', 'w') as script:
        script.write(contentjs)
    print('Ok, está tudo quase pronto!')
    with open('.gitignore', 'w') as git:
        git.write("")
    print("feito, até o próximo codigo")
#lembre de arrumar a parte do user, se nao ninguém poderá usar
print('Bem vindo ao criador de pastas amigo!')
print("Este aqui, é uma automatização das suas pastas, para que você apenas precise se preocupar em codar em html, css e js")
diretorio = input("Vamos começar então... Primeiro, qual diretório você deseja colocar?")
downloads = r'C:\Users\joaoh\Downloads'
documents = r'C:\Users\joaoh\Documents'
if diretorio == 'Downloads' or diretorio == 'downloads' or diretorio == 'download' or diretorio == 'Download':
    diretorio = downloads
    os.chdir(downloads)
if diretorio == 'Documents' or diretorio == 'documents' or diretorio == 'document' or diretorio == 'Document':
    diretorio = documents
    os.chdir(documents)
else:
    os.chdir(diretorio)
#Agora irei começar a automatização da criação dos documentos html, css e js
print('Certo detectamos o seu diretório!')
pasta = input("Deseja criar uma pasta?")
if pasta == 'Sim' or pasta == 'sim':
    nomepasta = input("Qual o nome da pasta que você deseja?")
    os.mkdir(nomepasta)
    os.chdir(diretorio + '\\' + nomepasta)
    criar()
if pasta == 'Não' or pasta == 'não':
    print("Beleza, você que manda!")
    criar()
    
#vamo la pensar primeiro, primeiro eu crirei uma função para que eu não precise repetir elas nos ifs, nessa função teriamos os inputs
#Esses inputs, teriam o nome do documento, cada um com seu arquivo referente, html, css e js
#após os inputs, oque eu fiz foi o with open('nome com tipo de arquivo', 'w para escrever') as archive como exemplo de comando para se passar pelo documento
#Logo após isso, como eu tinha resultados de inputs para nomes, eu apenas contantenei com o tipo de arquivo
#outra coisa que eu fiz foi criar um conteudo para ser escrito no documento correspondente, no caso o comando basico, lago que fazendo rapido demoraria 2 minuros
# Estilos e corpo de html basico feito, posso começar o codigo real, esse foi a função
# Primeiro, queremos o diretorio, criei três condições, duas para caminhos base, download e document, cada um com values de erros também sendo representados como or
# Nele, ele faria o valor do diretorio se tornar o próprio diretório que criei como variavel, e assim usando o os.chdir, que redireciona de acordo com o seu parametro
# Logo após isso, eu quis uma função de criar pastas, todo mundo precisa de uma pasta, assim, eu usei o mkdir com ifs, onde se sim ele criaria o mkdir com o nome da pasta que queria fazer
# criando uma pasta com o value do input, e se não não criaria, depois eu apenas usei a função, já que usaria o mesmo código duas vezes eu preferi o uso de função. 