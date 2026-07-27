class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        car=[]
        for i in range(len(position)):
            stack.append((position[i], speed[i]))

        stack.sort(reverse=True)

        for p,s in stack:


            fleet=((target)-p)/s
            if not car or fleet> car[-1]:
                car.append(fleet)

        return len(car)

        