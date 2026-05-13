# 英语单词科学记忆模板

用于背英语单词本身，重点是主动回忆、即时反馈、语境巩固和自动播放音频。

## 笔记类型

建议新建笔记类型：`英语单词-科学记忆`

## 字段

按下面顺序创建字段，便于 TSV 批量导入：

1. `Word`
2. `Meaning`
3. `Pronunciation`
4. `Audio`
5. `Example`
6. `ExampleMeaning`
7. `ExampleAudio`
8. `PartOfSpeech`
9. `Collocation`
10. `Register`
11. `Synonyms`
12. `Antonyms`
13. `Confusable`
14. `Mnemonic`
15. `Etymology`
16. `Note`
17. `SelfSentencePrompt`

## 卡片

### 卡片 1：Word -> Meaning

- `front.html` -> `Front Template`
- `back.html` -> `Back Template`
- `style.css` -> `Styling`

正面显示单词、音频和音标，让你主动回忆核心释义、词性、搭配和例句。背面按重要性分层展示完整词条。

### 卡片 2：Meaning -> Word

可以在 Anki 里复制卡片 1，再把正面改成只显示 `Meaning` 和 `ExampleMeaning`，用于训练主动输出。

## HyperTTS

如果你已经安装并习惯使用 HyperTTS，可以使用 HyperTTS 的 Collection Audio：

1. 先导入文本字段。
2. 用 HyperTTS 批量为 `Word` 生成音频，写入 `Audio` 字段。
3. 可选：为 `Example` 生成音频，写入 `ExampleAudio` 字段。

模板正面和背面都直接放置 `{{Audio}}`，背面不会依赖 `{{FrontSide}}` 继承音频，因此翻面后也能再次播放。

## edge-tts + AnkiConnect 音频流程

如果不想使用 HyperTTS，可以在导入时由脚本自动生成音频并写入 Anki。

推荐流程：

1. 用 AI 生成完整词条字段。
2. 用 `edge-tts` 为 `Word` 生成单词 MP3。
3. 用 `edge-tts` 为 `Example` 生成例句 MP3。
4. 用 AnkiConnect `storeMediaFile` 写入 Anki 媒体库。
5. 创建或更新笔记时写入：
   - `Audio` -> `[sound:english_word_<word>.mp3]`
   - `ExampleAudio` -> `[sound:english_word_<word>_example.mp3]`

本项目已经验证过的音频生成方式：

```bash
python3 -m venv .context/tts-venv
.context/tts-venv/bin/python -m pip install edge-tts
```

建议把临时工具安装在 `.context/` 下，避免污染项目依赖。生成后的 MP3 应通过 AnkiConnect 存入 Anki 媒体库，而不是手工复制到项目目录。

## 导入

优先使用 `import-template.tsv`。TSV 比 CSV 更适合例句，因为例句里经常出现逗号。

导入时：

1. 打开 Anki 的导入功能。
2. 选择 `import-template.tsv` 或同结构 TSV。
3. 选择笔记类型 `英语单词-科学记忆`。
4. 确认字段顺序一致。
5. 导入后用 HyperTTS 或 `edge-tts + AnkiConnect` 生成音频字段。

## AI 生成

使用 `ai-generation-prompt.md` 让 AI 按固定列输出 TSV。生成后可以直接导入 Anki，再批量生成音频。

如果由自动化脚本直接创建 Anki 笔记，可以跳过 TSV 文件，但仍应保持字段顺序和字段含义一致。
