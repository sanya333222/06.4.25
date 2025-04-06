x=1
def setup():
    size(600,400)
def draw():
    fill(x,0,0)
    global x
    ellipse(300,200,50,50)#красный
    fill(0,x,0)
    ellipse(350,200,50,50)#зеленый
    fill(0,0,x)
    ellipse(400,200,50,50)#синий
    fill(x,x,0)
    ellipse(450,200,50,50)#желтый
    fill(0,x,x)
    ellipse(500,200,50,50)#голубой
    fill(x,0,x)
    ellipse(550,200,50,50)#розовый
    x=x+1
    
