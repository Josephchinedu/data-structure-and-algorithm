class Array:
    def __init__(self) -> None:
        self.length = 0
        self.data = {}

    def __str__(self) -> str:
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        lastItem = self.data[self.length - 1]

        del self.data[self.length-1]

        self.length -= 1

        return lastItem

    def delete(self,index):
        deleteditem = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]

        del self.data[self.length-1]
        self.length-=1
        return deleteditem




arr=Array()
arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
print(arr)