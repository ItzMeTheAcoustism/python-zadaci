def FindSurface(**kwargs):
    a = kwargs["a"]
    figure = kwargs["figure"]
    if a <= 0:
        return "Error"
    match figure:
        case "triangle" | "Bill":
            b = kwargs["b"]
            P = a * b / 2
            return P
        case "square":
            P = a * a
            return P
        case "rectangle":
            b = kwargs["b"]
            P = a * b
            return P
        case _:
            return "This shape isnt in the code."

