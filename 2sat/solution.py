from twosat import TwoSat
from pathlib import Path

def read_file(input_path):
  full_path = Path(__file__).parent / input_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')[1:]

def get_2sat(input_path):
  two_sat = TwoSat()
  for row in read_file(input_path):
    str1, str2 = row.split(' ')
    two_sat.add_clause(int(str1), int(str2))
  return two_sat

def solve_2sat(input_path):
  two_sat = get_2sat(input_path)
  return two_sat.is_satisfiable()

print("#1:", solve_2sat('./2sat1.txt'))
print("#2:", solve_2sat('./2sat2.txt'))
print("#3:", solve_2sat('./2sat3.txt'))
print("#4:", solve_2sat('./2sat4.txt'))
print("#5:", solve_2sat('./2sat5.txt'))
print("#6:", solve_2sat('./2sat6.txt'))
