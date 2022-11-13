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
    print("If you want use it as a normal calculator just type one number and in result ignore imaginary number")
    print("Example of operation: ")
    print("1 -1 ")
    print("-")
    print("2 1 ")
    print("Result: -1.0 + 0.0i\n")

    elems1 = input("Enter first complex number: ").split()
    #if elems1 have 1 number that means user inserted only 1 number so we need to put 0 as imaginary
    if(len(elems1) == 1):
        elems1.append(0)
    a = ComplexNumbers(*[float(x) for x in elems1])

    sign = input("Enter sign: ")

    elems2 = input("Enter first complex number: ").split()
    if (len(elems2) == 1):
        elems2.append(0)
    b = ComplexNumbers(*[float(x) for x in elems2])

    if(sign == "+"):
        result = a + b
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")
    elif(sign == "-"):
        result = a - b
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")
    elif (sign == "*"):
        result = a * b
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")
    elif (sign == "/"):
        result = a / b
        print("Result: " + str(result.real) + " + " + str(result.imag) + "i")

if __name__ == "__main__":
    #test1()
    Calculator()
