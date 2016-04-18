qimport random

# 1. 產生出不重複且首位數不等於0的4位整數(答案)
def ans_number():
    x = 0
    while (x==0):
        li = list(range(10))
        random.shuffle(li)
        x = li[0]
    ans_num=[]
    for i in range(4):
        ans_num.append(li[i])
    return ans_num

# 2. 輸入數字
def input_number():
    n = input('請輸入一個4位數的數字\n')
    number_or_not = n
    if number_or_not.isnumeric():
        return n
    else:
        print('輸入含非數字，請重新輸入')
        i = 'c'
        while (i.isnumeric()==False):
            n = input('請輸入一個4位數的數字\n')
            i = n
            if (i.isnumeric()==False):
                print('輸入含非數字，請重新輸入')
        return n

# 2.1. 將數字轉成 每一位獨立的list
def n_to_list(n) :
    n_list=[]
    for i in range(len(str(n))):
        n_list.append(int(str(n)[i]))
    return n_list

# 3. 檢查是否猜中，若沒中回傳 ? A ? B
def check(guess):
    a_count = 0
    b_count = 0
    # print(ans)
    guess = n_to_list(guess)
    # print(guess)
    for i in range(4):
        if ans[i] == guess[i]:
            a_count += 1
        elif guess[i] in ans:
            b_count += 1
    if a_count ==4:
        mess = str('bingo')
    else:
        mess= ('A: %d  B: %d'% (a_count, b_count))
    return mess


# 主要程式

times = 1
# 歡迎
print('我們來猜一組4位數的數字')
# 2. 產生答案
ans = ans_number()
# 1. 使用者輸入數字
n = input_number()
# 如果輸入數字不是4位數
while (int(n) < 999 or int(n) >9999):
    print ('輸入不為4位整數，請重新輸入')
    n = input_number()
else:  # 如果是 3. 檢查是否猜中
    mess = ''
    while (mess!= ('bingo')):
        mess = check(n)
        if mess == 'bingo':
            print ('Bingo!答案是 %s 你總共猜了 %d 次'% (n,times ))
            break
        else:
            print(mess)
            n = input_number()
            times += 1