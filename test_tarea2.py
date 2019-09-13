import Tarea2


def test_exito():
    r, s, m = Tarea2.funcion(5, 5)
    assert r == 0
    assert s == 10
    assert m == 25


def test_errorAB():
    e = Tarea2.funcion(5, 10)
    assert e == -1


def test_errorvalorliteral():
    e = Tarea2.funcion('valor', 10)
    assert e == -1
