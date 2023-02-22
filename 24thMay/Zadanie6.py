import datetime


def main():
    file = open("dane.txt", "w")
    for i in range(1, 12):
        date = datetime.datetime(2020, i, 1)
        file.write(date.strftime("%B") + "\n")

    file = open("dane.txt", "r")
    for line in file:
        if line[0] in {'m', 'M'}:
            print(line.strip('\n'))

    file.close()
    file = open("dane.txt", "r")
    file_results = open("wyniki.txt", "w")
    for line in file:
        if len(line) > 8 and line[8] != '\n':
            file_results.write(line + "\n")

    file_results = open("wyniki.txt", "r")
    for line in file_results:
        if line != '\n':
            print(line.strip('\n'))

if __name__ == "__main__":
    main()