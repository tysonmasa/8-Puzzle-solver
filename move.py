# always return a new state as a list

def tileLeft(state):                # if possible move tile left
    updateState = state.copy()
    index = updateState.index(0)
    if index not in [0, 1, 2]:      # Ensure not in the first column, then swap
        updateState[index], updateState[index - 3] = updateState[index - 3], updateState[index]
        return updateState
    return None

def tileRight(state):               # if possible move tile right
    updateState = state.copy()
    index = updateState.index(0)
    if index not in [6, 7, 8]:      # Ensure not in the last column
        updateState[index], updateState[index + 3] = updateState[index + 3], updateState[index]
        return updateState
    return None
    
def tileUp(state):                  # if possible move tile up
    updateState = state.copy()
    index = updateState.index(0)
    if index not in [0, 3, 6]:      # Ensure not in the first row
        updateState[index], updateState[index - 1] = updateState[index - 1], updateState[index]
        return updateState
    return None

def tileDown(state):                # if possible move tile up
    updateState = state.copy()
    index = updateState.index(0)
    if index not in [2, 5, 8]:      # Ensure not in the last row
        updateState[index], updateState[index + 1] = updateState[index + 1], updateState[index]
        return updateState
    return None
