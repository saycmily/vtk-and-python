def findMedianSortedArrays(self, nums1, nums2):
    new_list = nums1 + nums2
    new_list.sort()
    length = len(new_list)
    num = (length) % 2
    if num == 1:
        index = int((length - 1)/2)
        return new_list[index]
    elif num == 0:
        index = int((length)/2)
        return (new_list[index]+new_list[index-1])/2
