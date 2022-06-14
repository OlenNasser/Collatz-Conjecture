import matplotlib.pyplot as plt
import numpy as np
import excelpart
plt.style.use('bmh')

class MAIN:
    def __init__(self):
        self.x = []
        self.y = []
        self.y2 = []
        None
    def main(self):
        self.graphing()
        None
    def record(self, n, max, length):
        self.x.append(n)
        self.y.append(max)
        self.y2.append(length)
    def graphing(self):
        fig, ax = plt.subplots(2)
        fig.suptitle('Collatz Conjecture', fontsize = 20)
        ax[0].plot(self.x, self.y)
        ax[0].set_title('Max number reached')
        ax[1].plot(self.x, self.y2)
        ax[1].set_title('Length before loop')
        #plt.xlim([min(self.x), max(self.x)])
        #ax.set_xlabel('Number used')  # Add an x-label to the axes.
        #ax.set_ylabel('Max #, times before loop')  # Add a y-label to the axes.
        #ax.set_title("Collatz Conjecture")  # Add a title to the axes.
        #ax.legend()  # Add a legend.
        #ax.grid()
        
        fig.savefig("test.png")
        fig.tight_layout()
        plt.show()

main = MAIN()


