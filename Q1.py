# 要求一:函式與流程控制
# 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
# 提醒:請勿更動題目中任何已經寫好的程式。

def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    ans = 0
    for i in range(min,max+1):
        ans += i
    print(ans)
    return



calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30