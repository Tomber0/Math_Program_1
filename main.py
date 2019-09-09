import math
class Razbt:
    def __init__(self):
        self.n = -1
        self.b = 0
    def striling(self, n, m):
        n1 = n
        m1 = m
        if n <= 0:
            return 1
        elif m <= 0:
            return 0
        elif (n != 0 and m == n):
            return 1
        elif (n==0 and m==0):
            return -1
        elif n < m:
            return 0
        else:

            return (m1*(self.striling(n1-1, m1)))+self.striling(n1-1, m1-1)
    def bell(self, n):
        self.b = 0
        if n == 0:
            return 1
        if n >= 1:
            for m in range(1, n+1):
                self.b += self.striling(n, m)
            return self.b
def main():
    exex = Razbt()
    for i in range(1):
        print(exex.bell(10))
if __name__ == '__main__':
    main()