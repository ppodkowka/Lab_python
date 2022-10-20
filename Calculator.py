class ComplexNumbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumbers(self.real * other.real, self.imag * other.imag)

    def __truediv__(self, other):
        return ComplexNumbers(self.real / other.real, self.imag / other.imag)


def test1():
    x = ComplexNumbers(1, -1)
    y = ComplexNumbers(-3, 2)
    z = x + y
    t = x - y
    print(str(z.real) + " + " + str(z.imag) + "i")
    print(str(t.real) + " + " + str(t.imag) + "i")

def Calculator():
    print("This is calculator for Complex numbers")
    print("Example of operation: ")
    print("1 -1i ")
    print("-")
    print("2 1i \n")

    x1,x2= input("Enter first complex number: ").split()
    sign = input("Enter sign: ")
    y1,y2= input("Enter second complex number: ").split()

    x2 = x2.strip("i")
    y2 = y2.strip("i")

    x = ComplexNumbers(float(x1),float(x2))
    y = ComplexNumbers(float(y1),float(y2))

    if(sign == "+"):
        result = x + y
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")
    elif(sign == "-"):
        result = x - y
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")
    elif (sign == "*"):
        result = x * y
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")
    elif (sign == "/"):
        result = x / y
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")

if __name__ == "__main__":
    #test1()
    Calculator()