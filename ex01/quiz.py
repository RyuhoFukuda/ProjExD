import random
def syutudai():
    syutudai_jisyo = {"サザエの旦那の名前は？": ("マスオ", "ますお"),"カツオの妹の名前は？" : ("ワカメ", "わかめ"),"タラオはカツオから見てどんな関係？" : ("甥", "おい", "甥っ子", "おいっこ")}
    mondai, kaitou = random.choice(list(syutudai_jisyo.items()))
    print(f"問題\n {mondai}")
    return kaitou

def kaito(score, ans):
    if ans:
        if type(score) == tuple:
            for i in score:
                if i == ans:
                    print("正解")
                    break
                else:
                    pass
        elif type(score) == str:
            if score == ans:
                print("正解")
            else:
                print("不正解")
        else:
            print("不正解")
    else:
        print("不正解")

def main():
    a = syutudai()
    kaito(a, input())

main()