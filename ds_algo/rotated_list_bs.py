"""
Given a list of numbers, obtained by rotating a sorted list
an unkwon number of times. Write a dunction to determine the
minimum number of times the orgional list was sorted. 
Return numbers of rotations

Worst-Case complexity: O(log N); N is length of the list

Example:
    input : [10,11,3,4,5]
    output: 2

"""

"""tests = []

tests.append = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

tests.append({
    'input': {
        'nums': [4, 2, 1, -1],
    },
    'output': 0
})

tests.append({
    'input': {
        'nums': [3, -1, -9, -127],
    },
    'output': 3
})

tests.append({
    'input': {
        'nums': [6],
    },
    'output': 0 
})

tests.append({
    'input': {
        'nums': [9, 7, 5, 2, -9],
    },
    'output': -1
})

tests.append({
    'input': {
        'nums': [],
    },
    'output': -1
})

tests.append({
    'input': {
        'nums': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
    },
    'output': 7
})

large_test = {
    'input': {
        'nums': list(range(10000000, 0, -1)),
    },
    'output': 9999998    
}"""

"""
inputs: nums : List[int]
outputs: rotation_count : int

"""

def first_occur(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi :
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if mid - 1 > 0 and nums[mid - 1] == target:
                hi = mid - 1
                continue
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def last_occur(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi :
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if mid + 1 < len(nums) and nums[mid + 1] == target:
                lo = mid + 1
                continue
            return mid
    return -1

def count_rotations(nums):

    # look from start of list to end of list
    n = len(nums)
    lo, hi = 0, n - 1

    # if given list is empty
    if len(nums) == 0:
        return -1

    # while list still exists
    while lo <= hi:
        
        # already sorted
        if nums[lo] <= nums[hi]:
            target = nums[lo]
            dup = first_occur(nums, target)
            print(dup)
        mid = lo + (hi - lo) // 2

        # search list in circular fashion while staying in bounds
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n

        # track progresion
        nl = '\n'
        print(f"{nl} nums: {nums[lo:hi]}, mid: {mid}, hi: {hi}, lo: {lo} {nl}")

        # if ess than both neighbors then it is min value in list 
        if nums[mid] <= nums[prev] and nums[mid] <= nums[next] : return mid

        # look either right or left
        elif nums[mid] <= nums[hi] : hi = mid - 1 # look/move left  
        elif nums[mid] >= nums[lo] : lo = mid + 1 # look/move right [19,25,29,3] - > lo = 3 [29,3], lo = 3 mums[3:3] - > 3
    return -1

# def count_rotations_pos(nums, target):

def main():
    nums = [19, 25, 29, 3, 3, 4, 4, 5, 5, 6, 7, 9, 11, 14]
    # result = count_rotations(nums)
    first = first_occur(nums, 3)
    print(first)
    # print(result)

if __name__ == "__main__":
    main()