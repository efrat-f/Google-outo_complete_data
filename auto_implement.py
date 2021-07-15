from string import ascii_lowercase


class Auto_Implement:
    def __init__(self):
        pass

    def run(self):
        pass

    def switching_manipulation(self, string):
        for i in range(4, len(string)):
            for letter in ascii_lowercase:
                string = string[:i+1] + letter + string[i+2:]
                return self.search(string)


