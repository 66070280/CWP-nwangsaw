def checkmate(board):
    rows = board.split("\n")
    size = len(rows)

    for row in rows:
        if len(row) != size:
            print("Error")
            return

    king_row = -1
    king_col = -1
    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                if king_row != -1:
                    print("Error")
                    return
                king_row = r
                king_col = c
    if king_row == -1:
        print("Error")
        return

    pawn_positions = [
        (king_row + 1, king_col - 1),
        (king_row + 1, king_col + 1)
    ]

    for r, c in pawn_positions:
        if 0 <= r < size and 0 <= c < size:
            if rows[r][c] == "P":
                print("Success")
                return

    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:
        r = king_row + dr
        c = king_col + dc
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece != ".":
                if dr != 0 and dc != 0:
                    if piece == "B" or piece == "Q":
                        print("Success")
                        return
                else:
                    if piece == "R" or piece == "Q":
                        print("Success")
                        return
                break
            r += dr
            c += dc
    print("Fail")