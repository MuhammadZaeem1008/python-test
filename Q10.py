#Write a Python function that removes all duplicate
# elements from a list while maintaining the order of elements.
def duplicatae(lst):
    new=[]
    for i in lst:
        if i not in new:
            new.append(i)
    return new
        
lst=list(map(int,input().split()))
print(duplicatae(lst))
        