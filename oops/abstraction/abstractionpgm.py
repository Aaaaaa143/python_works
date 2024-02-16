from abc import ABC,abstractmethod
class car(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelarate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class swift(car):

    def start(self):
        print("swift start method")

    def accelarate(self):
        print("swift accelarate method")

    def stop(self):
        print("swift stop method")

# obj of swift is only created when  all the abstract method is defined

obj=swift()
obj.start()