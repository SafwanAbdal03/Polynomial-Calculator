#                                                2             n
# Polyn representing polynomials a0 + a1 x + a2 x  + ... + an x
# where a0 ... an are floating-point numbers
import numpy

class Polyn:

    # constructor for creating a polynomial, default is zero
    def __init__(self, a=[0]):
        self.a = a
    def input(self):  # input the coefficients of each term of the polynomial
        print("f(x) = a0 + a1 x + a2 x^2 ... + an x^n"
              "\ninput a0  a1  a2  ...  an: ")
        self.a = [float(a) for a in input().split()]

    def __str__(self):  # convert to str for display
        n = len(self.a)
        s = f"({self.a[0]:g}"  # (first coeff
        for i in range(1, n):
            s += f"{self.a[i]:+g}x^{i}"  # remaining coeff
        return s + ")"  # end with )

    def __sub__(self, y):  # polynomial subtraction
        n1 = len(self.a);
        n2 = len(y.a)
        if (n1 >= n2):
            res = self.a[:]
            for i in range(n2):
                res[i] -= y.a[i]
        else:
            res = [-x for x in y.a]
            for i in range(n1):
                res[i] += self.a[i]
        return Polyn(res)


#Finds roots of the polynomial utilizing numpy
    def find_roots(self):
        return numpy.roots(self.a[::-1])





