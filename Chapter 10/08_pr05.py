class Train:
    
    def __init__(self) -> None:
        self.seats = 78
        self.fare = 100
    
    def bookTickets(self):
        self.seats = self.seats - 1
        
    def getStatus(self):
        print(self.seats)
        
    def getFareInfo(self):
        print(self.fare)   
        
tr = Train()  
tr.getFareInfo()
tr.getStatus()
tr.bookTickets()
tr.getStatus()