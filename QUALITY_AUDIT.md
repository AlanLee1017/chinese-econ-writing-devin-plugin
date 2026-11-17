# Skill quality audit

## 2026-11-17

The first Devin run revealed a real acceptance failure: single coefficients were still written as `1.143（p=0.025）` and `1.136（p=0.034）`.

The audit found four related risks:

1. The unified router did not define staged execution and could describe routing without applying each stage's acceptance checks.
2. The skills did not consistently forbid invented sample sizes, citations, dates, mechanisms, or estimates when inputs were incomplete.
3. The result-format scanner initially missed unparenthesized `p=` patterns and standard-error parentheses.
4. The result skill did not explicitly suppress process narration such as “I will first check every position” in manuscript-editing output.

The current version addresses these risks through a staged router protocol, evidence-preservation rules, broader scanning patterns, and an explicit process-output boundary.

## Verification

Run:

```bash
python3 skills/chinese-econ-results/scripts/check_result_style.py path/to/result.txt
```

The scanner returns `PASS` only when no p/t/z-value or standard-error technical-output patterns remain. Any hit requires manual classification; an explicitly labelled joint or overall test may be retained after review.
