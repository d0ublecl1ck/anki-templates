# 多选题模板

## 模板字段

创建一个新的 Note Type，并添加这 4 个字段：

1. `question`
2. `options`
3. `answer`
4. `note`

## 字段说明

### question

题干。

### options

每行一个选项，支持手写字母前缀，也支持纯文本逐行填写：

```text
A. TCP
B. UDP
C. HTTP
D. IP
```

### answer

填写所有正确选项，支持这些格式：

- `A C`
- `A,C`
- `1 3`
- `1,3`

模板会按选项顺序比较，不要求输入时自己排序。

### note

解析，可留空。

## 模板安装

把下面 3 个文件内容分别粘到 Anki 的模板设置里：

- `front.html` -> `Front Template`
- `back.html` -> `Back Template`
- `style.css` -> `Styling`

## 模板行为

- 正面显示题干和所有选项
- 每次出题随机打乱选项显示顺序
- 点击可切换选中状态
- 快捷键支持 `1-9`
- 背面按原始选项字母判断是否答对，并显示你的选择、标准答案和解析

## 示例

### question

下面哪些属于传输层协议？

### options

```text
A. TCP
B. UDP
C. HTTP
D. IP
```

### answer

A,B

### note

`TCP` 和 `UDP` 属于传输层；`HTTP` 属于应用层，`IP` 属于网络层。
