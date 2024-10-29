def multiply_matrix(A, B): 

    n = len(A) 

    result = [[0] * n for _ in range(n)] 

    for i in range(n): 

        for j in range(n): 

            for k in range(n): 

                result[i][j] += A[i][k] * B[k][j] 

    print("Result matrix ") 

    for row in result: 

        print(row) 

    return result
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

M = multiply_matrix(A, B)

