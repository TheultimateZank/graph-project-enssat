__author__ = 'azank'

class Warshall_Matrices:
    """
    Contains several matrices and their expected results for the verifications
    """
    def __init__(self):
        self.matrix_one = [[0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1],
                           [0, 0, 0, 0]]

        self.matrix_one_expected = [[0, 1, 1, 1],
                                    [0, 0, 1, 1],
                                    [0, 0, 0, 1],
                                    [0, 0, 0, 0]]

        self.matrix_two = [[0, 1, 0, 1, 0, 0],
                           [0, 0, 1, 0, 1, 0],
                           [0, 0, 0, 0, 1, 0],
                           [0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0],
                           [0, 0, 1, 0, 1, 0]]

        self.matrix_two_expected = [[0, 1, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 1, 0]]

        self.matrix_routage = [[0, 2, 0, 0],
                               [0, 0, 3, 0],
                               [0, 0, 0, 4],
                               [0, 0, 0, 0]]

        self.matrix_routage_expected = [[0, 2, 2, 2],
                                        [0, 0, 3, 3],
                                        [0, 0, 0, 4],
                                        [0, 0, 0, 0]]
