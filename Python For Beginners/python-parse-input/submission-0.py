from typing import List

def read_integers() -> List[int]:
    num_string = input()

    num_list = num_string.split(",")

    num_list_length = len(num_list)

    for i in range(num_list_length):
        num_list[i] = int(num_list[i])


    return num_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
