This is my self study from the YouTube video: https://www.youtube.com/watch?v=7_hNvwSYEmo [Japanese]

The original files are on https://github.com/kiyodori/oop_pokemon

行った変更：
- 下の Step 3 にある，素早さのパラメータの追加
- ポケモンにゼニガメを追加，ランダムに2匹選ばれバトルが行われる

# OOP Pokemon

ポケモンのポーカーゲームをオブジェクト指向を使って実装する演習問題です(Python)。

## 演習問題

ポケモンのコンソールゲームを作成しましょう。

以下の要件を満たすように実装してください。

- 2匹のポケモンがバトルします
- それぞれのポケモンにはHP（体力）があり、また攻撃を一つ持っています
- 各ターンではそれぞれのポケモンが相手に対して攻撃を行います。攻撃を受けるとダメージをもらい、HPが減ります
- 攻撃する順番は適当に決めてください
- 先に相手のHPを0にしたポケモンが勝ちです

具体的には、プログラムを実行すると以下のように動作します。

```bash
ピカチュウがあらわれた。ピカチュウのHPは20だ。
ヒトカゲがあらわれた。ヒトカゲのHPは18だ。
ピカチュウのこうげき！10万ボルト！ヒトカゲは10ダメージをもらった。ヒトカゲのHPは8だ。
ヒトカゲのこうげき！ひのこ！ピカチュウは5ダメージをもらった。ピカチュウのHPは15だ。
ピカチュウのこうげき！10万ボルト！ヒトカゲは10ダメージをもらった。ヒトカゲのHPは0だ。
ヒトカゲはたおれた。ピカチュウのかち！
```

### Step 1

オブジェクト指向（クラス）を使わずに実装しましょう。

オブジェクト指向を使わないことで、クラスを使わないことの不便さを実感することが狙いです。

### Step 2

オブジェクト指向を使って実装しましょう。

### Step 3

素早さのパラメータを追加しましょう。素早さが高いポケモンが先に攻撃するようにします。素早さが同じ場合はランダムに攻撃する順番を決めます。

オブジェクト指向を使うことで、素早さのパラメータを追加することが容易になることを実感するのが狙いです。

## 開発方法

プロジェクト直下にファイルを設置して開発しましょう。

以下、Docker を使用する場合の開発方法について説明します。

Docker コンテナを起動します。

```bash
docker-compose up -d --build
```

Docker コンテナに接続します。

```bash
docker-compose exec python3 bash
```

プログラムを実行します。

```bash
python oop_pokemon.python
```
