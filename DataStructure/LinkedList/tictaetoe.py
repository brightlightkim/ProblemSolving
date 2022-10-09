# Constraints 3 x 3
# Return OX empty progress.
# If it's a tie or not

def tictaetoe(board):
    for i in range(3):

        for j in range(3):
            # check for the progress
            if board[i][j] is None:
                return 'in progress'
            else:
                # check straight, check line, check cross

