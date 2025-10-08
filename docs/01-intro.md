---
marp: true
theme: default
paginate: true
---

# 2025年 情報システム実験Ⅰ
# AIエージェントを作ってみよう

---

## 概要

本授業では、7回の講義を通してAIエージェントを開発します。

- AIエージェントの概要
- mcp(Model Context Protocol)
- Pythonを使用したAIエージェントの構築
- Discordを使用したAIエージェントの公開

---

## 自己紹介

---

## 授業内容とスケジュール

本授業では、7回の講義を通してAIエージェントを開発します。

---

| 日付 | 内容 |
|---|---|
| 10/8 | AIエージェントとmcpについての説明<br>claude desktopのインストールとmcpの利用 |
| 10/15 | 13:00〜 discordへのinvite作業／作成したいAIエージェントの案を出す<br>15:00〜 mcpサーバーを自作してclaude desktopから呼び出す |
| 10/22 | 13:00〜 前回の続き<br>15:00〜 OpenAIのAPIをPythonから呼び出す／パラメータ調整 |
| 10/29 | 前回の続き |
| 11/12 | 13:00〜 前回の続き<br>15:00〜 AIエージェントをdiscordと接続+スライド作り |
| 11/19 | AIエージェントをdiscordと接続+スライド作り |
| 11/26 | 発表+他の人の作品を触る |


---

### スケジュールについて

- 講師の都合により、一部先生とTAさんに進行してもらう会があります。

---

## インターンの紹介（宣伝）

株式会社ヴァル研究所ではインターンを実施しています！

- [会社紹介](https://drive.google.com/file/d/1Kr8fQGCUHr_oTb_B_vD2fnUMdBf5amGR/view?usp=drive_link)
- [27卒会社説明会・選考案内](https://drive.google.com/file/d/1zJAKpR8jKkyR2yl3pVsQ8ynWF_9SMXbN/view?usp=drive_link)

---

## 今日の内容

- AIエージェントとはなにか
- mcp(Model Context Protocol)とはなにか
- 既存のAIツールを触ってみよう

---

## 今日のゴール

- AIエージェントとはなにか理解できている
- mcp(Model Context Protocol)とはなにか理解できている
- Claude Desktopを使用し、3つ以上のmcpサーバーを試すことができている

---

# AIエージェント



---


## claude desktop でmcpサーバーを使ってみる

### claude desktop のインストール

https://claude.ai/download
