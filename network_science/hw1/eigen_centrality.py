def eig_centrality(G):
    max_iter = 100
    weight = 'weight'
    tol = 1.0e-6

    from math import sqrt

    x = dict([(n, 1.0 / len(G)) for n in G])
    s = 1.0 / sum(x.values())
    print(G[1])
    for k in x:
        x[k] *= s
    nnodes = G.number_of_nodes()

    for i in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast, 0)
        # do the multiplication y^T = x^T A
        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
        # normalize vector
        try:
            s = 1.0 / sqrt(sum(v ** 2 for v in x.values()))
        except ZeroDivisionError:
            s = 1.0
        for n in x:
            x[n] *= s
        # check convergence
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < nnodes * tol:
            return x