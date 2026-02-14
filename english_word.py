import sys
import random
from random import randint, randrange

# コマンドライン引数
if len(sys.argv) < 2:
    print("使用法: python script.py <ファイル名>")
    sys.exit()

# 引数の1番目（0番目はスクリプト名）をファイル名として取得
target_file = sys.argv[1]
# ファイルの読み込み
try:
    with open(target_file,"r",encoding="utf-8") as open_file:
        words_data = open_file.read().splitlines()
except FileNotFoundError:
    print("エラー: {target_file}が見つかりません")
    sys.exit

# データ整形
English_dict = {}

for i,line in enumerate(words_data, 1):
    if "," in line:
        English, Japanese = line.split(",")
        # 前後の余計な空白を削除しておく
        English_dict[i] = (English.strip(), Japanese.strip())
dict_len = len(English_dict)

# 英単語テスト
while True:
    # 問題の選択
    num = randint(1, dict_len)
    correct_eng, correct_jp = English_dict[num]

    # --- モード選択（英字を見て日本語を当てる or 日本語を見て英字を当てる） ---
    # 0なら英→日、1なら日→英
    mode = random.randint(0, 1)
    
    if mode == 0:
        print(f"\n問題: {correct_eng}")
        user_answer = input("日本語訳を入力してください: ").strip()
        if user_answer.lower() == "end":
            break
        if user_answer == correct_jp:
            print("正解")
        else:
            print(f" 残念、正解は「{correct_jp}」")
            
    else:
        print(f"\n問題: {correct_jp}")
        user_answer = input("英単語を入力してください: ").strip()
        if user_answer.lower() == "end":
            break
        # 英語の場合は大文字小文字を区別せずに判定するのが一般的です
        if user_answer.lower() == correct_eng.lower():
            print("正解")
        else:
            print(f"残念、正解は「{correct_eng}」")

    # 次へ進むための入力
    cont = input("\n--- Enterで次の問題へ（'end'で終了） ---")
    if cont.lower() == "end":
        break

print("\nテスト終了")