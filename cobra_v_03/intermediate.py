class Car:
    
    def __init__(self , name):
        self.name = name
    
    def start(self):
        print("dew dew dew ...... ")
        
    def beep(self):
        print("peeeeeeeee...." , self.name)
        
volvo = Car("hii");
abc = Car("hii2");
volvo.beep()
abc.beep()