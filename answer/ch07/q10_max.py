# 第7章　リスト　問10　解答例
nums = [int(x) for x in input('整数をスペース区切りで：').split()]
mx = nums[0]
for x in nums[1:]:
    if x > mx:
        mx = x
print(f'最大値は{mx}です')
