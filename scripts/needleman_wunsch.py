def pprint_matrix(M, pattern, text):
    try:
        if (len(pattern) + 1 != len(M)) or (len(text) + 1 != len(M[0])):
            raise Exception('Invalid matrix dimensions')
        # Print first row
        print('    ', end='')
        for idx in range(len(M[0]) - 1):
            print(text[idx], end=' ')
    
        print()
            
        for ridx, row in enumerate(M):
            for cidx, col in enumerate(range(len(row)+1)):
                try:
                    if cidx == 0:
                        if ridx == 0:
                            print(' ', end='')


                        else:
                            print(pattern[ridx-1], end='')
                        continue
                    else:
                        print(M[ridx][cidx-1], end='')
                finally:
                    print(' ', end='')
            print()
    except Exception as e:
        print(f'Invalid dynamic programming matrix! Are you sure you are creating the matrix with the correct dimensions?')
        raise e
"""
It takes a filled dynamic programming matrix and the two sequences as input.
Starting at the final cell, it backtraces the path with minimum cost that led to the solution.
Returns a tuple as (distance, cigar). E.g. (3, 'MMXXDMMMM')
"""
def backtrace_dp(M, pattern, text):
    # Start at the final cell
    v = len(pattern)
    h = len(text)

    cigar = ''
    distance = M[v][h]

    # Loop while still in the DP matrix
    while v > 0 and h > 0:
        # Check if the current value comes from an upper cell (Deletion)
        if M[v][h] == M[v-1][h] + 1:
            cigar = 'D' + cigar
            v -= 1
        # Check if the current value comes from a left cell (Insertion)
        elif M[v][h] == M[v][h-1] + 1:
            cigar = 'I' + cigar
            h -= 1
        else:
            # Check if the current value comes from a diagonal (Match or Mismatch)
            if pattern[v-1] == text[h-1]:
                cigar = 'M' + cigar  # Match
            else:
                cigar = 'X' + cigar  # Mismatch
            v -= 1
            h -= 1

    # If we end up on a border of the DP matrix, add the remaining CIGAR (insertions or deletions)
    if v > 0 and len(pattern) == len(text):
        cigar = 'D' * v + cigar
    if h > 0 and len(pattern) == len(text):
        cigar = 'I' * h + cigar

    return (distance, cigar)



def edit_distance_dp(pattern, text):
    # Initialize the DP Matrix (M)
    
    m = len(pattern)
    n = len(text)
    M = [[0] * (n + 1) for _ in range(m + 1)]
    
    print('Dynamic programming matrix initialized:')
    pprint_matrix(M, pattern, text)

    # Initialize the first column
    for i in range(m + 1):
        M[i][0] = i

    # Initialize the first row
    for j in range(n + 1):
        M[0][j] = j

    print('M matrix after initializing the first column and row:')
    pprint_matrix(M, pattern, text)
    
    # Fill the rest of the DP matrix with the appropriate costs
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == text[j - 1]:
                num = 0  # No penalty for match
            else:
                num = 1  # Penalty for mismatch

            insertion = M[i - 1][j]
            deletion = M[i][j - 1]
            mismatch_match = M[i - 1][j - 1]

            M[i][j] = min(insertion + 1, deletion + 1, mismatch_match + num)

    print('After filling the M matrix:')
    pprint_matrix(M, pattern, text)

    # Call backtrace_dp to get the distance and cigar
    return backtrace_dp(M, pattern, text)

# Test the code
pattern = 'DEFUNCIÓ'
text = 'DIFUSIÓ'

distance, cigar = edit_distance_dp(pattern, text)

print(f'The distance between {pattern} and {text} is: {distance}')
print(f'The cigar is: {cigar}')

