class Orange:
    def __init__(self, c, w):
        self.color = c
        self.weight = w
        self.mold = 0
        print("Utworzono!")

    def rot(self, days, temp):
        self.mold = days * temp


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    gayOrang = Orange("v", 7)
    print(gayOrang)
