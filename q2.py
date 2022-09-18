

def get_filled_container(i, j):
    


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        N, Q = int(input().split())
        all_containers = []
        all_queries = []
        for q in range(Q):
            i, j = input().split()
            all_queries.append([i, j])
        out = get_filled_container(i,j)

        print(f'Case #{test_case}: {out}')

if __name__ == "__main__":
    main()
