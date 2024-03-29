
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
        self.lineEditLastName = self.findChild(QtWidgets.QLineEdit, 'lineEditLastName')
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


        self.pushButtonCopyCity = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyCity') # Find the button
        self.lineEditCity = self.findChild(QtWidgets.QLineEdit, 'lineEditCity')
        self.pushButtonCopyCity.clicked.connect(self.copyCity)

        self.pushButtonCopyAbstract = self.findChild(QtWidgets.QPushButton, 'pushButtonCopyAbstract') # Find the button
        self.plainTextEditAbstract = self.findChild(QtWidgets.QPlainTextEdit, 'plainTextEditAbstract')
        self.pushButtonCopyAbstract.clicked.connect(self.copyAbstract)

        self.pushButtonNewId.clicked.connect(self.generatePerson)




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
        self.abstract = ""

        self.populate()        
        # self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!
        self.show()

    # def printButtonPressed(self):
    #     # This is executed when the button is pressed
    #     print('printButtonPressed')

    def generatePerson(self):
        self.appleId = AppleIdInfo()
        self.populate()

    def populate(self):
        


        self.name = self.appleId.name
        self.lastName = self.appleId.lastName
        self.mail = self.appleId.mail
        self.password = self.appleId.password
        self.city = self.appleId.city
        self.friend = self.appleId.friend
        self.occupation = self.appleId.occupation
        self.date = self.appleId.date
        self.phonePrefix = "786"
        self.phone = self.appleId.phone
        self.payCity = "Orlando"
        self.payState = "Florida"
        self.payStreet = "911 Evergreen"
        self.payCP = "32789"
        self.abstract = self.appleId.getStringResume()


        self.lineEditName.setText(self.name)
        self.lineEditLastName.setText(self.lastName)
        self.lineEditMail.setText(self.mail)
        self.lineEditPass.setText(self.password)
        self.lineEditFriend.setText(self.friend)
        self.lineEditOccupation.setText(self.occupation)
        self.lineEditDate.setText(self.date)
        self.lineEditPhonePre.setText(self.phonePrefix)
        self.lineEditPhone.setText(self.phone)
        self.lineEditCityPay.setText(self.payCity)
        self.lineEditCp.setText(self.payCP)
        self.lineEditStreet.setText(self.payStreet)
        self.lineEditCity.setText(self.city)
        self.plainTextEditAbstract.setPlainText(self.abstract)


    def copyName(self):
        clipboard.copy(self.lineEditName.text())

    def copyLastName(self):
        clipboard.copy(self.lineEditLastName.text())
    
    def copyMail(self):
        clipboard.copy(self.lineEditMail.text())

    def copyPass(self):
        clipboard.copy(self.lineEditPass.text())
    
    def copyFriend(self):
        clipboard.copy(self.lineEditFriend.text())

    def copyOccupation(self):
        clipboard.copy(self.lineEditOccupation.text())
    
    def copyDate(self):
        clipboard.copy(self.lineEditDate.text())
    
    
    def copyPhonePre(self):
        clipboard.copy(self.lineEditPhonePre.text())
    
    def copyPhone(self):
        clipboard.copy(self.lineEditPhone.text())
    
    
    def copyCityPay(self):
        clipboard.copy(self.lineEditCityPay.text())
    
    
    def copyCp(self):
        clipboard.copy(self.lineEditCp.text())
    
    
    def copyStreet(self):
        clipboard.copy(self.lineEditStreet.text())

    def copyCity(self):
        clipboard.copy(self.lineEditCity.text())

    def copyAbstract(self):
        clipboard.copy(self.abstract)    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GeneratorIcloudUser()
    window.setWindowTitle("IcloudHelper")
    app.exec_()



