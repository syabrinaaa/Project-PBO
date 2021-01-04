from Controller import Controller
from dbCon import MySql
from board import Board

class Account(Controller):
    def __init__(self):
        self._accountID = 0
        self._email = ''
        self._fullName = ''
        self._password = ''
        self._board = {}

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
        self._accountID = 0
        self._email = ''
        self._fullName = ''
        self._password = ''
        self._board = {}

    def getProfile(self):
        print(f"""
----------Profile----------
Email: {self.getEmail()}
Name: {self.getFullName()}
---------------------------""")

    def addBoard(self):
        nameBoard=str(input("Enter a board name: "))
        if self._is_Null(nameBoard):
            key = str(len(self._board))
            self._board[key] = Board()
            self._board[key].setBoardName(nameBoard)
            MySql.update("INSERT INTO `board`(`Board_Name`) VALUES (%s)", (self._board[key].getBoardName(),))
            my_ID = self._loadID("SELECT `ID_Board` FROM `board` WHERE `Board_Name` = %s", (self._board[key].getBoardName(),))
            self._board[key].setBoardID(my_ID)
            MySql.update("INSERT INTO `detail_board`(`ID_Account`, `ID_Board`) VALUES (%s, %s)", (self.getID(), self._board[key].getID()))
        else:
            print("Please enter an valid board name")
            self.addBoard()

    def setAccountID(self, param):
        self._accountID = param
    def setEmail(self, param):
        self._email = param
    def setFullName(self, param):
        self._fullName = param
    def setPassword(self, param):
        self._password = param
    def setBoard(self):
        self._board = {}
        loadBoard = MySql.read(f"SELECT board.ID_Board, board.Board_Name FROM board JOIN detail_board ON board.ID_Board = detail_board.ID_Board WHERE detail_board.ID_Account = {self.getID()}", ())
        for index, value in enumerate(loadBoard):
            self._board[str(index)] = Board()
            self._board[str(index)].setBoardID(value[0])
            self._board[str(index)].setBoardName(value[1])


    def getID(self):
        return self._accountID
    def getEmail(self):
        return self._email
    def getFullName(self):
        return self._fullName
    def getPassword(self):
        return self._password
    def getBoard(self):
        return self._board

    def saveChange(self):
        MySql.update("UPDATE `account` SET `full_Name`=%s,`email`=%s,`password`=%s WHERE `ID_Account`=%s", (self.getFullName(), self.getEmail(), self.getPassword(), self.getID()))

    def delete(self):
        index = 0
        for index, board in enumerate(self.getBoard()):
            print(f"{index}. {self.getBoard()[board].getBoardName()}")
        print(f"{index+1}. Back")
        pilih = int(input("Enter the board to be removed: "))
        if pilih == index+1:
            pass
        elif pilih != index+1:
            MySql.update("DELETE FROM `detail_board` WHERE ID_Account = %s AND ID_Board = %s", (self.getID(), self.getBoard()[str(pilih)].getID()))
            self.setBoard()
        else:
            self.delete()