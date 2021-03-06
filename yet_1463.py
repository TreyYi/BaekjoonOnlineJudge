# DP SOLUTION TRIAL
# Time Complexity: O()
# Space Complexity: O()

n=int(input())
dp=[-1 for i in range(n+1)]

def f(n):
    global dp

    if n==1:return 0
    if dp[n]!=-1:return dp[n]

    result=f(n-1)+1
    if n%3==0: result = min(result, f(n//3)+1)
    if n%2==0: result = min(result, f(n//2)+1)
    dp[n]=result
    return result

print(f(n))




# def divide_by_three(n):
#     new_n = n%3
#     tmp = n//3
#     if new_n == 0 and new_n != 1:
#         g_three_count+=1
#         minus_one = minus_one(new_n)
#         two = divide_by_two = divide_by_two(new_n)
#     elif new_n == 1:
#         return g_three_count
#
# def divide_by_two(n):
#     new_n = n%2
#     if new_n == 0 and new_n != 1:
#         g_two_count+=1
#         three = divide_by_three(new_n)
#         two = divide_by_two(new_n)
#     elif new_n == 1:
#         return g_two_count
#
# def minus_one(n):
#     new_n = n-1
#     if new_n != 1 and new_n != 1:
#         g_one_count+=1
#         three = divide_by_three(new_n)
#         two = divide_by_two(new_n)
#     elif new_n == 1:
#         return g_one_count
#
# X=int(input())
# g_three_count=0
# g_two_count=0
# g_one_count=0
# while(1):
#     mod_three = X%3
#     mod_two = X%2
#     minus_one = X-1
#
