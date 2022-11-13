import random
import os
import time
import multiprocessing
import numpy as np


def creating_file(number, directoryPath, name):
    path = os.path.join(directoryPath + "/" + name)
    temp_file = open(path, 'w')
    for i in range(number):
        temp_file.write(str(random.randint(1, 5000)) + "\n")
    temp_file.close()
    time.sleep(3)
    print('Created file {}'.format(path))

def countAverageInFile(path, return_dict):
    tempfile = open(path,'r')
    sum = 0
    elementsCounter = 0
    for i in tempfile:
        sum += int(i)
        elementsCounter += 1
    tempfile.close()
    avg = float(sum) / elementsCounter
    print("Average value in file: {} is: {}".format(path,avg))
    time.sleep(2)
    return_dict[path] = avg


def pathCreator(directoryPath, name):
    path = os.path.join(directoryPath + "/" + name)
    return path

if __name__ == '__main__':
    start_time = time.time()
    processes = []
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    pathToDirectory = r"C:\Users\ppodk\OneDrive\Pulpit\programowanie\Lab_Python\Multiprocess_test"
    for i in range(0, 50):
        createFile = multiprocessing.Process(target=creating_file, args=(50,pathToDirectory,"file" + str(i+1) + ".txt"))
        processes.append(createFile)
        createFile.start()

    for process in processes:
        process.join()

    for i in range(0,50):
        print((pathCreator(pathToDirectory, "file" + str(i+1) + ".txt")))
        countAverageFile = multiprocessing.Process(target=countAverageInFile, args=(pathCreator(pathToDirectory,"file" + str(i+1) + ".txt"), return_dict))
        processes.append(countAverageFile)
        countAverageFile.start()

    time.sleep(3)

    print('Elapsed time: {} '.format(time.time() - start_time))

    import matplotlib.pyplot as plt

    counts, bins = np.histogram(return_dict.values(), bins=15, range=(2000, 3000))

    plt.hist(return_dict.values(), bins)
    plt.show()
