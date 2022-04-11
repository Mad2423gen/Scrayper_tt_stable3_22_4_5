import subprocess
import time


print("""
************************************************************

Scyatper_tt　メインメニュー

スクレイピング開始
Scrayper_tt"の終了は　Ctrl ＋　C　で終了します。

************************************************************
""")


def main():

    # 本番用
    # t = 2500

    # テスト用
    t = 5

    for i in range(t):
        print("\r{1}/{2}".format(
            "="*(i+1)+"-"*(t-i-1) , i+1, t), end="")
        time.sleep(1)
    print("")


i = 0
while i < 5:
    command = ["py", "mn.py"] # 実行するファイル名を指定
    proc = subprocess.Popen(command)  # ->コマンドが実行される(処理の終了は待たない)
    result = proc.communicate()
    print("""
    次の起動まで
    """)
    main()







