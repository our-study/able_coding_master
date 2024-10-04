import math


def build_accumulation_tree(arr):
    # 배열의 길이를 2의 거듭제곱으로 맞추기 위해 필요한 0의 개수를 구한다
    n = len(arr)
    power_of_two = 2 ** math.ceil(math.log2(n))
    arr += [0] * (power_of_two - n)  # 부족한 부분을 0으로 채움

    tree = [arr]  # 트리의 바닥 레벨(리프 노드)

    # 상위 레벨을 계속 만들어 나감
    while len(tree[0]) > 1:
        current_level = tree[0]  # 현재 레벨
        next_level = []  # 다음 레벨(상위 레벨)

        # 하위 두 노드의 합으로 상위 노드를 만듦
        for i in range(0, len(current_level), 2):
            next_level.append(current_level[i] + current_level[i + 1])

        tree.insert(0, next_level)  # 상위 레벨을 트리의 앞에 삽입

    return tree


def print_accumulation_tree(tree):
    # 각 레벨을 출력
    for level in tree:
        print(' '.join(map(str, level)), end=" ")
        print()


# 입력
n = int(input())  # 원소의 개수
arr = list(map(int, input().split()))  # 원소 배열

# 트리 생성
tree = build_accumulation_tree(arr)

# 트리 출력
print_accumulation_tree(tree)
