from pathlib import Path
from huffman import Symbol, Huffman

def get_input(input_path):
  full_path = Path(__file__).parent / input_path
  file = open(full_path, 'r')
  return file.read().strip().split('\n')[1:]

def get_symbols(input_path):
  tag = 0
  symbols = []
  for frequency in get_input(input_path):
    tag += 1
    symbols.append(Symbol(tag, frequency))
  return symbols

def huffman_coding(symbols):
  return Huffman(symbols).encoding

def solve(input_path):
  symbols = get_symbols(input_path)
  codewords = list(huffman_coding(symbols).values())
  lengths = list(map(lambda w: len(w), codewords))
  print('Min: ', min(lengths))
  print('Max: ', max(lengths))

solve('./input.txt')
