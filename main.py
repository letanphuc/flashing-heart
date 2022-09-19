i = 0
def on_forever():
    global i
    basic.show_number(i)
    basic.pause(500)
    i = (i + 1) % 10

basic.forever(on_forever)