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
        self.__allList = {}
        loadList = MySql.read("SELECT * FROM `list` WHERE ID_Board=%s", (self.getID(),))
        for index, value in enumerate(loadList):
            self.__allList[str(index)] = The_List()
            self.__allList[str(index)].setListID(value[0])
            self.__allList[str(index)].setListName(value[1])
    def setBoardName(self, param):
        self.__boardName = param
    def setBoardID(self, param):
        self.__boardID = param

    def getBoardName(self):
        return self.__boardName
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

    def delete(self):
        index = 0
        for index, is_list in enumerate(self.getAllList()):
            print(f"{index}. {self.getAllList()[is_list].getListName()}")
        print(f"{index+1}. Back")
        pilih = int(input("Enter the board to be removed: "))
        if pilih == index+1:
            pass
        elif pilih != index+1:
            MySql.update("DELETE FROM `list` WHERE ID_List = %s", (self.getAllList()[str(pilih)].getID(),))
            self.setAllList()
        else:
            self.delete()

    def invite(self):
        invite_email = str(input("Enter your friend's email: "))
        if self._is_Null(invite_email):
            get_ID_Account = self._loadID("SELECT ID_Account FROM `account` WHERE email = %s", (invite_email,))
            MySql.update("INSERT INTO `detail_board`(`ID_Account`, `ID_Board`) VALUES (%s, %s)", (get_ID_Account, self.getID()))
            print("Invite successful....")
        else:
            self.invite()
            