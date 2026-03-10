def checktriangle(a, b, c):
    if (c < a + b) and (b < a + c) and (a < c + b):
        if a == b and a == c:
            return "Triangulo equilatero"
        elif a == b or b == c:
            return "Triangulo isosceles"
        else:
            return "Triangulo escaleno"
    else:
        return "No es un triangulo"