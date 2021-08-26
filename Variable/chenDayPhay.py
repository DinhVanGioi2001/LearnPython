# def solution(str): # dao nguoc chuoi str
#     tmp = ""
#     for i in str:
#         tmp = i + tmp
#     return tmp
# num = input()
# num2 = solution(num)
# rev = ",".join(num2[i: i + 3] for i in range(0, len(num2), 3))
# res = solution(rev)
# print(res)

str = int(input())
str = "{:,}".format(str)
print(str)