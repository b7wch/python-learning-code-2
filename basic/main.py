__author__ = 'jasonyang'


class Animal(object):
    def __init__(self):
        self.signal = 'animal'

    def run(self):
        print("piapia" + self.signal)


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        signal = 'dog'

    def run(self):
        super(Dog, self).run()
        print('wangwang!')


if __name__ == '__main__':
    dog = Dog()
    dog.run()
