import random


def get_random(floor: int, ceiling: int) -> int:
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list: list[int]) -> None:
    list_length = len(the_list)

    for i in range(list_length):
        # get a random number within the range of the list indices
        # save the value at the random index
        # assign the value at the new index to the value at the currently iterating index
        # assign the value at the current index to the saved value at the random index
        new_index = get_random(0, (list_length - 1))
        value_at_random_index = the_list[new_index]
        the_list[new_index] = the_list[i]
        the_list[i] = value_at_random_index


sample_list = [1, 2, 3, 4, 5]
print("Sample list:", sample_list)

print("Shuffling sample list...")
shuffle(sample_list)
print(sample_list)
