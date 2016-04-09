# Uses python3
def edit_distance(s, t):
    score = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    # intialize first row and column
    for i in range(len(s) + 1):
        score[i][0] = i
    for j in range(len(t) + 1):
        score[0][j] = j

    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):
            insert = score[i][j-1] + 1
            delete = score[i-1][j] + 1
            match = score[i-1][j-1]
            mismatch = score[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                score[i][j] = min(insert, delete, match)
            else:
                score[i][j] = min(insert, delete, mismatch)
    return score[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
