from pathlib import Path
from PIL import Image


def hello_world():
    print("Hello World\n")
    print("Type your name, surname, and your birth date:")
    data = input()
    print(data)


def lock():
    print("Set 4-digit code:")
    code = input()
    print("Type code:")
    code_temp = input()
    for x in range(5):
        if code == code_temp:
            print("Correct code")
            break
        elif x < 4:
            print("Wrong code, try again")
            code_temp = input()
        else :
            print("Wrong code, lock is blocked")


def count_files():
    file_number = 0
    for path in Path("C:\PP_1350").iterdir():
        if path.is_file():
            file_number += 1
    print(file_number)


def file_tree():
    for path in Path("C:\BartyzelBarczyk").rglob('*'):
        print(path)


def convert_to_png():
    for path in Path("C:\PP_1350\jpg").rglob('*.jpg'):
        print(path)
        convert(path)

def convert(path):
    im = Image.open(path)
    path.with_suffix('.png')
    im.save(path)

def delete_words():

    words = ["sie", "oraz", "nigdy", "dlaczego", " i "]
    for word in words:
        with open(r"C:\PP_1350\text.txt","r") as file:
            text = file.read()
        with open(r"C:\PP_1350\text.txt","w") as file:
            new_text = text.replace(word, "")
            file.write(new_text)


def replace_words():
     how_to_replace = {
         "i": "oraz",
         "oraz": "i",
         "nigdy": "prawie nigdy",
         "dlaczego": "czemu",
     }

     infile = r"C:\Users\ppodk\OneDrive\Pulpit\programowanie\Lab_Python\sth"
     outfile = r"C:\Users\ppodk\OneDrive\Pulpit\programowanie\Lab_Python\sthnew"

     with open(infile,"r") as fin, open(outfile, "w") as fout:
         for line in fin:
             for keys, values in how_to_replace.items():
                 line = line.replace(keys, values)
         fout.write(line)

     # with open(infile,'r+') as file:
     #     text = file.read()
     #     for keys,values in how_to_replace.items():
     #         text = text.replace(keys,values)
     #     file.seek(0)
     #     file.truncate()
     #     file.write(text)


def rownaniekwadratowe():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    delta = (b*b) - 4*(a*c)

    if(delta > 0):
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        print("There are 2 results:")
        print("x1=" + str(x1) + " and x2=" + str(x2))
    elif(delta == 0):
        x=-b/(2*a)
        print("There is 1 result:")
        print("x=" + str(x))
    else:
        print("NO RESULTS")



def create_random_numbers(num, start, end):
    array = []
    number = random.randint(start, end)

    for x in range(num):
        while number in array:
            number = random.randint(start, end)
        array.append(number)
    print("Random numbers:")
    print(array)
    return array


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                # when array[j] < array[j + 1] we have sort from higher to lower, when > we have from lower to higher
                array[j], array[j + 1] = array[j + 1], array[j]
                
                already_sorted = False
                
        if already_sorted:
            break

    print("After bubble sort:")
    print(array)
    return array


def product_of_2_vectors():
    a=[1,2,12,4]
    b=[2,4,2,8]
    x = np.dot(a, b)
    print(x)

def sum_2_matrix():
    array1 = np.random.randint(10, size=(128, 128))
    array2 = np.random.randint(10, size=(128, 128))

    sum = array1 + array2
    print(sum)

def product_2_matrix():
    array1 = np.random.randint(10, size=(8, 8))
    array2 = np.random.randint(10, size=(8, 8))

    product = np.matmul(array1, array2)
    print(product)


def determinant_of_matrix():
    x = random.randint(0, 50)
    array = np.random.randint(10, size=(x, x))

    np.linalg.det(array)
    print(array)




if __name__ == '__main__':
    #bubble_sort(create_random_numbers(50,1,100))
    #product_of_2_vectors()
    #sum_2_matrix()
    #product_2_matrix()
    determinant_of_matrix()
