def missingNumber(nums):
    # 計算數組的長度 n
    n = len(nums)
    
    # 計算 0 到 n 的總和
    c_sum = n * (n + 1) // 2
    
    # 計算數組中的總和
    now_sum = sum(nums)
    
    # 缺失的數字就是總和實際總和
    missing_num = c_sum - now_sum
    
    # 返回缺失的數字
    return missing_num


nums1 = [3, 0, 1]
print(missingNumber(nums1)) 

nums2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums2))
