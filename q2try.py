class Node:
    ID = 1
    def __init__(self, data):
        self.left = None
        self.right = None
        self.id = ID+1
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data        
        ID += 1

    
def construct_containers(all_containers):
    ac = sorted(all_containers)[-1] # pick the highest value (all we need)
    containers = Node(0)
    for id in range(ac-1):
        containers.insert(0)
    return containers

def pour(C, all_queries):



def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        N, Q = int(input().split())
        all_containers = []
        all_queries = []
        for q in range(Q):
            i, j = input().split()
            all_containers.append(j)
            all_queries.append([i, j])
        
        C = construct_containers(all_containers)
        out = pour(C, all_queries)

        print(f'Case #{test_case}: {out}')

if __name__ == "__main__":
    main()
