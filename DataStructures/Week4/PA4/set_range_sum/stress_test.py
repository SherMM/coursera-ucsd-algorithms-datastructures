import random

def sum(l, r, tree):
    stree = sorted(tree)
    index = 0
    n = len(stree)
    while index < n and stree[index] < l:
        index += 1
    total = 0
    while index < n and stree[index] <= r:
        total += stree[index]
        index += 1
    return total

tree = set()
ops = ['+', '-', '?', 's']
found = []
output = []
MODULO = 1000000001
n = 26
#print("number of operations: {}".format(n))
output.append(n)
last_sum_result = 0
for i in range(n):
    line = []
    op = random.choice(ops)
    line.append(op)
    out_line = ''
    if line[0] == '+':
        x = random.randrange(0, 201)
        out_line += line[0] + ' ' + str(x)
        tree.add((x + last_sum_result) % MODULO)
        found.append(x)
    elif line[0] == '-':
        if len(found) > 0:
            x = random.choice(found)
        else:
            x = random.randrange(0, 101)
        out_line += line[0] + ' ' + str(x)
        if x in tree:
            tree.remove((x + last_sum_result) % MODULO)
            found.remove((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = random.randrange(0, 101)
        out_line += line[0] + ' ' + str(x)
        #print("Finding: {}".format(x))
        print('Found' if ((x + last_sum_result) % MODULO) in tree else 'Not found')
    elif line[0] == 's':
        l = random.randrange(0, 101)
        r = random.randrange(l, 101)
        out_line += line[0] + ' ' + str(l) + ' ' + str(r)
        #print("Summing from {} to {}".format(l, r))
        res = sum((l + last_sum_result) %
                  MODULO, (r + last_sum_result) % MODULO, tree)
        print(res)
        last_sum_result = res % MODULO
    output.append(out_line)

print()

for line in output:
    print(line)
