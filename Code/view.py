from Account import Account
from Controller import Controller


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