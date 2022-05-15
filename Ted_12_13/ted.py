from time import sleep
glossário = {"Python":" Uma linguagem de programação", "VScode":" uma IDE", "Pycharm":" é uma IDE focada em Python" , "Web scraping":
" é um processo de coleta de dados estruturados da web de maneira automatizada"
, "Google Colab":"Google Colab é um serviço de armazenamento em nuvem de notebooks voltados à criação e execução de códigos em Python, diretamente em um navegador"



}


for i in glossário:
    sleep(1)
    print("\n---------------------")
    print(f"{i} é {glossário[i]}")




