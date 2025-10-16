import sys
from PyQt5.QtGui import QPixmap, QIcon 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton

class CadastroClientes(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(50, 50, 1000, 800)
        self.setFixedSize(1200,800)

        self.setWindowIcon(QIcon(".venv/cliente.png"))

        self.horizontal_layout = QHBoxLayout()
        self.esquerda_label = QLabel()
        
        self.esquerda_label.setPixmap(QPixmap(".venv/client.jpeg"))
        self.esquerda_label.setFixedWidth(600)
        self.esquerda_label.setScaledContents(True)

        self.direita_label = QLabel()
        self.direita_label.setFixedWidth(550)
        self.direita_label.setStyleSheet("QLabel{background-color:#C7E7F2}")

        self.vertical_layout = QVBoxLayout()
        self.titulo_label = QLabel("Cadastro de Clientes")
        self.titulo_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:20pt;color:black}")
        self.vertical_layout.addWidget(self.titulo_label)
        
        # font-family:??; (fonte)
        #   
        # font-weight:bold (NEGRITO)
        #----------- NOME 
        self.nome_label = QLabel("Nome Completo")
        self.nome_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:15pt;}")
        
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")

        self.vertical_layout.addWidget(self.nome_label)
        self.vertical_layout.addWidget(self.nome_edit)

        #FIM DO NOME

        #E-MAIL FORMULARIO
        self.email_label = QLabel("E-mail")
        self.email_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:15pt}")

        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")

        self.vertical_layout.addWidget(self.email_label)
        self.vertical_layout.addWidget(self.email_edit)

        #FIM FORMULARIO E E-MAIL

        #TELEFONE
        self.telefone_label = QLabel("Telefone")
        self.telefone_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:15pt}")

        self.telefone_edit = QLineEdit()
        self.telefone_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")

        self.vertical_layout.addWidget(self.telefone_label)
        self.vertical_layout.addWidget(self.telefone_edit)

        #FIM TELEFONE

        #CPF
        self.cpf_label = QLabel("CPF")
        self.cpf_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:15pt}")

        self.cpf_edit = QLineEdit()
        self.cpf_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")

        self.vertical_layout.addWidget(self.cpf_label)
        self.vertical_layout.addWidget(self.cpf_edit)

        #FIM DO CPF
        #Data de Nascimento
        self.data_label = QLabel("Data de nascimento")
        self.data_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:15pt}")

        self.data_edit = QLineEdit()
        self.data_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")

        self.vertical_layout.addWidget(self.data_label)
        self.vertical_layout.addWidget(self.data_edit)

        #Fim da data de nascimento

        #Endereço
        self.endereco_label = QLabel("Endereço")
        self.endereco_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:15pt}")

        self.endereco_edit = QLineEdit()
        self.endereco_edit.setStyleSheet("QLineEdit{font-weight:bold; font-family:; font-size:15pt}")

        self.vertical_layout.addWidget(self.endereco_label)
        self.vertical_layout.addWidget(self.endereco_edit)

        #FIM DO ENDEREÇO

        #GENERO
        self.sexo_label = QLabel("Sexo")
        self.sexo_label.setStyleSheet("QLabel{font-weight:bold; font-family:; font-size:15pt}")

        self.sexo_combo = QComboBox()
        self.sexo_combo.setStyleSheet("QComboBox{font-weight:bold; font-family:; font-size:15pt}")
        self.sexo_combo.addItem("Selecione...")
        self.sexo_combo.addItem("Masculino...")
        self.sexo_combo.addItem("Cisgênero...")
        self.sexo_combo.addItem("Transgênero:...")
        self.sexo_combo.addItem("Não-binário...")
        self.sexo_combo.addItem("Agênero...")
        self.sexo_combo.addItem("Gênero fluido...")

        self.vertical_layout.addWidget(self.sexo_label)
        self.vertical_layout.addWidget(self.sexo_combo)

        #-----------------BOTAO-----------

        self.gravar_button = QPushButton("Gravar")
        self.gravar_button.clicked.connect(self.gravar)
        self.gravar_button.setStyleSheet("QPushButton{font-size:15pt}")
        self.vertical_layout.addWidget(self.gravar_button)

        #FIM GENERO

        self.direita_label.setLayout(self.vertical_layout)

        self.horizontal_layout.addWidget(self.esquerda_label)

        self.horizontal_layout.addWidget(self.direita_label)

        self.setLayout(self.horizontal_layout)

    def gravar(self):
        print("Clicou no botão")
        #COMANDO ARQUIVOS
        arquivo = open("genero.txt","a",encoding="utf8")
        arquivo.write(f"nome: {self.nome_edit.text()}\n")
        arquivo.write(f"E-mail: {self.email_edit.text()}\n")
        arquivo.write(f"Telefone: {self.telefone_edit.text()}\n")
        arquivo.write(f"CPF:  {self.cpf_edit.text()}\n")
        arquivo.write(f"Data de Nascimento: {self.data_edit.text()}\n")
        arquivo.write(f"Endereço: {self.endereco_edit.text()}\n")
        arquivo.write(f"Sexo: {self.sexo_combo.currentText()}\n")
        arquivo.write("-----------------------------------\n")
        #CURRENTTEXT = grava oq foi selecionado

        
        arquivo.close()    
        #FIM ARQUIVOS

app = QApplication(sys.argv)
janela = CadastroClientes()
janela.show()
sys.exit(app.exec_())
