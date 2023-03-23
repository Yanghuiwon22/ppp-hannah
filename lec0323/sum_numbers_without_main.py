def sum_n(n):
    total = 0
    for i in range(n):
        i = i + 1
        total = total + i
    return total


def main():
    n = 100
    print(f'1부터 {n}까지의 합은 {sum_n(n)}입니다')

print(__name__)