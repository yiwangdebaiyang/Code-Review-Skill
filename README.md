# AI Code Review Skill / Python代码审查技能

一个适合初学者的 Python 代码审查 Skill。使用 Python 标准库 AST 检查语法、列出函数和循环、提示少量潜在问题，并生成 Markdown 报告。**不依赖 API，也不调用大模型；检查规则有限，不能保证找出所有 Bug。**

## 文件说明
- `SKILL.md`：供 AI 助手读取的技能使用说明
- `app.py`：命令行入口
- `core/`：语法分析、问题提示、注释建议、结构总结模块
- `examples/demo.py`：测试用例
- `requirements.txt`：依赖说明（无需额外安装库）

## 快速使用
在 VS Code 打开项目文件夹，点击“终端 → 新建终端”，输入：

```bash
python app.py examples/demo.py
```

Windows 如果 `python` 无法使用，可尝试 `py app.py examples/demo.py`。

可选：保存报告到文件：

```bash
python app.py examples/demo.py --output report.md
```

## 当前支持
- 语法检查（SyntaxError）
- 函数、类与循环结构统计
- 明确写出的除零表达式、`eval/exec` 和裸 `except` 提示
- 缺失函数 docstring 的提醒
- Markdown 分析报告

## 注意
本项目只检查代码，不执行被分析的文件。`SKILL.md` 描述 AI 助手如何使用此工具；是否能被某个 AI 产品直接安装，取决于其 Skill 支持方式。
