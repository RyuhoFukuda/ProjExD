import random
import datetime

taisyo_al = 13
kesson_al = 4
all_al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_num = 10

###対象文字を表示させる関数
def syutudai():
    all_al_list = list(all_al)    
    taisyo_list = random.sample(all_al_list, taisyo_al)
    kesson_list = random.sample(taisyo_list, kesson_al)
    hyouji_list = list(set(taisyo_list) - set(kesson_list))
    print(f"対象文字:\n{hyouji(taisyo_list)}\n欠損文字:\n{hyouji(kesson_list)}\n表示文字:\n{hyouji(hyouji_list)}")
    print(f"欠損文字はいくつあるでしょうか？:")
    return kesson_list
###欠損文字を作る関数（対象文字から受け取ってランダムで決定）
def kaito(kesson, ans):
    for i in range(max_num):
        if ans in kesson:
            if kesson:
                print(kesson)
                kesson.remove(ans)
            else:
                ans = input()
            if not kesson:
                print("正解です")
                break
        else:
            print("不正解です。もう一度やり直してください")
            

def kessonsuu(ans):
    for i in range(max_num):
        if ans == kesson_al:
            print("正解です。次に消えた文字を答えてください")
            break
        else:
            print("不正解です。もう一度やり直してください")
            ans = int(input())
            
    
###文字を表示させる関数(listから取り出してstr型に)
def hyouji(al_list):
    hyouji_al = ""
    for i in al_list:
        hyouji_al += str(i)
        hyouji_al += " "
    return(hyouji_al)

def main():
    kesson = syutudai()
    kessonsuu(int(input()))
    kaito(kesson, input())

main()