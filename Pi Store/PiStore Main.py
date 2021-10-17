from guizero import App, Text, TextBox, PushButton, Slider, Picture, Box

app = App(title="Pi Store", layout="grid", width="900")

def search():
    print(search_input.value)
    search_input.value = ""

def resize():
    header.width = app.width

header = Box(app, layout="auto", grid=[1,1,100,1], width="900", height=100, align="left")
header.bg = "red"
app.when_resized = resize

logo = Picture(header, image="logo.gif", align="left")
search_input = TextBox(header, width=30, align="right")
search_button = PushButton(header, command=search, text="Search", align="right")


app.display()
