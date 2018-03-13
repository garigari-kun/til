"""

Programming Challenge Description:
ボブはサーカスで電灯を操作しています。最近、回路基板が故障してしまい、仕事に支障が出ています。この回路基板はN×M個の長方形のライトをコントロールしており、ショーのタイミングに応じてオン/オフにすることができます。しかし、彼が特定のライトのオン/オフを切り替えると、そのライトだけでなく上下左右のライトのオン/オフも切り替わってしまいます。

O = オン . = オフ

例： （行2、列2のライトを切り替えた場合）

.O..     ....
OOO. - > ....
.O..     ....
（行1、列2のライトを切り替えた場合）

OOO.     ....
.O.. - > ....
....     ....
（ライトを次のように切り替えた場合　行1、列4→行2、列3→行2、列4→行3、列4）

....     ..OO     ...O     ....     ....
.O.. - > .O.O - > ..O. - > ...O - > ....
....     ....     ..O.     ..OO     ....
ボブは全てのライトをオフにする必要があります。全てのライトをオフにするために最低限必要なスイッチの操作回数を求めるプログラムを書いて下さい。ただし、全てのライトを消すことが不可能な場合は「-1」を出力するものとします。


Input:
入力値は、スペースで区切られた2つの整数N、M（1 <= N、M <= 10）から始まります。その後、M個の「.」か「O」で構成される文字列がN行続きます。これらの文字は各位置のライトが現在オンまたはオフであることを意味します。


Output:
全てのライトをオフにするために必要な最小限のスイッチ操作回数を出力して下さい。ただし、N×M回以内の操作で全てのライトを消すことができない場合「-1」を出力して下さい。


Test 1
Test Input Download Test Input4 5
.....
.O...
.....
.....
Expected Output Download Test Output9
Test 2
Test Input Download Test Input3 4
....
.O..
....
Expected Output Download Test Output4


"""

def turn_switch_off(line):
    line_list = [l for l in line.splitlines() if l]
    size_of_board = line_list.pop(0)
    light_board_matrix = []
    for i in line_list:
        light_board_matrix.append([i])
    print(light_board_matrix)



test = """
4 5
.....
.O...
.....
.....
"""
turn_switch_off(test)
