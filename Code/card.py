from Controller import Controller
from dbCon import MySql

class Card(Controller):
    def __init__(self):
        self.__cardName = ""
        self.__cardID = None
        self.__deadline = ""

    def setCardName(self, param):
        self.__cardName = param
    def setCardID(self, param):
        self.__cardID = param
    def setDeadline(self, param):
        self.__deadline = param

    def getCardName(self):
        return self.__cardName
    def getID(self):
        return self.__cardID
    def getDeadline(self):
        return self.__deadline