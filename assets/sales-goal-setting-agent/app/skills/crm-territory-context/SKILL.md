---
name: crm-territory-context
description: Summarises raw CRM territory data from SAP Sales Cloud into a concise snapshot for the sales representative.
---

# CRM Territory Context Summarisation

Use this skill after you have retrieved all four CRM data categories (accounts, leads, open opportunities, historical sales performance) from SAP Sales Cloud.

## Summarisation Steps

1. Count total managed accounts; highlight the top 3 by segment or revenue potential.
2. Count active leads; note any leads that have been open for more than 30 days.
3. List open opportunities for the current quarter; highlight the top 3 by deal value; include stage and expected close date for each.
4. Summarise historical performance for the previous 2 quarters:
   - Quota attainment percentage
   - Number of deals closed
   - Revenue vs. target (over/under)
   - Quarter-over-quarter trend (improving / stable / declining)

## Output Format

Present the summary in the following structure to the rep:

```
--- Your Territory Snapshot (Q[X] [YEAR]) ---

Accounts: [N] managed accounts
  Top segments: [segment 1], [segment 2], [segment 3]

Leads: [N] active leads ([N] open > 30 days)

Open Opportunities: [N] deals
  Highest value: [Opportunity Name] — [Value] (Stage: [X], Close: [Date])
  [Opportunity Name 2] — [Value] (Stage: [X], Close: [Date])
  [Opportunity Name 3] — [Value] (Stage: [X], Close: [Date])

Performance History:
  Last quarter ([Q-1]): [X]% quota attainment, [N] deals closed, [over/under] target by [amount]
  Prior quarter ([Q-2]): [X]% quota attainment, [N] deals closed, [over/under] target by [amount]
  Trend: [improving / stable / declining]
```

## Error Handling

- If any data category is missing or empty, state this explicitly in the relevant section (e.g., "No open opportunities found for Q[X]").
- Do NOT fabricate any numbers. If a data retrieval failed, note the failure and continue with available data.
