import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from threading import Thread


numbers = []


def task(identifier, array):
    value = np.random.randint(10, size=1)
    sleep(1)
    array.append(value)
    print(f'.thread {identifier} got {value}')


if __name__ == '__main__':
    # generate threads
    for i in range(10):
        # create and configure the thread
        thread = Thread(target=task, args=(i, numbers))
        thread.start()

    thread.join()
    sleep(5)

    print("Generated numbers: ", numbers)
    plt.hist(numbers)
    plt.show()
