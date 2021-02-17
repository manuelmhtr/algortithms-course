import sys
import math

def multiply(m1, m2):
  largest = max(len(str(m1)), len(str(m2)))

  if largest <= 1:
    return m1 * m2

  mid = int(math.ceil(largest / 2))
  n = mid * 2

  m1str = str(m1).zfill(n)
  m2str = str(m2).zfill(n)

  a = int(m1str[:mid])
  b = int(m1str[mid:])
  c = int(m2str[:mid])
  d = int(m2str[mid:])

  s1 = multiply(a, c)
  s2 = multiply(b, d)
  s3 = multiply((a + b), (c + d))
  s4 = s3 - (s2 + s1)

  t1 = int(str(s1) + '0' * n)
  t2 = s2
  t3 = int(str(s4) + '0' * mid)

  return t1 + t2 + t3

first  = int(sys.argv[1])
second = int(sys.argv[2])

print(multiply(first, second))
