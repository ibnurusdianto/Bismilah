# Import package turtle dulu
import turtle
  
# Buat objek turtle
pen = turtle.Turtle()
def curve():
    for i in range(200):
  
        # Definisikan Curve Morse
        pen.right(1)
        pen.forward(1)
  
# Definisi Method Draw Hati
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
  
def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
  
  
    pen.write("semangat yumaa....", font=(
      "Verdana", 12, "bold"))
  
  
heart()
txt()
pen.ht()