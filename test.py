from time import sleep


class A():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.run()
    
    def test(self):
        self.c = 3
    
    def run(self):
        while 1:
            print(self.a)
            print(self.b)
            print(self.c)
            sleep(1)
            
if __name__ == "__main__":
    ad = A()