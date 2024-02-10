import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\rohan\\OneDrive\\Desktop\\CT16\\Automation_Testing#Part_2 By Tushar Sir\\nop_com\\class 1 nopcom_Pytest\\Configuration\\config.ini")

# config.read("..\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password

