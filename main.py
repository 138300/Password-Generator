from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QMessageBox
import string,random,pyperclip 


class Ui_Password_Generator(object):
    def setupUi(self, Password_Generator):
        Password_Generator.setObjectName("Password_Generator")
        Password_Generator.resize(888, 252)
        Password_Generator.setStyleSheet("background-color:#222831;")
        Password_Generator.setWindowIcon(QIcon('icons/padlock (2).png'))
        Password_Generator.setStyleSheet("background-color:#222831;")
        self.centralwidget = QtWidgets.QWidget(Password_Generator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.length_input = QtWidgets.QLineEdit(self.centralwidget)
        self.length_input.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.length_input.setFont(font)
        self.length_input.setStyleSheet("background-color:#F5F5F5;\n""border-radius:15px;\n""padding:5px 10px;\n""")
        self.length_input.setObjectName("length_input")
        self.gridLayout.addWidget(self.length_input, 0, 0, 1, 1)
        self.count_input = QtWidgets.QLineEdit(self.centralwidget)
        self.count_input.setMinimumSize(QtCore.QSize(400, 30))
        self.count_input.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.count_input.setFont(font)
        self.count_input.setStyleSheet("background-color:#F5F5F5;\n""border-radius:15px;\n""padding:5px 10px;\n""")
        self.count_input.setObjectName("count_input")
        self.gridLayout.addWidget(self.count_input, 2, 0, 1, 1)
        self.power = QtWidgets.QComboBox(self.centralwidget)
        self.power.setMinimumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.power.setFont(font)
        self.power.setStyleSheet("QComboBox\n""{\n""background-color:#F5F5F5;\n""border-radius:15px;\n""padding:5px 10px;\n""} \n""QComboBox::drop-down {\n""border-radius:1px;\n""padding:10px 15px;\n""}\n""")
        self.power.setObjectName("power")
        self.power.addItem("")
        self.power.addItem("")
        self.power.addItem("")
        self.gridLayout.addWidget(self.power, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_btn.sizePolicy().hasHeightForWidth())
        self.create_btn.setSizePolicy(sizePolicy)
        self.create_btn.setMinimumSize(QtCore.QSize(200, 35))
        self.create_btn.setMaximumSize(QtCore.QSize(500, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_btn.setFont(font)
        self.create_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_btn.setStyleSheet("#create_btn{\n""background-color:#FF2E63;\n""border-radius:15px;\n""color:white;\n""}\n""#create_btn::hover{\n""background-color:white;\n""color:#FF2E63;\n""}\n""#create_btn::pressed{\n""border-radius:5px;\n""}\n""\n""")
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.copy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.copy_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.copy_btn.setFont(font)
        self.copy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_btn.setStyleSheet("#copy_btn{\n""background-color:#08D9D6;\n""border-radius:15px;\n""color:white;\n""}\n""#copy_btn::hover{\n""background-color:white;\n""color:#08D9D6;\n""}\n""#copy_btn::pressed{\n""border-radius:5px;\n""}\n""")
        self.copy_btn.setObjectName("copy_btn")
        self.horizontalLayout.addWidget(self.copy_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        Password_Generator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Password_Generator)
        QtCore.QMetaObject.connectSlotsByName(Password_Generator)

        self.create_btn.clicked.connect(self.create_password)
        self.copy_btn.clicked.connect(self.copy_password)

    def retranslateUi(self, Password_Generator):
        _translate = QtCore.QCoreApplication.translate
        Password_Generator.setWindowTitle(_translate("Password_Generator", "MainWindow"))
        self.length_input.setPlaceholderText(_translate("Password_Generator", "length"))
        self.count_input.setPlaceholderText(_translate("Password_Generator", "count"))
        self.power.setItemText(0, _translate("Password_Generator", "weak"))
        self.power.setItemText(1, _translate("Password_Generator", "normal"))
        self.power.setItemText(2, _translate("Password_Generator", "strong"))
        self.create_btn.setText(_translate("Password_Generator", "Create"))
        self.copy_btn.setText(_translate("Password_Generator", "Copy"))

    def create_password(self):
        try:
            power=self.power.currentText()
            length=int(self.length_input.text())
            count=int(self.count_input.text())
            global list_of_password
            list_of_password=[]
        
            if power=='weak':
                list_of_password.clear()
                all_characters=string.ascii_letters
                for i in range(count):
                    psw=random.sample(all_characters,length)                       
                    created_password=''.join(psw)
                    list_of_password.append(created_password)
                    print(created_password)
        
            elif power=='normal':
                list_of_password.clear()
                all_characters=string.ascii_letters+string.digits
                for i in range(count):
                    psw=random.sample(all_characters,length)                       
                    created_password=''.join(psw)
                    list_of_password.append(created_password)
                    print(created_password)
        
            elif power=='strong':
                list_of_password.clear()
                all_characters=string.ascii_letters+string.digits+string.punctuation
                for i in range(count):
                    psw=random.sample(all_characters,length)                       
                    created_password=''.join(psw)
                    list_of_password.append(created_password)
                    print(created_password)

        except:
            QMessageBox.warning(self.centralwidget,'error','something went wrong')

    def copy_password(self):
        pyperclip.copy(list_of_password[-1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Password_Generator = QtWidgets.QMainWindow()
    ui = Ui_Password_Generator()
    ui.setupUi(Password_Generator)
    Password_Generator.show()
    sys.exit(app.exec_())
