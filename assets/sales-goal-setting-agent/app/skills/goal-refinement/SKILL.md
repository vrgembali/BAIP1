---
name: goal-refinement
description: Manages the conversational goal refinement loop — presenting goals, accepting edits, ensuring dimension completeness, and reaching explicit sales rep confirmation before any write-back to SAP SuccessFactors.
---

# Goal Refinement Flow

Use this skill after goal recommendations have been presented to the sales representative.

## Refinement Loop

1. Present each recommended goal with its title and description.
2. Ask the rep: "Would you like to keep this goal as written, edit the wording, or skip it?"
3. If the rep edits: update the goal text and show the revised version. Ask: "Does this look right?"
4. If the rep skips: note the goal as skipped and continue to the next.
5. Continue for all goals across all three dimensions.

## Re-edit Rule

The rep may revise any previously accepted goal at any time before the final confirmation step. If the rep says "actually, change the pipeline goal", go back and re-apply the edit. Show the updated version before proceeding.

## Dimension Completeness Check

Before proceeding to the final confirmation step:
- Verify at least one goal is selected from each dimension: Pipeline, Activity, Growth.
- If a dimension has zero selected goals, prompt: "You haven't selected a goal for the [dimension] dimension. Would you like to add one, or skip this dimension for this quarter?"
- Wait for the rep to respond before proceeding.

## Policy Compliance Pre-check

Before presenting the final confirmation, verify each confirmed goal has:
- A title (non-empty string)
- A description (non-empty string, at least 20 characters)

If any field is missing, ask the rep to provide it before proceeding to write-back.

## Final Confirmation Protocol

Present the final list of confirmed goals in a summary:

```
--- Your Confirmed Goals for Q[X] ---

1. [PIPELINE] [Goal Title]
   [Goal Description]

2. [ACTIVITY] [Goal Title]
   [Goal Description]

3. [GROWTH] [Goal Title]
   [Goal Description]

Ready to save these goals to SAP SuccessFactors? Reply "yes, confirm" or "confirm" to save, or let me know if you'd like any changes.
```

Only proceed to write-back after the rep sends an explicit confirmation such as:
- "yes, confirm"
- "confirm"
- "save my goals"
- "yes, save"

Ambiguous responses (e.g., "ok", "sure", "I guess") are NOT sufficient — ask for explicit confirmation.

## Cancellation Handling

If the rep says "cancel", "stop", "never mind", or ends the conversation without confirming:
- Do NOT call any write tools.
- Acknowledge clearly: "Your goals have not been saved. You can start a new goal-setting session at any time."

## Post Write-back Confirmation

After goals are successfully written to SAP SuccessFactors:
- Report how many goals were created and how many were updated (not duplicated).
- Suggest: "You can review your goals in the Goals section of SAP SuccessFactors."

If the write-back fails:
- Report the error clearly.
- Provide the full text of the confirmed goals so the rep can save them manually.
- Do NOT retry automatically.
