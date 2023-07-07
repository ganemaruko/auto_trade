# auto_trade

## 設計思想メモ書き

- カプセル化(というよりgetter, setterによるアトリビュート参照の抽象化)は開発工程において重要なので、pythonicではないかもしれないですが、内部で隠蔽される予定のクラスにはgetter, setterをつけています
    - といっても、propertyによる隠蔽は嫌いなので明示的にget_hogeをつくっているだけですが
- Enumには`Type`を末尾につけています
- 時刻周りはtimezoneを考えたくないので、UNIX時間で与えることにしています