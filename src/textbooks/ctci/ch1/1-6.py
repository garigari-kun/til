


def rotate_matrix_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for row in matrix:
        print(row)



if __name__ == "__main__":
    TEST_DATA = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    rotate_matrix_clockwise(TEST_DATA)
