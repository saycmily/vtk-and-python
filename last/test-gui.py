from guizero import App
from guizero.Picture import Picture
from guizero.PushButton import PushButton
from guizero.Slider import Slider
from guizero.Text import Text
from guizero.TextBox import TextBox

def say_my_name():
    welcome_message.clear()
    s = my_name.value
    welcome_message.append(s)

def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title="test")

welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")
my_name = TextBox(app)
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command = change_text_size, start = 10, end = 80)
my_picture = Picture(app, image="C:/Users/cmily/Desktop/文件/壁纸/0018.jpg", width=403, height=268)

app.display()
