class pair_elements:
    def twosum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i 

value = int(input("Enter the sum for you want to this search: "))
print("Index1 = %d, Index2 = %d" %pair_elements().twosum((10, 20, 30, 40, 50, 60, 70),value )) 