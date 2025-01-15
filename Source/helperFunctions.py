def simplifyNumber(number):
    number = int(number)
    if number >= 1000000000000000:
        return f"{(number / 1000000000000000):.2f} Qa"
    elif number >= 1000000000000:
        return f"{(number / 1000000000000):.2f} T"
    elif number >= 1000000000:
        return f"{(number / 1000000000):.2f} B"
    elif number >= 1000000:
        return f"{(number / 1000000):.2f} M"
    else: return f"{number}"