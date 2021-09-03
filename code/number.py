numbers = [0, 1, 1]

n = 5

def buildlist(n, max_number):
    if max_number==0: return
    if n == 1 and max_number >= 1: return [[1]]
    if max_number == n: return [[n]] + buildlist(n, max_number-1)
    if n < max_number and n >= 1: return buildlist(n, n)
    if n > max_number:
        a = buildlist(n-max_number, max_number)
        ta = []
        for t in a:
            ta.append([max_number]+t)
        b = buildlist(n, max_number-1)
        if b:
            return ta+b
        return ta
    print("what")

print(buildlist(5,4))


print("___________________________________")

till = 20

for i in range(3, till):
    result = 0
    tmp = buildlist(i, i-1)
    for k in tmp:
        sample = 1
        for t in k:
            sample = sample * numbers[t]
        result += sample
    numbers.append(result)

print(numbers)

