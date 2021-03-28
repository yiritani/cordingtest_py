def order(nums):
    for out_index, out_value in enumerate(nums):
        if nums[out_index] % 2 != 0:
            for j in range(out_index, len(nums)):
                if nums[j] % 2 == 0:
                    nums[out_index], nums[j] = nums[j], nums[out_index]
                    break

        print(nums)


nnn = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
order(nnn)
