from tkinter import *
from tkinter import messagebox

class Game(object):

    def __init__(self):
        self.fields = ['-' for i in range(9)]
        self.marker = ''
        self.draw = False

    def check_win_cond(self):
        """
            Method return True when one of the players already won the game
            or if it is a draw. Method returns False if game is still going.
        """
        # firs row
        if ''.join(self.fields[0:3]) in ('xxx', 'ooo'):
            return True
        # second row
        if ''.join(self.fields[3:6]) in ('xxx', 'ooo'):
            return True
        # third row
        if ''.join(self.fields[6:9]) in ('xxx', 'ooo'):
            return True
        # first column
        if ''.join(self.fields[0::3]) in ('xxx', 'ooo'):
            return True
        # second column
        if ''.join(self.fields[1::3]) in ('xxx', 'ooo'):
            return True
        # third column
        if ''.join(self.fields[2::3]) in ('xxx', 'ooo'):
            return True
        # first diagonal
        if ''.join(self.fields[0::4]) in ('xxx', 'ooo'):
            return True
        # second diagonal
        if ''.join(self.fields[2:8:2]) in ('xxx', 'ooo'):
            return True
        # game still going
        return False

    def check_if_empty(self, index):
        """
            Method returns True if field is empty. Method returns False if it's not.
        """
        if self.fields[index] == '-':
            return True
        else:
            return False

    def check_if_draw(self):
        """
            Method checks if it is draw.
        """
        if not self.check_win_cond() and ('-' not in self.fields):
            self.draw = True

class GameWindow(object):

    def __init__(self):
        self.game = Game()
        self.root = Tk()
        self.root.title('TIC TAC TOE GAME')
        self.root.minsize(500, 500)
        self.center_window()
        self.place_widgets()
        self.root.mainloop()

    def center_window(self):
        """
            Method calculates coordinates needed and centers game window onto a screen.
        """
        window_width = 500
        window_height = 500

        screen_width = self.root.winfo_screenwidth()  # gets screen width
        screen_height = self.root.winfo_screenheight()  # gets screen height

        x = int(screen_width / 2 - window_width / 2)  # calculates horizontal padding
        y = int(screen_height / 2 - window_height / 2)  # calculates vertical padding

        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def place_widgets(self):
        """
            Method places widgets onto a tkinter window.
        """
        self.main_frame = Frame(self.root, bg='#7f57db')
        self.main_frame.pack(expand=True, fill=BOTH)

        self.left_frame = Frame(self.main_frame, bg='#b99ac9', borderwidth=3, relief=RIDGE)
        self.left_frame.pack(expand=True, fill=BOTH, side=LEFT, pady=10, padx=10)

        # configuring rows and columns of the left frame
        for i in range(3):
            self.left_frame.columnconfigure(index=i, weight=1)
            self.left_frame.rowconfigure(index=i, weight=1)

        self.right_frame = Frame(self.main_frame, bg='#b99ac9', borderwidth=3, relief=RIDGE, width=300, height=350)
        self.right_frame.pack(expand=True, fill=BOTH, pady=10, padx=10)

        self.start_button = Button(self.right_frame, text='START', width=12, command=self.start_game)
        self.start_button.pack(expand=True, fill=Y, padx=4, pady=4)

        # right frame's sub-frame with options
        self.options_subframe = Frame(self.right_frame, bg='#b99ac9')
        self.options_subframe.pack(expand=True, fill=BOTH, pady=4, padx=4)

        # configuring rows and columns of the sub-frame
        for i in range(2):
            self.options_subframe.columnconfigure(index=i, weight=1)
            self.options_subframe.rowconfigure(index=i, weight=1)

        # adding widgets to a sub-frame
        self.question = Label(self.options_subframe, text='Choose a sign')
        self.question.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=4, padx=4)

        self.answer1 = Button(self.options_subframe, text='X', command=lambda: self.assign_marker('x'))
        self.answer1.grid(row=1, column=0, sticky=NSEW, pady=4, padx=4)

        self.answer2 = Button(self.options_subframe, text='O', command=lambda: self.assign_marker('o'))
        self.answer2.grid(row=1, column=1, sticky=NSEW, pady=4, padx=4)

        self.info = Label(self.right_frame, text='', borderwidth=3, relief=RIDGE)
        self.info.pack(expand=True, fill=BOTH, padx=4, pady=4)

        # creating string variables for buttons
        self.svars = [StringVar() for i in range(9)]
        for i in range(9):
            self.svars[i].set('')

        # creating buttons
        self.btn = Button(self.left_frame, textvariable=self.svars[0], width=8,
                          command=lambda: self.next_round(0, self.game.marker))
        self.btn.grid(row=0, column=0, pady=3, padx=3, sticky=NSEW)

        self.btn1 = Button(self.left_frame, textvariable=self.svars[1], width=8,
                           command=lambda: self.next_round(1, self.game.marker))
        self.btn1.grid(row=0, column=1, pady=3, padx=3, sticky=NSEW)

        self.btn2 = Button(self.left_frame, textvariable=self.svars[2], width=8,
                           command=lambda: self.next_round(2, self.game.marker))
        self.btn2.grid(row=0, column=2, pady=3, padx=3, sticky=NSEW)

        self.btn3 = Button(self.left_frame, textvariable=self.svars[3], width=8,
                           command=lambda: self.next_round(3, self.game.marker))
        self.btn3.grid(row=1, column=0, pady=3, padx=3, sticky=NSEW)

        self.btn4 = Button(self.left_frame, textvariable=self.svars[4], width=8,
                           command=lambda: self.next_round(4, self.game.marker))
        self.btn4.grid(row=1, column=1, pady=3, padx=3, sticky=NSEW)

        self.btn5 = Button(self.left_frame, textvariable=self.svars[5], width=8,
                           command=lambda: self.next_round(5, self.game.marker))
        self.btn5.grid(row=1, column=2, pady=3, padx=3, sticky=NSEW)

        self.btn6 = Button(self.left_frame, textvariable=self.svars[6], width=8,
                           command=lambda: self.next_round(6, self.game.marker))
        self.btn6.grid(row=2, column=0, pady=3, padx=3, sticky=NSEW)

        self.btn7 = Button(self.left_frame, textvariable=self.svars[7], width=8,
                           command=lambda: self.next_round(7, self.game.marker))
        self.btn7.grid(row=2, column=1, pady=3, padx=3, sticky=NSEW)

        self.btn8 = Button(self.left_frame, textvariable=self.svars[8], width=8,
                           command=lambda: self.next_round(8, self.game.marker))
        self.btn8.grid(row=2, column=2, pady=3, padx=3, sticky=NSEW)

    def assign_marker(self, sign):
        """
            Method assigns a marker.
        """
        self.game.marker = sign

    def change_button_text(self, index, sign):
        """
            Method replaces current text on a button with another one if field is not occupied.
        """
        if self.game.check_if_empty(index):
            self.svars[index].set(sign)
            self.game.fields[index] = sign
        else:
            messagebox.showerror('Error', 'This field is occupied!')

    def change_info(self):
        """
            Method replaces text on info label.
        """
        if self.game.marker == 'x':
            self.info['text'] = "Player's 2 turn!"
        else:
            self.info['text'] = "Player's 1 turn!"

    def change_marker(self):
        """
            Method replaces marker with another one.
        """
        if self.game.marker == 'x':
            self.game.marker = 'o'
        else:
            self.game.marker = 'x'

    def start_game(self):
        """
            Method start game.
        """
        if self.game.marker == '':
            messagebox.showerror('Marker error', 'You have not specified your marker!')
        else:
            self.info['text'] = "Player's 1 turn!"
            # Buttons are disabled so the player can't click them during game.
            self.answer1['state'] = DISABLED
            self.answer2['state'] = DISABLED
            self.start_button['state'] = DISABLED

    def next_round(self, index, sign):
        """
            Method is responsible for handling button clicks.
        """
        if self.game.marker == '':
            messagebox.showerror('Marker error', 'You have not specified your marker!')
        else:
            self.change_button_text(index, sign)
            self.game.check_if_draw()
            if self.game.check_win_cond() or self.game.draw:
                self.end_game()
            else:
                self.change_info()
                self.change_marker()

    def end_game(self):
        """
            Method runs when the game is over and either closes the window or re-run the game.
        """
        if self.game.draw:
            messagebox.showinfo('Draw!', "It's a draw!")
        elif self.game.marker == 'x':
            messagebox.showinfo('Congratulations!', 'Player 1 won the game!')
        else:
            messagebox.showinfo('Congratulations!', 'Player 2 won the game!')

        # Buttons are enabled so the player can click them in a nwe round.
        self.answer1['state'] = NORMAL
        self.answer2['state'] = NORMAL
        self.start_button['state'] = NORMAL

        x = messagebox.askyesno(title='Info', message='Do you want to play again?')
        if x:
            self.game.fields = ['-' for i in range(9)]
            self.game.marker = ''
            self.game.draw = False
            self.main_frame.destroy()
            self.place_widgets()
        else:
            self.root.destroy()


if __name__ == '__main__':
    w = GameWindow()
