"""

Write an algorithm such that if an element in an M*N matrix is 0, its entire row and column are set to 0


"""




class MatrixProcessor(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.col_count = len(matrix)
        self.cell_count = len(matrix[0])

    def set_zero_to_matrix(self):
        columns_to_zero, rows_to_zero = self.generate_zero_rows_and_columns_list()
        for row_index in rows_to_zero:
            self.set_zero_to_row(row_index)
        for col_index in columns_to_zero:
            self.set_zero_to_columns(col_index)
        return self.matrix

    def set_zero_to_row(self, row_index):
        new_row = []
        for i in range(self.cell_count):
            new_row.append(0)
        self.matrix[row_index] = new_row

    def set_zero_to_columns(self, col_index):
        for i in range(self.col_count):
            self.matrix[i][col_index] = 0

    def generate_zero_rows_and_columns_list(self):
        columns_to_zero = []
        rows_to_zero = []
        for row_index, row in enumerate(self.matrix):
            for cell_index, cell in enumerate(row):
                if cell == 0:
                    columns_to_zero.append(cell_index)
                    rows_to_zero.append(row_index)

        return columns_to_zero, rows_to_zero





if __name__ == '__main__':
    TEST_DATA = [[1,2,3],[4,5,0],[7,8,9],[0,11,12]]

    matrix = MatrixProcessor(TEST_DATA)
    print(matrix.set_zero_to_matrix())
