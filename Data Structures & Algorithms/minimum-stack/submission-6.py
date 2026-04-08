class MinStack:

    def __init__(self):
        self.st = []
        self.minele = float('inf')

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(0)
            self.minele = val
        else:
            self.st.append(val - self.minele)
            if val < self.minele:
                self.minele = val
        
        print(self.minele, self.st)


    def pop(self) -> None:
        if self.st[-1] >= 0:
            self.st.pop()
        else:
            top = self.st.pop(-1)
            self.minele = self.minele - top
            
        print(self.minele, self.st)

    def top(self) -> int:
        if self.st[-1] >= 0:
            return self.st[-1] + self.minele
        else:
            return self.minele

    def getMin(self) -> int:

        return self.minele
        
