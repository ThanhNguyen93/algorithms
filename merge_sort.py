import time
def split(input_list):
    """
    Splits a list into two pieces
    :param input_list: list
    :return: left and right lists (list, list)
    """
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]

def merge_sorted_lists(list_left, list_right):

    # Special case: one or both of lists are empty
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left
    
    # General case
    index_left = index_right = 0
    list_merged = []  # list to build and return
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            print('merging:')
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            # Right value bigger
            print('merging:')
            list_merged.append(list_right[index_right])
            index_right += 1
            
        # If we are at the end of one of the lists we can take a shortcut
        if index_right == len(list_right):
            # Reached the end of right
            # Append the remainder of left and break
            print('merging shortcut:')
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            # Reached the end of left
            # Append the remainder of right and break
            print('merging shortcut:')
            list_merged += list_right[index_right:]
            break        
    return list_merged

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        print('\nleft:', left)
        print('right: ', right)
        print('RECURSIVE MERGE_SORT: merge_sort(left):', merge_sort(left))
        print('RECURSIVE MERGE_SORT: merge_sort(right):', merge_sort(right), '\n')
        # The following line is the most important piece in this whole thing
        print('MERGE_SORTED_LIST:')
        return merge_sorted_lists(merge_sort(left), merge_sort(right))

l = [4,7,2,1, 7, 5, 8, 55, 23, 0, 78, 12, 15]
r = [6, 7, 8]

merge_sorted_lists(l, r)

start = time.time()
merge_sort(l)
time.time() - start
