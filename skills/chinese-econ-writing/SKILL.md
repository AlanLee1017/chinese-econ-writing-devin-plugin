---
name: chinese-econ-writing
description: Coordinate Chinese economics and management writing tasks by routing introduction, empirical-results, and broader top-journal style work to focused skills. Use as the unified entry point when a manuscript needs section-specific revision or several Chinese writing modes.
metadata:
  short-description: 中文经管论文写作总入口
---

# 中文经管论文写作总入口

这是一个协调型 Skill，用于把不同论文部分交给更窄的写作技能，避免用同一套规则处理引言、实证结果和全文风格。

## 路由

- 摘要、关键词和研究设计压缩 → `chinese-econ-abstract`
- 引言第一段至结构安排 → `chinese-econ-introduction`
- 文献综述、理论机制、研究假说、贡献定位 → `chinese-econ-literature`
- 制度背景、数据来源、样本构造、变量和描述性统计 → `chinese-econ-data`
- 识别策略、模型、识别假设、固定效应和标准误 → `chinese-econ-identification`
- 基准回归、稳健性、机制、异质性、表格解读 → `chinese-econ-results`
- 稳健性、机制、异质性和替代解释的专题重组 → `chinese-econ-discussion`
- 结论、政策含义、研究局限和外部有效性 → `chinese-econ-conclusion`
- 表格、图形、表注和正文之间的一致性 → `chinese-econ-tables`
- 期刊范本、作者风格、分部分整体诊断 → `chinese-top-econ-writing`
- 同时涉及多个部分 → 先分别应用对应 Skill，再统一检查术语、因果边界、表号、变量名和作者语气。

## 统一工作协议

1. 明确目标部分、目标期刊或期刊组、研究领域和证据状态。
2. 保留用户事实、数字、引用、表号、变量名和识别设计，不因追求“顶刊语气”而扩张结论。
3. 先诊断段落功能和论证顺序，再改写句子。
4. 实证结果默认采用中文经管论文的自然叙述：正文报告方向、量级、显著性和经济含义；单个系数后的精确 p/t/z 值括号必须删除，只有明确标注的联合或整体检验可以保留精确 p 值。
5. 交付前必须做完整文本扫描，检查 `p=`、`p值`、`t=`、`z=` 等技术输出残留，并检查技术报告腔、逐系数复述、因果措辞越界、机制过度解释、引言贡献夸大和编辑残留。

## 组合方式

在本地 Skill 系统中，这个总入口负责路由；各个 focused skills 保持独立、可单独调用和更新。需要增加新部分时，新增窄技能并在本文件的路由表中登记即可。

## 交付格式

- 诊断任务：按论文部分给出问题、范式和可操作修改。
- 改写任务：先给可直接放入正文的中文文本，再给简短修改说明。
- 多部分任务：按部分分组输出，最后附一轮统一一致性检查。
