# Input Cloze 题类

适用于支持 `Cloze` 语法的自定义笔记类型，但前面会把当前卡片的挖空位置替换成行内输入框。

## 用法

1. 推荐直接导入 `dist/输入挖空卡.apkg`
2. 或者在 Anki 里复制内置 `Cloze` 笔记类型
3. 打开新笔记类型的 `卡片...`
4. 替换以下内容：
   - `Front Template` -> `front.html`
   - `Back Template` -> `back.html`
   - `Styling` -> `style.css`

## 字段

沿用 Cloze 的默认字段：

- `Text`
- `Back Extra`

## 录入示例

### Text

C++ 的 main 函数返回的类型是 `{{c1::int}}`。

在 `{{c1::C 加加}}` 中 `{{c2::int}}` 是 main 函数返回的类型。

## 行为

- 继续使用标准 Cloze 语法出卡
- 当前卡片对应的挖空会在原句位置变成输入框
- 支持句首、句中、句尾挖空
- 背面行为与普通 Cloze 一致
