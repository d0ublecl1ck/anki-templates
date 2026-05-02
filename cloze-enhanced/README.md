# Cloze 增强模板

适用于 Anki 内置的 `Cloze` 笔记类型。

## 用法

1. 打开 Anki
2. 进入 `工具 -> 管理笔记类型`
3. 选择 `Cloze`
4. 点 `卡片...`
5. 替换以下内容：
   - `Front Template` -> `front.html`
   - `Back Template` -> `back.html`
   - `Styling` -> `style.css`

## 字段

这个模板沿用 Anki 内置 Cloze 的默认字段：

- `Text`
- `Back Extra`

## 录入示例

### Text

The capital of France is `{{c1::Paris}}`.

### Back Extra

Paris 也是法国最大城市。

## 设计目标

- 让挖空内容更显眼
- 提高长文本可读性
- 保留内置 Cloze 语法兼容性
- 给 `Back Extra` 一个更清晰的解析区
