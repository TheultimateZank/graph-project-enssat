__author__ = 'azank'


class Matrix:
    def __init__(self, size, name):
        self.name = name # name of the matrix
        self.nbrSom = size # numbers of nodes of the matrix
        self.apex = [] # apex is where the matrix is stored
        self.start = 0
        self.arrive = 0
        self.size = size # size of the matrix
        """
        matrix creation
        """
        self.apex = [[0] * size for i in range(size)]

    def diagonal_zero(self):
        for i in range(self.nbrSom):
            self.replace_val(i, i, 0)

    def replace_val(self, x, y, val):
        self.apex[x][y] = val

    def print(self):
        print(str(self.name) + ' matrix : ')
        for i in range(self.size):
            print(self.apex[i])
