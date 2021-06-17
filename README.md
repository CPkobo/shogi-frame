# メンヤンの将棋スクリプト保管庫

パソコンで棋譜を管理したり、将棋について物書きするのに便利なスクリプトを制作しています。

さらにGithub Pages でホストした棋譜プレイヤーをBloggerに組み込んでいます。

[マイナーB級テレワーカー](https://sheepy-farm.blogspot.com/)
[Github Pages](https://cpkobo.github.io/shogi-frame/)

## 使い方

### listsing.py

```py
python listing.py
```

とすることで、resources フォルダ内のファイル名を files.js にリスト型で書き込みます。
files.js の内容は、list.js によって index.html内でリンクの一覧に変換されます。

### converter.html

▲や△、アラビア数字と漢数字の混在する将棋の記号は、タイプするのに不便で時間がかかりがちです。

そんなときは converter.html を使います。

テキストエリア内に、一定ルールで記述された文字列が将棋の符合に変換されます。

{26p} \[77b!\] のように記述することで、それぞれ ▲２六歩　△７七角成 のように変換されます。
半角・全角は区別しませんので、日本語入力状態のままどんどん打ち込んでも問題ありません。

記述ルールの詳細は、[コンバーター](https://cpkobo.github.io/shogi-frame/converter.html) を参照ください。

