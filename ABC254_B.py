import io
import sys

_INPUT = """\
6
3
10
30
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=[1]
  print(*A)
  for i in range(N-1):
    tmp=[0]*(i+2)
    for j in range(i+2):
      if j>0: tmp[j]+=A[j-1]
      if j<i+1: tmp[j]+=A[j]
    print(*tmp)
    A=tmp