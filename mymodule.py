# function is used to find the index of provided value

def find_index(lis, target):
    for i, value in enumerate(lis):
        if value == target:
            return i
        return "Not Available"
