import time
def locate_card_bf(cards, query):
    # Create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print(f"mid: {mid}, mid_number: {mid_number}")
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card_bs(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1  
        elif result == 'right':
            lo = mid + 1
    
    return -1

tests = []

# query occurs in the middle

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998    
}

for test in tests:
    
    # Binary Search Method
    start_time = time.time()
    check = locate_card_bs(**large_test['input']) == large_test['output']
    bs_time = ((time.time() - start_time))
    result = locate_card_bs(**large_test['input'])
    print(f"Binary Search took {bs_time} seconds")

    # Brute Force Method
    start_time = time.time()
    locate_card_bf(**large_test['input'])
    bf_time = time.time() - start_time
    print(f"Brute Force method took {bf_time} seconds")
    if result == -1:
        print("Target value not located in cards given")
    else:
        print(f"{check} the target value located at index {result} in the list of cards")
