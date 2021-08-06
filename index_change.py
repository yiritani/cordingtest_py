def index_change(nums, indexes):
    result = [None] * len(nums)
    for k,v in enumerate(indexes):
        result[v] = nums[k]
    print(result)


def index_change_v2(nums, indexes):
    for k, v in enumerate(indexes):
        if k > v :
            nums[k],nums[v] = nums[v], nums[k]
    print(''.join(nums))

c = ['h','y','n','p','t','o']
n = [3,1,5,0,2,4]
index_change_v2(c,n)