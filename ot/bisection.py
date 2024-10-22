import math

def f(x):
  result = 0
  for i in range(DEGREE + 1):
    result = result + (coeffs[i] * (x ** (DEGREE - i)))
  return result

def getInterval(initial=1):
  last = -1 if f(initial-1) < 0 else 1
  for i in range(initial, initial+100):
    if last == -1 and f(i) > 0: return i-1, i, '-+'
    if last == 1 and f(i) < 0: return i-1, i, '+-'
    last = -1 if f(i) < 0 else 1
  print("No opposite signs")
  exit()

def bisection():
  lower, upper, signs = getInterval()
  while True:
    x = (lower + upper)/2
    answer = f(x)
    if round(answer, 5) == 0.0000: return x, answer
    if signs == '-+':
      if f(x) < 0: lower = x
      else: upper = x
    else:
      if f(x) > 0: lower = x
      else: upper = x

coeffs = [1, 0, 0, 0, -5, 1]
DEGREE = 5
root, approx = bisection()
if root:
  print(f'Root: {root}')
  print(f'f(x): {approx}')
else: print('No root')