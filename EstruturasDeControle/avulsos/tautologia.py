def se(p, q):
    if p is True and q is False:
        return False
    else:
        return True


def ehPar(valor):
    if valor % 2 == 0:
        return True
    else:
        return False


for i in range(2):
    p = True if ehPar(i) else False
    for j in range(2):
        q = True if ehPar(j) else False
        for k in range(2):
            r = True if ehPar(k) else False
            for l in range(2):
                s = True if ehPar(l) else False
                respUm = (p and (not ((not p) or q))) or (p and q)
                respDois = (r and s)
                respFinal = se(respUm, respDois)
                print(f'{p} {q} {r} {s} = {respFinal}')