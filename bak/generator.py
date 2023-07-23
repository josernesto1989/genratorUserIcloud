import random
import json
import secrets
import string

class ResourceGenerator:
    @staticmethod
    def generateCity() -> str:
        with open('resources/us_cities.json') as json_file:
            data = json.load(json_file)

            cities = data["cities"]
            random_index = random.randint(0, len(cities)-1)
            return (data["cities"][random_index]["city"]).lower()
        return "La Habana"

    @staticmethod
    def generatePass() -> str:
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        password = "1A{}z*".format(password)
        return password

    @staticmethod
    def generateOcuppation() -> str:
        with open('resources/occupations.json') as json_file:
            data = json.load(json_file)
            occupations = data["occupations"]
            random_index = random.randint(0, len(occupations)-1)
            return (data["occupations"][random_index]).lower()
        return "actor"

    @staticmethod
    def generateName() -> str:
        with open('resources/firstNames.json') as json_file:
            data = json.load(json_file)
            occupations = data["firstNames"]
            random_index = random.randint(0, len(occupations)-1)
            return (data["firstNames"][random_index]).lower()
        return "peter"

    @staticmethod
    def generateFriend() -> str:
        return ResourceGenerator.generateName()


    @staticmethod
    def generateLastName():
        with open('resources/lastNames.json') as json_file:
            data = json.load(json_file)
            occupations = data["lastNames"]
            random_index = random.randint(0, len(occupations)-1)
            return (data["lastNames"][random_index]).lower()
        return "smith"


    @staticmethod
    def generateMail(name, lastName) -> str:
        mail= name + lastName + str( random.randint(100, 999) ) + "@hotmail.com"
        return mail
    
    @staticmethod
    def generateMailV() -> str:
        name=generateName()
        lastName=generateLastName()
        generateMail(name,lastName)
        return mail

    @staticmethod
    def generateDate() -> str:
        return str(random.randint(1, 28))+"_"+str(random.randint(1, 12))+"_"+str(random.randint(1970, 1999))


    @staticmethod
    def telef7Digit() -> str:
        return str(random.randint(1000000, 9999999))

#    for x in range(10):
#        print("{}:{}:{}:{}:{}:{}".format(generateMail(), generatePass(),
#        generateCity(),generateFriend(), generateOcuppation(), generateDate()))
