#merge sort

test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def merge_sort(n):
    return merge_sort_helper(n,0)

def merge_sort_helper(n,c):
    length = len(n)
    counter = c
    if length <= 1:
        return [n,counter] #if the list only has one element
    else:
        size = int(length / 2) #right heavy
        left = merge_sort_helper(n[:size],counter) #sort left list
        right = merge_sort_helper(n[size:],counter) #sort right list
        merge_call = merge(left[0],right[0]) #returns merged list [0] and number of operations in that merge [1]
        merged = merge_call[0] #the merged list
        counter = left[1] + right[1] + merge_call[1] #total number of operations until this point
        return [merged]+[counter]


def merge(left, right):
    big = []
    count = 0
    while len(left) > 0 and len(right) > 0:
        count += 1 #add one to count for every comparison
        if left[0] > right[0]:
            big = big+[right[0]] #put the smaller value into "big"
            right = right[1:]
        else:
            big = big+[left[0]]
            left = left[1:]
    if len(left)>len(right): #the rest is whichever list is non-empty
      big = big + left #add the rest to "big"
    else:
      big = big + right #add the rest to "big"
    #count += 1 #uncomment for append as elementary operation
    if len(big) > 0:
      return [big,count]
    else:
      return False #just an error check, probably not necessary, and also undealt with anyway

print(merge_sort(test))
