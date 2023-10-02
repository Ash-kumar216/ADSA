def matrix_chain_multiplication(matrices):
    n = len(matrices)
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    
    for i in range(1, n):
        m[i][i] = 0

    
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')  
            for k in range(i, j):
            
                cost = m[i][k] + m[k + 1][j] + matrices[i - 1][0] * matrices[k][1] * matrices[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k  

    
    def print_optimal_parenthesization(i, j):
        if i == j:
            print(f'Matrix {i}', end='')
        else:
            print('(', end='')
            print_optimal_parenthesization(i, s[i][j])
            print_optimal_parenthesization(s[i][j] + 1, j)
            print(')', end='')

    print("Optimal Parenthesization: ", end='')
    print_optimal_parenthesization(1, n - 1)
    print()
    return m[1][n - 1]

matrices = [(2, 3), (3, 4), (4, 2)]
min_scalar_multiplications = matrix_chain_multiplication(matrices)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)

