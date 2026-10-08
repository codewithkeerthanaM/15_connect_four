import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        # Find all columns that are not full
        legal = [c for c in range(7) if board.grid[0][c] == "."]

        # No legal moves available
        if not legal:
            return None

        # 1. Check whether the AI can win immediately
        for col in legal:
            row = board.drop(col, me)

            if row is not None:
                won = board.winner(me)

                # Undo the simulated move
                board.grid[row][col] = "."

                if won:
                    return col

        # 2. Check whether the opponent can win immediately
        for col in legal:
            row = board.drop(col, opponent)

            if row is not None:
                won = board.winner(opponent)

                # Undo the simulated move
                board.grid[row][col] = "."

                if won:
                    return col

        # 3. No immediate win or block
        # Choose any legal column
        return random.choice(legal)