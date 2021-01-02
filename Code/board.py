from Controller import Controller
from dbCon import MySql
from The_list import The_List

class Board(Controller):
    def __init__(self):
        self.__boardName = ''
        self.__boardID = None
        self.__allList = {}

    def addList(self):
        nameList = str(input("Enter a list name: "))
        if self._is_Null(nameList):
            key = str(len(self.__allList))
            self.__allList[key] = The_List()
            self.__allList[key].setListName(nameList)
            MySql.update("INSERT INTO `list`(`list_name`, `ID_Board`) VALUES (%s, %s)", (self.__allList[key].getListName(), self.getID()))
            my_ID = self._loadID("SELECT ID_List FROM list WHERE list_name = %s AND ID_Board = %s", (self.__allList[key].getListName(), self.getID()))
            self.__allList[key].setListID(my_ID)
        else:
            print("Please enter an valid list name")
            self.addList()
        
    def setAllList(self):
        loadList = MySql.read("SELECT * FROM `list` WHERE ID_Board=%s", (self.getID(),))
        for index, value in enumerate(loadList):
            self.__allList[str(index)] = The_List()
            self.__allList[str(index)].setListID(value[0])
            self.__allList[str(index)].setListName(value[1])
    def setBoardName(self, param):
        self.boardName = param
    def setBoardID(self, param):
        self.__boardID = param

    def getBoardName(self):
        return self.boardName
    def getID(self):
        return self.__boardID
    def getAllList(self):
        return self.__allList



    def changeNameBoard(self):
        self.setBoardName(str(input("Enter a new name: ")))
        if self._is_Null(self.getBoardName()):
            MySql.update("UPDATE `board` SET `Board_Name`=%s WHERE `ID_Board`= %s", (self.getBoardName(), self.getID()))
        else:
            print('Please enter an valid board name')
            self.changeNameBoard()