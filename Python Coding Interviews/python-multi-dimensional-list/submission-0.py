from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_list = []

    for sublist in nested_arr: 
        max_ = 0
        
        for element in sublist: 
            if element > max_: 
                max_ = element 
        
        max_list.append(max_)
            
    return max_list 



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
