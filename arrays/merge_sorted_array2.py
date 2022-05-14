from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    new_list = nums1[0:m]
    ## new list [1,2,3]
    ## because values after nums1[0:m] is zero. so, we remove the zero

    nums1[:] = []
    ## turn nums1 into an empty list []

    print(new_list)
    print(nums2)

    while new_list and nums2:
        if new_list[0] <= nums2[0]:
            nums1.append(new_list.pop(0))
        else:
            nums1.append(nums2.pop(0))
    
    ## now that one of the this list(new_list, nums2) is empty. we need to add the one that's not empty to nums1
    if new_list:
        nums1 += new_list
    else:
        nums1 += nums2

    print(nums1)



merge(nums1= [1,2,3,0,0,0], m = 3, nums2= [2,5,6], n =3)


### explanation https://gist.github.com/Josephchinedu/ab5ec0745b0274c14f65e1539a7deda5