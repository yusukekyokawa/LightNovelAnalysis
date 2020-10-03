# ラノベ解析
## 

## Environments
- OS: MacOS Catalina 10.15.4
- python 3.7.3
### Requirements
- tqdm
  - https://github.com/tqdm/tqdm

## Usage
1. 本文フォルダを`novel-txts`リネームし，`analysis.py`と同じディレクトリに配置
2. `python3 analysis.py`で実行

## Notice

- 人物リストにいらないい`,`があるとエラーになるので事前に除去しておくとこと．もしくはcharacters.txtを使用すること

## Memo
- 本文内に誰と誰が登場するのか？
  - ex.
    - AさんとBさんが話した．
    - A, B
    - AさんがBさん，Cさん，Dさんについて話した．
    - リスト: AB, AC,AD, BC,BD, CD
- 人物リストについて
  - カンマ区切りで同一人物を別の呼び名にしている．
  - 包含する要素があればそれに従う．
- 本文について
  - 序盤にあらすじ****が目印
  - 後半に登場人物紹介が入る．
  - 名前は正規化する
