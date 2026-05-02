# Basic 增强模板

适用于 Anki 内置的 `Basic` 笔记类型。

## 字段

这个模板直接使用 Anki 内置 Basic 的默认字段：

1. `Front`
2. `Back`

## 安装

把下面 3 个文件内容分别粘到 Anki 的模板设置里：

- `front.html` -> `Front Template`
- `back.html` -> `Back Template`
- `style.css` -> `Styling`

## 行为

- 正面显示 `Front`
- 背面通过 `{{FrontSide}}` 保留正面内容，再显示 `Back`
- 样式保持简洁，不添加无关元素

## 示例

### Front

法国的首都是哪里？

### Back

巴黎。
