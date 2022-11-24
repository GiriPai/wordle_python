def black_on_gray(text):
    """Return text coloured black, with gray background. Remaining letters."""

    return "\033[0;30;47m"+text+"\033[0m"


def white_on_black(text):
    """Return text coloured white with black background. Not in word."""

    return "\033[5;37;40m"+text+"\033[0m"


def white_on_green(text):
    """Return text coloured white with green background. Correct Position."""

    return "\033[0;37;42m"+text+"\033[0m"


def white_on_yellow(text):
    """Return text coloured white with yellow background. In word, wrong position."""

    return "\033[0;37;43m"+text+"\033[0m"
