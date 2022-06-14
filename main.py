import sys
import matplotlib.pyplot as plt
import numpy as np
import graphingpart
import excelpart

sys.setrecursionlimit(10**9)

class MAIN:
    def __init__(self):
        None
    def main(self):
        self.length = 1
        self.max = 1
        main.user()
        None
    def user(self):
        inputed1 = int(input("Enter the minimum value you would like to start the collatz conjecture with\n"))
        inputed2 = int(input("Enter the maximum value you would ike to end the collatz conjecture with\n"))
        self.forloop(inputed1, inputed2)
        main.done()
    def done(self):
        sys.exit()
    def forloop(self, min, max):
        r = np.arange(min,max+1)
        #print (r)
        for i in r:
            #print(i)
            self.max = 1
            self.length = 1
            self.loop(i, i)
        excelpart.main.main()
        graphingpart.main.main()
    def loop(self, n, on):
        if n > self.max and n !=1:
            self.max = n
        if n % 2 == 0 and n !=1:
            n = n/2
        elif n % 2 != 0 and n !=1:
            n = n*3 + 1
        
        if n == 1:
            graphingpart.main.record(on, self.max, self.length)
        elif n !=1:
            self.length += 1
            self.loop(n, on)
main = MAIN()
main.main()
        
        