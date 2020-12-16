from guizero import App, ButtonGroup, CheckBox, PushButton, Text
from guizero.Combo import Combo
from guizero.dialog import info

def do_booking():
    info("Booking", "Thank you for booking")

app = App(title="My second GUI app",  width=300, height=200, layout="grid")

film_description = Text(app, text="Which film?", grid=[0,0], align="left")
film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[1,0], align="left")
vip_seat = CheckBox(app, text="VIP seat?", grid=[0,1], align="left")
row_choice = ButtonGroup(app, options=[ ["Front", "F"],["Fron", "F"], ["Middle", "M"],["Back", "B"] ],
  selected="M", horizontal=True, grid=[0,2], align="left")
book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[0,3], align="left")
app.display()