n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
nums1.sort()
nums2.sort(reverse=True)
print(sum(max(0, y-x) for x, y in zip(nums1, nums2)))