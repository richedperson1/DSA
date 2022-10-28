def generateBracket(output, close, open, i, n):
    if i == 2*n:
        print(output)
        return

    if close < open:
        generateBracket(output+")", close+1, open, i+1, n)
    if open < n:
        generateBracket(output+"(", close, open+1, i+1, n)


generateBracket("", 0, 0, 0, 3)
