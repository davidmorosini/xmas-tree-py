colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "gray": "\033[90m",
    "light-red": "\033[91m",
    "light-green": "\033[92m",
    "light-yellow": "\033[93m",
    "light-blue": "\033[94m",
    "light-magenta": "\033[95m",
    "light-cyan": "\033[96m",
}

full_colored = {
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
    "gray": "\033[100m",
    "light-red": "\033[101m",
    "light-green": "\033[102m",
    "light-yellow": "\033[103m",
    "light-blue": "\033[104m",
    "light-magenta": "\033[105m",
    "light-cyan": "\033[106m",
}
end_color_code = "\033[0m"


def get_color_names():
    return colors.keys()


def get_colored_string(message, color, full = False):
    if full:
        color_code = full_colored[color]
    else:
        color_code = colors[color]
    return f"{color_code}{message}{end_color_code}"
