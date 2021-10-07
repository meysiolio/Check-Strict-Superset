A = set(input().split())
number_of_sets = int(input())
result = True

for i in range(number_of_sets):
    newSet = set(input().split())
    result = result and A.issuperset(newSet)
    
print(result)