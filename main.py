import random
import json
import secrets
import string


def generateCity() -> str :
    with open('resources/us_cities.json') as json_file:
        data = json.load(json_file)

        cities = data["cities"]
        random_index = random.randint(0, len(cities)-1)
        return (data["cities"][random_index]["city"]).lower()
    return "La Habana"

def generatePass() -> str :
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    password+="*"
    return password

def generateOcuppation() -> str :
    with open('resources/occupations.json') as json_file:
        data = json.load(json_file)
        occupations = data["occupations"]
        random_index = random.randint(0, len(occupations)-1)
        return (data["occupations"][random_index]).lower()
    return "actor"

def generateFriend():
    with open('resources/firstNames.json') as json_file:
        data = json.load(json_file)
        occupations = data["firstNames"]
        random_index = random.randint(0, len(occupations)-1)
        return (data["firstNames"][random_index]).lower()
    return "peter"


def generateMail() -> str :
    mail=""
    with open('resources/firstNames.json') as json_file:
        data = json.load(json_file)
        occupations = data["firstNames"]
        random_index = random.randint(0, len(occupations)-1)
        mail += (data["firstNames"][random_index]).lower()
    with open('resources/lastNames.json') as json_file:
        data = json.load(json_file)
        occupations = data["lastNames"]
        random_index = random.randint(0, len(occupations)-1)
        mail += "."+(data["lastNames"][random_index]).lower()
    
    mail+=str(random.randint(100, 999))+"@hotmail.com"
    return mail
    



def generateDate():
    return str(random.randint(1,28))+"_"+str(random.randint(1,12))+"_"+str(random.randint(1970,1999))


for x in range(10):
    print("{}:{}:{}:{}:{}:{}".format(generateMail(), generatePass(), generateCity(),generateFriend(), generateOcuppation(), generateDate()))
