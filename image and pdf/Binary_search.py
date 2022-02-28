

def Binary_search(l,n):
    pos = -1
    l.sort()
    beg = 0
    end = len(l)-1
    while beg < end:
        mid = (beg+end) // 2
        if l[mid] == n:
            pos = mid
        elif l[mid] > n:
            end = mid
        else:
            beg=mid

    return pos


list1=[0,2,54,12,32,56,67,23,121,11,65]
print(Binary_search(list1,65))
