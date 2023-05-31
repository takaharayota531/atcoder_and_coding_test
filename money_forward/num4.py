import sys

def count_divisible_product(nums, k):
    count = 0
    # for num in nums:
    #     while num % k == 0:
    #         count += 1
    #         num //= k
    tmp=1
    for i in range(len(nums)):
        tmp=tmp*nums[i]
        
    # print("thiw",tmp)
    while tmp%k==0:
        count+=1
        tmp //=k
    return count

def main():
   
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

   
    ans = count_divisible_product(nums, k)

    
    print(ans)

if __name__ == "__main__":
    main()
