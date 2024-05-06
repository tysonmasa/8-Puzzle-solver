if user_choice == '1':
        print(f"Default puzzle selected.")
        # default puzzle, the very easy
        default_puzzle = ['1', '2', '3', '4', '5', '6', '7', '0', '8'] 
        # creat node
        initial_node = Node(default_puzzle, 0, None, 0, None)