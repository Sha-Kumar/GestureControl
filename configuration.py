one = True
two = True
three = True
four = True
five = True
full = True
close = True
rock = True

def resetVal() :
    global one
    global two
    global three
    global four
    global five
    global close
    global full
    global rock

    one = True
    two = True
    three = True
    four = True
    five = True
    full = True
    close = True
    rock = True



def cnfg(strval) :
    # Referencing paraneters
    global one
    global two
    global three
    global four
    global five
    global close
    global full
    global rock

    # Checkig conditions...
    if strval == 'one' :
        one = not one
        return one

    elif strval == 'two' :
        two = not two
        return two

    elif strval == 'three' :
        three = not three
        return three

    elif strval == 'four' :
        four = not four
        return four

    elif strval == 'five' :
        five = not five
        return five

    elif strval == 'open' :
        full = not full
        return full

    elif strval == 'close' :
        close = not close
        return close

    elif strval == 'rock' :
        rock = not rock
        return rock

    else :
        return False