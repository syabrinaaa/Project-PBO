from Controller import Controller
from dbCon import MySql
from card import Card

class The_List(Controller):
    def __init__(self):
        self.__listName = ''
        self.__listID = None
        self.__allCard = {}

    def addCard(self):
        nameCard = str(input("Enter a card name: "))
        if self._is_Null(nameCard):    
            key = str(len(self.__allCard))
            self.__allCard[key] = Card()
            self.__allCard[key].setCardName(nameCard)
            self.__allCard[key].setDeadline(str(input("Enter a deadline (optional) year-month-date: ")))
            MySql.update("INSERT INTO `card`(`card_name`, `deadline`, `ID_List`) VALUES (%s, %s, %s)", (self.__allCard[key].getCardName(), self.__allCard[key].getDeadline(), self.getID()))
            my_ID = self._loadID("SELECT ID_Card FROM card WHERE card_name = %s AND ID_List = %s", (self.__allCard[key].getCardName(), self.getID()))
            self.__allCard[key].setCardID(my_ID)
        else:
            print("Please enter an valid card name")
            self.addCard()
        
    def setAllCard(self):
        self.__allCard = {}
        loadCard = MySql.read("SELECT * FROM card WHERE ID_List=%s", (self.getID(),))
        for index, value in enumerate(loadCard):
            self.__allCard[str(index)] = Card()
            self.__allCard[str(index)].setCardID(value[0])
            self.__allCard[str(index)].setCardName(value[1])
            if value[2] != None:
                self.__allCard[str(index)].setDeadline(value[2])

    def setListName(self, param):
        self.__listName = param
    def setListID(self, param):
        self.__listID = param

    def getListName(self):
        return self.__listName
    def getID(self):
        return self.__listID
    def getAllCard(self):
        return self.__allCard

    def changeNameList(self):
        self.setListName(str(input("Enter a new name: ")))
        if self._is_Null(self.getListName()):
            MySql.update("UPDATE list SET `list_name`=%s WHERE `ID_List`= %s", (self.getListName(), self.getID()))
        else:
            print('Please enter an valid list name')
            self.changeNameList()

    def delete(self):
        index = 0
        for index, is_card in enumerate(self.getAllCard()):
            print(f"{index}. {self.getAllCard()[is_card].getCardName()}")
        print(f"{index+1}. Back")
        pilih = int(input("Enter the board to be removed: "))
        if pilih == index+1:
            pass
        elif pilih != index+1:
            MySql.update("DELETE FROM `card` WHERE ID_Card = %s", (self.getAllCard()[str(pilih)].getID(),))
            self.setAllCard()
        else:
            self.delete()