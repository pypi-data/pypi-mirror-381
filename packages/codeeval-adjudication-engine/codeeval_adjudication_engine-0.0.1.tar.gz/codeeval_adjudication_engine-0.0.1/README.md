# codeeval_adjudication_engine

## I. Introduction and Scope

### 1.1 Purpose

The `codeeval_adjudication_engine` package orchestrates the business logic for Phase 2 of the MMM experiment (Blinded Comparative Adjudication). It is responsible for managing the flow of "Delta" concepts to the Adjudicators, ensuring strict adherence to the blinding and randomization protocols (BRD F3), recording votes with high integrity under concurrent load, calculating consensus in real-time (BRD F4.1), managing operational overrides required for live event resilience, and ultimately constructing the True Gold Standard (TGS) (BRD F4.2).

### 1.2 Scope

This package manages the logic between the backend data layer (provided by `platform`) and the front-end user interface.

| Area                  | In-Scope                                                                                                  | Out-of-Scope                                                                       |
| :-------------------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **Workflow Management** | Managing the state of concepts, Clinical Ideas, and the active Adjudicator Roster.                        |                                                                                    |
| **Blinded Data Filtering** | CRITICAL: Actively filtering the Concept Pool to ensure restricted information (e.g., Agreement Level) is never exposed. (BRD F3.3.2, NFR7) | Arm Anonymization (identity blinding) (handled by `security_core`).                  |
| **Randomization**     | Ensuring the sequence of Delta concepts is randomized independently per user session. (BRD F3.2.1)        |                                                                                    |
| **Vote Recording**    | Recording votes within robust transaction boundaries utilizing concurrency control mechanisms. (BRD F3.4) | Implementation of the Data Access Layer (DAL) or locking mechanisms (handled by `platform`). |
| **Consensus Calculation**| Implementation of the Unanimity consensus rule, accounting for dynamic adjudicator assignments. (BRD F4.1) |                                                                                    |
| **TGS Construction**  | Finalizing the TGS based on the Intersection and consensus outcomes. (BRD F4.2)                           | Statistical analysis (handled by `sap_engine`).                                      |
| **Operational Overrides**| Logic for handling dynamic adjudicator removal/replacement (e.g., dropout) and triggering consensus recalculation. | The API endpoints or RBAC enforcement for overrides (handled by `platform`).          |