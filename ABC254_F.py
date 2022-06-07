import io
import sys

_INPUT = """\
6
3 5
3 5 2
8 1 3
1 2 2 3
1 3 1 3
1 1 1 1
2 2 2 2
3 3 1 1
1 1
9
100
1 1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from math import gcd
  class SegTree:
    X_unit = 0
    X_f = gcd

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)
  N,Q=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  asg,bsg=SegTree(N-1),SegTree(N-1)
  asg.build([A[i+1]-A[i] for i in range(N-1)])
  bsg.build([B[i+1]-B[i] for i in range(N-1)])
  for _ in range(Q):
    h1,h2,w1,w2=map(int,input().split())
    print(gcd(gcd(asg.fold(h1-1,h2-1),bsg.fold(w1-1,w2-1)),A[h1-1]+B[w1-1]))