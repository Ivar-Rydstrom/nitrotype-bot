from pynput.keyboard import Key

dict = {
    Key.shift_l: 'shift',
    Key.shift_r: 'shift',
    Key.space: ' '
}


def convert_to_char(char):
    dict[char]
