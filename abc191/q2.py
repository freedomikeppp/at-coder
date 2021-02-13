N, X = map(int, input().split())
a_list = list(map(int, input().split()))
removed_list = [s for s in a_list if s != X]

if removed_list is None:
    print('')
else:
    print(" ".join([str(_) for _ in removed_list]))