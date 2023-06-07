import PySimpleGUI as sg

class TicTacToe:
    def __init__(self):

        self.tile_size = (120, 120)
        self.window_size = (410, 400)
        sg.theme("DarkBlue9")

        self.Turn = 0

        self.game_running = True

        self.Sprite = { "Tile": "Sprite/Tile.png","X": "Sprite/X Tile.png", "O": "Sprite/O Tile.png"}

        self.available_tile = {"a1": 0,"a2":0,"a3":0,"b1": 0,"b2":0,"b3":0,"c1": 0,"c2":0,"c3":0}

        self.layout = [
            [self.Tile(self.Sprite["Tile"],"a1"),self.Tile(self.Sprite["Tile"],"a2"),self.Tile(self.Sprite["Tile"],"a3")],
            [self.Tile(self.Sprite["Tile"],"b1"),self.Tile(self.Sprite["Tile"],"b2"),self.Tile(self.Sprite["Tile"],"b3")],
            [self.Tile(self.Sprite["Tile"],"c1"),self.Tile(self.Sprite["Tile"],"c2"),self.Tile(self.Sprite["Tile"],"c3")]
        ]

        self.window = sg.Window("PyTicTacToe",layout=self.layout,size=self.window_size)

    def CheckWinner(self,key):
        pass


    def ChangeTile(self,key):

        if self.available_tile[key] <= 0:
            self.Turn += 1
            
            if self.Turn % 2: #even numbers
                self.available_tile[key] = 2

                self.window[key].update(filename=self.Sprite["O"])

            else: #odd numbers
                self.available_tile[key] = 1
                self.window[key].update(filename=self.Sprite["X"])





    def Tile(self,content,key):
        return sg.Image(content,size=self.tile_size,enable_events=True,key=key)

    def Run(self):

        while self.game_running:

            event, values = self.window.read()

            if event in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
                self.ChangeTile(event)


            if event == sg.WINDOW_CLOSED:
                self.game_running = False











game = TicTacToe()
game.Run()

