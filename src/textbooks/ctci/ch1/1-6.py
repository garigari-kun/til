


def format_matrix_for_rotating(matrix):
    container_list = [[] for i in range(len(matrix))]
    for row in matrix:
        for i in range(len(row)):
            container_list[i].append(row[i])

    return container_list

def rotate_matrix_clockwise(matrix):
    formatted_matrix = format_matrix_for_rotating(matrix)
    print(formatted_matrix)












if __name__ == "__main__":
    TEST_DATA = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    rotate_matrix_clockwise(TEST_DATA)
