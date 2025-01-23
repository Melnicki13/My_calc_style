from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(40, 20, 321, 51))
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.answer_box = QtWidgets.QLineEdit(self.top_frame)
        self.answer_box.setReadOnly(True)  # Am facut setare ca sa fie read only ca sa nu poata
        #sa fie modificat manual de catre cineva
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.answer_box.setFont(font)
        self.answer_box.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.answer_box.setObjectName("answer_box")
        self.horizontalLayout.addWidget(self.answer_box)
        self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
        self.bottom_frame.setGeometry(QtCore.QRect(40, 120, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bottom_frame.setFont(font)
        self.bottom_frame.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.bottom_frame.setObjectName("bottom_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.bottom_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 133, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(45, 133, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_reset.setFont(font)
        self.btn_reset.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_reset.setObjectName("btn_reset")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 170, 320, 156))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_7 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 0, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 0, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 0, 2, 1, 1)
        self.btn_multiplication = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_multiplication.setFont(font)
        self.btn_multiplication.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_multiplication.setObjectName("btn_multiplication")
        self.gridLayout_2.addWidget(self.btn_multiplication, 0, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout_2.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"background-color: rgb(85, 170, 0);")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout_2.addWidget(self.btn_plus, 2, 3, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_2.addWidget(self.btn_dot, 3, 0, 1, 1)
        self.btn_zero = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_zero.setObjectName("btn_zero")
        self.gridLayout_2.addWidget(self.btn_zero, 3, 1, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout_2.addWidget(self.btn_equal, 3, 2, 1, 1)
        self.btn_slash = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_slash.setFont(font)
        self.btn_slash.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_slash.setObjectName("btn_slash")
        self.gridLayout_2.addWidget(self.btn_slash, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
          # aicea creem conexiunile fiecarui buton inclusiv celor al operatiilor

        # Butoanele cu numere (1-9, 0) unde self.btn_? este butonul propriu-zis din interfață
        #.clicked este semnalul care se activează când apeși butonul
        #.connect() face legătura între apăsarea butonului și funcția care trebuie executată
        #lambda :self.pressed(?) este o funcție temporară care transmite numărul ? către funcția pressed
        self.btn_1.clicked.connect(lambda :self.pressed(1))
        self.btn_2.clicked.connect(lambda: self.pressed(2))
        self.btn_3.clicked.connect(lambda: self.pressed(3))
        self.btn_4.clicked.connect(lambda: self.pressed(4))
        self.btn_5.clicked.connect(lambda: self.pressed(5))
        self.btn_6.clicked.connect(lambda: self.pressed(6))
        self.btn_7.clicked.connect(lambda: self.pressed(7))
        self.btn_8.clicked.connect(lambda: self.pressed(8))
        self.btn_9.clicked.connect(lambda: self.pressed(9))

        #Butoanele pentru operații (+, -, *, /) funcționează la fel ca butoanele cu numere
        #Diferența este că transmite simboluri pentru operații ("+", "-", "*", "/") în loc de numere
        self.btn_plus.clicked.connect(lambda: self.pressed("+"))
        self.btn_minus.clicked.connect(lambda: self.pressed("-"))
        self.btn_slash.clicked.connect(lambda: self.pressed("/"))
        self.btn_multiplication.clicked.connect(lambda: self.pressed("*"))
        self.btn_dot.clicked.connect(lambda: self.pressed("."))
        self.btn_zero.clicked.connect(lambda: self.pressed(0))
          # Butoanele pentru funcții speciale nu folosesc lambda pentru că nu trebuie să transmită parametri


        self.btn_equal.clicked.connect(self.equal) #equal calculează rezultatul
        self.btn_reset.clicked.connect(self.all_clear)  #all_clear șterge tot
        self.btn_cancel.clicked.connect(self.clear)  #clear șterge ultima cifră introdusă


    def pressed(self,number):  # Scriem o functie ca atunci cand apesi unul dintre butoane sa apara
        #pe displayul calculatorului
        self.answer_box.insert(str(number)) # trebuie sa folosim str atunci cand e chemat cu funcia lambda
    def equal(self):
        content = self.answer_box.text().strip()#acesta o sa ne deie raspunsul in partea de sus a calculatorului
        answer = eval(content) #Funcția eval(content) este o funcție încorporată
        #în Python care evaluează un șir de caractere ca și cod Python
        self.answer_box.setText(str(answer)) # punem  string deoarece setText() accepta doar text
    def all_clear(self):   ## Șterge TOT conținutul din caseta de text
        self.answer_box.clear()
    def clear(self):
        content = self.answer_box.text().strip()
        self.answer_box.setText(content[:-1]) #:-1 inseamna ca o sa stearga de la inceput pana la ultimul
        #cate un numar pe rand daca in loc de -1 punem -2 o sa stearga cate 2



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Calc"))
        self.btn_cancel.setText(_translate("MainWindow", "DEL"))
        self.btn_reset.setText(_translate("MainWindow", "AC"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_multiplication.setText(_translate("MainWindow", "*"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_slash.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion") # Aicea schimbam stilul de thema a aplicatiei se mai poate folosi
    # "Windows" "WindowsVista" "Fusion" "Macintosh" (doar pe macOS)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
