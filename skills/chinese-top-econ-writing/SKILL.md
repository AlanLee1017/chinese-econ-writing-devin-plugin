---
name: chinese-top-econ-writing
description: Analyze, emulate, and revise Chinese economics and management manuscripts using section-specific patterns distilled from high-impact articles in Economic Research, Finance & Trade Economics, The World Economy, Management World, China Economic Quarterly, and related journals. Use when the user asks for Chinese top-journal writing style, section templates, empirical-result phrasing, or a style guide grounded in Zotero and the Awesome-Journal-Skills repository.
metadata:
  short-description: 中文经管顶刊分部分写作范式
---

# 中文经管顶刊写作范式

Use this skill to produce evidence-bounded, section-aware guidance for Chinese economics and management writing. The goal is to recover reusable reasoning and sentence structures from real papers, not to imitate an author mechanically or add unsupported claims.

## Source and evidence rules

- When a Zotero library is available, inspect the user's local records first. Prefer records with full text, abstracts, publication title, year, authors, and a dated citation-count snapshot.
- Treat citation counts as dated snapshots. Never present a Zotero `extra` count as a current ranking unless it has been rechecked against a current source.
- Use the repository [Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) as a discovery index and method/ topic map. Verify the journal, year, issue, title, and substantive claims against the original article or a reliable journal page before using them.
- Preserve the boundary between association and causality. Do not strengthen “相关”“对应”“伴随” into “影响”“导致” unless the design supports that wording.
- Do not reproduce long passages. Paraphrase patterns and provide short, newly written templates tied to the user's variables and design.
- Distinguish observed sample evidence, proposed mechanisms, robustness checks, and policy interpretation.

## Choose the operating mode

1. **Corpus map**: rank or group local articles by journal, field, author, method, and dated citation snapshot.
2. **Section diagnosis**: compare a draft with the relevant pattern for introduction, institutional background, data, identification, results, mechanisms, heterogeneity, conclusion, or policy implications.
3. **Patterned rewrite**: rewrite a supplied passage while preserving facts, estimates, citations, terminology, and causal boundaries.
4. **Style comparison**: contrast authors or fields, for example macro, public finance, finance, corporate finance, labor, agriculture, or digital economy.
5. **Style guide**: produce a reusable checklist, sentence bank, or project-specific writing protocol.

## Required workflow

1. Define the target section, field, journal family, and evidence status.
2. Select at least three genuinely different exemplars when the user asks for a general pattern; include the article keys or bibliographic identifiers when available.
3. Read the relevant abstract, introduction, methods, results, or conclusion. Do not infer full-paper style from an abstract alone; state when only metadata or abstracts were available.
4. Extract the argument sequence, paragraph function, recurrent sentence moves, verb strength, qualification, result ordering, and transition logic.
5. Convert those observations into a compact pattern: purpose → sentence structure → acceptable verbs → evidence boundary → example template.
6. Apply the pattern to the user's passage only after checking variables, sample, identification, estimates, and references.
7. Run a residue check: remove conversational instructions, drafting commentary, generic praise, unsupported mechanism claims, and inflated contribution language.

## Section-specific priorities

- **Introduction**: phenomenon or puzzle → literature gap → research question → design/data → main findings → contribution. Keep the gap specific and make the contribution proportional to what the design identifies.
- **Institutional background**: explain the policy or institution only to the extent needed to motivate variation, timing, treatment assignment, or mechanism. Separate institutional facts from the author's interpretation.
- **Data and variables**: identify source, sample construction, unit of observation, key variables, measurement choices, and exclusions. Report definitions before motivations and avoid adjectives such as “高质量数据” without evidence.
- **Identification and model**: state the estimand, source of variation, identifying assumption, fixed effects, clustering, and threats. Use “用于识别”“缓解内生性担忧” unless the design justifies stronger language.
- **Baseline results**: report sign, magnitude, uncertainty, and economic meaning in that order. Link each sentence to a table or figure. Separate statistical significance from economic significance.
- **Result-format hard check**: single coefficients must not be followed by exact `(p=...)`, `(t=...)`, or `(z=...)` parentheses. Rewrite them as Chinese significance-level prose; retain an exact p-value only when it belongs to an explicitly labelled joint or overall test, and scan the complete output before delivery.
- **Mechanisms**: state the mechanism before the test, then explain the observable implication, proxy, interaction, or mediation evidence. Do not treat a subgroup difference as proof of a mechanism.
- **Robustness and heterogeneity**: group checks by threat addressed: measurement, sample, specification, inference, timing, placebo, or alternative explanation. Explain why each check matters.
- **Conclusion and policy implications**: restate the identified result, boundary conditions, and feasible policy implication. Avoid claims broader than the sample, period, institution, or estimand.

## Output format

For a section analysis, use:

- **Section function**
- **Observed pattern from exemplars**
- **Sentence and paragraph structure**
- **Evidence and causal-language boundary**
- **Adaptable templates**
- **Application to the user's text**

For a rewrite, return the revised Chinese prose first, followed by a short change log that names only factual, logical, causal-language, or sentence-structure changes. Do not put editorial instructions inside manuscript正文.

For detailed patterns and example structures, read [references/section-patterns.md](references/section-patterns.md). For corpus-selection and source-verification rules, read [references/corpus-and-sources.md](references/corpus-and-sources.md).
