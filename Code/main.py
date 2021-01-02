from dbCon import MySql
from abc import ABC, abstractmethod

class Controller:
    def _is_Null(self, *argv):
        for i in argv:
            if len(i) == 0:
                return False
        return True

    def _loadID(self, query, value):
        is_ID = MySql.read(query, value)
        return is_ID[0][0]

    @staticmethod
    def isEmpty_Table(table):
        if len(table) != 0:
            return True
        return False

    @abstractmethod
    def getID(self):
        pass

class Account(Controller):
    def __init__(self):
        self.__accountID = 0
        self.__email = ''
        self.__fullName = ''
        self.__password = ''
        self.__board = {}

    def register(self):
        self.setEmail(str(input("Enter Email: ")))
        self.setFullName(str(input("Enter Full Name: ")))
        self.setPassword(str(input("Enter Password: ")))
        
        if self._is_Null(self.getEmail(), self.getFullName(), self.getPassword()):
            MySql.update("INSERT INTO `account`(`full_Name`, `email`, `password`) VALUES (%s, %s, %s)", (self.getFullName(), self.getEmail(), self.getPassword()))
            print("\nRegistration was successful")

            my_ID = self._loadID("SELECT `ID_Account` FROM `account` WHERE full_Name = %s AND email = %s AND password = %s", (self.getFullName(), self.getEmail(), self.getPassword()))
            self.setAccountID(my_ID)
            self.setBoard()
        else:
            print("Please enter an valid email, full name and password")
            self.register()

    def login(self):
        self.setEmail(str(input("Enter Email: ")))
        self.setPassword(str(input("Enter Password: ")))

        if self._is_Null(self.getEmail(), self.getPassword()):
            valid_account = MySql.read("SELECT * FROM `account` WHERE email = %s AND password = %s", (self.getEmail(), self.getPassword()))
            if len(valid_account) == 0:
                print("----------Please Enter a valid email and password----------\n")
                self.login()
            else:
                self.setAccountID(valid_account[0][0])
                self.setFullName(valid_account[0][1])
                self.setBoard()
        else:
            print("Please enter an valid email and password")
            self.login()

    def logout(self):
        self.__accountID = 0
        self.__email = ''
        self.__fullName = ''
        self.__password = ''
        self.__board = {}

    def getProfile(self):
        print(f"""
----------Profile----------
Email: {self.getEmail()}
Name: {self.getFullName()}
---------------------------""")

    def addBoard(self):
        nameBoard=str(input("Enter a board name: "))
        if self._is_Null(nameBoard):
            key = str(len(self.__board))
            self.__board[key] = Board()
            self.__board[key].setBoardName(nameBoard)
            MySql.update("INSERT INTO `board`(`Board_Name`) VALUES (%s)", (self.__board[key].getBoardName(),))
            my_ID = self._loadID("SELECT `ID_Board` FROM `board` WHERE `Board_Name` = %s", (self.__board[key].getBoardName(),))
            self.__board[key].setBoardID(my_ID)
            MySql.update("INSERT INTO `detail_board`(`ID_Account`, `ID_Board`) VALUES (%s, %s)", (self.getID(), self.__board[key].getID()))
        else:
            print("Please enter an valid board name")
            self.addBoard()

    def setAccountID(self, param):
        self.__accountID = param
    def setEmail(self, param):
        self.__email = param
    def setFullName(self, param):
        self.__fullName = param
    def setPassword(self, param):
        self.__password = param
    def setBoard(self):
        loadBoard = MySql.read(f"SELECT board.ID_Board, board.Board_Name FROM board JOIN detail_board ON board.ID_Board = detail_board.ID_Board WHERE detail_board.ID_Account = {self.getID()}", ())
        for index, value in enumerate(loadBoard):
            self.__board[str(index)] = Board()
            self.__board[str(index)].setBoardID(value[0])
            self.__board[str(index)].setBoardName(value[1])


    def getID(self):
        return self.__accountID
    def getEmail(self):
        return self.__email
    def getFullName(self):
        return self.__fullName
    def getPassword(self):
        return self.__password
    def getBoard(self):
        return self.__board

    def saveChange(self):
        MySql.update("UPDATE `account` SET `full_Name`=%s,`email`=%s,`password`=%s WHERE `ID_Account`=%s", (self.getFullName(), self.getEmail(), self.getPassword(), self.getID()))

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
        loadCard = MySql.read("SELECT * FROM card WHERE ID_List=%s", (self.getID(),))
        for index, value in enumerate(loadCard):
            self.__allCard[str(index)] = Card()
            self.__allCard[str(index)].setCardID(value[0])
            self.__allCard[str(index)].setCardName(value[1])
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

def view_card(user, board, the_list):
    the_list.setAllCard()
    print(f"-----------My Card in {the_list.getListName()}-----------")
    while True:
        index = 0
        if len(the_list.getAllCard()) != 0:
            for index, key_card in enumerate(the_list.getAllCard()):
                print(f"{index}. {the_list.getAllCard()[key_card].getCardName()} {the_list.getAllCard()[key_card].getDeadline()}")
        else:
            print("-----You don't have a card-----")
        print(f"""
{index+1}. Add Card
{index+2}. Change List Name
{index+3}. Back
""")

        pilih = int(input("Input Menu: "))
        if pilih == index+1:
            the_list.addCard()
        elif pilih == index+2:
            the_list.changeNameList()
        elif pilih == index+3:
            view_list(user, board)
        else:
            print("Enter an valid input")

def view_list(user, board):
    board.setAllList()
    print(f"-----------My List in {board.getBoardName()}-----------")
    while True:
        index = 0
        if len(board.getAllList()) != 0:
            for index, key_list in enumerate(board.getAllList()):
                print(f"{index}. {board.getAllList()[key_list].getListName()}")
        else:
            print("-----You don't have a list-----")
        print(f"""
{index+1}. Add List
{index+2}. Change Board Name
{index+3}. Back
""")

        pilih = int(input("Input Menu: "))
        if pilih == index+1:
            board.addList()
        elif pilih == index+2:
            board.changeNameBoard()
        elif pilih == index+3:
            view_board(user)
        elif pilih <= index:
            view_card(user, board, board.getAllList()[str(pilih)])
        else:
            print("Enter an valid input")

def view_board(user):
    print("-----------My Board-----------")
    while True:
        index = 0
        if Controller.isEmpty_Table(user.getBoard()):
            for index, board in enumerate(user.getBoard()):
                print(f"{index}. {user.getBoard()[board].getBoardName()}")
        else:
            print("-----You don't have a board-----")
        print(f"""
{index+1}. Add Board
{index+2}. Back
""")

        pilih = int(input("Input Menu: "))
        if pilih == index+1:
            user.addBoard()
        elif pilih == index+2:
            view_beranda(user)
        elif pilih <= index:
            view_list(user, user.getBoard()[str(pilih)])
        else:
            print("Enter an valid input")


def view_profile(user):
    while True:
        user.getProfile()
        print("""
Menu:
1. Change Name
2. Change Email
3. Back
            """)

        pilih = int(input("Input Menu: "))
        if pilih == 1:
            user.setFullName(str(input("Enter a new name: ")))
        elif pilih == 2:
            user.setEmail(str(input("Enter a new email: ")))
        elif pilih == 3:
            user.saveChange()
            view_beranda(user)
        else:
            print("Enter an valid input menu")

def view_beranda(user):
    while True:
        print("""
Hello {}
Menu:
1. Board
2. Profile
3. Logout
        """.format(user.getFullName()))

        pilih = int(input("Input Menu: "))
        if pilih == 1:
            view_board(user)
        elif pilih == 2:
            view_profile(user)
        elif pilih == 3:
            user.logout()
            main()
        else:
            print("Enter an valid input menu")
    


def main():
    while True:
        print("""
Welcome to Synergasia
Main menu:
1. Register
2. Login
3. Exit
        """)
        pilih = int(input("Input Menu: "))
        user = Account()
        if pilih == 1:
            user.register()
            view_beranda(user)
        elif pilih == 2:
            user.login()
            view_beranda(user)
        elif pilih == 3:
            exit()
        else:
            print("Enter an valid input menu")



main()