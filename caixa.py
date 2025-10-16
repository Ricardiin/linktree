import sys
# - QLineEdit -> Uma caixa de texto 
# - QPushButton -> Um botão para clicar
# - QVBoxLayout -> Utilizado para organizar os elementos
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit, QPushButton,QVBoxLayout, QComboBox


# Importar uma nova biblioteca para trabalhar com imagens.
#vamos usar o controle chamado QPixmap do pacote GUI
from PyQt5.QtGui import QPixmap

# Inciar a contrução da janela usando como base o controle
#QWidget. Ele possuye as configuraçoes iniciais de uma 
#janela

class CadastroProduto(QWidget):
# para inciar a janela, iremos usar a função chamada
#__ init__, que ira inicializar a nossa janela
#o termo self é um reflexivo que trata da propria
#classe, neste CadastroProduto
    def __init__(self):
        super().__init__()

        #Define o texto que aparece na barra de titulo
        self.setWindowTitle("Cadastro de Produtos")

        # Definir a posição inical da nossa janela, iremos
        #setar os valores para ( X e Y) e, também as dimensoes
        #largura e altura
        self.setGeometry(410,350,800,800)
        self.setFixedWidth(800)
        #(x,x,altura,largura)


        #vAMOS CRIAR DUAS LABELS QUE REPRESENTARAO AS PARTES
        #Superior, onde ficara a imagem, e a parte inferior
        #Onde teremos os controles
        self.superior_label = QLabel()
        self.superior_label.setPixmap(QPixmap(".venv/videogame.jpg"))
        self.superior_label.setScaledContents(True)
        # Ajustar a altura da label
        self.superior_label.setFixedHeight(400)




        self.inferior_label = QLabel()
        self.inferior_label.setStyleSheet("QLabel{background-color:#9500F4}")

        self.nome_label = QLabel("Nome do Produto")
        self.nome_label.setStyleSheet("QLabel{font-size:15pt}")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-size:15pt}")


        self.tipo_label = QLabel("Selecione o tipo de Produto")
        self.tipo_label.setStyleSheet("QLabel{font-size:15pt}")
        self.tipo_combo = QComboBox()
        self.tipo_combo.setStyleSheet("QComboBox{font-size:15pt}")
        self.tipo_combo.addItem("PlayStation 5")
        self.tipo_combo.addItem("PlayStation 4")
        self.tipo_combo.addItem("Playstation 2")
        self.tipo_combo.addItem("Xbox X/S")
        self.tipo_combo.addItem("Xbox One")
        self.tipo_combo.addItem("Nintendo Switch")
        self.tipo_combo.addItem("Nintendo Wii")
        self.tipo_combo.addItem("SuperNintendo")

        self.descricao_label = QLabel("Descrição do Produto")
        self.descricao_label.setStyleSheet("QLabel{font-size:15pt}")
        self.descricao_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("QLabel{font-size:15pt}")
        self.descricao_edit.setFixedHeight(80)


        self.preco_label = QLabel("Preço do Produto")
        self.preco_label.setStyleSheet("QLabel{font-size:15pt}")
        self.preco_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("QLabel{font-size:15pt}")


        # Organizar estes controles em um layou vertical
        self.vcontroles = QVBoxLayout()

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.superior_label)
        self.v_layout.addWidget(self.inferior_label)
        

app = QApplication(sys.argv)
janela = CadastroProduto()
janela.show()
app.exec_()
