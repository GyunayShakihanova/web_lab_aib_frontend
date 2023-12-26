import heapq

def find(n, arr):
    maximum, minimum, result = [], [], 0
    for i in range(n):
        heapq.heappush(maximum, -arr[i])
        heapq.heappush(minimum, -heapq.heappop(maximum))

        if len(minimum) > len(maximum):
            heapq.heappush(maximum, -heapq.heappop(minimum))
        result -= maximum[0]

    return result


n, arr = int(input()), list(map(int, input().split()))
print(find(n, arr))