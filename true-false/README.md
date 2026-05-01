# 判断题 Anki 模板

## 字段

创建一个新的 Note Type，并添加这 3 个字段：

1. `question`
2. `answer`
3. `note`

`answer` 建议只填以下值之一：

- `True`
- `False`
- `正确`
- `错误`

## 安装

把下面 3 个文件内容分别粘到 Anki 的模板设置里：

- `front.html` -> `Front Template`
- `back.html` -> `Back Template`
- `style.css` -> `Styling`

## 行为

- 正面显示题干和“正确 / 错误”两个按钮
- 按 `1` 代表“正确”
- 按 `0` 代表“错误”
- 背面会显示你选得对不对，以及标准答案和解析

## 示例

### question

地球是围绕太阳公转的。

### answer

正确

### note

这是基础天文学常识。地球围绕太阳公转，同时地球自转导致昼夜变化。
