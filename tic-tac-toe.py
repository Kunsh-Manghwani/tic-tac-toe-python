import random

board = [' ' for x in range(10)]


def insertletter(letter, pos):
    board[pos] = letter


def designboard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")


def spaceisfree(pos):
    return board[pos] == ' '


def isboradfull(board):
    if board.count(' ') > 1:
        return False
    return True


def winner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))


def playermove():
    run = True
    while run:
        move = input("Please select a position to enter the x")
        try:
            move = int(move)
            if spaceisfree(move):
                if 0 < move < 10:
                    run = False
                    insertletter('X', move)
            else:
                print("Sorry this space is occupied ")
        except ValueError:
            print("Please enter a number")


def computermove():
    possiblemoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner(boardcopy, let):
                move = i
                return move

    corneropens = []

    for i in possiblemoves:
        if i in [1, 3, 7, 9]:
            corneropens.append(i)

    if len(corneropens) > 0:
        move = selectRandom(corneropens)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgesopen = []

    for i in possiblemoves:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)

    if len(edgesopen) > 0:
        move = selectRandom(edgesopen)
        return move
    return move


def selectRandom(a):
    ln = len(a)
    r = random.randrange(0, ln)
    return a[r]


def main():
    print("Welcome to the game!")
    designboard(board)

    while not isboradfull(board):
        if not winner(board, 'O'):
            playermove()
            designboard(board)
        else:
            print("Sorry you lose")
            break

        if not winner(board, 'X'):
            move = computermove()
            if move == 0:
                pass
            else:
                insertletter('O', move)
                print("Computer placed a O at position ", move)
                designboard(board)
        else:
            print("You Win!")
            break

    if isboradfull(board):
        print("Tie game")


while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("--------------------------")
        main()
    else:
        print("We will be waiting for your next visit")
        break
