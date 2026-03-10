import pytest
from triangulo import checktriangle

def test_case1_escaleno():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"

def test_case2_equilatero():
    assert checktriangle(6, 6, 6) == "Triangulo equilatero"

def test_case3_isosceles():
    assert checktriangle(3, 3, 4) == "Triangulo isosceles"

def test_case4_no_triangulo():
    assert checktriangle(4, 3, 0) == "No es un triangulo"

def test_case5_no_triangulo_bis():
    assert checktriangle(8, 2, 4) == "No es un triangulo"

#nuevos casos de la parte 2:

def test_simetria_isosceles():
    # Detecta el bug corregido arriba
    assert checktriangle(5, 8, 5) == "Triangulo isosceles"

def test_limite_desigualdad():
    # Rompe el cortocircuito de la condición inicial
    assert checktriangle(1, 1, 2) == "No es un triangulo"

def test_valores_negativos():
    # Caso especial de caja negra
    assert checktriangle(-3, -3, -3) == "No es un triangulo"