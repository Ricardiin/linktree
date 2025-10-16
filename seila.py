import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QTableWidget, QTableWidgetItem, QLineEdit
)

class caixa2(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 40, 1700, 1000)
        self.setWindowTitle("Caixa 2 - Sistema de Produtos")

        # ======= COLUNA ESQUERDA =======
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/pao.jpg"))
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setFixedSize(900, 590)

        # Código
        self.codigo_produto_label = QLabel("Código do Produto")
        self.codigo_edit = QLineEdit()
        self.codigo_edit.setStyleSheet("QLineEdit{font-weight:bold; font-size:15pt}")

        # Nome
        self.nome_label = QLabel("Nome do Produto")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-weight:bold; font-size:15pt}")

        # Descrição
        self.descricao_label = QLabel("Descrição do Produto")
        self.descricao_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("QLineEdit{font-weight:bold; font-size:15pt}")

        # Quantidade
        self.quantidade_label = QLabel("Quantidade do Produto")
        self.quantidade_edit = QLineEdit()
        self.quantidade_edit.setStyleSheet("QLineEdit{font-weight:bold; font-size:15pt}")

        # Preço unitário
        self.preco_label = QLabel("Preço Unitário do Produto")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{font-weight:bold; font-size:15pt}")

        # Total
        self.total_label = QLabel("Sub Total:")
        self.total_edit = QLineEdit("Tecle F2 para calcular")
        self.total_edit.setStyleSheet("QLineEdit{font-weight:bold; font-size:15pt}")

        # Layout da esquerda
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
        self.vertical_esquerda_layout.addWidget(self.total_label)
        self.vertical_esquerda_layout.addWidget(self.total_edit)

        self.coluna_esquerda_label = QLabel()
        self.coluna_esquerda_label.setLayout(self.vertical_esquerda_layout)

        # ======= TABELA (COLUNA DIREITA) =======
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)
        self.tabela.setRowCount(5)
        colunas = ["Código", "Produto", "Tipo", "Fabricante", "Quantidade", "Preço", "Total"]
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setItem(0, 0, QTableWidgetItem("001"))
        self.tabela.setItem(0, 1, QTableWidgetItem("Mouse"))
        self.tabela.setItem(0, 2, QTableWidgetItem("Informática"))
        self.tabela.setItem(0, 3, QTableWidgetItem("Logitech"))
        self.tabela.setItem(0, 4, QTableWidgetItem("10"))
        self.tabela.setItem(0, 5, QTableWidgetItem("R$ 50,00"))
        self.tabela.setItem(0, 6, QTableWidgetItem("R$ 500,00"))

        # Layout horizontal (tela completa)
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.coluna_esquerda_label)
        self.horizontal_layout.addWidget(self.tabela)
        self.setLayout(self.horizontal_layout)

    # ======= CAPTURA DE TECLA =======
    def keyPressEvent(self, e):
        if e.key() == (Qt.Key_F2):
            try:
                quantidade = float(self.quantidade_edit.text())
                preco = float(self.preco_edit.text())
                total = quantidade * preco
                self.total_edit.setText(f"{total:.2f}")
                print(f"Total calculado: {total:.2f}")
            except ValueError:
                print("Erro: digite números válidos em quantidade e preço.")

        elif e.key() == Qt.Key_F3:
            print("Você apertou F3")

        elif e.key() == Qt.Key_F4:
            print("Você apertou F4")


# ======= EXECUÇÃO =======
app = QApplication(sys.argv)
janela = caixa2()
janela.show()
sys.exit(app.exec_())
