def partition(x,low,high):
    pivot = x[high]
    left = low
    right = high-1
    while(left <= right):
        while x[left] < pivot:
            left+=1
        while x[right] > pivot:
            right-=1
        if (left <= right):
            x[left],x[right] = x[right],x[left]
            left+=1
            right-=1
    x[high],x[left] = x[left],x[high]
    return left
    

def quicksort(x,low,high):
    if low < high:
        part = partition(x,low,high)
        quicksort(x,low,part-1)
        quicksort(x,part+1,high)
        return True
    else:
        return True

def hanoi(n,start,tmp,final):
    if n > 0:
        hanoi(n-1,start,final,tmp)
        final.append(start.pop())
        hanoi(n-1,tmp,start,final)
        return True
    else:
        return True


