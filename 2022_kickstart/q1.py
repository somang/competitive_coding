def sort_fabric(N, ada, charles):
    count = 0
    ada.sort()
    charles.sort()
    for i in range(N):
        if ada[i][1]==charles[i][1]:
            count += 1
    return count


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        N = int(input())
        ada, charles = [], []
        for _ in range(N):
            C, D, U = input().split()
            ada.append((C, int(U)))
            charles.append((int(D), int(U)))
        out = sort_fabric(N, ada, charles)
        print(f'Case #{test_case}: {out}')

if __name__ == "__main__":
    main()