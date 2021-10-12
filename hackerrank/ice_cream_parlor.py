def icecreamParlor(m, arr):
    for i in range(len(arr)):
        prices = []
        if m - arr[i] in arr[i+1:]:
            prices.append(i+1)
            prices.append(arr[i+1:].index(m - arr[i]) + 2 + i)

            return ("%d %d" % (prices[0], prices[1]))
