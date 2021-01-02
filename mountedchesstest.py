import chess.variant
board = chess.variant.MountedChessBoard()
Nf3 = chess.Move.from_uci("g1f3")
board.push(Nf3)
Nf6 = chess.Move.from_uci("g8f6")
board.push(Nf6)
for move in board.generate_pseudo_legal_moves():
    board.push(move)
    print(board)
    print()
    board.pop()
