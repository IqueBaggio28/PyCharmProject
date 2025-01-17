def sorting(array):
    n = len(array)
    for i in range(n):
        lowest = array[i]
        for j in range(i, n):
            lowest = min(lowest, array[j])

        temp = array[array.index(lowest)]
        array[array.index(lowest)] = array[i]
        array[i] = temp

    return array


def find_target_sum(array, target):
    array = sorted(array)
    n = len(array)
    l = 0
    r = n - 1

    while l < r:
        sum = array[l] + array[r]

        if sum > target:
            sum -= array[r]
            r -= 1
        elif sum < target:
            sum -= array[l]
            l += 1

        else:
            return [l, r]

    return 'not found'






def main():
    arr = [2, 4, 12, 8, 5, 1, 7]

    print(find_target_sum(arr, 22))

main()