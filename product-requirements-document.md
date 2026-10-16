# Product Requirements Document (PRD)

**Title:** Sales Quarterly Goal-Setting Agent
**Date:** 2026-10-16
**Owner:** Sales Enablement / HR Technology
**Solution Category:** AI Agent

---

## Product Purpose & Value Proposition

**Elevator Pitch:**
Sales representatives lose up to two hours every quarter manually assembling territory data and HR profile information just to fill in goal forms — resulting in late, low-quality objectives that don't reflect actual business conditions. This agent eliminates that friction by retrieving the relevant data automatically, proposing meaningful goal options, and guiding each rep through a focused conversation that ends with goals written directly into SAP SuccessFactors.

**Business Need:**
There is no integrated, data-driven process connecting CRM territory performance with employee goal-setting in SAP SuccessFactors. Reps must navigate two disconnected systems, manually interpret their pipeline and activity data, and translate that into goal language — a process prone to inconsistency, missed deadlines, and goals misaligned with organisational priorities.

**Expected Value:**
- 80% reduction in time spent on quarterly goal-setting (from 2 hours to 20–25 minutes per rep)
- 90% on-time goal completion within the first week of each quarter
- 95% goal alignment to team and organisational objectives
- ≥ 85% user satisfaction among sales representatives and managers
- ≥ 95% compliance with goal-setting policies and required fields

**Product Objectives (Prioritised):**
1. Automate CRM and HR data retrieval so reps start with their context already loaded
2. Deliver personalised, data-grounded goal recommendations across pipeline, activity, and growth dimensions
3. Guide reps through a conversational refinement flow that results in confirmed, policy-compliant goals
4. Write approved goals to SAP SuccessFactors Goal Management (PMGM) without manual data entry

---

## Business Metrics

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Goal-setting time per employee | 2 hours | 20–25 minutes (80% reduction) | Each quarter | Quarterly goal creation | user |
| On-time goal completion rate | — | 90% within first week of quarter | Each quarter | Goal setup completion | user |
| Goal alignment to team/org objectives | — | 95% | Each quarter | Goal alignment & review | user |
| User satisfaction (employees & managers) | — | ≥ 85% | Each quarter | Agent usability | user |
| Goal policy compliance rate | — | ≥ 95% | Each quarter | Policy adherence & approval workflow | user |

---

## User Profiles & Personas

### Primary Persona: Alex — Sales Representative

Alex is a 34-year-old field sales rep managing a territory of 40–60 accounts across a mid-market segment. Each quarter, they are expected to set 4–6 development objectives in SAP SuccessFactors that reflect their pipeline reality and align with regional targets. Alex is comfortable using CRM tools daily but finds goal-setting admin burdensome — it requires logging into a separate HR system, recalling pipeline figures from memory, and translating numbers into HR-friendly language. At the start of each quarter, they are already under pressure to hit the ground running, so goal-setting gets delayed or rushed. Alex needs a tool that does the preparation for them and asks simple, direct questions — not one that adds more screens to navigate.

### Secondary Persona: Morgan — Sales Manager

Morgan is a 42-year-old sales manager responsible for a team of 8–12 sales reps. Each quarter, Morgan's biggest administrative headache is chasing reps who haven't completed their goals and reviewing submissions that are vague, inconsistent, or misaligned with the team's priorities. Morgan spends 2–3 hours per quarter following up and correcting goal entries. Morgan needs confidence that every rep has set goals on time, that those goals are meaningful, and that they align with the regional plan — without having to intervene in each case individually.

### Other User Types

- **HR Administrator**: Responsible for configuring goal plan templates in SAP SuccessFactors and ensuring the agent respects required fields and policy rules.
- **IT / Integration Owner**: Responsible for maintaining the MCP integration layer between the agent and SAP Sales Cloud.

---

## User Goals & Tasks

### For Alex (Sales Representative):

**Goals:**
- Complete quarterly goal-setting in under 30 minutes without switching between systems
- Receive goal suggestions that actually reflect their territory and pipeline situation
- Be able to adjust the wording of suggested goals before they are saved

**Key Tasks:**
- Initiate a goal-setting conversation with the agent at the start of the quarter
- Review the CRM territory summary the agent presents (accounts, leads, open deals, historical performance)
- Select and refine goal options from the agent's recommendations across pipeline, activity, and growth dimensions
- Confirm the final list of goals and have them written to SAP SuccessFactors

### For Morgan (Sales Manager):

**Goals:**
- Ensure all direct reports complete their goal-setting on time each quarter
- Have confidence that submitted goals are aligned with team and regional objectives
- Spend less time chasing and correcting goal submissions

**Key Tasks:**
- Monitor goal completion status across the team (via SAP SuccessFactors, outside agent scope)
- Review the goals created by the agent on behalf of reps in SuccessFactors

---

## Product Principles

1. **Data before dialogue**: The agent always retrieves and presents the rep's actual CRM and HR data before asking any questions — reps start from facts, not from a blank form.
2. **Human confirmation as a hard gate**: No goal is created or updated in SAP SuccessFactors without explicit, unambiguous confirmation from the sales rep. The agent proposes; the human decides.
3. **Conversation, not configuration**: The rep experience is a natural, step-by-step conversation — not a form with dropdowns. The agent handles system complexity invisibly.
4. **Grounded recommendations**: Every goal option the agent proposes must be traceable to a specific data point from the rep's CRM territory or SuccessFactors profile. Generic suggestions are not acceptable.
5. **Compliance by design**: Goal entries written to SuccessFactors must satisfy all required fields and policy rules defined in the PMGM goal plan template — the agent must not bypass these constraints.

---

## Business Context

**Current State:**
Sales representatives manually navigate between SAP Sales Cloud (for territory, pipeline, and performance data) and SAP SuccessFactors (for goal management). There is no integration between these systems for goal-setting purposes. Reps must recall or export CRM data, interpret it themselves, and manually translate it into goals in the PMGM module. This process is inconsistent, time-consuming, and prone to quality issues.

**Strategic Alignment:**
This agent directly supports two strategic priorities: (1) sales productivity improvement by removing administrative overhead from field reps, and (2) HR process excellence by increasing goal quality and on-time completion rates in SAP SuccessFactors.

**Success Criteria:**
See Business Metrics section.

---

## Goals and Non-Goals

### Goals (In Scope)

- Retrieve territory accounts, leads, open opportunities, and historical sales performance from SAP Sales Cloud for the current quarter
- Fetch the sales rep's profile and existing goals from SAP SuccessFactors PMGM
- Generate personalised goal recommendations across pipeline, activity, and growth dimensions
- Support conversational goal wording refinement by the rep
- Create new goals in SAP SuccessFactors PMGM upon explicit rep confirmation
- Update or replace existing quarterly goals in SAP SuccessFactors PMGM upon explicit rep confirmation

### Non-Goals (Out of Scope)

- Manager approval workflows or multi-step review chains within the agent
- Performance review forms or mid-year/end-of-year review processes
- Incentive or commission management (separate SAP SuccessFactors module)
- Reporting dashboards or analytics on goal completion trends
- Integration with SAP Analytics Cloud or SAP Business Data Cloud
- Automatic goal-setting without any human interaction or confirmation

---

## Requirements

### Must-Have Requirements

**R1: CRM Territory Data Retrieval**

- **Problem to Solve**: Reps currently spend significant time manually gathering territory data before they can begin goal-setting. This data should be available instantly at the start of the conversation.
- **User Story**: As a sales representative, I need the agent to automatically retrieve my current territory accounts, active leads, open opportunities, and historical sales performance from SAP Sales Cloud so that I can see my actual business context without switching systems.
- **Acceptance Criteria**:
  - Given the rep initiates a goal-setting conversation, when the agent starts, then it retrieves territory data from SAP Sales Cloud for the current quarter and presents a concise summary to the rep.
  - Given SAP Sales Cloud is unavailable, when data retrieval fails, then the agent informs the rep clearly and offers to continue with manually provided context or to retry.
- **Maps to Objective**: Objective 1 — Automate data retrieval
- **Priority Rank**: 1

**R2: SAP SuccessFactors Profile and Goals Retrieval**

- **Problem to Solve**: Reps and the agent need visibility into the rep's current SuccessFactors profile and any goals already set for the quarter to avoid duplication and ensure continuity.
- **User Story**: As a sales representative, I need the agent to fetch my employee profile and existing goals from SAP SuccessFactors so that recommendations are personalised and existing goals are not duplicated.
- **Acceptance Criteria**:
  - Given the agent has retrieved CRM data, when it proceeds to the SuccessFactors step, then it fetches the rep's employee profile (using `sap.sf:apiResource:ECEmployeeProfile:v1`) and existing goal plan entries (using `sap.sf:apiResource:PerformanceandGoalsPMGM:v1`).
  - Given no existing goals are found, when the agent presents context, then it indicates this is a fresh goal-setting cycle.
- **Maps to Objective**: Objective 1 — Automate data retrieval
- **Priority Rank**: 2

**R3: Goal Recommendation Generation**

- **Problem to Solve**: Reps lack the time and context to translate raw CRM data into well-structured development objectives. The agent should do this synthesis for them.
- **User Story**: As a sales representative, I need the agent to propose a set of relevant quarterly goal options — across pipeline, activity, and growth dimensions — based on my actual CRM territory data and SuccessFactors profile so that I have a strong starting point for my objectives.
- **Acceptance Criteria**:
  - Given the agent has loaded both CRM and SuccessFactors data, when it generates recommendations, then it proposes at least one goal option for each of the three dimensions: pipeline, activity, and growth.
  - Given the agent proposes a goal, when the rep asks why it was suggested, then the agent can trace it to a specific data point (e.g., "You have 12 open opportunities in the enterprise segment — this pipeline goal targets closing 3 this quarter").
- **Maps to Objective**: Objective 2 — Personalised, data-grounded recommendations
- **Priority Rank**: 3

**R4: Conversational Goal Refinement**

- **Problem to Solve**: Auto-generated goal text may not match a rep's preferred phrasing or nuance. Reps must be able to adjust wording without losing the data-grounded intent.
- **User Story**: As a sales representative, I need to be able to edit the wording of suggested goals through the conversation so that the final goals reflect my own voice and specific intentions.
- **Acceptance Criteria**:
  - Given the agent has presented a goal recommendation, when the rep requests a wording change, then the agent updates the goal text accordingly and presents the revised version for review.
  - Given the rep approves a goal, when they later want to revise it before final confirmation, then the agent allows re-editing at any point prior to the write-back step.
- **Maps to Objective**: Objective 3 — Conversational refinement
- **Priority Rank**: 4

**R5: Human-Confirmed Goal Write-Back to SAP SuccessFactors**

- **Problem to Solve**: Goals must not be created or changed in SAP SuccessFactors without the rep's explicit approval — accidental or premature write-back would undermine trust.
- **User Story**: As a sales representative, I need to explicitly confirm my final list of goals before the agent saves them to SAP SuccessFactors so that I retain full control over what gets recorded.
- **Acceptance Criteria**:
  - Given the rep has reviewed and refined all goal options, when the agent asks for final confirmation and the rep confirms, then the agent creates or updates goals in SAP SuccessFactors PMGM via the Goal Plan API.
  - Given the rep has not confirmed, when the session ends or the rep says "cancel", then no goals are written to SAP SuccessFactors.
  - Given existing quarterly goals are present, when the rep confirms new goals, then the agent updates or replaces the existing entries rather than creating duplicates.
- **Maps to Objective**: Objective 4 — Write approved goals without manual entry
- **Priority Rank**: 5

**R6: Policy Compliance Enforcement**

- **Problem to Solve**: SAP SuccessFactors goal plans have required fields and configuration rules that vary by tenant. Goal entries that fail validation waste the rep's time and erode confidence in the agent.
- **User Story**: As a sales representative, I need the agent to ensure that every goal it writes meets the required fields and policy rules of our SAP SuccessFactors goal plan configuration so that submissions are not rejected.
- **Acceptance Criteria**:
  - Given a goal is ready for write-back, when the agent calls the PMGM API, then all required fields (as defined by the tenant's goal plan template) are populated.
  - Given a field validation error is returned by the API, when this occurs, then the agent surfaces the issue to the rep in plain language and requests the missing information before retrying.
- **Maps to Objective**: Objective 4 — Write approved goals without manual entry
- **Priority Rank**: 6

### High-Want Requirements

**R7: Goal Dimension Completeness Check**

- **Problem to Solve**: Reps may inadvertently skip one of the three goal dimensions (pipeline, activity, growth), resulting in imbalanced development objectives.
- **User Story**: As a sales representative, I need the agent to prompt me if I haven't selected a goal from one of the three dimensions so that my quarterly plan is balanced.
- **Priority Rank**: 1

**R8: Session Resumption**

- **Problem to Solve**: A rep may not complete the goal-setting flow in a single session. They should be able to resume without starting over.
- **User Story**: As a sales representative, I need to be able to resume an in-progress goal-setting conversation so that I don't lose my selections if I'm interrupted.
- **Priority Rank**: 2

### Nice-to-Have Requirements

**R9: Manager Visibility Notification**

- **Problem to Solve**: Managers are currently unaware when a rep completes their goal-setting via the agent.
- **User Story**: As a sales manager, I would like to receive a notification when a direct report completes their quarterly goal-setting via the agent so that I can review their goals promptly.
- **Priority Rank**: 1

---

## Non-Functional Requirements

### Performance

- **Latency**: CRM data retrieval and SuccessFactors fetches should complete within 10 seconds per call. Goal write-back should complete within 5 seconds.
- **Throughput**: The agent should support concurrent sessions for multiple sales reps during the high-traffic period at the start of each quarter.

### Reliability

- **Availability**: The agent should be available during standard business hours. Degraded-mode behaviour (e.g., CRM data unavailable) must be handled gracefully without crashing the session.
- **Fallback**: If CRM data retrieval fails, the agent informs the rep and offers to proceed with a manually described context.

### Explainability

- **Traceability**: Each goal recommendation must be traceable to a specific data point from CRM or SuccessFactors. The agent must be able to explain why it suggested a given goal if asked.
- **Decision Logging**: All goal write operations (create, update, replace) must be logged with the rep's identity, the session ID, and a timestamp.
- **Uncertainty Communication**: If the agent cannot retrieve data or cannot generate a well-grounded recommendation, it must say so explicitly rather than hallucinating context.

---

## Solution Architecture

**Architecture Overview:**
A Python AI agent implementing the A2A (Agent-to-Agent) protocol, deployed on SAP BTP. The agent integrates with SAP Sales Cloud via a custom MCP server and with SAP SuccessFactors via OData APIs wrapped as MCP tools. All conversation state is managed within the agent session.

**Key Components:**

- **Sales Goal-Setting Agent (Python, A2A)**: Core agent responsible for conversation management, data synthesis, goal generation, and orchestration of tool calls.
- **SAP Sales Cloud MCP Server (custom)**: Custom MCP integration layer exposing SAP Sales Cloud territory, account, lead, opportunity, and historical performance data as tools callable by the agent.
- **SAP SuccessFactors MCP Tools**: MCP-wrapped OData calls to `sap.sf:apiResource:ECEmployeeProfile:v1` (read employee profile) and `sap.sf:apiResource:PerformanceandGoalsPMGM:v1` (read and write goals).
- **SAP Generative AI Hub**: LLM provider used by the agent for natural language understanding, goal recommendation generation, and conversational turn management.

**Integration Points:**

- **SAP Sales Cloud**: Custom MCP server, read-only, called at session start to retrieve territory context for the current quarter.
- **SAP SuccessFactors Employee Profile API**: OData, read-only, called at session start to load rep profile.
- **SAP SuccessFactors PMGM Goal Plan API**: OData, read and write, called at session end (after explicit confirmation) to create or update goals.

**Deployment Environments:**

- **Development**: Connected to SAP Sales Cloud sandbox and SuccessFactors test tenant; no production data.
- **Production**: Connected to live SAP Sales Cloud and SuccessFactors tenant; write operations restricted to confirmed goal entries only.

### Agent Extensibility & Instrumentation

**Agent Extensibility:**
The agent is designed with explicit extension points to support future capabilities without requiring a full rebuild:
- **Tool extension**: Additional MCP tools can be registered (e.g., SAP Analytics Cloud for historical quota attainment, SAP Concur for activity-based goals) without modifying core agent logic.
- **Goal dimension extension**: The pipeline / activity / growth recommendation framework is parameterised and can be extended with additional dimensions (e.g., learning & development, customer satisfaction) by updating the agent's skill configuration.
- **Post-confirmation hook**: A hook is defined at the goal write-back step to allow future integrations (e.g., triggering a manager notification workflow) to be attached without modifying the core confirmation flow.

**Business Step Instrumentation:**
All five key business milestones emit structured log statements to support observability, monitoring, and debugging in production. Log pattern: `[MILESTONE_ID].[achieved|missed]: [description]`.

### Automation & Agent Behaviour

**Automation Level:** Autonomous agent with mandatory human confirmation gate before any write operation.

**Actions the system performs without human approval:**
- Retrieval of territory data from SAP Sales Cloud
- Retrieval of employee profile and existing goals from SAP SuccessFactors
- Generation of goal recommendations based on retrieved data
- Wording updates during conversational refinement

**Actions that require human review or approval:**
- Creating new goals in SAP SuccessFactors PMGM
- Updating or replacing existing goals in SAP SuccessFactors PMGM

**Model or engine used:** LLM via SAP Generative AI Hub (model selection subject to SAP BTP availability)

**Knowledge & data sources accessed:**
- **SAP Sales Cloud**: Territory accounts, active leads, open opportunities, historical quarterly sales performance — read-only, CRM domain
- **SAP SuccessFactors Employee Profile**: Rep's role, department, manager, tenure — read-only, HR domain
- **SAP SuccessFactors Goal Plan (PMGM)**: Existing quarterly goals, goal plan template configuration — read and write, HR domain

**Tools or connectors invoked:**
- `get_territory_accounts`: Retrieves managed accounts for the rep's territory from SAP Sales Cloud — read-only
- `get_territory_leads`: Retrieves active leads in the rep's territory — read-only
- `get_open_opportunities`: Retrieves open opportunities for the current quarter — read-only
- `get_sales_performance_history`: Retrieves historical quarterly performance metrics — read-only
- `get_employee_profile`: Fetches the rep's SAP SuccessFactors employee profile — read-only
- `get_existing_goals`: Fetches the rep's current goal plan entries from SAP SuccessFactors PMGM — read-only
- `create_goal`: Creates a new goal entry in SAP SuccessFactors PMGM — write, requires explicit confirmation
- `update_goal`: Updates or replaces an existing goal entry in SAP SuccessFactors PMGM — write, requires explicit confirmation

**Guardrails & fail-safes:**
- No goal is written to SAP SuccessFactors without explicit rep confirmation — this is a hard gate, not a soft warning.
- If the agent cannot retrieve CRM data, it must not fabricate territory context. It must inform the rep and offer to continue with manually provided information.
- If the PMGM API returns a validation error, the agent must surface the issue in plain language and not silently fail.
- The agent must never impersonate a manager or claim that goals have been approved by a manager.
- If the rep confirms but the write operation fails, the agent must report the failure and provide the rep with a copy of the confirmed goal text so they can submit manually if needed.

---

## Governance, Risk & Compliance

**Data Handling:**
- CRM territory data (accounts, leads, opportunities) is sales-sensitive and must not be stored beyond the active agent session.
- Employee profile data from SAP SuccessFactors must be treated in accordance with HR data policies and GDPR requirements where applicable.
- No PII beyond what is necessary for goal personalisation (rep name, role, territory) should be retained in agent logs.

**Compliance Frameworks:**
- SAP SuccessFactors PMGM goal plan required fields must be enforced at write time.
- All goal write operations must be attributable to the authenticated sales rep's user identity.

**Approval Flows:**
- Goal creation and update in SAP SuccessFactors requires explicit verbal confirmation from the rep within the conversation. No automated or timer-based confirmation is acceptable.

---

## Milestones

### M1: CRM Data Retrieved

- **Description**: The agent has successfully fetched the rep's territory accounts, active leads, open opportunities, and historical quarterly sales performance from SAP Sales Cloud.
- **Achieved when**: All four CRM data categories are successfully retrieved and a non-empty summary is ready to present to the rep.
- **Log on achievement**: `M1.achieved: CRM territory data retrieved successfully for rep {rep_id}, quarter {quarter}`
- **Log on miss**: `M1.missed: CRM territory data retrieval failed or returned empty for rep {rep_id} — proceeding with manual context or aborting`

### M2: Employee Context Loaded

- **Description**: The agent has fetched the rep's employee profile and existing goals from SAP SuccessFactors Goal Management.
- **Achieved when**: Both the employee profile and the current goal plan entries are successfully retrieved from SAP SuccessFactors PMGM.
- **Log on achievement**: `M2.achieved: SAP SuccessFactors profile and goals loaded for rep {rep_id}`
- **Log on miss**: `M2.missed: SuccessFactors profile or goals retrieval failed for rep {rep_id}`

### M3: Goal Recommendations Generated

- **Description**: The agent has synthesised the CRM and HR data and produced a set of goal recommendations across pipeline, activity, and growth dimensions.
- **Achieved when**: At least one goal recommendation is produced for each of the three dimensions and presented to the rep.
- **Log on achievement**: `M3.achieved: goal recommendations generated for rep {rep_id} — pipeline: {n}, activity: {n}, growth: {n}`
- **Log on miss**: `M3.missed: goal recommendation generation failed or produced incomplete dimensions for rep {rep_id}`

### M4: Goals Refined and Confirmed by Rep

- **Description**: The sales representative has reviewed the goal options, optionally edited wording, and given explicit confirmation of the final goal list.
- **Achieved when**: The rep sends an explicit confirmation message and the agent records a confirmed goal list for write-back.
- **Log on achievement**: `M4.achieved: rep {rep_id} confirmed {n} goals for write-back to SuccessFactors`
- **Log on miss**: `M4.missed: rep {rep_id} did not confirm goals — session ended without write-back`

### M5: Goals Written to SAP SuccessFactors

- **Description**: The confirmed goals have been successfully created or updated in SAP SuccessFactors PMGM.
- **Achieved when**: All confirmed goals are successfully persisted in the PMGM Goal Plan API with no validation errors.
- **Log on achievement**: `M5.achieved: {n} goals written to SAP SuccessFactors for rep {rep_id}, quarter {quarter}`
- **Log on miss**: `M5.missed: goal write-back to SAP SuccessFactors failed for rep {rep_id} — {error_detail}`

---

## Risks, Assumptions, and Dependencies

### Risks

- **SAP Sales Cloud API availability**: CRM APIs for territory, accounts, leads, and opportunities are not available as connected MCP servers in the current landscape. A custom MCP integration layer must be built and maintained — this adds delivery risk and ongoing maintenance responsibility.
- **SuccessFactors PMGM schema variability**: Goal plan templates vary between tenants. Required fields, character limits, and picklist values must be mapped during implementation and may need updating after SuccessFactors upgrades.
- **LLM output quality**: Recommendation quality depends on the LLM's ability to interpret CRM data in context. Poor recommendations will undermine trust and adoption — prompt design and testing are critical.

### Assumptions (Validate These)

- SAP Sales Cloud exposes territory, account, lead, opportunity, and performance data via APIs accessible from SAP BTP.
- The SAP SuccessFactors PMGM Goal Plan API (`sap.sf:apiResource:PerformanceandGoalsPMGM:v1`) supports programmatic goal creation and update for the tenant's configured goal plan.
- Sales reps are authenticated via a common identity provider accessible to both SAP Sales Cloud and SAP SuccessFactors.
- The tenant's SAP SuccessFactors goal plan template is stable enough for the integration period.

### Dependencies

- SAP Sales Cloud API access credentials and connectivity from SAP BTP
- SAP SuccessFactors PMGM API access with write permissions for goal plan entries
- SAP Generative AI Hub access for the LLM model used by the agent
- SAP BTP runtime environment for agent deployment

---

## Open Questions

- What authentication mechanism does SAP Sales Cloud expose for API access from SAP BTP? (OAuth 2.0, API key, certificate?)
- Does the tenant's SAP SuccessFactors PMGM goal plan have mandatory fields beyond title and description? (e.g., category, metric type, weight)
- Should the agent support reps across multiple sales territories (e.g., a rep who covers two regions), or is one territory per rep assumed?
- Is there a desired cadence trigger (e.g., first Monday of each quarter) that should initiate the goal-setting flow, or is it always rep-initiated?

---

## Appendix

### Glossary

- **PMGM**: Performance and Goal Management — the SAP SuccessFactors module used to manage employee performance reviews and goal plans.
- **A2A**: Agent-to-Agent — the protocol used by SAP AI agents to communicate with other agents and tools in a standardised way.
- **MCP**: Model Context Protocol — the tool integration standard used by the agent to call external APIs and services.
- **Territory**: A defined set of accounts, leads, and opportunities assigned to a specific sales representative in SAP Sales Cloud.
- **Goal dimensions**: The three categories used to classify quarterly goals in this solution — Pipeline (deals and revenue), Activity (sales activities and behaviours), Growth (skill and capability development).

### References

- SAP SuccessFactors Goal Management API: `sap.sf:apiResource:PerformanceandGoalsPMGM:v1`
- SAP SuccessFactors Employee Profile API: `sap.sf:apiResource:ECEmployeeProfile:v1`
- SAP Sales Cloud V2 — Territory Management capability (SC4704)
- SAP Sales Cloud V2 — Pipeline Management capability (SC3426)
- RBA Sub-process: Plan sales and manage performance (BPS-369)
