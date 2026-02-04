def solve_non_homogeneous_3d(A, b, tolerance=1e-10):
    """
    Solves the 3D non-homogeneous system Ax = b.
    
    Args:
        A: 3x3 coefficient matrix (list of lists or numpy array)
        b: 3x1 constant vector (list or numpy array)
        tolerance: Numerical tolerance for zero checks
        
    Returns:
        - If unique solution: [x1, x2, x3]
        - If infinitely many solutions: {"solution": [x1_particular], "free_vars": [free_var_expr]}
        - If no solution: "No solution"
    """
    # Step 1: Form augmented matrix [A | b]
    aug_matrix = [row + [b[i]] for i, row in enumerate(A)]
    
    # Step 2: Gaussian elimination with partial pivoting
    aug_matrix = gaussian_elimination(aug_matrix, tolerance)
    
    # Step 3: Check for inconsistency (0 0 0 | c) where c ≠ 0
    for row in aug_matrix:
        if all(abs(x) < tolerance for x in row[:3]) and abs(row[3]) > tolerance:
            return "No solution"
    
    # Step 4: Determine rank and solution type
    rank = sum(1 for row in aug_matrix if any(abs(x) > tolerance for x in row[:3]))
    
    if rank == 3:
        # Unique solution: back-substitute
        return back_substitute(aug_matrix, tolerance)
    else:
        # Infinitely many solutions: parametric form
        return find_general_solution(aug_matrix, tolerance)

# --- Helper Functions ---

def gaussian_elimination(matrix, tolerance):
    """Converts matrix to REF with partial pivoting."""
    n = len(matrix)
    for k in range(n):
        # Partial pivoting
        max_row = max(range(k, n), key=lambda i: abs(matrix[i][k]))
        if abs(matrix[max_row][k]) < tolerance:
            continue  # Skip if column is all zeros
        matrix[k], matrix[max_row] = matrix[max_row], matrix[k]
        
        # Elimination
        for i in range(k + 1, n):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, n + 1):
                matrix[i][j] -= factor * matrix[k][j]
    return matrix

def back_substitute(matrix, tolerance):
    """Solves upper-triangular system."""
    n = len(matrix)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(matrix[i][i]) < tolerance:
            if abs(matrix[i][n]) > tolerance:
                return "No solution"  # Should not happen if checked earlier
            else:
                continue  # Free variable (infinitely many solutions)
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]
    return x

def find_general_solution(matrix, tolerance):
    """Finds parametric solution for underdetermined systems."""
    n = len(matrix)
    pivot_cols = []
    for i in range(n):
        for j in range(n):
            if abs(matrix[i][j]) > tolerance:
                pivot_cols.append(j)
                break
    
    free_vars = [j for j in range(n) if j not in pivot_cols]
    solution = [0] * n
    
    # Find particular solution (set free variables to 0)
    for i in range(n):
        if i in pivot_cols:
            solution[i] = matrix[i][n]
            for j in range(i + 1, n):
                solution[i] -= matrix[i][j] * solution[j]
            solution[i] /= matrix[i][i]
    
    # Find basis for null space (homogeneous solutions)
    null_basis = []
    for free in free_vars:
        vec = [0] * n
        vec[free] = 1
        for i in range(n):
            if i in pivot_cols:
                for j in range(i + 1, n):
                    vec[i] -= matrix[i][j] * vec[j]
                vec[i] /= matrix[i][i]
        null_basis.append(vec)
    
    return {
        "particular_solution": solution,
        "free_variables": null_basis,
        "description": "General solution: x_particular + t1 * v1 + ... + tk * vk"
    }


A = [[2, 1, 2],
     [-1, 2, 1],
     [3, 5, 9]]
b = [2, 2, 2]

solution = solve_non_homogeneous_3d(A, b)
print(solution)  # Output: [x1, x2, x3] (unique solution)