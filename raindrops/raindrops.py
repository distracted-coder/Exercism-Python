def convert(number):
    ans = ""
    divides = False
    if number % 3 == 0:
        ans += "Pling"
        divides = True
    if number % 5 == 0:
        ans += "Plang"
        divides = True
    if number % 7 == 0:
        ans += "Plong"
        divides = True
    if not divides:
        ans = str(number)
    return ans