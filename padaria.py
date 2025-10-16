import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap , QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QTableWidget,QTableWidgetItem,QLineEdit,QComboBox,QMessageBox


class caixa2(QWidget):
    def __init__(self):
        super().__init__()

        self.total = 0.0
        self.linha = 0

        self.setGeometry(0, 40, 1700, 1000)

        #CRIAR OS ELEMENTOS QUE IRÃO PARA A COLUNA DA ESQUERDA

        #CRIAR UMA LABEL PARA ADICIONAR UMA IMAGEM E DEPOIS ADICIONAR
        #A COLUNA DA ESQUERDA
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/pao.jpg"))
        self.imagem_label.setScaledContents(True)
        #LARGURA DA FOTO 
        self.imagem_label.setFixedSize(900,590)
        #codigo do produto
        self.codigo_produto_label = QLabel("Codigo do Produto")
        self.codigo_produto_label.setStyleSheet("QLabel")
        self.codigo_edit = QLineEdit()
        self.codigo_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")
        
        #nome do produto
        self.nome_label = QLabel("Nome do Produto")
        self.nome_label.setStyleSheet("QLabel")

        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")
        
        #descrição do produto
        self.descricao_label = QLabel("Descricão do Produto")
        self.descricao_label.setStyleSheet("QLabel")
        self.descricao_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")
        #quantidade do produto
        self.quantidade_label = QLabel("Quantidade do Produto")
        self.quantidade_label.setStyleSheet("QLabel")
        self.quantidade_edit = QLineEdit()
        self.quantidade_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")
        #preço unitario do produto
        self.preco_label = QLabel("Preço Unitario do Produto")
        self.preco_label.setStyleSheet("QLabel")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")
        #total parte editado -
        self.subtotal_label = QLabel("Sub Total:")
        self.subtotal_label.setStyleSheet("QLabel")
        self.subtotal_edit = QLineEdit(" ")
        self.subtotal_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")
        self.subtotal_edit.setEnabled(False)
        self.subtotal_edit.setStyleSheet("QlineEdit{padding:10px;font-size:15pt; width:400}")

        #fim

        self.vcontroles = QVBoxLayout()
        self.vcontroles.addWidget(self.nome_label)
        self.vcontroles.addWidget(self.nome_edit)

        #ADICIONAR OS ELEMENTOS QUE FICARÃO AO LADO ESQUERDO
        #A UM LAYOUT VERTICAL QUE SERA APLICADA NA COLUNA
        #DA ESQUERDA
        self.vertical_esquerda_layout = QVBoxLayout()
        self.vertical_esquerda_layout.addWidget(self.imagem_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_produto_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_edit)
        self.vertical_esquerda_layout.addWidget(self.nome_label)
        self.vertical_esquerda_layout.addWidget(self.nome_edit)
        self.vertical_esquerda_layout.addWidget(self.descricao_label)
        self.vertical_esquerda_layout.addWidget(self.descricao_edit)
        self.vertical_esquerda_layout.addWidget(self.quantidade_label)
        self.vertical_esquerda_layout.addWidget(self.quantidade_edit)
        self.vertical_esquerda_layout.addWidget(self.preco_label)
        self.vertical_esquerda_layout.addWidget(self.preco_edit)
        self.vertical_esquerda_layout.addWidget(self.subtotal_label)
        self.vertical_esquerda_layout.addWidget(self.subtotal_edit)
        

        self.coluna_esquerda_label = QLabel()
        # cor da coluna 
        # self.coluna_esquerda_label.setStyleSheet("QLabel{background-color:#73C7C7}")
        #ADICIONAR O LAYOUT VERTICAL DA ESQUERAD Á COLUNA ESQUERDA

        self.coluna_esquerda_label.setLayout(self.vertical_esquerda_layout)

        #LADO DIREITO

        self.coluna_direita_label = QLabel()
        self.coluna_direita_label.setStyleSheet("QLabel{background-color:#615B5B}")

        self.horizontal_layout = QHBoxLayout()
        self.layoutvertical_direita = QVBoxLayout()
        #comando self.tabela adiciona AS "TABELAS" 
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)
        self.tabela.setRowCount(10)
        colunas = ["Código", "Nome do Produto", "Quantidade", "Preço Unitário", "Preço Total", ]
        self.tabela.setHorizontalHeaderLabels(colunas)
        # preenchendo a tabela
        self.tabela.setItem(0, 0, QTableWidgetItem(""))
        self.tabela.setItem(0, 1, QTableWidgetItem(""))
        self.tabela.setItem(0, 2, QTableWidgetItem(""))
        self.tabela.setItem(0, 3, QTableWidgetItem(""))
        self.tabela.setItem(0, 4, QTableWidgetItem(""))
        self.tabela.setItem(0, 5, QTableWidgetItem(""))
        self.tabela.setItem(0, 6, QTableWidgetItem(""))

        #editou isso
        self.totalapagar_label = QLabel("Total a Pagar")
        self.totalapagar_label.setStyleSheet("QLabel { font-size: 25pt; font-weight: bold; }")

        self.totalapagar_edit = QLineEdit("0,00")
        self.totalapagar_edit.setStyleSheet("QLineEdit { font-size: 100pt; font-weight: bold; }")



        
        #ADICIONAR A COLUNA DA ESQUERDA NO LAYOUT HORIZONTAL
        self.horizontal_layout.addWidget(self.coluna_esquerda_label)
        #ADICIONAR A COLUNA DA DIREITA NO LAYOUT HORIZONTAL
        self.layoutvertical_direita.addWidget(self.tabela)
        #isso
        self.layoutvertical_direita.addWidget(self.totalapagar_label)
        self.layoutvertical_direita.addWidget(self.totalapagar_edit)
        self.coluna_direita_label.setLayout(self.layoutvertical_direita)
        self.horizontal_layout.addWidget(self.coluna_direita_label)
        #ADICIONAR O LAYOUT HORIZONTAL NA TELA
        
        self.setLayout(self.horizontal_layout)

        #EDITAR AULA DE HOJE
        #keypress quando aperta (ira disparar o evento), key release quando vc solta a tecla.
        self.keyPressEvent = self.capturaTecla

    #voltar 1 função e usar o def para capturar
    def capturaTecla(self, e):
        if(e.key()==Qt.Key_F2):
            #print(self.quantidade_edit.text())
            #print(self.preco_edit.text())
            self.subtotal_edit.setText(str(float(self.quantidade_edit.text)) * float(self.preco_edit.text()))
            #print(float(self.quantidade_edit.text()) * float(self.quantidade_edit.text ()) ) float(self.total_edit.setText()str(self.quantidade_edit)())
        if(e.key()==Qt.Key_F3):
            print(self.codigo_edit.text())
            self.tabela.setItem(self.linha,0,QTableWidgetItem(self.codigo_edit.text()))
            self.tabela.setItem(self.linha,1,QTableWidgetItem(self.nome_edit.text()))
            self.tabela.setItem(self.linha,2,QTableWidgetItem(self.quantidade_edit.text()))
            self.tabela.setItem(self.linha,3,QTableWidgetItem(self.preco_edit.text()))
            self.tabela.setItem(self.linha,4,QTableWidgetItem(self.subtotal_edit.text()))

            self.linha = self.linha + 1
            #self.total = self.total + float(self.totalapagar_edit.text())

            #self.totalapagar_edit.setText(str(self.subtotal_edit))


        if(e.key()==Qt.Key_F4):
            op = QMessageBox.question(self,"Pagamento","Deseja efetuar o pagamento?")
            if op == QMessageBox.Yes:
                print("Pagar")
            else:
                print("Não pagar")


app = QApplication(sys.argv)
janela = caixa2()
janela.show()
app.exec_()