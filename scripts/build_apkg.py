from __future__ import annotations

from pathlib import Path
import random

import genanki


ROOT = Path("/Users/d0ublecl1ck/anki-templates")
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def stable_id(seed: int) -> int:
    random.seed(seed)
    return random.randrange(1 << 30, 1 << 31)


def package_basic() -> None:
    folder = ROOT / "basic-enhanced"
    deck = genanki.Deck(stable_id(1001), "中文::基础问答（简洁版）")
    model = genanki.Model(
        stable_id(2001),
        "基础问答（简洁版）",
        fields=[
            {"name": "Front"},
            {"name": "Back"},
        ],
        templates=[
            {
                "name": "卡片 1",
                "qfmt": read_text(folder / "front.html"),
                "afmt": read_text(folder / "back.html"),
            }
        ],
        css=read_text(folder / "style.css"),
    )
    note = genanki.Note(
        model=model,
        fields=[
            "法国的首都是哪里？",
            "巴黎。",
        ],
    )
    deck.add_note(note)
    genanki.Package(deck).write_to_file(str(DIST / "基础问答-简洁版.apkg"))


def package_true_false() -> None:
    folder = ROOT / "true-false"
    deck = genanki.Deck(stable_id(1002), "中文::判断题")
    model = genanki.Model(
        stable_id(2002),
        "判断题",
        fields=[
            {"name": "question"},
            {"name": "answer"},
            {"name": "note"},
        ],
        templates=[
            {
                "name": "卡片 1",
                "qfmt": read_text(folder / "front.html"),
                "afmt": read_text(folder / "back.html"),
            }
        ],
        css=read_text(folder / "style.css"),
    )
    note = genanki.Note(
        model=model,
        fields=[
            "地球围绕太阳公转。",
            "正确",
            "这是基础天文学常识。",
        ],
    )
    deck.add_note(note)
    genanki.Package(deck).write_to_file(str(DIST / "判断题.apkg"))


def package_cloze() -> None:
    folder = ROOT / "cloze-enhanced"
    deck = genanki.Deck(stable_id(1003), "中文::挖空卡（简洁版）")
    model = genanki.Model(
        stable_id(2003),
        "挖空卡（简洁版）",
        fields=[
            {"name": "Text"},
            {"name": "Back Extra"},
        ],
        templates=[
            {
                "name": "挖空卡",
                "qfmt": read_text(folder / "front.html"),
                "afmt": read_text(folder / "back.html"),
            }
        ],
        css=read_text(folder / "style.css"),
        model_type=genanki.Model.CLOZE,
    )
    note = genanki.Note(
        model=model,
        fields=[
            "中国的首都是 {{c1::北京}}。",
            "北京也是中国的政治中心。",
        ],
    )
    deck.add_note(note)
    genanki.Package(deck).write_to_file(str(DIST / "挖空卡-简洁版.apkg"))


def package_input_single() -> None:
    folder = ROOT / "input-exact" / "single-line"
    deck = genanki.Deck(stable_id(1004), "中文::严格输入（单行）")
    model = genanki.Model(
        stable_id(2004),
        "严格输入（单行）",
        fields=[
            {"name": "prompt"},
            {"name": "answer"},
            {"name": "note"},
            {"name": "feedback"},
        ],
        templates=[
            {
                "name": "卡片 1",
                "qfmt": read_text(folder / "front.html"),
                "afmt": read_text(folder / "back.html"),
            }
        ],
        css=read_text(folder / "style.css"),
    )
    note = genanki.Note(
        model=model,
        fields=[
            "请输入 Python 中用于返回结果的关键字。",
            "return",
            "必须逐字符完全一致。",
            "on",
        ],
    )
    deck.add_note(note)
    genanki.Package(deck).write_to_file(str(DIST / "严格输入-单行.apkg"))


def package_input_multi() -> None:
    folder = ROOT / "input-exact" / "multi-line"
    deck = genanki.Deck(stable_id(1005), "中文::严格输入（多行）")
    model = genanki.Model(
        stable_id(2005),
        "严格输入（多行）",
        fields=[
            {"name": "prompt"},
            {"name": "answer"},
            {"name": "note"},
            {"name": "feedback"},
        ],
        templates=[
            {
                "name": "卡片 1",
                "qfmt": read_text(folder / "front.html"),
                "afmt": read_text(folder / "back.html"),
            }
        ],
        css=read_text(folder / "style.css"),
    )
    note = genanki.Note(
        model=model,
        fields=[
            "请逐行输入下面两行文本。",
            "第一行\n第二行",
            "换行、空格、标点都必须完全一致。",
            "on",
        ],
    )
    deck.add_note(note)
    genanki.Package(deck).write_to_file(str(DIST / "严格输入-多行.apkg"))


def package_code_completion() -> None:
    folder = ROOT / "code-completion"
    deck = genanki.Deck(stable_id(1006), "中文::代码补全")
    model = genanki.Model(
        stable_id(2006),
        "代码补全",
        fields=[
            {"name": "prompt"},
            {"name": "code"},
            {"name": "answers"},
            {"name": "language"},
            {"name": "note"},
        ],
        templates=[
            {
                "name": "卡片 1",
                "qfmt": read_text(folder / "front.html"),
                "afmt": read_text(folder / "back.html"),
            }
        ],
        css=read_text(folder / "style.css"),
    )
    note = genanki.Note(
        model=model,
        fields=[
            "补全下面的 Python 代码。",
            "def add(a, b):\n    return [[1]] + [[2]]",
            "a\nb",
            "python",
            "这里要求把两个变量名都完整填对。",
        ],
    )
    deck.add_note(note)
    genanki.Package(deck).write_to_file(str(DIST / "代码补全.apkg"))


def main() -> None:
    package_basic()
    package_true_false()
    package_cloze()
    package_input_single()
    package_input_multi()
    package_code_completion()
    print(f"已生成到: {DIST}")


if __name__ == "__main__":
    main()
