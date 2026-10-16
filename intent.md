# Sales Quarterly Goal-Setting Agent

AI-powered assistant that guides sales representatives through quarterly development objective creation.

## Business challenge

Sales representatives spend significant time and effort creating meaningful quarterly development objectives, often lacking easy access to their own CRM territory data and SuccessFactors profile in one place. The agent retrieves territory data from SAP Sales Cloud — including managed accounts, leads in the territory, open opportunities, and historical sales performance — on a quarterly basis. It also fetches the representative's current profile and existing goals from SAP SuccessFactors Goal Management. Based on this combined data, the agent recommends relevant goal options across pipeline, activity, and growth dimensions, guides the representative through goal selection and refinement in a conversational flow, and upon explicit confirmation, creates or updates the approved goals directly in SAP SuccessFactors.

## Business Goals & Success Criteria

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Goal-setting time per employee | 2 hours | 20–25 minutes (80% reduction) | Each quarter | Quarterly goal creation | user |
| On-time goal completion rate | — | 90% within first week of quarter | Each quarter | Goal setup completion | user |
| Goal alignment to team/org objectives | — | 95% | Each quarter | Goal alignment & review | user |
| User satisfaction (employees & managers) | — | ≥ 85% | Each quarter | Agent usability | user |
| Goal policy compliance rate | — | ≥ 95% | Each quarter | Policy adherence & approval workflow | user |

## Key Milestones

1. **CRM Data Retrieved** — Agent successfully fetches territory accounts, leads, open opportunities, and historical sales performance from SAP Sales Cloud for the current quarter.
2. **Employee Context Loaded** — Agent fetches the sales rep's profile and existing goals from SAP SuccessFactors Goal Management.
3. **Goal Recommendations Generated** — Agent produces a set of relevant goal options across pipeline, activity, and growth dimensions based on the combined data.
4. **Goals Refined by Rep** — Sales representative reviews, edits wording, and confirms their selected goals through the conversational flow.
5. **Goals Written to SuccessFactors** — Upon explicit confirmation, the agent creates new goals and updates or replaces existing goals directly in SAP SuccessFactors PMGM.

## Business Architecture (RBA)

### End-to-End Process

Lead to Cash (generic)

### Process Hierarchy

```
Lead to Cash (E2E)
└── Plan to Optimize Marketing and Sales
    └── Plan sales and manage performance (BPS-369)
        └── Establish sales goals and measures
        └── Manage sales performance using CRM territory and opportunity data
Cross-linked:
Recruit to Retire
└── Develop to Grow
    └── Plan career development
    └── Develop and train employees
```

### Summary

The challenge maps primarily to Lead to Cash → Plan sales and manage performance, covering territory-based sales goal setting using CRM data. The SAP SuccessFactors goal creation dimension cross-links to Recruit to Retire → Develop to Grow for employee development objectives.

## Fit Gap Analysis

| Requirement (business) | Standard asset(s) found | API ORD ID | MCP Server ORD ID | MCP Server Version | Webhook API ORD ID | Data Product ORD ID | Gap? | Notes / assumptions |
|------------------------|------------------------|------------|-------------------|--------------------|--------------------|---------------------|------|---------------------|
| Retrieve territory accounts, leads, opportunities from SAP Sales Cloud | SAP Sales Cloud V2 — Territory Management, Pipeline Management | — | — | — | — | — | Yes | No MCP server found; SAP Sales Cloud REST/OData APIs for accounts/leads/opportunities show as unavailable in connected systems; custom MCP integration to SAP Sales Cloud required |
| Retrieve historical sales performance data | SAP Sales Cloud V2 — Sales Analytics, Sales Forecasting | — | — | — | — | — | Yes | Same as above; custom integration needed |
| Fetch employee profile from SAP SuccessFactors | SAP SuccessFactors Employee Profile | `sap.sf:apiResource:ECEmployeeProfile:v1` | — | — | — | — | No | API available; direct OData integration |
| Fetch existing goals from SAP SuccessFactors | SAP SuccessFactors PMGM — Goal Plan | `sap.sf:apiResource:PerformanceandGoalsPMGM:v1` | — | — | — | — | No | API available; direct OData integration |
| Create new goals in SAP SuccessFactors | SAP SuccessFactors PMGM — Goal Plan | `sap.sf:apiResource:PerformanceandGoalsPMGM:v1` | — | — | — | — | No | API available; direct OData integration |
| Update/replace existing goals in SAP SuccessFactors | SAP SuccessFactors PMGM — Goal Plan | `sap.sf:apiResource:PerformanceandGoalsPMGM:v1` | — | — | — | — | No | API available; direct OData integration |
| Conversational goal recommendation and refinement (pipeline, activity, growth dimensions) | No standard SAP product covers AI-guided conversational goal refinement | — | — | — | — | — | Yes | Custom AI agent required |

### Key findings

- SAP Sales Cloud V2 covers territory management, pipeline management, and sales analytics capabilities natively, but its CRM APIs (accounts, leads, opportunities, territory) are not available as connected MCP servers — a custom MCP integration layer to SAP Sales Cloud is required.
- SAP SuccessFactors Goal Plan (PMGM) and Employee Profile APIs are available and will be used directly via OData for reading and writing goals and profile data; no MCP servers exist for these APIs.
- The conversational AI-guided goal recommendation and refinement flow has no standard SAP product coverage — a custom Python AI agent is the right approach.
- The agent must support both creating new goals and updating or replacing existing quarterly goals in SuccessFactors upon explicit rep confirmation.
- Goal editing (wording refinement) is in scope; the rep can adjust suggested goal text before final confirmation.

## Recommendations

### AI Agent for Sales Quarterly Goal Setting

#### Executive Summary

Python A2A agent connecting SAP Sales Cloud and SuccessFactors PMGM.

#### Recommended Solution

A custom Python-based AI agent built on the A2A protocol, integrating with SAP Sales Cloud (via custom MCP tools for territory, accounts, leads, opportunities, and historical performance) and SAP SuccessFactors (via OData for employee profile and Goal Management PMGM). The agent conducts a multi-turn conversation with the sales rep, retrieves and synthesises the relevant CRM and HR data, proposes goal options across three dimensions (pipeline, activity, growth), allows the rep to refine goal wording, and writes confirmed goals back to SAP SuccessFactors.

#### Problem Statement

Sales representatives lack a streamlined, data-driven process to set meaningful quarterly objectives. Manually gathering territory data from the CRM and cross-referencing it with HR goals in SuccessFactors is time-consuming and inconsistent, leading to poor goal quality and missed deadlines.

#### Affected User Roles

- Sales Representatives
- Sales Managers

#### Important factors

##### Data-driven goal relevance
Goals are grounded in actual CRM territory data (accounts, leads, open deals, historical performance) and the rep's existing SuccessFactors profile, ensuring recommendations are specific and actionable rather than generic.

##### Conversational UX
The agent guides reps step by step through data review, goal selection, and wording refinement — reducing cognitive load compared to manually filling in goal forms.

##### Write-back to SuccessFactors
Goals are created or updated directly in SAP SuccessFactors PMGM only upon explicit rep confirmation, preserving auditability and compliance.

#### Potential risks

##### SAP Sales Cloud API availability
CRM APIs for territory, accounts, leads, and opportunities are not yet available as MCP servers in the connected landscape. A custom integration layer must be built and maintained.

##### SuccessFactors PMGM schema variability
Goal plan configurations vary between SuccessFactors tenants. The agent's goal creation logic must handle tenant-specific required fields and approval workflows.

#### Recommended solution category

AI Agent

#### Intent fit
92%
