# # task 1
# with open("text1.txt","r+") as file1, open("text2.txt", "r+") as file2:
#     a=file1.readlines()
#     b=file2.readlines()
#     for i in range(max(len(a),len(b))):
#         if a[i]!=b[i]:
#             print(f"string:{a[i]} and string:{b[i]}")
#         else:
#             print(f"strings {i} of files is the same")
# # task 2
# with open("text.txt","r") as file1, open("text2.txt","w") as file2:
#     file2.write(f"кількість символів:{len(file1.read())}")
#     file1.seek(0)
#     file2.write(f"\nкількість рядків:{len(file1.readlines())}")
#     file1.seek(0)
#     n=0
#     a=0
#     b=0
#     for i in file1.read():
#         try:
#             int(i)+1
#             n+=1
#         except:
#             if i in ["a","A","e","E","i","I","o","O","u","U","y","Y"]:
#                 a+=1
#             else:
#                 b+=1
#     file2.write(f"\nкількість голосних літер:{a}")
#     file2.write(f"\nкількість приголосних літер:{b}")
#     file2.write(f"\nкількість цифр:{n}")
# # task 3
# with open("text1.txt","r") as file1, open("text2.txt","w") as file2:
#     lines = file1.readlines()
#     del lines[-1]
#     for line in lines:
#         file2.write(line)
# # task 4
# with open("text1.txt","r") as file1:
#     print(len(max(file1.readlines(), key=len)))
# # task 5
# word=input()
# a=0
# with open("text1.txt","r") as file1:
#     for i in file1.read().split():
#         if i == word:
#             a+=1
#     print(a)
# # task 6
# word = input()
# swap = input()

# with open("text1.txt", "r+") as file1:
#     a = file1.read()
#     b = a.replace(word, swap)
#     file1.seek(0)
#     file1.truncate()
#     file1.write(b)