# sort() -> changes the original list 
# sorted() -> returns the sorted list 

def binary_search(a, n, t):

    l = 0
    r = n-1

    while(l <= r):
        m = int((l+r) / 2)

        if(a[m] < t):
            l = m+1

        elif(a[m] > t):
            r = m-1
        else:
            return "Number {} was found at index {}".format(t, m)

    return "Number {} was not found".format(t)


number = 20
my_list = [11, 20, 1]
my_list.sort()

print(binary_search(my_list, len(my_list), number))

