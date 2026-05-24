from turtle import *

Screen().setup(1.0, 1.0)
delay(50)

# переносимось на кординати човна
up()
goto(-30, -150)
down()

# малюємо човен
fillcolor("brown")
begin_fill()
goto(-50, -200)
goto(-140, -200)
goto(-160, -150)
goto(-30, -150)
end_fill()

# переносимось на кординати щогли
up()
goto(-90, -150)
down()
# малюємо щоглу

goto(-90, -80)

# малюємо вітрило
fillcolor("blue")
begin_fill()
goto(-70, -100)
goto(-90, -120)
end_fill()

color("blue")
up()
goto(-180, -190)
down()
goto(-160, -190)

up()
goto(-20, -190)
down()
goto(40, -190)
goto(40, -180)

up()
goto(10, -210)
down()
goto(50, -210)
goto(50, -200)


# малюємо кита
color("black")

up()
goto(120, -210)
down()
fillcolor("grey")
left(90)
begin_fill()
circle(30, 180)
goto(130, -210)
goto(130, -190)
goto(120, -210)
end_fill()

# переходимо на кординати ока
up()
goto(80, -200)
down()

# малюэмо око
dot(10)

# переходимо на кординати сонця
color("orange")
up()
goto(-120, 190)
down()

# малюємо сонце
fillcolor("orange")
begin_fill()
left(90)
circle(30)
end_fill()

up()
goto(-120, 280)
down()
goto(-120, 160)

up()
goto(-60, 220)
down()
goto(-170, 220)

up()
goto(-179, 270)
down()
goto(-60, 160)

up()
goto(-70, 270)
down()
goto(-170, 170)


done()
