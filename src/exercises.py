def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    start_index = 0
    end_index = len(input_list)-1
    while start_index < end_index:
        t = input_list[start_index]
        input_list[start_index] = input_list[end_index]
        input_list[end_index] = t
        start_index +=1
        end_index -=1

    return input_list


def count_digits(number):
    """
    Return count of digit
    """
    count_digit = 0
    while number:
        number = number//10
        count_digit += 1
    return count_digit
