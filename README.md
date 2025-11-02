> **【追記 / Added by @kjikuhar — 2025-11-02 JST】**
> このリポジトリ内のコードは、学習目的で整理されています。
> 自学用に作成した章ごとの実装は **`Chapter-X` ディレクトリ** にまとめています（例：`Chapter-1`, `Chapter-2`, …）。
> これらは書籍『ゼロから作る Deep Learning』の内容をもとに、手を動かして理解を深めるための個人学習用コードです。
>
> 一方で、**`ch0X` 系ディレクトリ（例：`ch01`, `ch02`）** は書籍の著者が用意した公式回答・参照実装です。
> 同一章の実装を比較することで、書籍の内容理解や改善点の検証に役立てられます。
>
> 各フォルダの対応関係：
>
> | 区分          | 用途              | 例                  |
> | ----------- | --------------- | ------------------ |
> | `Chapter-X` | 自学・再実装・試行実験用コード | `Chapter-2/AND.py` |
> | `ch0X`      | 著者提供の公式実装       | `ch02/and_gate.py` |
>
> 自分の学習過程での考察や修正を、`Chapter-X` ディレクトリ内に独立して記録する設計にしています。

---

> **【追記 / Added by @kjikuhar — 2025-11-01 JST】**
> このリポジトリは **Conda なし（venv + pip）** で即動作します。
> `Makefile` により環境構築が自動化されているため、どの端末でも同じ手順でセットアップ可能です。
> *元のREADME本文はこの追記の下にあります。*

## 🚀 最短セットアップ（Makefile使用 / Conda不要）

### 推奨環境
- Python 3.8–3.13（本書は3系を想定。安定性重視なら3.8–3.11を推奨）
- make コマンドが使用可能であること（Linux / macOS / WSLで標準搭載）

---

### 1️⃣ 準備
まずこのリポジトリをクローンします：

```bash
git clone https://github.com/oreilly-japan/deep-learning-from-scratch.git
cd deep-learning-from-scratch
````

---

### 2️⃣ セットアップ（ワンコマンド）

以下のコマンドだけで仮想環境の作成・依存関係のインストール・Jupyter登録がすべて自動実行されます👇

```bash
make install
```

> `.venv` ディレクトリが自動作成され、`requirements.txt` に基づく環境が構築されます。

---

### 3️⃣ 実行

Jupyter Notebookを開く場合：

```bash
make jupyter
```

その後、ブラウザで `http://localhost:8888` にアクセスするとノートブックが使えます。
または、章ごとのPythonスクリプトを直接実行できます：

```bash
cd ch01
python man.py

cd ../ch05
python train_neuralnet.py
```

---

### 4️⃣ 依存関係（requirements.txt）

必要なPythonパッケージは以下の通りです：

```txt
numpy==1.26.4
matplotlib==3.8.4
ipython==8.18.1
ipykernel==6.29.5
notebook==7.2.1
tqdm==4.66.5
pillow==10.4.0
```

> 書籍で使うNumPy・Matplotlibに加え、Notebook・進捗バー・画像処理をサポートする実用的な構成です。

---

### 5️⃣ 環境の削除（任意）

作成した仮想環境を削除する場合：

```bash
make clean
```

---

### 💡 補足

* Windows環境では `make` の代わりに **Git Bash** や **WSL** で実行してください。
* 仮想環境を手動で扱いたい場合は `. .venv/bin/activate` で有効化できます。

---

ゼロから作る Deep Learning
==========================


[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch/images/deep-learning-from-scratch.png" width="200px">](https://www.oreilly.co.jp/books/9784873117584/)

書籍『[ゼロから作る Deep Learning](http://www.oreilly.co.jp/books/9784873117584/)』(オライリー・ジャパン発行)のサポートサイトです。本書籍で使用するソースコードがまとめられています。



## ファイル構成

|フォルダ名 |説明                         |
|:--        |:--                          |
|ch01       |1章で使用するソースコード    |
|ch02       |2章で使用するソースコード    |
|...        |...                          |
|ch08       |8章で使用するソースコード    |
|common     |共通で使用するソースコード   |
|dataset    |データセット用のソースコード |


ソースコードの解説は本書籍をご覧ください。

## Pythonと外部ライブラリ
ソースコードを実行するには、下記のソフトウェアが必要です。

* Python 3.x
* NumPy
* Matplotlib

※Pythonのバージョンは、3系を利用します。

## 実行方法

各章のフォルダへ移動して、Pythonコマンドを実行します。

```
$ cd ch01
$ python man.py

$ cd ../ch05
$ python train_nueralnet.py
```

## クラウドサービスでの実行

本書のコードは次の表にあるボタンをクリックすることで、AWSの無料の計算環境である[Amazon SageMaker Studio Lab](https://studiolab.sagemaker.aws/)上に実行できます(事前に[メールアドレスによる登録](https://studiolab.sagemaker.aws/requestAccount)が必要です)。SageMaker Studio Labの使い方は[こちら](https://github.com/aws-sagemaker-jp/awesome-studio-lab-jp/blob/main/README_usage.md)をご覧ください。[Amazon SageMaker Studio Lab Community](https://github.com/aws-studiolab-jp/awesome-studio-lab-jp)で最新情報が取得できます。

|フォルダ名 |Amazon SageMaker Studio Lab
|:--        |:--                          |
|ch01       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch01.ipynb)|
|ch02       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch02.ipynb)|
|ch03       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch03.ipynb)|
|ch04       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch04.ipynb)|
|ch05       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch05.ipynb)|
|ch06       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch06.ipynb)|
|ch07       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch07.ipynb)|
|ch08       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/ch08.ipynb)|
|common       |[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch/blob/master/notebooks/common.ipynb)|


## ライセンス

本リポジトリのソースコードは[MITライセンス](http://www.opensource.org/licenses/MIT)です。
商用・非商用問わず、自由にご利用ください。

## 正誤表

本書の正誤情報は以下のページで公開しています。

https://github.com/oreilly-japan/deep-learning-from-scratch/wiki/errata

本ページに掲載されていない誤植など間違いを見つけた方は、[japan@oreilly.co.jp](<mailto:japan@oreilly.co.jp>)までお知らせください。
