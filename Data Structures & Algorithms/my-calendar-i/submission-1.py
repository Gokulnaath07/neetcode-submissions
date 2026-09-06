class MyCalendar:
    
    def __init__(self):
        self.myCalendar=[]
        

    def book(self, startTime: int, endTime: int) -> bool:
                                #15,25
        if MyCalendar:
            for start, end in self.myCalendar:
                if startTime<end and start<endTime:
                    return False
        self.myCalendar.append((startTime, endTime))
        return True
        
        

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)