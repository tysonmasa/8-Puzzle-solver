def main():
    print(f"Welcome to Group 29s 8 puzzle solver.")
    userChoice = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n")

    if userChoice == '1':
        print(f"Default puzzle selected.")
        # Insert default puzzle here
    elif userChoice == '2':
        print(f"Enter your puzzle, use a zero to represent the blank.")
        firstRow = input("Enter the first row, use space or tabs between numbers: ")
        secondRow = input("Enter the second row, use space or tabs between numbers: ")
        thirdRow = input("Enter the third row, use space or tabs between numbers: ")

        # Uses split function to split the input into a list of strings by the spaces or tabs
        firstRow = firstRow.split(" ")
        secondRow = secondRow.split(" ")
        thirdRow = thirdRow.split(" ")

        # Combines them into list
        userPuzzle = firstRow, secondRow, thirdRow

    
    userAlgo = input("Enter your choice of algorithm: \nUniform Cost Search\nA* with the Misplaced Tile heuristic.\nA* with the Manhattan distance heuristic.\n")

    if userAlgo == 1:
        print(f"Uniform Cost Search selected.")
        # Do Uniform Cost Search
    elif userAlgo == 2:
        print(f"A* with the Misplaced Tile heuristic selected.")
        # Do A* with Misplaced Tile heuristic
    elif userAlgo == 3:
        print(f"A* with the Manhattan distance heuristic selected.")
        # Do A* with Manhattan distance heuristic
main()