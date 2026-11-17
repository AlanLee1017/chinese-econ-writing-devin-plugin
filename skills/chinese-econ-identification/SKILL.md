---
name: chinese-econ-identification
description: Write and audit Chinese empirical economics identification-strategy, model, assumptions, and estimation sections with precise causal language and transparent threats.
metadata:
  short-description: 中文经管识别策略与模型
---

# 中文经管识别策略与模型

把计量模型写成识别论证，而不是公式说明。先明确估计对象和变异来源，再说明假设、固定效应、推断方式与威胁。

## 推荐顺序

估计目标 → 处理变量和对照 → 外生变化来源 → 识别假设 → 模型与固定效应 → 标准误聚类 → 主要威胁和检验。

## 句法

- “本文利用……造成的时间/空间差异识别……。”
- “该设计依赖于……在政策实施前具有相似趋势。”
- “模型控制……固定效应，以吸收……。”
- “标准误聚类于……层级，原因是处理变量在该层级变化。”
- “该策略能够缓解……，但仍可能受到……影响，因此本文进一步进行……。”

## 方法边界

DID要说明处理时间、平行趋势和错位实施；IV要说明第一阶段、相关性和排除限制；RD要说明断点、带宽和操纵；事件研究要说明动态系数和基准期；匹配和控制变量不能自动消除不可观测混淆。

避免“解决了内生性”“完全排除了选择偏误”等绝对表述。详细模板见 [references/identification-patterns.md](references/identification-patterns.md)。
