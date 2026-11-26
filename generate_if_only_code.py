from pathlib import Path

MAX = int(input("max =>"))

if MAX < 0:
    print("0以上")
else:
    lines = [
        'n = int(input("判定する数を入力してください: "))',
        '',
        'if n == 0:',
        '    print("0: 偶数")'
    ]

    for i in range(1, MAX + 1):
        kind = "奇数" if i % 2 else "偶数"
        lines.extend([
            f'elif n == {i}:',
            f'    print("{i}: {kind}")'
        ])

    lines.extend([
        'else:',
        '    print("指定範囲外です。")'
    ])

    output = "\n".join(lines) + "\n"
    path = Path("if_only_generated.py")
    path.write_text(output, encoding="utf-8")

    print(f"{path} を生成しました。")
    print(f"if/elif 条件数: {MAX + 1}")
