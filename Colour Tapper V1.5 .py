import tkinter as tk
import random
from colour import Color

class MainMenu(object):
    def __init__(self, master):
        self.master = master

        self.colourTapper = []

        self.x = 1
        self.colourGrad = list()

        self.colourTapperLbl = tk.Label(text="")

        self.Start()

    def Start(self):
        if self.x == 1:
            self.ChangeColour()
        self.HomeScreen()
        

    def HomeScreen(self):
        self.colourTapperLbl.config(text="Colour Tapper", font=("Verdana", 25), fg="Red")
        self.colourTapperLbl.grid(column=0, columnspan=3)

        startBtn = tk.Button(text="Start Game", font=("Verdana", 10),
                             command=lambda: [destroy(), CountdownPage(root)])
        startBtn.grid(column=0, columnspan=3)


        madeby = tk.Label(text="Made by: Xander Golding", font=("Verdana", 5))
        madeby.grid(column=2, sticky="ES")

    def ChangeColour(self):
        startCol = Color("#F00000")
        self.colourGrad = list(startCol.range_to(Color("#F00001"),100))

        def colour_change():
            self.colourTapperLbl.config(fg=self.colourGrad[-1])

            self.colourGrad.remove(self.colourGrad[-1])

            if self.colourGrad == []:
                self.colourGrad = list(startCol.range_to(Color("#F00001"),100))

            self.colourTapperLbl.after(100, lambda: colour_change())       
        colour_change()

        
class CountdownPage(object):
    def __init__(self, master):
        self.master = master

        self.size = 100
        self.count = 3

        self.countdownLabel = tk.Label(text=self.count, font=("Verdana", self.size))
        
        self.changeSize()

    def changeSize(self):
        self.countdownLabel.place(relx=0.5, rely=0.5, anchor="center")

        self.size = self.size-10

        self.countdownLabel.config(font=("Verdana", self.size))
        if self.size > 0:
            self.countdownLabel.after(100, lambda: self.changeSize())
        if self.size == 0:
            self.count = self.count-1
            self.size = 100
            self.countdownLabel.config(text=self.count)
            if self.count > 0:
                self.changeSize()
            else:
                destroy()
                ColourTapper(root)
                return self.count
    

class ColourTapper(object):
    def __init__(self, master):
        global score
        
        self.master = master
        self.button = []
        
        self.number = 0
        self.Btn_Colour = 0
        self.Btn_Number = 0
        self.rand_num = 0
        score = 0

        self.ansCol = ""
        self.ansTxt = ""

        self.timeleft = 10
        
        self.timeLabel = tk.Label(font=("Verdana", 15))
        self.scoreLabel = tk.Label(text=score, font=("Verdana", 20))

        self.colourLabel = tk.Label(font=("Verdana", 20))
        
        self.startGame()

    def startGame(self):
        if self.timeleft == 10:
            self.countdown()
        self.onEnter()

    def onEnter(self):
        Numbers = ["1","2","3","4"]
        Btn_Colours = ["Red", "Blue", "Green", "Purple"]
        
        self.create_answer()

        self.timeLabel.grid(row=0, column=0, columnspan=4)
        
        self.scoreLabel.config(text=score)
        self.scoreLabel.grid(row=2, column=1)
        
        self.colourLabel.config(text=self.ansTxt, fg=self.ansCol)
        self.colourLabel.grid(row=1, columnspan=3)      
        
        for number in range(1, 5):
            self.Btn_Number = str(random.choice(Numbers))
            Numdex = Numbers.index(self.Btn_Number)
            Numbers.pop(Numdex)
            assingedNum = self.Btn_Number    

            self.Btn_Colour = Btn_Colours[Numdex]
            Btn_Colours.pop(Numdex)

            self.button.append(tk.Button(self.master,
                                bg=self.Btn_Colour,
                                command=lambda num=assingedNum: [self.check(num)]))
            self.button[-1].grid(row=(position[str(number)]["Row"]), column=position[str(number)]["Column"],
                                 padx=15, pady=10, sticky="NSEW", ipadx=20)
                
        self.rand_num = random.randint(1,4)

    def create_answer(self):
        Btn_Colours = ["Red", "Blue", "Green", "Purple"]

        self.ansTxt = random.choice(Btn_Colours)
        Btn_Colours.remove(self.ansTxt)

        self.ansCol = random.choice(Btn_Colours)       

    def countdown(self):
        #print(self.timeleft)

        if self.timeleft == -1:
            destroy()
            ScorePage(root)
            
        if self.timeleft >= 0:
            self.timeLabel.config(text="Time Remaining:" + str(self.timeleft))
            self.timeLabel.after(1000, self.countdown)
            self.timeleft -=1

    def Clear(self):
        for i in range(1, 5):
            self.button[-1].destroy()
            self.button.pop(-1)
            
        self.onEnter()

    def check(self, num):
        global score
        
        ansNum = str(Btn_Colours.index(self.ansTxt)+1)

        if ansNum == num:
            score = score + 1
            self.scoreLabel.config(text=score, font=("Verdana", 20))
            self.rand_num = random.randint(1,4)
            self.onEnter()
        else:
            self.rand_num = random.randint(1,4)
            self.onEnter()

class ScorePage(object):
    def __init__(self, master):
        self.master = master
        self.label = tk.Label()
        self.playAgainBtn = tk.Button()
        self.finishBtn = tk.Button()
        
        self.Start()

    def Start(self):
        self.label.config(text="Your score is: " + str(score), font=("Verdana", 15))
        self.label.grid(columnspan=3, row=0)

        self.playAgainBtn.config(text="Play again", font=("Verdana", 10), bg="Green",
                                 command=lambda:[destroy(),
                                                 MainMenu(root)])
        self.playAgainBtn.grid(column=1, row=1, ipadx=10, pady=10)

        self.finishBtn.config(text="Quit", font=("Verdana", 10), bg="Red", command=finish)
        self.finishBtn.grid(column=1, row=2, ipadx=10, pady=10)
        
def destroy():
    for widget in root.winfo_children():
        widget.destroy()

def finish():
    root.destroy()


colours = { "1" : {"Colour" : "Red"},
            "2" : {"Colour" : "Blue"},
            "3" : {"Colour" : "Green"},
            "4" : {"Colour" : "Purple"},}

position = { "1" : {"Row":"3",
                    "Column":"0"},
             "2" : {"Row":"3",
                    "Column":"2"},
             "3" : {"Row":"4",
                    "Column":"0"},
             "4" : {"Row":"4",
                    "Column":"2"}}

positions = { "1" : "1",
             "2" : "2",
             "3" : "3",
             "4" : "4"}

Btn_Colours = ["Red", "Blue", "Green", "Purple"]

score = 0

root = tk.Tk()
MainMenu(root)
root.mainloop()
