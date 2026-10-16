---
name: goal-recommendation
description: Translates the CRM territory snapshot and SAP SuccessFactors employee profile into personalised quarterly goal recommendations across pipeline, activity, and growth dimensions.
---

# Goal Recommendation Logic

Use this skill after the CRM territory snapshot and the SuccessFactors employee profile and existing goals have been loaded.

## Dimensions

Always produce at least one recommendation per dimension:

### 1. Pipeline Dimension
Focused on deals, revenue, and quota.

Mapping rules:
- If quota attainment in the prior quarter was below 90%: suggest a goal to close a specific number of high-value opportunities (derive the number from open opportunities count).
- If quota attainment was above 100%: suggest a stretch goal (e.g., exceed quota by X%).
- If open opportunities are concentrated in one stage: suggest advancing N deals past that stage.

Example goal: "Close [N] enterprise opportunities in Q[X], targeting [€/$ value] in new revenue."

### 2. Activity Dimension
Focused on sales behaviours, outreach, and daily execution.

Mapping rules:
- If active leads count is low (< 5): suggest a prospecting or lead generation goal.
- If several deals have been in the same stage for > 30 days: suggest a goal around customer meetings or demos to advance stalled deals.
- Otherwise: suggest a goal around customer touchpoints (visits, calls, proposals submitted).

Example goal: "Conduct [N] discovery calls with new prospects in Q[X] to grow the active pipeline."

### 3. Growth Dimension
Focused on skill, capability, and professional development.

Mapping rules:
- Review the rep's existing goals in SuccessFactors for any open growth goals from the prior quarter; if present, suggest carrying one forward with a concrete completion target.
- Otherwise: suggest a development goal relevant to their role and tenure (e.g., complete product certification, shadow a senior rep, improve CRM data quality).

Example goal: "Complete [product/skill] certification by [date] to strengthen expertise in the [segment] market."

## Traceability Requirement

For EVERY recommendation, include a one-sentence rationale that cites the specific data point that informed it. Examples:
- "Based on your 2 open enterprise deals in proposal stage, this goal targets moving them to close."
- "Based on only 3 active leads in your territory, this goal addresses pipeline growth."
- "Based on your 78% quota attainment last quarter, this goal sets a recovery target."

## Existing Goals Conflict Check

Before presenting recommendations, check the rep's existing goals in SuccessFactors:
- Do NOT suggest a goal that is identical (or near-identical) to an existing goal.
- If an existing goal overlaps, note it and ask the rep whether to replace it or keep it alongside.

## Output Format

Present recommendations clearly grouped by dimension:

```
--- Recommended Goals for Q[X] ---

PIPELINE
[Goal title]
[Goal description — 1-2 sentences]
Why: [Traceability rationale]

ACTIVITY
[Goal title]
[Goal description — 1-2 sentences]
Why: [Traceability rationale]

GROWTH
[Goal title]
[Goal description — 1-2 sentences]
Why: [Traceability rationale]

Would you like to select, edit, or skip any of these? You can also ask me to suggest alternatives for any dimension.
```
