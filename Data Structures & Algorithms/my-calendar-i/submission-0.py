class MyCalendar:
    
    def __init__(self):
        self.myCalendar=[]
        

    def book(self, startTime: int, endTime: int) -> bool:
                                #15,25
        if self.myCalendar:
            for start, end in self.myCalendar:#(10,20)
                if start<endTime and startTime<end:
                    return False

        self.myCalendar.append((startTime, endTime))
        return True
    
        

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)