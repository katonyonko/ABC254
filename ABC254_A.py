import io
import sys

_INPUT = """\
6
254
101
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  print(input()[1:])