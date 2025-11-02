# Copilot Repository Instructions (JA-first)

## 目的
このリポジトリでは **日本語** でのレビュー／提案を既定とします。Copilot のコードレビュー（PR Review）や提案コメントは、まず日本語で書いてください。必要に応じて英訳を併記しても構いません。

## レビュー言語とトーン
- 常に **日本語** で応答する（技術用語は原語を保持してOK）。
- 指摘は箇条書きで簡潔に。必要なら **具体的な修正パッチ**（差分やコードブロック）を提示。
- 可読性・命名・例外処理・テスト（実行確認）を基本観点に含める。

## このリポジトリの概要
- 種別: Python 学習用（『ゼロから作る Deep Learning』相当）
- 主言語: Python 3.x
- 構成: `Chapter-*/` 以下にスクリプト。Jupyter を使うこともある。
- 依存: `numpy`, `matplotlib` など。整形は `autopep8` を採用。

## ビルド / 実行 / 体裁
**常に最初に仮想環境を用意**すること。
- 初回:
  1. `python3 -m venv .venv`
  2. `. .venv/bin/activate`
  3. `python -m pip install --upgrade pip`
  4. （必要に応じて）`pip install -r requirements.txt` もしくは `pip install numpy matplotlib autopep8`
- 実行例: `. .venv/bin/activate && python Chapter-1/1.6_Matplotlib.py`
- Jupyter 使用時: `. .venv/bin/activate && python -m ipykernel install --user --name dlscratch --display-name "Python (dlscratch)"`
- 整形: `autopep8 -i <file.py>`（VS Code は `ms-python.autopep8`、保存時整形を推奨）

**注意（Linux/Debian 系）**
システム Python へのグローバル `pip` は PEP 668 により拒否される場合があるため、**常に .venv 内の pip を使用**すること（`<repo>/.venv/bin/pip`）。

## バリデーション手順（PR 前後）
1. `. .venv/bin/activate`
2. `python --version` で Python が .venv を指していることを確認
3. 変更したスクリプトを実行してエラーが出ないか確認
4. `autopep8 -r --in-place .` で整形
5. 可能なら Jupyter も落ちずに起動確認（必要な章のみ）

## PR レビュー時のチェックリスト（Copilot 用）
- [ ] 日本語で総評 → その後に詳細指摘
- [ ] 実行エラーの可能性（未インポート、モジュール名相違、パス）
- [ ] 数値・配列形状の取り扱い（`numpy`）
- [ ] 可視化（`matplotlib`）の保存/表示（非対話環境でも壊れないか：`plt.savefig` 併用など）
- [ ] コード整形（autopep8 適用）と簡潔な命名
- [ ] 仮想環境前提のコマンド記述（グローバル pip の使用は勧めない）

## 変更提案の出し方（Copilot へ）
- 可能なら **差分提案**（```diff ... ```）または **完成コードブロック**を添付。
- 章ディレクトリごとのファイルパスを明示（例: `Chapter-2/AND.py`）。

## 既知の落とし穴
- `python import numpy` のような実行は不可。`python -c "import numpy"`、またはスクリプトに `import numpy as np` を書く。
- `FigureCanvasAgg is non-interactive` 警告が出る環境では `plt.show()` は無視される。必要なら `plt.savefig('out.png')` を併記。
- Debian 系で `pip install` が失敗したら `.venv` を確認（PEP 668）。グローバルに入れない。

## 検索方針
この文書を**最優先で信頼**し、情報が欠けている場合のみリポジトリ内検索を行うこと。
