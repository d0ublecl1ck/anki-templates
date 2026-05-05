# 单选题模板

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

每行一个选项，支持两种写法：

```text
A. 苹果
B. 香蕉
C. 葡萄
```

或：

```text
苹果
香蕉
葡萄
```

如果不手写 `A/B/C`，模板会自动按顺序补上。

### answer

填写正确选项的字母或序号，例如：

- `B`
- `2`

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
- 点击选项即可作答
- 快捷键支持 `1-9`
- 背面按原始选项字母判断是否答对，并显示你的选择、标准答案和解析

## 示例

### question

以下哪一个是 Python 的内置可变序列类型？

### options

```text
A. tuple
B. list
C. str
D. frozenset
```

### answer

B

### note

`list` 是可变序列，`tuple` 和 `frozenset` 不可变。
