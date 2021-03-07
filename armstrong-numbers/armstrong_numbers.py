def is_armstrong_number(number):
    s = str(number)
    power = len(s)
    num = 0
    for i in s:
        num += int(i)**power
    return number == num
