initial = int(input())
final = int(input())

periods = 0
days = 0

while initial >= final:
    periods += 1
    initial /= 2

days = int(periods) * 12

print(days)
