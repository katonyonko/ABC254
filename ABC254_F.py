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
  N,Q=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))