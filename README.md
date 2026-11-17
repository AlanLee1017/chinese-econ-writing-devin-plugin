# 中文经管论文写作 Devin Plugin

一个面向中文经济学与管理学论文的 Devin 插件，按论文部分提供可组合 Skills：摘要、引言、文献综述与理论机制、制度背景与数据、识别策略、实证结果、稳健性与机制、表格图形、结论与政策含义。

## 安装到 Devin

Devin CLI：

```bash
devin plugins install <github-owner>/<github-repository>
devin plugins list
devin plugins info chinese-econ-writing
```

如果使用 Git URL：

```bash
devin plugins install https://github.com/<github-owner>/<github-repository>.git
```

安装后可以用插件命名空间调用，例如：

```text
/chinese-econ-writing:chinese-econ-results
/chinese-econ-writing:chinese-econ-introduction
/chinese-econ-writing:chinese-econ-literature
```

## 技能目录

- `chinese-econ-writing`：统一路由入口
- `chinese-top-econ-writing`：期刊和作者风格、全文诊断
- `chinese-econ-abstract`：摘要
- `chinese-econ-introduction`：引言分段
- `chinese-econ-literature`：文献综述、理论机制和研究假说
- `chinese-econ-data`：制度背景、数据、样本和变量
- `chinese-econ-identification`：识别策略、模型和识别假设
- `chinese-econ-results`：基准实证结果陈述
- `chinese-econ-discussion`：稳健性、机制、异质性和替代解释
- `chinese-econ-tables`：表格、图形和表注
- `chinese-econ-conclusion`：结论、政策含义和局限

## 设计原则

- 中文经济学论文正文默认不逐个报告括号内的精确 p 值，优先使用“在1%的统计水平上显著”等自然表述。
- 区分统计显著、经济显著和因果解释。
- 保留变量、样本、表号、估计结果、引用和识别边界。
- 范式参考本地 Zotero 样本以及 `Awesome-Journal-Skills` 的期刊范本与分技能工作流；具体文献结论应回到原文核验。
