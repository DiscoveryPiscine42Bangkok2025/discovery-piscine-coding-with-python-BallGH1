
from checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board) 

    board2 = """\
..
.K\
"""
    checkmate(board2)  # ควรพิมพ์ Fail




if __name__ == "__main__" : 
    main()
