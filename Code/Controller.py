from abc import ABC, abstractmethod
from dbCon import MySql

class Controller(ABC):
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