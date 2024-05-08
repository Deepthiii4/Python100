line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
position=input("Where do you want to put your treasure")
abc=["a","b","c"]
letter_index=abc.index(position[0])
num_index=int(position[1])-1
map[num_index][letter_index]="X"

# if position[0]=="A":
#     if position[1]=="1":
#         line1[0]='X'
#     elif position[1]=="2":
#         line2[0]='X'
#     else:
#         line3[0]='X'
# elif position[0]=="B":
#     if position[1]=="1":
#         line1[1]='X'
#     elif position[1]=="2":
#         line2[1]='X'
#     else:
#         line3[1]='X'
# else:
#     if position[1]=="1":
#         line1[2]='X'
#     elif position[1]=="2":
#         line2[2]='X'
#     else:
#         line3[2]='X'
print(map)
