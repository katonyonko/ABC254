import io
import sys

_INPUT = """\
6
5 2
3 4 1 3 4
5 3
3 4 1 3 4
7 5
1 2 3 4 5 5 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  tmp=[[] for _ in range(K)]
  for i in range(N):
    tmp[i%K].append(A[i])
  for i in range(K):
    tmp[i].sort()
  tmp2=[]
  for i in range(N):
    tmp2.append(tmp[i%K][i//K])
  ans='Yes'
  for i in range(N-1):
    if tmp2[i]>tmp2[i+1]:
      ans='No'
  print(ans)