import random
from matrices.ConnectivityMatrix import ConnectivityMatrix

__author__ = 'azank'


class RoutingMatrix(ConnectivityMatrix):
    def __init__(self, size):
        super(ConnectivityMatrix, self).__init__(size, 'Routage')
        # matrix filling
        for i in range(size):
            for j in range(size):
                if random.randint(0, 1) == 0:
                    self.apex[i][j] = 0
                else:
                    self.apex[i][j] = j
        # put 0 on the diagonal
        self.diagonal_zero()

