def mergesortedarr(a,b):
    if len(a) == len(b) or len(b) == 0:
        return a + b
    
    new_list = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            new_list.append(a[i])
            i += 1

        elif b[j] < a[i]:
            new_list.append(b[j])
            j += 1

    return new_list+a[i:] + b[j:]
    
a=[1,3,4,6,20]
b=[2,3,4,5,6,9,11,76]
x=mergesortedarr(a,b)
print(x)