# Marp Slides

このディレクトリには、Marpで作成されたプレゼンテーションスライドが含まれています。

## スライドの追加方法

1. このディレクトリに新しい `.md` ファイルを作成します
2. ファイルの先頭に以下のfront matterを追加します：

```markdown
---
marp: true
theme: default
paginate: true
---

# スライドのタイトル

スライドの内容...

---

## 次のスライド

さらにコンテンツ...
```

3. `---` でスライドを区切ります
4. メインブランチにプッシュすると、GitHub Actionsが自動的にスライドをビルドしてGitHub Pagesにデプロイします

## 出力形式

- **HTML**: ブラウザで表示可能なスライド
- **PDF**: ダウンロード・印刷可能なスライド

## Marpの詳細

- [Marp公式ドキュメント](https://marpit.marp.app/)
- [Marp CLI](https://github.com/marp-team/marp-cli)
