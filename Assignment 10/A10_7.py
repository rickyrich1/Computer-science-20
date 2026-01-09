# Problem 7 (Rook Moves)
# pos = 'e4'; pos[0] = 'e'; pos[1] = '4'
def rook_moves(pos):
    # Convert 'e4' into (5,4)
    first = 'abcdefgh'
    second = '12345678'
    numPos = (first.index(pos[0]) + 1, int(pos[1]))

    # Numeric board
    board = []
    for i in range(1,9):
        for j in range(1,9):
            board.append((i,j))

    # Alpha board
    alphaBoard = []
    for letter in first:
        for number in second:
            alphaBoard.append(f"{letter}{number}")

    # Board dictionary
    boardPairings = dict(zip(board, alphaBoard))

    ######## ROOK MOVES ########
    allMoves = []
    for i in range(1,8):
        # (5,4) -> (6,4), etc.
        allMoves.append((numPos[0] + i, numPos[1]))

        # (5,4) -> (5,5), etc.
        allMoves.append((numPos[0], numPos[1] + i))

        # (5,4) -> (4,4), etc.
        allMoves.append((numPos[0] - i, numPos[1]))

        # (5,4) -> (5,3), etc.
        allMoves.append((numPos[0], numPos[1] - i))


    # Filter for valid moves
    validMoves = []
    for T in allMoves:
        if T in board:
            validMoves.append(boardPairings[T])

    validMoves.sort()
    return validMoves


print(*rook_moves(user))
