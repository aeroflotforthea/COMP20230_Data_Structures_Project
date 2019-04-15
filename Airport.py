
class Airport:
    
    def __init__(self, name, longitude, latitude, exchange_rate):
        self.__name = name
        self.longitude = longitude
        self.latitude = latitude
        self.__exchange_rate = exchange_rate
        
    def getExchangeRate(self):
        return self.__exchange_rate
    
    def getName(self):
        return self.__name
    
    def setExchangeRate(self, new_exchange_rate):
        self.__exchange_rate = new_exchange_rate
        print("Exchange rate set to ", new_exchange_rate)
        return self.getExchangeRate()