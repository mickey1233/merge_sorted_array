def merge(nums1, m, nums2, n):
    nums1[m:] = nums2[:n]
    nums1.sort()
    print(nums1)


def main():
    merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    merge([1], 1, [], 0)
    merge([0], 0, [1], 1)


if __name__ == "__main__":
    main()
