class cars:
# define Private variables    
    __name=None
    __type=None

    def __init__(self,name,typ):
        self.__name=name
        self.__type=typ        
    def printcars(self):
        print self.__name
        print self.__type

class bus(cars):
    def __init__(self,name,typ,size):
        self.__name=name
        self.__type=typ  
        self.__size=size
    def printbuses(self):
        print self.__name
        print self.__type
        
c1=cars("Wolkswagen","Sedan")
c2=cars("Toyota","Sedan")
print "WE PRINT C1 CARS NOW"
print c1.printcars()
print "WE PRINT C2 CARS NOW"
print c2.printcars()


b1=bus("Ashoka","Truck","larege")
print "WE PRINT BUSES NOW"
print b1.printbuses()
