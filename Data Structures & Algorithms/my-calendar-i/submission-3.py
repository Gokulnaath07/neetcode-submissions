class MyCalendar:
    
    def __init__(self):
        self.MyCalendar=[]

    def book(self, startTime: int, endTime: int) -> bool:


#------exis
#  ------new return False
        if MyCalendar:
            for st, en in self.MyCalendar:
                if startTime<en and st<endTime:
                    return False
            self.MyCalendar.append((startTime, endTime))
            return True
        
        

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)