def solution(arr):
    count = {}
    result = []
    for i in range(len(arr)):
        if count.get(arr[i]):
            result.append(i - count[arr[i]][1])
            count[arr[i]] = [count[arr[i]][0] + 1, i]
        else:
            count[arr[i]] = [1, i]
    if not result:
        return -1
    return min(result)