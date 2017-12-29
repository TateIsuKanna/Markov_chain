# Markov_chain
2階マルコフ連鎖で文章生成するTwitterbot

## Required
https://github.com/sixohsix/twitter
```
pip install twitter
```

## Usage
```
python markc.py file
```
```
python bot.py file
```

file:1文1行の分かち書きされているファイル．文字エンコーディングはUTF-8．(デフォルトはres.txt)

botとして使う時はこんな感じのauth.jsonを作って下さい．
```
{"consumer_key": "[A-Za-z\d]{25}",
"consumer_secret": "[A-Za-z\d]{50}",
"token": "\d{18}-[A-Za-z\d]{31}",
"token_secret": "[A-Za-z\d]{45}"}
```
