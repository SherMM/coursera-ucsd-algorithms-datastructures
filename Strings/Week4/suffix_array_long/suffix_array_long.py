# python3
import sys


def sort_chars(text, alpha):
    order = [0] * len(text)
    count = [0] * len(alpha)
    
    for i in range(len(text)):
        count[alpha[text[i]]] += 1
    for j in range(1, len(alpha)):
        count[j] += count[j-1]
    for i in range(len(text)-1, -1, -1):
        c = alpha[text[i]]
        count[c] -= 1
        order[count[c]] = i
    return order

def compute_char_classes(text, order):
    classes = [0] * len(text)
    for i in range(1, len(text)):
        if text[order[i]] != text[order[i-1]]:
            classes[order[i]] = classes[order[i-1]] + 1
        else:
            classes[order[i]] = classes[order[i-1]]
    return classes

def sort_doubled(text, l, order, classes):
    count = [0] * len(text)
    new_order = [0] * len(text)
    
    for i in range(len(text)):
        count[classes[i]] += 1
    for j in range(1, len(text)):
        count[j] += count[j-1]
    for i in range(len(text)-1, -1, -1):
        start = (order[i] - l + len(text)) % len(text)
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(order, classes, l):
    n = len(order)
    new_classes = [0] * n
    
    for i in range(1, n):
        curr, prev = order[i], order[i-1]
        mid, mid_prev = (curr + l) % n, (prev + l) % n
        if classes[curr] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[curr] = new_classes[prev] + 1
        else:
            new_classes[curr] = new_classes[prev]
    return new_classes


def build_suffix_array(text, alpha):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = sort_chars(text, alpha)
  classes = compute_char_classes(text, order)
  l = 1
  while l < len(text):
      order = sort_doubled(text, l, order, classes)
      classes = update_classes(order, classes, l)
      l = 2*l
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  alpha = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
  print(" ".join(map(str, build_suffix_array(text, alpha))))
