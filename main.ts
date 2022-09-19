let i = 0
basic.forever(function on_forever() {
    
    basic.showNumber(i)
    basic.pause(500)
    i = (i + 1) % 10
})
