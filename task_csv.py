import csv


def read_csv():
    with open('movies.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))


def add_csv(title: str, rating: str, description: str):
    fields = [title, rating, description]
    with open('movies.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)


def rem_csv(to_remove: str):
    lines = list()
    with open('movies.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == to_remove:
                    lines.remove(row)

    with open('movies.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


def main():
    print("List of movies:\n")
    read_csv()
    choice = input("\nEnter: \nadd - write row to CSV\ndelete - delete from CSV\n")

    if(choice == "add"):
        title = input("Type Title:\n")
        rating = input("Type Rating(0-5):\n")
        description = input("Type Description:\n")
        add_csv(title, rating, description)
    elif(choice == "delete"):
        to_remove = input("Type Title or Description of Movie to remove:\n")
        rem_csv(to_remove)
    else:
        print("Invalid operation")

if __name__ == '__main__':
    main()
