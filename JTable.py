__author__ = 'dream-admin'
from JItem import JItem
import os

class JTable():
    __default_color = "\033[0;36;40m"
    __selected_color = "\033[1;32;40m"
    __selected_current_color = "\033[1;31;40m"
    __selectedItemIndex = 1


    def moveUp(self):
        if 0 <= self.__selectedItemIndex - 1:
            self.__selectedItemIndex -= 1
            self.clear()
            self.__load_screen()

    def moveDown(self):
        if len(self.__list) > self.__selectedItemIndex + 1:
            self.__selectedItemIndex += 1
            self.clear()
            self.__load_screen()


    def setItems(self, itemList):
        self.__list = itemList
        self.__load_screen()

    def clear(self):
        os.system('clear')
#        print('\n' * 100)

    def __load_screen(self):
        print("\033[1;34;40m")
        print("JIRA TASK MANAGER".center(100, '='))
        it = iter(self.__list)
        for item in it:
            if isinstance(item,JItem):
                color = self.__default_color
                if item.getOrder() == self.__selectedItemIndex:
                    color = self.__selected_color
                elif item.getSelected() == True:
                    color = self.__selected_current_color

                print("{}{} - {}".format(color, item.getKey(), item.getSummaryText()))

    def selectCurrent(self):
        item = self.__list[self.__selectedItemIndex]
        item.setSelected(not item.getSelected())
        self.moveDown()
