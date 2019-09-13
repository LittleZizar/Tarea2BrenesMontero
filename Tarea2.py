def funcion(A, B):
    try:
        A/1
        B/1
        if A < B:
            return -1
        else:
            pass
    except:
        return -1

    return A-B, A+B, A*B
