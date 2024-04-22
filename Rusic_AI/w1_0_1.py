from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(50, 490, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.pushButton_calculation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculation.setGeometry(QtCore.QRect(530, 490, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_calculation.setFont(font)
        self.pushButton_calculation.setObjectName("pushButton_count")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 651, 131))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выйти"))
        self.pushButton_calculation.setText(_translate("MainWindow", "Расчитать"))
        self.label_2.setText(_translate("MainWindow", "Какие-то параметры"))

    def actions(self):
        self.pushButton_exit.clicked.connect(self.exit)
        self.pushButton_calculation.clicked.connect(self.calculation)

    @staticmethod
    def exit():
        import sys
        sys.exit()

    def calculation(self):
        from result import Game
        game = Game()
        game.start_game()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
