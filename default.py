def print_puzzle(puzzle):
    print("Very Easy")
    for i in range(0, len(puzzle), 3):
        row = puzzle[i:i+3]
        print(' '.join(str(x) for x in row).replace('0', '*'))

puzzle = [1, 2, 3, 4, 5, 6, 7, 0, 8]
print_puzzle(puzzle)
