import sys
from PyQt5.QtGui import QPixmap , QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel

class caixa2(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 40, 1900, 970)

        #CRIAR OS ELEMENTOS QUE IRÃO PARA A COLUNA DA ESQUERDA

        #CRIAR UMA LABEL PARA ADICIONAR UMA IMAGEM E DEPOIS ADICIONAR
        #A COLUNA DA ESQUERDA
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/padaria.jpg"))
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setFixedSize(900,300)
        #codigo
        self.codigo_produto_label = QLabel("Codigo do Produto")
        self.codigo_produto_label.setStyleSheet("QLabel")

        #nome
        self.nome_label = QLabel("Nome do Produto")
        self.nome_label.setStyleSheet("QLabel")
        #descrição
        self.descricao_label = QLabel("Descricão do Produto")
        self.descricao_label.setStyleSheet("QLabel")
        #quantidade
        self.quantidade_label = QLabel("Quantidade do Produto")
        self.quantidade_label.setStyleSheet("QLabel")
        #preço unitario
        self.preco_label = QLabel("Preço Unitario do Produto")
        self.preco_label.setStyleSheet("QLabel")


        #ADICIONAR OS ELEMENTOS QUE FICARÃO AO LADO ESQUERDO
        #A UM LAYOUT VERTICAL QUE SERA APLICADA NA COLUNA
        #DA ESQUERDA
        self.vertical_esquerda_layout = QVBoxLayout()
        self.vertical_esquerda_layout.addWidget(self.imagem_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_produto_label)
        self.vertical_esquerda_layout.addWidget(self.nome_label)
        self.vertical_esquerda_layout.addWidget(self.descricao_label)
        self.vertical_esquerda_layout.addWidget(self.quantidade_label)
        self.vertical_esquerda_layout.addWidget(self.preco_label)


        self.coluna_esquerda_label = QLabel()
        self.coluna_esquerda_label.setStyleSheet("QLabel{background-color:white}")
        #ADICIONAR O LAYOUT VERTICAL DA ESQUERAD Á COLUNA ESQUERDA

        self.coluna_esquerda_label.setLayout(self.vertical_esquerda_layout)

        self.coluna_direita_label = QLabel()
        self.coluna_direita_label.setStyleSheet("QLabel{background-color:#F54927}")

        self.horizontal_layout = QHBoxLayout()
        #ADICIONAR A COLUNA DA ESQUERDA NO LAYOUT HORIZONTAL
        self.horizontal_layout.addWidget(self.coluna_esquerda_label)
        #ADICIONAR A COLUNA DA DIREITA NO LAYOUT HORIZONTAL
        self.horizontal_layout.addWidget(self.coluna_direita_label)

        #ADICIONAR O LAYOUT HORIZONTAL NA TELA
        self.setLayout(self.horizontal_layout)
        


app = QApplication(sys.argv)
janela = caixa2()
janela.show()
app.exec_()