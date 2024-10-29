def add_matrices(A, B):
    # Ավելացնում ենք երկու մատրիցները
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    # Հանում ենք երկու մատրիցները
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def split_matrix(A):
    n = len(A)
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

def strassen(A, B):
    # չափսի ստուգում
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    # Բաժանում ենք մատրիցները
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    P1 = strassen(A11, subtract_matrices(B12, B22))
    P2 = strassen(add_matrices(A11, A12), B22)
    P3 = strassen(add_matrices(A21, A22), B11)
    P4 = strassen(A22, subtract_matrices(B21, B11))
    P5 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen(subtract_matrices(A11, A21), add_matrices(B11, B12))

    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = add_matrices(subtract_matrices(add_matrices(P1, P5), P3), P7)

    #արդյունք
    n = len(C11) * 2
    C = [[0] * n for _ in range(n)]
    for i in range(len(C11)):
        for j in range(len(C11)):
            C[i][j] = C11[i][j]
            C[i][j + len(C11)] = C12[i][j]
            C[i + len(C11)][j] = C21[i][j]
            C[i + len(C11)][j + len(C11)] = C22[i][j]

    return C

# Օրինակ
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32]
]

C = strassen(A, B)
for row in C:
    print(row)
