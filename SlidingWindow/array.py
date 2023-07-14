from collections import deque

def sliding_window_maximum(nums, windowSize):
    result = []
    window = deque()

    for i in range(len(nums)):
        while window and nums[window[0]] <= nums[i]:
            window.popleft()

        window.appendleft(i)

        if window[-1] <= i - windowSize:
            window.pop()

        if i >= windowSize - 1:
            result.append(nums[window[-1]])

    return result
