import PySimpleGUI as sg

class TicTacToe:
    def __init__(self):

        self.tile_size = (120, 120)
        self.window_size = (410, 400)
        sg.theme("DarkBlue9")

        self.Turn = 0
        self.currentPlayer = None
        self.game_running = True

        self.Sprite = { "Tile": "Sprite/Tile.png","X": "Sprite/X Tile.png", "O": "Sprite/O Tile.png"}

        self.Board = [
            ["*","*","*"],
            ["*","*","*"],
            ["*","*","*"]
        ]

        self.layout = [
            [self.Tile(self.Sprite["Tile"],"a1"),self.Tile(self.Sprite["Tile"],"a2"),self.Tile(self.Sprite["Tile"],"a3")],
            [self.Tile(self.Sprite["Tile"],"b1"),self.Tile(self.Sprite["Tile"],"b2"),self.Tile(self.Sprite["Tile"],"b3")],
            [self.Tile(self.Sprite["Tile"],"c1"),self.Tile(self.Sprite["Tile"],"c2"),self.Tile(self.Sprite["Tile"],"c3")]
        ]

        self.window = sg.Window("PyTicTacToe",layout=self.layout,size=self.window_size)


    def resetBoard(self,tile):

        self.Board = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
        ]

        board_length = len(self.Board)

        for row_index,row in enumerate(self.layout):
            for column_index,column in enumerate(row):
                key = self.layout[row_index][column_index].key
                self.window[key].update(filename=tile)

    def PlayerWon(self):
        win = None

        board_length = len(self.Board)
        for i in range(board_length):
            win = True
            for j in range(board_length):
                if self.Board[i][j] != self.currentPlayer:
                    win = False
                    break
            if win:
                return win
        for i in range(board_length):
            win = True
            for j in range(board_length):
                if self.Board[j][i] != self.currentPlayer:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(board_length):

            for j in range(board_length):
                if self.Board[i][i] != self.currentPlayer:
                    win = False
                    break
        if win:
            return win

        win = True
        for i in range(board_length):

            for j in range(board_length):
                if self.Board[i][board_length - 1 - i] != self.currentPlayer:
                    win = False
                    break
        if win:
            return win

        for row in self.Board:
            for item in row:
                if item == "*":
                    return False
        return True

    def GameDraw(self):

        for row in self.Board:
            for items in row:
                if items == "*":
                    return False
        return True

    def UpdateBoard(self,key,row,column):

        if self.Board[row][column] == "*":
            self.Turn += 1

            if self.Turn % 2:
                # odd number turns
                self.currentPlayer = "X"
                self.window[key].update(filename=self.Sprite["X"])
            else:
                # even number turns
                self.currentPlayer = "0"
                self.window[key].update(filename=self.Sprite["O"])

            self.Board[row][column] = self.currentPlayer


    def Tile(self,content,key):
        return sg.Image(content,size=self.tile_size,enable_events=True,key=key)

    def getEvents(self,event):

        if event == "a1":
            self.UpdateBoard(event, 0, 0)

        elif event == "a2":
            self.UpdateBoard(event, 0, 1)

        elif event == "a3":
            self.UpdateBoard(event, 0, 2)

        elif event == "b1":
            self.UpdateBoard(event, 1, 0)

        elif event == "b2":
            self.UpdateBoard(event, 1, 1)

        elif event == "b3":
            self.UpdateBoard(event, 1, 2)

        elif event == "c1":
            self.UpdateBoard(event, 2, 0)

        elif event == "c2":
            self.UpdateBoard(event, 2, 1)

        elif event == "c3":
            self.UpdateBoard(event, 2, 2)
    def Run(self):

        while self.game_running:

            event, values = self.window.read()

            self.getEvents(event)

            if self.GameDraw():
                if sg.PopupYesNo(f"    Game Draw!!"
                                 f"\n     Reset Game?") == "Yes":
                    self.resetBoard(self.Sprite["Tile"])
                else:
                    break

            if self.PlayerWon():
                if sg.PopupYesNo(f"    Player : {self.currentPlayer}  Win!!"
                                 f"\n     Reset Game?") == "Yes":
                    self.resetBoard(self.Sprite["Tile"])
                else:
                    break




            if event == sg.WINDOW_CLOSED:
                self.game_running = False











game = TicTacToe()
game.Run()

