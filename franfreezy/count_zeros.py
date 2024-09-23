#Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0 's in that array. For example, 
#given [1, 0, 5, 6, 0, 2], the function/method should return 2.
class CountZeros:
    def __init__(self, array):
        self.array = array
    def zerocounter(self):
        count=0
        for i in range(len(self.array)):
            if self.array[i] == 0:
                count += 1
        
        return count


if __name__ == '__main__':
    c = CountZeros([1, 0, 5, 6, 0, 2])
    print(c.zerocounter())