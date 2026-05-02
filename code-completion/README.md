# code-completion

代码补全题模板。

## 字段

新建一个 Note Type，并添加：

1. `prompt`
2. `code`
3. `answers`
4. `language`
5. `note`

## 挖空语法

在 `code` 里用下面格式写占位：

- `[[1]]`
- `[[2]]`
- `[[3]]`

示例：

```python
def add(a, b):
    return [[1]] + [[2]]
```

`answers` 按行对应填写：

```text
a
b
```

## 规则

- 每个空严格逐字符比较
- 大小写、空格、标点都必须完全一致
- 即时差异提示改为全局开关
- 在任意一张代码补全卡正面点按钮后，后续代码补全卡都会沿用同一状态

## 语言高亮

`language` 填常见语言名即可，例如：

- `python`
- `javascript`
- `java`
- `cpp`
- `go`
- `rust`

- 正面为了保留输入框，使用内置轻量高亮
- 背面使用外部高亮脚本；如果加载失败，仍可正常使用，只是退回普通代码显示

## 安装

- `front.html` -> `Front Template`
- `back.html` -> `Back Template`
- `style.css` -> `Styling`

## 示例

### prompt

补全下面的 Python 代码。

### code

```python
def add(a, b):
    return [[1]] + [[2]]
```

### answers

a
b

### language

python

### note

这里要求把两个变量名都完整填对。
