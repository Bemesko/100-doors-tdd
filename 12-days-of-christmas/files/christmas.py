def to_ordinal(number: int):
    ordinals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
                'seventh', 'eight', 'ninth', 'tenth', 'eleventh', 'twelfth']
    return ordinals[number - 1]

def get_present(day: int):
    try:
        presents = ['A partridge in a pear tree.',
                    'Two turtle doves and',
                    'Three french hens',
                    'Four calling birds',
                    'Five golden rings',
                    'Six geese a-laying',
                    'Seven swans a-swimming',
                    'Eight maids a-milking',
                    'Nine ladies dancing',
                    'Ten lords a-leaping',
                    'Eleven pipers piping',
                    'Twelve drummers drumming',
                    'Unknown present']
        return presents[day - 1]
    except IndexError:
        return presents[-1]
    
def sing_verse(day: int):
    day_of_christmas = to_ordinal(day)
    presents = ""
    
    for day in range(1, day + 1):
        presents = f"{get_present(day)} {presents}"
    
    return f"On the {day_of_christmas} day of Christmas\
 my true love gave to me: {presents}"

def sing():
    for day in range(1, 13):
        sing_verse(day)
