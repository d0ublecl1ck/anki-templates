# 英语单词 TSV 生成提示词

请把我提供的英语单词整理成 Anki 可导入的 TSV。必须严格遵守下面规则：

1. 只输出 TSV 内容，不要输出解释。
2. 第一行必须是字段名。
3. 字段顺序必须完全一致：
   `Word	Meaning	Pronunciation	Audio	Example	ExampleMeaning	ExampleAudio	PartOfSpeech	Collocation	Register	Synonyms	Antonyms	Confusable	Mnemonic	Etymology	Note	SelfSentencePrompt`
4. 每个单词一行。
5. 单元格内不要换行。
6. 不要使用 Markdown 表格。
7. `Audio` 和 `ExampleAudio` 留空，后续由 HyperTTS 或 edge-tts 自动生成。
8. `Meaning` 使用中文，保留 1 到 3 个最高频核心义。
9. `Example` 使用自然、简洁、适合记忆的英文例句。
10. `ExampleMeaning` 给出自然中文翻译。
11. `Collocation` 用分号分隔常见搭配。
12. `Synonyms`、`Antonyms`、`Confusable` 不要堆砌，优先给最有区分价值的内容。
13. `Mnemonic` 要短，不能牵强。
14. `SelfSentencePrompt` 用中文提出一个输出练习。

待处理单词：

```text
在这里粘贴单词列表
```
