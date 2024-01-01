class Assignment2_Python_Template(object):
    ''' This method should accept the number to test and the maximum number of iterations
        to try before halting execution. If num is NOT magic (or the maximum number
        of iterations has been reached), return (-1 \tnum) (i.e., the negative of num).
        If num IS magic, return the number of iterations it took to reduce num to 1.
     
        Remember that a number is magic if it can be reduced to 1 by dividing it by 2 if
        it is even or multiplying it by 3 and adding 1 if it is odd.
        '''
    @staticmethod
    def IsMagic(num: int, max_iterations: int) -> int:
        temp = num
        itr = 0
        for i in range (0, max_iterations):
            if(temp % 2 == 0):
                temp = Assignment2_Python_Template.even(temp)
            else:
                temp = Assignment2_Python_Template.odd(temp)
            if(temp <=0):
                return num/-1
            if temp == 1:
                return itr
            itr+= 1
        return num/-1

    ''' This method should be used to check if each number in the range [start, stop]
        is a magic number. If all numbers in the range are magic, return the number of
        iterations that it took to reduce the number passed into "stop" to 1. If you 
        find a number that is NOT magic, this method should return the negative of
        that number.
        '''
    @staticmethod
    def TestRange(start: int, stop: int, max_iterations: int) -> int:
        for i in range(start, stop + 1):
            if(Assignment2_Python_Template.IsMagic(i, max_iterations) == i/-1):
                return i/-1
        return Assignment2_Python_Template.IsMagic(stop, max_iterations)

    def even(num: int):
        return num / 2
    def odd(num: int):
        return num * 3 + 1
start = 5
stop = 20
max_iterations = 500

result = Assignment2_Python_Template.TestRange(start, stop, max_iterations)
print(result)