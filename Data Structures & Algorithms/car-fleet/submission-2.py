class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        car=[]
        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        
        stack.sort(reverse=True)
        for p, s in stack:
            time=(target-p)/s
            if not car or time>car[-1]:
                car.append(time)
        return len(car)
        

        