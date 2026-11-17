# セットアップ手順（講師用リポジトリ → 受講者用リポジトリ 自動同期）

このリポジトリには GitHub Actions のワークフロー（`.github/workflows/sync-to-student-repo.yml`）が
用意されています。宛先の受講者用リポジトリ名（`user00-practice/meikai-python-exercises-student`）も
設定済みです。以下の手順で、実際に動くように設定してください。

## 全体像

```
講師用リポジトリ   user00-practice/meikai-python-exercises（Private 推奨）
      │ main へ push
      ▼
GitHub Actions
      │ answer/・teacher/・README.md・SETUP.md を除外
      │ STUDENT_README.md → README.md
      ▼
受講者用リポジトリ user00-practice/meikai-python-exercises-student
```

## 手順1：2つのリポジトリを GitHub 上に用意する

1. 講師用リポジトリ `meikai-python-exercises` を作成します（作成済みならそのままでよい）。
   - 解答例が入っているので **Private** にしてください。
   - 中身は空のまま（README を追加しない）で作成します。手順4でこのフォルダの中身を push します。
2. 受講者用リポジトリ `meikai-python-exercises-student` を作成します。
   - Public / Private は運用に合わせて選びます（受講者のアカウントからクローンできる設定にする）。
   - **必ず初回コミットを1つ入れた状態で作成します。** 作成画面で **Add a README file** にチェックを
     入れるのが一番簡単です。完全に空（コミット0件）だと `main` ブランチが存在せず、ワークフローが
     `couldn't find remote ref refs/heads/main` というエラーで失敗します。
     README の中身は、最初の同期で自動的に上書きされます。

## 手順2：受講者用リポジトリへの書き込み権限を持つトークンを作る

1. GitHub の **Settings → Developer settings → Personal access tokens → Fine-grained tokens** を開く
2. **Generate new token** をクリック
3. 次のように設定する
   - Token name：`meikai-python-student-sync` など分かりやすい名前
   - Expiration：運用に合わせて（学期ごとに更新するなら 90 日など）
   - Repository access：**Only select repositories** → `meikai-python-exercises-student` だけを選ぶ
   - Permissions：**Contents** の権限を追加して **Read and write** にする
     （2025年8月の時点では、**+ Add permissions** → Repositories タブ → Contents を追加し、
     右側の **Access: Read-only** を **Read and write** に変更する画面でした）。
     自動で追加される `Metadata` は Read-only のままでかまいません。
     ※GitHub の画面は変わることがあります。ボタン名が違うときは
     「Contents 権限を Read and write にする」という目的で探してください。
4. **Generate token** を押し、表示されたトークンをコピーしておく（画面を閉じると二度と表示されません）

## 手順3：講師用リポジトリにシークレットとして登録する

1. 講師用リポジトリの **Settings → Secrets and variables → Actions** を開く
2. **New repository secret** をクリック
3. Name：`STUDENT_REPO_TOKEN`、Secret：手順2でコピーしたトークンを貼り付け
4. **Add secret** を押す

## 手順4：講師用リポジトリへ push する

PyCharm の［ターミナル］で、このプロジェクトのフォルダで次を実行します。
（リモート `origin` は講師用リポジトリに設定済みです）

```
git push -u origin main
```

PyCharm の画面で行う場合は、メニューの［Git］→［プッシュ…］でもかまいません。

## 手順5：動作確認（最初の1回は手動で実行する）

ワークフローファイルを初めて追加する push では、GitHub Actions が実行されないことがあります
（ワークフローファイルが「すでにブランチにある状態」の push から動く、という GitHub の挙動）。
そのため、手順4の直後に Actions タブを見てもワークフローが動いていないのは正常です。
最初の1回だけ、次のように手動で実行してください。

1. 講師用リポジトリの **Actions** タブを開き、左のメニューに
   「受講者用リポジトリへ自動同期」が表示されていることを確認する。
2. ワークフロー名をクリックし、右上の **Run workflow** ボタンから実行する
   （「All workflows」の一覧ページのままだとボタンは出ません）。
3. 緑のチェックが付いたら、受講者用リポジトリを開いて次を目で確認する。
   - `exercises/`・`explanations/`（解答例・解説）・`tools/`・`.gitignore` がある
   - `answer/`（解答例の .py）・`SETUP.md`・`.github/` が**ない**
   - README.md が受講者向けの内容（`STUDENT_README.md` の内容）になっている
4. 以降は、`answer/`・`teacher/`・`README.md`・`SETUP.md` 以外のファイルを変更して
   push するたびに、自動で受講者用リポジトリへ反映されます。

実行ログに「Node.js 20 is deprecated …」などの warning が出ることがありますが、
同期の成否とは関係ありません。

## トラブルシューティング

| 症状 | 主な原因・対処 |
|---|---|
| 最初の push で Actions が動かない | 上の手順5のとおり、既知の挙動。**Run workflow** で手動実行する |
| `couldn't find remote ref refs/heads/main`（受講者用リポジトリのチェックアウト） | 受講者用リポジトリにコミットが1つもない。README.md などを1つ追加してコミットしてから再実行する |
| 受講者用リポジトリのチェックアウトで失敗（上記以外） | `STUDENT_REPO_TOKEN` が未登録、またはトークンの対象リポジトリ・権限が違う。手順2・3を見直す |
| 「除外漏れ・除外しすぎがないことを確認」で失敗 | `answer/`・`teacher/` 以外の場所に、名前に answer / teacher を含むファイルがある。名前を変えるか `answer/` に移す |
| Actions タブにワークフローが表示されない | (a) ブランチ名が `main` か確認する。(b) **Settings → Actions → General** で Actions が無効になっていないか確認する |
| 緑のチェックだが受講者用リポジトリが変わらない | `answer/` などの同期しないファイルだけを変更した（意図どおり） |

## 運用上の注意

- 受講者用リポジトリは**直接編集しない**（次の同期で上書き・削除されます）。
- 受講者が自分の解答を GitHub に保存する場合は、受講者用リポジトリを各自のアカウントに
  フォークする・テンプレートとして使う、などの方法を別途案内してください。
