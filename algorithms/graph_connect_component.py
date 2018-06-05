# -*- coding:utf-8 -*-
# 2017/7/14

a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f}
    , {c, e}
    , {d}
    , {e}
    , {f}
    , {c, g, h}
    , {f, h}
    , {f, g}
]


def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P

print N
print walk(N, b)


def components(G):
    comp = []
    seen = set()
    for u in range(len(G)):
        if u in seen:
            continue
        C = walk(G, u)
        seen.add(u)
        comp.append(C)
    return comp


print components(N)
