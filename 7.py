n, k, m = map(int, input().split())
if m + k >= n:
    print(n-k+m-1)
if m + k < n:
    if k > m:
        print(k-m-1)
    if k < m:
        print(m-k-1)
