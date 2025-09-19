# chess_pieces.py

from typing import List, Tuple

class Piece:
    """หมากทั่วไป"""
    def __init__(self, x: int, y: int):
        self.x = x  # row
        self.y = y  # col

    def can_attack(self, king: "King", board: List[List[str]]) -> bool:
        """override ใน subclass แต่ละตัว"""
        return False


class King(Piece):
    """เก็บตำแหน่ง King"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

#การเดิน Pawn
class Pawn(Piece):
    def can_attack(self, king: King, board: List[List[str]]) -> bool:
        # Pawn โจมตีเฉียงขึ้น (r-1, c-1) และ (r-1, c+1)
        for dx, dy in [(-1, -1), (-1, 1)]:
            if (self.x + dx, self.y + dy) == (king.x, king.y):
                return True
        return False

#การเดิน Rook 
class Rook(Piece):
    def can_attack(self, king: King, board: List[List[str]]) -> bool:
        n = len(board)
        # แนวตรง 4 ทิศ
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            r, c = self.x + dx, self.y + dy
            while 0 <= r < n and 0 <= c < n:
                if (r, c) == (king.x, king.y):
                    return True
                if board[r][c] != '.':  # มีตัวบัง
                    break
                r += dx
                c += dy
        return False

#การเดิน Bishop
class Bishop(Piece):
    def can_attack(self, king: King, board: List[List[str]]) -> bool:
        n = len(board)
        # แนวทแยง 4 ทิศ
        for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            r, c = self.x + dx, self.y + dy
            while 0 <= r < n and 0 <= c < n:
                if (r, c) == (king.x, king.y):
                    return True
                if board[r][c] != '.':
                    break
                r += dx
                c += dy
        return False


class Queen(Piece):
    def can_attack(self, king: King, board: List[List[str]]) -> bool:
        # เดินได้ทั้ง rook + bishop
        return Rook(self.x, self.y).can_attack(king, board) or \
               Bishop(self.x, self.y).can_attack(king, board)


#สร้างบอร์ด
def can_any_piece_capture_king(board_str: str) -> bool:
    allowed = {'.', 'K', 'Q', 'R', 'B', 'P'}  # ตัวหมากที่อนุญาต
    rows = board_str.strip().splitlines()
    board = []
    for line in rows:
        row = []
        for ch in line:
            if ch in allowed:
                row.append(ch)
            else:
                row.append('.')   # แปลงทุกตัวแปลก ๆ เป็นช่องว่าง
        board.append(row)
    n = len(board)

    king = None
    pieces: List[Piece] = []

    for i in range(n):
        for j in range(len(board[i])):
            ch = board[i][j]
            if ch == 'K':
                king = King(i, j)
            elif ch == 'P':
                pieces.append(Pawn(i, j))
            elif ch == 'R':
                pieces.append(Rook(i, j))
            elif ch == 'B':
                pieces.append(Bishop(i, j))
            elif ch == 'Q':
                pieces.append(Queen(i, j))

    if not king:
        return False

    for piece in pieces:
        if piece.can_attack(king, board):
            return True

    return False

def checkmate(board: str):
    result = can_any_piece_capture_king(board)  
    if result == True:
        print("Success")
    else:
        print("Fail")



