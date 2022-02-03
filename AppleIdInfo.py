# This Python file uses the following encoding: utf-8
from generator import ResourceGenerator


class AppleIdInfo:
    def __init__(self):
        self.name = "Jon"
        self.lastName = "Doe"
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
        self.changePerson()

    def changePerson(self):
        self.name = ResourceGenerator.generateName()
        self.lastName = ResourceGenerator.generateLastName()
        self.mail = ResourceGenerator.generateMail(self.name, self.lastName)
        self.password = ResourceGenerator.generatePass()
        self.city = ResourceGenerator.generateCity()
        self.friend = ResourceGenerator.generateFriend()
        self.occupation = ResourceGenerator.generateOcuppation()
        self.date = ResourceGenerator.generateDate()
        self.phone = ResourceGenerator.telef7Digit()

    def getStringResume(self):
        return "{}:{}:{}:{}:{}:{}".format(self.mail, self.password,
            self.city, self.friend, self.occupation, self.date)



#    for x in range(10):
#        print("{}:{}:{}:{}:{}:{}".format(generateMail(), generatePass(),
#        generateCity(),generateFriend(), generateOcuppation(), generateDate()))
