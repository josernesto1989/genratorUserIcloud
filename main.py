# This Python file uses the following encoding: utf-8
import os
from AppleIdInfo import AppleIdInfo
from PyQt5 import QtWidgets, uic
import sys
import pyperclip as clipboard

class GeneratorIcloudUser(QtWidgets.QWidget):
    def __init__(self):
        super(GeneratorIcloudUser, self).__init__()
        uic.loadUi('basic.ui', self)

        self.appleId = AppleIdInfo()

        self.pushButtonCopyName = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyName') # Find the button
        self.lineEditName = self.findChild(QtWidgets.QLineEdit, 'lineEditName')
        self.pushButtonCopyName.clicked.connect(self.copyName)

        self.pushButtonCopyLastName = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyLastName') # Find the button
        self.lineEditName = self.findChild(QtWidgets.QLineEdit, 'lineEditLastName')
        self.pushButtonCopyLastName.clicked.connect(self.copyLastName)

        self.pushButtonCopyMail = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyMail') # Find the button
        self.lineEditMail = self.findChild(QtWidgets.QLineEdit, 'lineEditMail')
        self.pushButtonCopyMail.clicked.connect(self.copyMail)

        self.pushButtonCopyPass = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyPass') # Find the button
        self.lineEditPass = self.findChild(QtWidgets.QLineEdit, 'lineEditPass')
        self.pushButtonCopyPass.clicked.connect(self.copyPass)

        self.pushButtonCopyFriend = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyFriend') # Find the button
        self.lineEditFriend = self.findChild(QtWidgets.QLineEdit, 'lineEditFriend')
        self.pushButtonCopyFriend.clicked.connect(self.copyFriend)

        self.pushButtonCopyOccupation = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyOccupation') # Find the button
        self.lineEditOccupation = self.findChild(QtWidgets.QLineEdit, 'lineEditOccupation')
        self.pushButtonCopyOccupation.clicked.connect(self.copyOccupation)

        self.pushButtonCopyDate = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyDate') # Find the button
        self.lineEditDate = self.findChild(QtWidgets.QLineEdit, 'lineEditDate')
        self.pushButtonCopyDate.clicked.connect(self.copyDate)

        self.pushButtonCopyPhonePre = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyPhonePre') # Find the button
        self.lineEditPhonePre = self.findChild(QtWidgets.QLineEdit, 'lineEditPhonePre')
        self.pushButtonCopyPhonePre.clicked.connect(self.copyPhonePre)

        self.pushButtonCopyPhone = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyPhone') # Find the button
        self.lineEditPhone = self.findChild(QtWidgets.QLineEdit, 'lineEditPhone')
        self.pushButtonCopyPhone.clicked.connect(self.copyPhone)

        self.pushButtonCopyCityPay = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyCityPay') # Find the button
        self.lineEditCityPay = self.findChild(QtWidgets.QLineEdit, 'lineEditCityPay')
        self.pushButtonCopyCityPay.clicked.connect(self.copyCityPay)

        self.pushButtonCopyCp = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyCp') # Find the button
        self.lineEditCp = self.findChild(QtWidgets.QLineEdit, 'lineEditCp')
        self.pushButtonCopyCp.clicked.connect(self.copyCp)

        self.pushButtonCopyStreet = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyStreet') # Find the button
        self.lineEditStreet = self.findChild(QtWidgets.QLineEdit, 'lineEditStreet')
        self.pushButtonCopyStreet.clicked.connect(self.copyStreet)


        self.name = "jon"
        self.lastName = "doe"
        self.mail = "jon.doe456@hotmail.com"
        self.password = "s3CreT*"
        self.city = "la habana"
        self.friend = "pepe"
        self.occupation = "cochero"
        self.date = "21_1_1990"
        self.phonePrefix = "786"
        self.phone = "5555555"
        self.payCity = "Orlando"
        self.payState = "Florida"
        self.payStreet = "911 Evergreen"
        self.payCP = "32789"
        
        # self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!
        self.show()

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')

    def generatePerson(self):
        self.appleId = AppleIdInfo()

    def populate(self):
        pass
        

    def copyName(self):
        clipboard.copy(self.lineEditName.text())

    def copyLastName(self):
        clipboard.copy(self.lineEditLastName.text())
    
    def copyMail(self):
        clipboard.copy(self.lineEditName.text())

    def copyPass(self):
        clipboard.copy(self.lineEditLastName.text())
    
    def copyFriend(self):
        clipboard.copy(self.lineEditName.text())

    def copyOccupation(self):
        clipboard.copy(self.lineEditLastName.text())
    
    
    def copyDate(self):
        clipboard.copy(self.lineEditLastName.text())
    
    
    def copyPhonePre(self):
        clipboard.copy(self.lineEditLastName.text())
    
    
    def copyPhone(self):
        clipboard.copy(self.lineEditLastName.text())
    
    
    def copyCityPay(self):
        clipboard.copy(self.lineEditLastName.text())
    
    
    def copyCp(self):
        clipboard.copy(self.lineEditLastName.text())
    
    
    def copyStreet(self):
        clipboard.copy(self.lineEditLastName.text())

    
    



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GeneratorIcloudUser()
    app.exec_()



