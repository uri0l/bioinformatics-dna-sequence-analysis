# SMITH-WATERMAN SEQUENCE ALIGNMENT ALGORITHM

def pprint_matrix(M, pattern, text):
    try:
        if (len(pattern) + 1 != len(M)) or (len(text) + 1 != len(M[0])):
            raise Exception('Invalid matrix dimensions')
        # Print the header row
        print('    ', end='')
        for idx in range(len(text)):
            print(text[idx], end=' ')
        print()

        # Print each row
        for ridx, row in enumerate(M):
            for cidx in range(len(row)):
                if cidx == 0:
                    # Print the pattern character for the row
                    print(' ' if ridx == 0 else pattern[ridx - 1], end=' ')
                print(M[ridx][cidx], end=' ')
            print()
    except Exception as e:
        print(f'Invalid dynamic programming matrix! Are you sure you are creating the matrix with the correct dimensions?')
        raise e

def traceback(M, pattern, text, max_position):
    i, j = max_position
    cigar = []

    while i > 0 and j > 0 and M[i][j] > 0:
        if M[i][j] == M[i-1][j-1] + (1 if pattern[i-1] == text[j-1] else -1):
            cigar.append("M")  # Match/Mismatch
            i -= 1
            j -= 1
        elif M[i][j] == M[i][j-1] - 2:
            cigar.append("I")  # Insertion
            j -= 1
        elif M[i][j] == M[i-1][j] - 2:
            cigar.append("D")  # Deletion
            i -= 1

    cigar.reverse()
    return M[max_position[0]][max_position[1]], "".join(cigar)

def edit_distance_dp(pattern, text):
    m = len(pattern)
    n = len(text)
    M = [[0] * (n + 1) for _ in range(m + 1)]

    print('Dynamic programming matrix initialized:')
    pprint_matrix(M, pattern, text)

    max_score = 0
    max_position = (0, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i-1] == text[j-1]:
                score = 1  # Match
            else:
                score = -1  # Mismatch

            diagonal = M[i-1][j-1] + score  # Match or mismatch
            insertion = M[i][j-1] - 2       # Insertion penalty
            deletion = M[i-1][j] - 2        # Deletion penalty

            M[i][j] = max(diagonal, insertion, deletion, 0)  # Use 0 for local alignment

            if M[i][j] > max_score:
                max_score = M[i][j]
                max_position = (i, j)

    print('After filling the M matrix:')
    pprint_matrix(M, pattern, text)

    return traceback(M, pattern, text, max_position)

# Test the code
pattern = 'AGCT'
text = 'ATGCT'

distance, cigar = edit_distance_dp(pattern, text)

print(f'The distance between {pattern} and {text} is: {distance}')
print(f'The cigar is: {cigar}')
