def simplifyNumber(number):
    number = int(number)
    if number >= 1000000000000:
        if (number >= 1000000000000000): # use scientific notation for very large numbers
            return "{:.2e}".format(number)
        else:
            return f"{(number / 1000000000000):.2f} T"
    elif number >= 1000000000:
        return f"{(number / 1000000000):.2f} B"
    elif number >= 1000000:
        return f"{(number / 1000000):.2f} M"
    else: return f"{number}"