#要求一
def calculate(min, max):
    sum = 0
    for min in range (min,max+1):
        sum=sum+min
        min+=1
    return sum
print (calculate(1, 3)) # 你的程式要能夠計算 1+2+3，最後印出 6
print (calculate(4, 8)) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


#要求二
def avg(data):
    x=len(data["employees"])
    sum = 0
    i =0
    for i in range (0,x):
        y=data["employees"][i]["salary"]
        sum+=y
        i+=1
    return (sum/x)   

print (avg({
     "count":3,
     "employees":[
                    {"name":"John","salary":30000},
                    {"name":"Bob","salary":60000},
                    {"name":"Jenny","salary":50000}
                ]
}) )# 呼叫 avg 函式


#要求三
def maxProduct(nums):
    length=len(nums)
    maxResult=nums[0]*nums[1]
    i=0
    for i in range (i,length):
        
        for k in range (i+1,length):
            sum=nums[i]*nums[k]
            if sum>maxResult:
                maxResult=sum  
    return (maxResult)

print (maxProduct([5, 20, 2, 6])) # 得到 120 因為 20 和 6 相乘得到最大值
print (maxProduct([10, -20, 0, 3])) # 得到 30 因為 10 和 3 相乘得到最大值


#要求四
def twoSum(nums, target):
    length1=len(nums)
    i=0

    for i in range (i,length1):
        for k in range (i+1,length1):
            sum=nums[i]+nums[k]
            if sum==target:
                nums=[i,k]
                return nums

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
