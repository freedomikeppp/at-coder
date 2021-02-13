A, B = map(str, input().split())

sum_a = sum([int(i) for i in A])
sum_b = sum([int(i) for i in B])

print(sum_a if sum_a >= sum_b else sum_b)