#Given a list of integers, write a function to find the second largest
# number without using built-in functions like sorted().
def second_largest(lst):
    n=len(lst)
    for i in range(1,n):
        for j in range(0,n-i):
           if lst[j]>lst[j+1]:
               lst[j],lst[j+1]=lst[j+1],lst[j]

    return lst[-2]
lst=list(map(int,input().split()))
print(second_largest(lst))
    
    