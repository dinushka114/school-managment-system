from PyQt4 import QtCore, QtGui
import sqlite3
from stcdb import Ui_Form
import sip
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_logwin(object):
    def ok(self):
        mg=QtGui.QMessageBox()
        mg.setIcon(QtGui.QMessageBox.Warning)
        mg.setText("Please enter password correctly!")
        mg.setWindowTitle("Warning")
        mg.setStandardButtons(QtGui.QMessageBox.Ok)
        retval=mg.exec_()
        
    def logging(self):
        db = sqlite3.connect("STC_DB.db")
        cursor = db.cursor()

        logpsw = self.password.text()

        sql = ("select*from user")

        results = cursor.execute(sql)

        for row in results:
            pasw = row[0]

        if(logpsw==pasw):
            self.mainwin=QtGui.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.mainwin)
            self.mainwin.show()
            logwin.hide()
        else:
            #print("Enter password correctly!!")
            self.ok()
    def setupUi(self, logwin):
        logwin.setObjectName(_fromUtf8("logwin"))
        logwin.resize(632, 374)
        logwin.setMinimumSize(QtCore.QSize(632, 374))
        logwin.setMaximumSize(QtCore.QSize(632, 374))
        self.label_2 = QtGui.QLabel(logwin)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 46, 13))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(logwin)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 611, 351))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 90, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(180, 40, 431, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Old English Text MT"))
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 161))
        self.label.setStyleSheet(_fromUtf8("image: url(:/newPrefix/stc.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 175, 591, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(163, 20, 21, 141))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(80, 220, 91, 61))
        self.label_5.setStyleSheet(_fromUtf8("image: url(:/newPrefix/pass.png);"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.password = QtGui.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(190, 230, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName(_fromUtf8("password"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 280, 211, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.login = QtGui.QPushButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/log.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login.setIcon(icon1)
        self.login.setObjectName(_fromUtf8("login"))
        self.horizontalLayout.addWidget(self.login)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(190, 210, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.login.clicked.connect(self.logging)

        self.retranslateUi(logwin)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), logwin.close)
        QtCore.QMetaObject.connectSlotsByName(logwin)

    def retranslateUi(self, logwin):
        logwin.setWindowTitle(_translate("logwin", "Login", None))
        self.label_4.setText(_translate("logwin", "Database Login", None))
        self.label_3.setText(_translate("logwin", "St. Thomas\' Collage Matale", None))
        self.pushButton_2.setText(_translate("logwin", "Exit", None))
        self.login.setText(_translate("logwin", "Log In", None))
        self.label_6.setText(_translate("logwin", "Enter password here:", None))

import exit_rc
import log_rc
import password_rc
import stc_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    logwin = QtGui.QWidget()
    ui = Ui_logwin()
    ui.setupUi(logwin)
    logwin.show()
    sys.exit(app.exec_())

