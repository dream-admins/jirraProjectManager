__author__ = 'dream-admin'

class JItem:

    def getOrder(self):
        return self.__order

    def setOrder(self, order):
        self.__order = order

    def getKey(self):
        return self.__key

    def setKey(self, key):
        self.__key = key

    def getSummaryText(self):
        return self.__summaryText

    def setSummaryText(self, summaryText):
        self.__summaryText = summaryText

    def getSelected(self):
        return self.__selected

    def setSelected(self, selected):
        self.__selected = selected
