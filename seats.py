import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"


class seat_label:

    def __init__(self, location, bg, x, y,):
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.but = tk.Button(self.location, bg = self.bg,
                             state="disabled", height = 1,
                             borderwidth=0)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

def screen_back():
    seats.pack_forget()
    import sessions as ss
    ss.session_screen.pack(expand=True, fill="both")

class create_button:

    def __init__(self, location, text, fg, bg, x, y, comm = None):
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.comm = comm
        self.but = tk.Button(self.location, bg = self.bg, text = self.text,
                             fg=bg_col, command= self.comm, height = 1,
                             borderwidth=0, highlightbackground=bg_col)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

window = None

# Creating and configuring root window settings
seats = tk.Frame(window, bg=bg_col)
seats.pack(expand=True, fill="both")

# Creating overall frame's widgets
image = tk.Label(seats, image=None, bg=bg_col)
image.place(relx=0.1, rely=0.15, anchor="center")

movie_title = tk.Label(seats, text=None, font=(font_name, 40), fg=btn_col, bg=bg_col)

# Availability labels
selected = tk.Label(seats, text="Selected", font=(font_name, 25), fg=btn_col, bg=bg_col)
selected.place(relx=0.3, rely=0.2, anchor="center")
selected_box = seat_label(seats, "green", 0.23, 0.2)

booked = tk.Label(seats, text="Booked", font=(font_name, 25), fg=btn_col, bg=bg_col)
booked.place(relx=0.5, rely=0.2, anchor="center")
booked_box = seat_label(seats, "red", 0.43, 0.2)

disability = tk.Label(seats, text="Disability", font=(font_name, 25), fg=btn_col, bg=bg_col)
disability.place(relx=0.7, rely=0.2, anchor="center")
disability_box = seat_label(seats, "yellow", 0.63, 0.2)

available = tk.Label(seats, text="Available", font=(font_name, 25), fg=btn_col, bg=bg_col)
available.place(relx=0.9, rely=0.2, anchor="center")
available_box = seat_label(seats, "white", 0.83, 0.2)

# Specified movie and session time
session_label = tk.Label(seats, text = "Session", justify="center", font=(font_name, 40),
                         fg=btn_col, bg=bg_col)
session_label.place(relx=0.1, rely=0.325, anchor="center")

time_label = tk.Label(seats, text=None, justify="center", font=(font_name, 25),
                      fg=btn_col, bg=bg_col)
time_label.place(relx=0.1, rely=0.45, anchor="center")


# Page controlling buttons
back = create_button(seats, "Back", bg_col, btn_col, 0.4, 0.95, comm=screen_back)


# Second frame containing seats
seat_container = tk.Frame(seats, height=400, width=750, relief="flat",
                          bg=img_bg, cursor="heart", bd=5)
seat_container.place(relx=0.2, rely=0.3)

class SeatMaker:
    def seat_clicked(self, seat_state, seat):
        if seat_state.get() == 0:
            seat_state.set(1)
        else:
            seat_state.set(0)
        if seat_state.get() == 1:
            seat['bg'] = 'green'
        else:
            seat['bg'] = '#D9D9D9'
        seat_position = seat.grid_info()
        print(seat_position["column"])
        print(seat_position["row"])

        

    def __init__(self, master, column):
        self.bg = '#D9D9D9'
        self.width_seat = '4'
        self.height_seat = '2'
        self.seat_1_state = tk.IntVar()
        self.seat_2_state = tk.IntVar()
        self.seat_3_state = tk.IntVar()
        self.seat_4_state = tk.IntVar()
        self.seat_5_state = tk.IntVar()

        self.seat_button_1 = tk.Button(master, background=self.bg, width=self.width_seat, height=self.height_seat, command =  lambda: self.seat_clicked(self.seat_1_state, self.seat_button_1))
        self.seat_button_1.grid(row = 0, column=column, pady=12, padx=10)

        self.seat_button_2 = tk.Button(master, background=self.bg, width=self.width_seat, height=self.height_seat, command =  lambda: self.seat_clicked(self.seat_2_state, self.seat_button_2))
        self.seat_button_2.grid(row = 1, column=column, pady=12, padx=10)

        self.seat_button_3 = tk.Button(master, background=self.bg, width=self.width_seat, height=self.height_seat, command =  lambda: self.seat_clicked(self.seat_3_state, self.seat_button_3))
        self.seat_button_3.grid(row = 2, column=column, pady=12, padx=10)

        self.seat_button_4 = tk.Button(master, background=self.bg, width=self.width_seat, height=self.height_seat, command =  lambda: self.seat_clicked(self.seat_4_state, self.seat_button_4))
        self.seat_button_4.grid(row = 3, column=column, pady=12, padx=10)

        self.seat_button_5 = tk.Button(master, background=self.bg, width=self.width_seat, height=self.height_seat, command =  lambda: self.seat_clicked(self.seat_5_state, self.seat_button_5))
        self.seat_button_5.grid(row = 4, column=column, pady=12, padx=10)
        


row_one_seats = SeatMaker(seat_container, 0)
row_two_seats = SeatMaker(seat_container, 1)
row_three_seats = SeatMaker(seat_container, 2)
row_four_seats = SeatMaker(seat_container, 3)
row_five_seats = SeatMaker(seat_container, 4)
row_six_seats = SeatMaker(seat_container, 5)
row_seven_seats = SeatMaker(seat_container, 6)
row_eight_seats = SeatMaker(seat_container, 7)
row_nine_seats = SeatMaker(seat_container, 8)
row_ten_seats = SeatMaker(seat_container, 9)
row_eleven_seats = SeatMaker(seat_container, 10)
row_twelve_seats = SeatMaker(seat_container, 11)


A_lable = tk.Label(seat_container, text="A", font=("Aerial", 24), background="#8DA9C4", fg="white")
A_lable.grid(row=0, column=12, sticky="NSWE", padx=2, pady=12)

B_lable = tk.Label(seat_container, text="B", font=("Aerial", 24), background="#8DA9C4", fg="white")
B_lable.grid(row=1, column=12, sticky="NSWE", padx=2, pady=12)

C_lable = tk.Label(seat_container, text="C", font=("Aerial", 24), background="#8DA9C4", fg="white")
C_lable.grid(row=2, column=12, sticky="NSWE", padx=2, pady=12)

D_lable = tk.Label(seat_container, text="D", font=("Aerial", 24), background="#8DA9C4", fg="white")
D_lable.grid(row=3, column=12, sticky="NSWE", padx=2, pady=12)

E_lable = tk.Label(seat_container, text="E", font=("Aerial", 24), background="#8DA9C4", fg="white")
E_lable.grid(row=4, column=12, sticky="NSWE", padx=2, pady=12)

lable_1 = tk.Label(seat_container, text="1", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_1.grid(row=9, column=0, sticky="NSWE", padx=2, pady=1)

lable_2 = tk.Label(seat_container, text="2", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_2.grid(row=9, column=1, sticky="NSWE", padx=2, pady=1)

lable_3 = tk.Label(seat_container, text="3", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_3.grid(row=9, column=2, sticky="NSWE", padx=2, pady=1)

lable_4 = tk.Label(seat_container, text="4", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_4.grid(row=9, column=3, sticky="NSWE", padx=2, pady=1)

lable_5 = tk.Label(seat_container, text="5", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_5.grid(row=9, column=4, sticky="NSWE", padx=2, pady=1)

lable_6 = tk.Label(seat_container, text="6", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_6.grid(row=9, column=5, sticky="NSWE", padx=2, pady=1)

lable_7 = tk.Label(seat_container, text="7", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_7.grid(row=9, column=6, sticky="NSWE", padx=2, pady=1)

lable_8 = tk.Label(seat_container, text="8", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_8.grid(row=9, column=7, sticky="NSWE", padx=2, pady=1)

lable_9 = tk.Label(seat_container, text="9", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_9.grid(row=9, column=8, sticky="NSWE", padx=2, pady=1)

lable_10 = tk.Label(seat_container, text="10", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_10.grid(row=9, column=9, sticky="NSWE", padx=2, pady=1)

lable_11 = tk.Label(seat_container, text="11", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_11.grid(row=9, column=10, sticky="NSWE", padx=2, pady=1)

lable_12 = tk.Label(seat_container, text="12", font=("Aerial", 24), background="#8DA9C4", fg="white")
lable_12.grid(row=9, column=11, sticky="NSWE", padx=2, pady=1)

