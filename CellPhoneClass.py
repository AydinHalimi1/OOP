class CellPhone:

    #The __init__ method initializes the attributes
    def __init__(self,manu,model,price):
        self.__manufact = manu
        self.__model = model
        self.__retail_price = price

    #The set_manufact method accepts an arguement for the phone's manufacturer

    def set_manufact(self,manu):
        self.__manufact = manu

    #The set_model method accepts an arguement for the phone's model

    def set_model(self,model):
        self.__model = model

    #The set_retail_price method accepts an arguement for the phone's price

    def set_retail_price(self,price):
        self.__retail_price = price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

    def __str__(self):
        return "The model is: " + self.__model
