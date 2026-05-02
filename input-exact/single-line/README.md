# 单行严格输入题

## 字段

新建一个 Note Type，并添加：

1. `prompt`
2. `answer`
3. `note`
4. `feedback`

## 规则

- 严格逐字符比较
- 大小写必须一致
- 空格必须一致
- 标点必须一致

`feedback` 是可选字段：

- 留空：不即时提示
- 填 `on` / `1` / `yes` / `true`：输入时立即高亮差异

## 安装

- `front.html` -> `Front Template`
- `back.html` -> `Back Template`
- `style.css` -> `Styling`

## 示例

### prompt

请输入 Python 关键字。

### answer

return

### note

这里只接受完全一致的 `return`。

### feedback

on
