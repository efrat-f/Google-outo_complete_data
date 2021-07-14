class Auto_Implement:
    def __init__(self):
        pass

    def run(self):


    def multi(self, string):
        for i in range(len(string), 0):
            for j in range(97, 123):
                search(string[:i-1] + chr(j) + string[i:])