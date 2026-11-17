# 新・明解Python入門（第2版）練習問題（講師用リポジトリ）

書籍『新・明解Python入門（第2版）』の各章に対応した練習問題と、解答例・解説です。
**このリポジトリは講師用です（Private 推奨）。** `main` に push すると、GitHub Actions が
`answer/`（解答例のプログラム）などの講師用ファイルを取り除いて、受講者用リポジトリ
[`user00-practice/meikai-python-exercises-student`](https://github.com/user00-practice/meikai-python-exercises-student)
へ自動で反映します。初回の設定手順は [SETUP.md](SETUP.md) を見てください。

- 対象：プログラミング未経験の受講者
- 動作確認：Python 3.11（書籍の対象）と Python 3.15 の両方で、解答例のプログラムがすべて正しく動くことを確認済み
- 全13章・135問（うちプログラム作成問題 36問）

## 講師用・受講者用の同期

```
講師用リポジトリ（このリポジトリ）
      │ main へ push
      ▼
GitHub Actions（.github/workflows/sync-to-student-repo.yml）
      │ answer/・teacher/・README.md・SETUP.md を除外
      │ STUDENT_README.md → README.md にリネーム
      ▼
受講者用リポジトリ（meikai-python-exercises-student）
```

| ファイル・フォルダ | 内容 | 受講者用に同期 |
| --- | --- | --- |
| `exercises/` | 問題と、プログラムを書くためのファイル | する |
| `explanations/` | 解答例・解説（Markdown） | する |
| `tools/` | 自動チェック（`check.py`・`tests.json`） | する |
| `.gitignore` | Git で管理しないファイルの指定 | する |
| `STUDENT_README.md` | 受講者用リポジトリの README.md になる | する（名前を変えて） |
| `answer/` | 解答例のプログラム（`.py`）と、その実行に使うデータ | **しない** |
| `teacher/` | スライド・Word などを置く場合はここへ | **しない** |
| `README.md`（このファイル）・`SETUP.md` | 講師用の説明 | **しない** |

- 受講者用リポジトリは直接編集しないでください（次の同期で上書き・削除されます）。
- 受講者の README を変えたいときは `STUDENT_README.md` を編集して push します。

## 章の一覧

| 章 | タイトル | 問題 | 解答例・解説 | 問題数 | プログラム作成 |
| --- | --- | --- | --- | --- | --- |
| 第1章 | Pythonをはじめよう！ | [問題](exercises/ch01/README.md) | [解答例・解説](explanations/ch01/README.md) | 12 | 0 |
| 第2章 | 画面への表示とキーボードからの入力 | [問題](exercises/ch02/README.md) | [解答例・解説](explanations/ch02/README.md) | 12 | 4 |
| 第3章 | プログラムの流れの分岐 | [問題](exercises/ch03/README.md) | [解答例・解説](explanations/ch03/README.md) | 12 | 2 |
| 第4章 | プログラムの流れの繰返し | [問題](exercises/ch04/README.md) | [解答例・解説](explanations/ch04/README.md) | 12 | 4 |
| 第5章 | オブジェクトと型 | [問題](exercises/ch05/README.md) | [解答例・解説](explanations/ch05/README.md) | 10 | 2 |
| 第6章 | 文字列 | [問題](exercises/ch06/README.md) | [解答例・解説](explanations/ch06/README.md) | 11 | 3 |
| 第7章 | リスト | [問題](exercises/ch07/README.md) | [解答例・解説](explanations/ch07/README.md) | 11 | 3 |
| 第8章 | タプルと辞書と集合 | [問題](exercises/ch08/README.md) | [解答例・解説](explanations/ch08/README.md) | 10 | 3 |
| 第9章 | 関数 | [問題](exercises/ch09/README.md) | [解答例・解説](explanations/ch09/README.md) | 12 | 3 |
| 第10章 | モジュールとパッケージ | [問題](exercises/ch10/README.md) | [解答例・解説](explanations/ch10/README.md) | 6 | 2 |
| 第11章 | クラス | [問題](exercises/ch11/README.md) | [解答例・解説](explanations/ch11/README.md) | 10 | 3 |
| 第12章 | 例外処理 | [問題](exercises/ch12/README.md) | [解答例・解説](explanations/ch12/README.md) | 9 | 3 |
| 第13章 | ファイル処理 | [問題](exercises/ch13/README.md) | [解答例・解説](explanations/ch13/README.md) | 8 | 3 |

## フォルダの構成

```
meikai-python-exercises/
├── README.md            このファイル（講師用の目次）
├── SETUP.md             受講者用リポジトリへの自動同期の設定手順
├── STUDENT_README.md    受講者用リポジトリの README.md
├── .github/workflows/
│   └── sync-to-student-repo.yml   自動同期のワークフロー
├── exercises/           問題と、プログラムを書くためのファイル（同期する）
├── explanations/        解答例・解説の Markdown（同期する）
├── answer/              解答例のプログラム .py（同期しない）
└── tools/
    ├── check.py         プログラム作成問題の自動チェック
    └── tests.json       チェック用の入力と期待される表示
```

## 講師用のメモ

- 解答例のプログラムの確認：`python tools/check.py --answer`（`answer/` のプログラムをチェック）
- 解説では、つまずきやすい点や、スライド（各章の解説用スライド・補足スライド）との対応にも触れています。
- 受講者は解答例・解説（`explanations/`）を読めますが、解答例の `.py` ファイルは受け取りません。
  プログラムは自分で `exercises/` に書いて、`tools/check.py` でチェックします。
- 受講者には受講者用リポジトリ（`meikai-python-exercises-student`）の URL を伝えてクローンしてもらいます。

## PyCharm でクローンする

1. PyCharm を起動し、ようこそ画面の［VCS から取得］をクリックします。
   （プロジェクトを開いている場合は、メニューの［Git］→［クローン…］）
2. ［URL］にこのリポジトリの URL を入力し、［ディレクトリー］に保存先を指定して［クローン］をクリックします。
3. プロジェクトが開いたら、左のプロジェクトツールウィンドウで `exercises/ch01/README.md` を開きます。
   PyCharm では Markdown がプレビュー表示されます（エディターの右上でプレビューの表示方法を切り替えられます）。

## 問題の解き方

1. `exercises/chXX/README.md` を開いて問題を読みます。
2. 答えを書く問題は、ノートや配布された解答用紙などに答えを書きます。
   インタラクティブシェル（PyCharm の［Python コンソール］）で試して確かめてもかまいません。
3. プログラムを作る問題（📝 マークの付いた問題）は、指定された `.py` ファイルを開いて、プログラムを書きます。
   ファイルを右クリック →［実行］で動かしてみましょう。

## 自動チェック

プログラムを作る問題は、決められた入力を与えたときに、実行例どおりに表示されるかを自動でチェックできます。
PyCharm の［ターミナル］で、プロジェクトのフォルダで次のように実行します。

```
python tools/check.py          すべての章をチェック
python tools/check.py ch04     第4章だけチェック
```

`○` が付けば正解です。`×` のときは、期待される表示と実際の表示が並んで表示されるので、違いを確かめましょう。
全角と半角、スペースの数、`：`（全角コロン）なども正確に一致している必要があります。

## 注意

- 第13章（ファイル処理）のプログラムは、`exercises/ch13/score.txt` を読み込みます。
  PyCharm でファイルを右クリック →［実行］で実行すると、作業ディレクトリはそのファイルのあるフォルダになります。
- 自分で作るファイルに `random.py` など、標準ライブラリと同じ名前を付けないでください（第10章 問3）。
