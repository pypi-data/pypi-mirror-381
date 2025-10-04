# FRD Compliance and Usage Audit Report

## Introduction

This document provides a comprehensive, line-by-line analysis of the `codeeval_adjudication_engine` package against its Functional Requirements Document (FRD). The purpose of this report is to serve as a definitive verification tool for both developers and end-users.

For developers, it validates that the implementation meets the specified requirements. For users, it provides clear, executable examples of how to use each feature of the package.

The report is structured to follow the FRD, with each requirement individually addressed under its corresponding section heading. Each entry includes:
- The original requirement statement from the FRD.
- A mapping to the specific implementation in the codebase.
- A detailed explanation of how the code fulfills the requirement.
- A direct code snippet from the implementation.
- Verifiable usage and test case examples.

---

## IV. Functional Requirements

### AL1. Adjudication Workflow Management (The `WorkflowManager`)

#### **AL1.1 Domain-Specific Authorization**

> **Requirement Statement:** Verify the Adjudicator is actively assigned (`Is_Active=True`) to the `Clinical_Idea_ID` (BRD F2.2).

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/workflow_manager.py`
*   **Class:** `WorkflowManager`
*   **Method:** `is_adjudicator_authorized(self, user_id: str, clinical_idea_id: int) -> bool`

**Detailed Explanation:**
This requirement is fulfilled by the `is_adjudicator_authorized` method. It retrieves the list of currently active adjudicators for a specific `clinical_idea_id` by calling `self._dal.get_active_roster()`. It then iterates through this roster to check if the given `user_id` is present and has their `is_active` flag set to `True`. This ensures that only users who are explicitly assigned and currently active on a clinical idea can participate in the adjudication process, directly satisfying the domain-specific authorization rule.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/workflow_manager.py

def is_adjudicator_authorized(self, user_id: str, clinical_idea_id: int) -> bool:
    """
    Verifies if an adjudicator is actively assigned to the clinical idea.
    FRD AL1.1: Domain-Specific Authorization.

    Args:
        user_id: The ID of the user to verify.
        clinical_idea_id: The ID of the clinical idea.

    Returns:
        True if the user is an active adjudicator for the clinical idea, False otherwise.
    """
    active_roster = self._dal.get_active_roster(clinical_idea_id)
    return any(adjudicator.user_id == user_id and adjudicator.is_active for adjudicator in active_roster)
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al1_1.py
from unittest.mock import MagicMock
from codeeval_adjudication_engine.workflow_manager import WorkflowManager
from codeeval_adjudication_engine.models import AdjudicatorRoster
from codeeval_adjudication_engine.interfaces import DataAccessLayer

# 1. Set up a mock Data Access Layer (DAL)
# In a real application, this would be a concrete implementation.
mock_dal = MagicMock(spec=DataAccessLayer)
clinical_idea_id = 101
active_roster_data = [
    AdjudicatorRoster(user_id="adjudicator_1", is_active=True),
    AdjudicatorRoster(user_id="adjudicator_2", is_active=True),
    AdjudicatorRoster(user_id="adjudicator_3", is_active=False), # Inactive user
]
mock_dal.get_active_roster.return_value = active_roster_data

# 2. Instantiate the WorkflowManager with the mock DAL
workflow_manager = WorkflowManager(dal=mock_dal)

# 3. Verify authorization for different users
authorized_user = "adjudicator_1"
inactive_user = "adjudicator_3"
unassigned_user = "adjudicator_4"

is_auth_1 = workflow_manager.is_adjudicator_authorized(authorized_user, clinical_idea_id)
is_auth_2 = workflow_manager.is_adjudicator_authorized(inactive_user, clinical_idea_id)
is_auth_3 = workflow_manager.is_adjudicator_authorized(unassigned_user, clinical_idea_id)

print(f"Authorizing user '{authorized_user}': {is_auth_1}")
print(f"Authorizing user '{inactive_user}': {is_auth_2}")
print(f"Authorizing user '{unassigned_user}': {is_auth_3}")

# Expected Output:
# Authorizing user 'adjudicator_1': True
# Authorizing user 'adjudicator_3': False
# Authorizing user 'adjudicator_4': False
```

**Test Case Example:**
```python
# From: tests/test_workflow_manager.py

@pytest.mark.parametrize(
    "user_id, is_in_roster, is_active_in_roster, expected",
    [
        ("authorized_user", True, True, True),
        ("inactive_user", True, False, False),
        ("unlisted_user", False, False, False),
    ],
)
def test_is_adjudicator_authorized(
    workflow_manager, mock_dal, user_id, is_in_roster, is_active_in_roster, expected
):
    """
    Tests the is_adjudicator_authorized method for various scenarios.
    FRD AL1.1
    """
    # Arrange
    roster = []
    if is_in_roster:
        roster.append(
            AdjudicatorRoster(user_id=user_id, is_active=is_active_in_roster)
        )
    mock_dal.get_active_roster = MagicMock(return_value=roster)
    clinical_idea_id = 1

    # Act
    is_authorized = workflow_manager.is_adjudicator_authorized(
        user_id, clinical_idea_id
    )

    # Assert
    assert is_authorized is expected
```

---
#### **AL1.2 Clinical Idea State Management**

> **Requirement Statement:** Manage the `ClinicalIdeaStatus` (PENDING, IN_PROGRESS, FINALIZED).

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/workflow_manager.py`
*   **Class:** `WorkflowManager`
*   **Method:** `update_clinical_idea_status(self, clinical_idea_id: int, new_status: ClinicalIdeaStatus) -> None`
*   **Helper Method:** `start_adjudication(self, clinical_idea_id: int) -> None`

**Detailed Explanation:**
This requirement is handled by the `update_clinical_idea_status` method within the `WorkflowManager`. This method acts as a gatekeeper for all state changes related to a `ClinicalIdea`. It contains a hardcoded dictionary, `valid_transitions`, which explicitly defines the legal state transitions (e.g., `PENDING` to `IN_PROGRESS`). Before instructing the Data Access Layer (DAL) to persist a change, it checks the current status and the requested new status against this dictionary. If the transition is not defined as valid (e.g., trying to move from `FINALIZED` back to `IN_PROGRESS`), it raises an `InvalidStateError`, thus preventing illegal workflow progression. The `start_adjudication` method provides a convenient, business-specific entry point to the more generic state update logic.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/workflow_manager.py

def update_clinical_idea_status(
    self, clinical_idea_id: int, new_status: ClinicalIdeaStatus
) -> None:
    """
    Manages the state transitions of a Clinical Idea.
    ...
    """
    current_status = self._dal.get_clinical_idea_status(clinical_idea_id)
    if current_status == new_status:
        return  # The operation is idempotent.

    # Define valid state transitions.
    valid_transitions = {
        ClinicalIdeaStatus.PENDING: {ClinicalIdeaStatus.IN_PROGRESS},
        ClinicalIdeaStatus.IN_PROGRESS: {ClinicalIdeaStatus.FINALIZED},
        ClinicalIdeaStatus.FINALIZED: set(),  # No transitions out of FINALIZED.
    }

    if new_status not in valid_transitions.get(current_status, set()):
        raise InvalidStateError(
            f"Invalid state transition for clinical idea {clinical_idea_id} "
            f"from '{current_status.name}' to '{new_status.name}'."
        )

    self._dal.update_clinical_idea_status(clinical_idea_id, new_status)
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al1_2.py
from unittest.mock import MagicMock
from codeeval_adjudication_engine.workflow_manager import WorkflowManager
from codeeval_adjudication_engine.models import ClinicalIdeaStatus, InvalidStateError
from codeeval_adjudication_engine.interfaces import DataAccessLayer

# 1. Set up a mock DAL
mock_dal = MagicMock(spec=DataAccessLayer)
workflow_manager = WorkflowManager(dal=mock_dal)
clinical_idea_id = 202

# 2. Simulate a valid state transition (PENDING -> IN_PROGRESS)
mock_dal.get_clinical_idea_status.return_value = ClinicalIdeaStatus.PENDING
print(f"Attempting to move from PENDING to IN_PROGRESS...")
try:
    workflow_manager.start_adjudication(clinical_idea_id)
    print("  Success! State transition was valid.")
    # Verify the DAL was called to persist the change
    mock_dal.update_clinical_idea_status.assert_called_with(
        clinical_idea_id, ClinicalIdeaStatus.IN_PROGRESS
    )
except InvalidStateError as e:
    print(f"  Failed: {e}")

# 3. Simulate an invalid state transition (FINALIZED -> IN_PROGRESS)
mock_dal.get_clinical_idea_status.return_value = ClinicalIdeaStatus.FINALIZED
print(f"\nAttempting to move from FINALIZED to IN_PROGRESS...")
try:
    workflow_manager.update_clinical_idea_status(clinical_idea_id, ClinicalIdeaStatus.IN_PROGRESS)
    print("  Success! State transition was valid.")
except InvalidStateError as e:
    print(f"  Failed as expected: {e}")

# Expected Output:
# Attempting to move from PENDING to IN_PROGRESS...
#   Success! State transition was valid.
#
# Attempting to move from FINALIZED to IN_PROGRESS...
#   Failed as expected: Invalid state transition for clinical idea 202 from 'FINALIZED' to 'IN_PROGRESS'.
```

**Test Case Example:**
```python
# test_case_al1_2.py
import pytest
from unittest.mock import MagicMock, call
from codeeval_adjudication_engine.workflow_manager import WorkflowManager
from codeeval_adjudication_engine.models import ClinicalIdeaStatus, InvalidStateError
from codeeval_adjudication_engine.interfaces import DataAccessLayer

@pytest.fixture
def mock_dal_al1_2():
    return MagicMock(spec=DataAccessLayer)

def test_valid_state_transitions(mock_dal_al1_2):
    """
    Tests that legally defined state transitions are executed correctly.
    """
    manager = WorkflowManager(dal=mock_dal_al1_2)
    idea_id = 1

    # Test PENDING -> IN_PROGRESS
    mock_dal_al1_2.get_clinical_idea_status.return_value = ClinicalIdeaStatus.PENDING
    manager.update_clinical_idea_status(idea_id, ClinicalIdeaStatus.IN_PROGRESS)
    mock_dal_al1_2.update_clinical_idea_status.assert_called_with(idea_id, ClinicalIdeaStatus.IN_PROGRESS)

    # Test IN_PROGRESS -> FINALIZED
    mock_dal_al1_2.get_clinical_idea_status.return_value = ClinicalIdeaStatus.IN_PROGRESS
    manager.update_clinical_idea_status(idea_id, ClinicalIdeaStatus.FINALIZED)
    mock_dal_al1_2.update_clinical_idea_status.assert_called_with(idea_id, ClinicalIdeaStatus.FINALIZED)

def test_invalid_state_transitions_raise_error(mock_dal_al1_2):
    """
    Tests that illegal state transitions raise an InvalidStateError.
    """
    manager = WorkflowManager(dal=mock_dal_al1_2)
    idea_id = 1

    # Test FINALIZED -> IN_PROGRESS (invalid)
    mock_dal_al1_2.get_clinical_idea_status.return_value = ClinicalIdeaStatus.FINALIZED
    with pytest.raises(InvalidStateError, match="from 'FINALIZED' to 'IN_PROGRESS'"):
        manager.update_clinical_idea_status(idea_id, ClinicalIdeaStatus.IN_PROGRESS)

    # Test PENDING -> FINALIZED (invalid, must go through IN_PROGRESS)
    mock_dal_al1_2.get_clinical_idea_status.return_value = ClinicalIdeaStatus.PENDING
    with pytest.raises(InvalidStateError, match="from 'PENDING' to 'FINALIZED'"):
        manager.update_clinical_idea_status(idea_id, ClinicalIdeaStatus.FINALIZED)

def test_idempotent_state_transition(mock_dal_al1_2):
    """
    Tests that attempting to set the same status does not result in a DAL call.
    """
    manager = WorkflowManager(dal=mock_dal_al1_2)
    idea_id = 1
    mock_dal_al1_2.reset_mock() # Reset call counts

    mock_dal_al1_2.get_clinical_idea_status.return_value = ClinicalIdeaStatus.IN_PROGRESS
    manager.update_clinical_idea_status(idea_id, ClinicalIdeaStatus.IN_PROGRESS)

    # Assert that the update method was NOT called again
    mock_dal_al1_2.update_clinical_idea_status.assert_not_called()
```

---
#### **AL1.3 Concept State Management**

> **Requirement Statement:** Manage the `ConceptStatus` (PENDING, CONSENSUS_INCLUDE, CONSENSUS_EXCLUDE).

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/workflow_manager.py`
*   **Class:** `WorkflowManager`
*   **Method:** `update_concept_status(self, clinical_idea_id: int, concept_id: int, new_status: ConceptConsensusStatus) -> None`

**Detailed Explanation:**
The `update_concept_status` method in the `WorkflowManager` is responsible for this requirement. Its primary role is to act as a safeguard before persisting a change to a concept's status. It first checks the status of the parent `ClinicalIdea`. As per FRD AL3.2, if the clinical idea is already `FINALIZED`, no further changes to its child concepts are allowed. In this case, the method raises an `InvalidStateError`, protecting the integrity of a finalized result. If the parent idea is still in an active state, the method proceeds to call the DAL (`self._dal.update_concept_status`) to persist the new status for the specified concept.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/workflow_manager.py

def update_concept_status(
    self,
    clinical_idea_id: int,
    concept_id: int,
    new_status: ConceptConsensusStatus,
) -> None:
    """
    Manages the state of an individual concept.
    FRD AL1.3: Concept State Management.

    Before updating a concept's status, it validates that the parent
    clinical idea is not finalized.
    ...
    """
    # FRD AL3.2: Validate the Clinical Idea State is not FINALIZED.
    idea_status = self._dal.get_clinical_idea_status(clinical_idea_id)
    if idea_status == ClinicalIdeaStatus.FINALIZED:
        raise InvalidStateError(
            f"Cannot update concept {concept_id} status; clinical idea "
            f"{clinical_idea_id} is already finalized."
        )

    # Persist the change via the Data Access Layer.
    self._dal.update_concept_status(concept_id, new_status)
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al1_3.py
from unittest.mock import MagicMock
from codeeval_adjudication_engine.workflow_manager import WorkflowManager
from codeeval_adjudication_engine.models import ClinicalIdeaStatus, ConceptConsensusStatus, InvalidStateError
from codeeval_adjudication_engine.interfaces import DataAccessLayer

# 1. Set up mock DAL and WorkflowManager
mock_dal = MagicMock(spec=DataAccessLayer)
manager = WorkflowManager(dal=mock_dal)
clinical_idea_id = 303
concept_id = 1

# 2. Scenario 1: Update status when Clinical Idea is IN_PROGRESS (valid)
mock_dal.get_clinical_idea_status.return_value = ClinicalIdeaStatus.IN_PROGRESS
print("Attempting to update concept status while idea is IN_PROGRESS...")
try:
    manager.update_concept_status(clinical_idea_id, concept_id, ConceptConsensusStatus.CONSENSUS_INCLUDE)
    print("  Success! Concept status updated.")
    mock_dal.update_concept_status.assert_called_once_with(concept_id, ConceptConsensusStatus.CONSENSUS_INCLUDE)
except InvalidStateError as e:
    print(f"  Failed: {e}")

# 3. Scenario 2: Attempt to update status when Clinical Idea is FINALIZED (invalid)
mock_dal.reset_mock()
mock_dal.get_clinical_idea_status.return_value = ClinicalIdeaStatus.FINALIZED
print("\nAttempting to update concept status while idea is FINALIZED...")
try:
    manager.update_concept_status(clinical_idea_id, concept_id, ConceptConsensusStatus.CONSENSUS_EXCLUDE)
    print("  Success! Concept status updated.")
except InvalidStateError as e:
    print(f"  Failed as expected: {e}")
    mock_dal.update_concept_status.assert_not_called()

# Expected Output:
# Attempting to update concept status while idea is IN_PROGRESS...
#   Success! Concept status updated.
#
# Attempting to update concept status while idea is FINALIZED...
#   Failed as expected: Cannot update concept 1 status; clinical idea 303 is already finalized.
```

**Test Case Example:**
```python
# From: tests/test_workflow_manager.py

def test_update_concept_status_success(workflow_manager, mock_dal):
    """
    Tests that update_concept_status successfully calls the DAL when the
    clinical idea is not finalized.
    FRD AL1.3
    """
    # Arrange
    clinical_idea_id = 1
    concept_id = 101
    new_status = "CONSENSUS_INCLUDE"
    mock_dal.get_clinical_idea_status = MagicMock(
        return_value=ClinicalIdeaStatus.IN_PROGRESS
    )
    mock_dal.update_concept_status = MagicMock()

    # Act
    workflow_manager.update_concept_status(clinical_idea_id, concept_id, new_status)

    # Assert
    mock_dal.get_clinical_idea_status.assert_called_once_with(clinical_idea_id)
    mock_dal.update_concept_status.assert_called_once_with(concept_id, new_status)


def test_update_concept_status_raises_error_for_finalized_idea(
    workflow_manager, mock_dal
):
    """
    Tests that update_concept_status raises an InvalidStateError if the
    clinical idea is already FINALIZED.
    FRD AL1.3
    """
    # Arrange
    clinical_idea_id = 1
    concept_id = 101
    new_status = "CONSENSUS_INCLUDE"
    mock_dal.get_clinical_idea_status = MagicMock(
        return_value=ClinicalIdeaStatus.FINALIZED
    )
    mock_dal.update_concept_status = MagicMock()

    # Act & Assert
    with pytest.raises(InvalidStateError) as excinfo:
        workflow_manager.update_concept_status(
            clinical_idea_id, concept_id, new_status
        )
    assert f"clinical idea {clinical_idea_id} is already finalized" in str(
        excinfo.value
    )
    mock_dal.update_concept_status.assert_not_called()
```

---
#### **AL1.4 CRITICAL: Adjudicator Roster Management**

> **Requirement Statement:** The module must maintain the definitive, active `AdjudicatorRoster` for each Clinical Idea. This roster is the basis for consensus calculation (AL4.3) and is dynamically updated via the Override mechanism (AL7).

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/workflow_manager.py`
*   **Class:** `WorkflowManager`
*   **Methods:**
    *   `get_roster(self, clinical_idea_id: int) -> List[AdjudicatorRoster]`
    *   `modify_roster(self, clinical_idea_id: int, user_id_to_modify: str, new_active_status: bool) -> None`

**Detailed Explanation:**
The `WorkflowManager` serves as the authoritative source for Adjudicator Roster information, as mandated by this critical requirement. It provides two key methods: `get_roster` and `modify_roster`.

The `get_roster` method provides a centralized, read-only access point to the active roster for a given clinical idea by fetching it from the DAL. This ensures that other components, such as the `ConsensusCalculator` (AL4.3), have a single, reliable source for determining who is eligible to vote.

The `modify_roster` method centralizes the logic for changing the roster. It orchestrates the DAL call to update an adjudicator's active status (`modify_roster_status`) and, critically, handles the necessary side-effect of invalidating that user's existing votes if they are being deactivated (`invalidate_votes`). This logic is designed to be called by the `OverrideManager` (AL7), ensuring that roster changes and their consequences are managed consistently.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/workflow_manager.py

def get_roster(self, clinical_idea_id: int) -> List[AdjudicatorRoster]:
    """
    Retrieves the active adjudicator roster for a given clinical idea.
    This method centralizes access to the roster as required by FRD AL1.4.
    ...
    """
    return self._dal.get_active_roster(clinical_idea_id)

def modify_roster(
    self,
    clinical_idea_id: int,
    user_id_to_modify: str,
    new_active_status: bool,
) -> None:
    """
    Modifies an adjudicator's status on the roster and invalidates their
    votes if they are being deactivated.
    This centralizes roster modification logic per FRD AL1.4.
    ...
    """
    self._dal.modify_roster_status(
        clinical_idea_id, user_id_to_modify, new_active_status
    )
    if not new_active_status:
        self._dal.invalidate_votes(clinical_idea_id, user_id_to_modify)
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al1_4.py
from unittest.mock import MagicMock, call
from codeeval_adjudication_engine.workflow_manager import WorkflowManager
from codeeval_adjudication_engine.models import AdjudicatorRoster
from codeeval_adjudication_engine.interfaces import DataAccessLayer

# 1. Set up mock DAL and WorkflowManager
mock_dal = MagicMock(spec=DataAccessLayer)
manager = WorkflowManager(dal=mock_dal)
clinical_idea_id = 404
user_to_deactivate = "adjudicator_beta"

# 2. Mock the initial roster
initial_roster = [
    AdjudicatorRoster(user_id="adjudicator_alpha", is_active=True),
    AdjudicatorRoster(user_id=user_to_deactivate, is_active=True),
]
mock_dal.get_active_roster.return_value = initial_roster

# 3. Use get_roster to retrieve the current roster
print("Initial Roster:")
current_roster = manager.get_roster(clinical_idea_id)
for adjudicator in current_roster:
    print(f"  - {adjudicator.user_id} (Active: {adjudicator.is_active})")
mock_dal.get_active_roster.assert_called_with(clinical_idea_id)

# 4. Use modify_roster to deactivate an adjudicator
print(f"\nDeactivating user '{user_to_deactivate}'...")
manager.modify_roster(clinical_idea_id, user_to_deactivate, new_active_status=False)
print("  Modification complete.")

# 5. Verify the correct DAL methods were called in sequence
print("\nVerifying DAL calls:")
expected_calls = [
    call.modify_roster_status(clinical_idea_id, user_to_deactivate, False),
    call.invalidate_votes(clinical_idea_id, user_to_deactivate)
]
mock_dal.assert_has_calls(expected_calls, any_order=False)
print("  - modify_roster_status called correctly.")
print("  - invalidate_votes called correctly.")

# Expected Output:
# Initial Roster:
#   - adjudicator_alpha (Active: True)
#   - adjudicator_beta (Active: True)
#
# Deactivating user 'adjudicator_beta'...
#   Modification complete.
#
# Verifying DAL calls:
#   - modify_roster_status called correctly.
#   - invalidate_votes called correctly.
```

**Test Case Example:**
```python
# test_case_al1_4.py
import pytest
from unittest.mock import MagicMock, call
from codeeval_adjudication_engine.workflow_manager import WorkflowManager
from codeeval_adjudication_engine.models import AdjudicatorRoster
from codeeval_adjudication_engine.interfaces import DataAccessLayer

@pytest.fixture
def manager_al1_4():
    mock_dal = MagicMock(spec=DataAccessLayer)
    manager = WorkflowManager(dal=mock_dal)
    return manager, mock_dal

def test_get_roster_calls_dal(manager_al1_4):
    """
    Tests that get_roster correctly calls the DAL to fetch the roster.
    """
    manager, mock_dal = manager_al1_4
    idea_id = 1
    expected_roster = [AdjudicatorRoster(user_id="test_user")]
    mock_dal.get_active_roster.return_value = expected_roster

    roster = manager.get_roster(idea_id)

    mock_dal.get_active_roster.assert_called_once_with(idea_id)
    assert roster == expected_roster

def test_modify_roster_deactivation_invalidates_votes(manager_al1_4):
    """
    Tests that deactivating a user via modify_roster also triggers vote invalidation.
    """
    manager, mock_dal = manager_al1_4
    idea_id, user_id = 1, "user_to_remove"

    manager.modify_roster(idea_id, user_id, new_active_status=False)

    # Check that both roster modification and vote invalidation were called
    mock_dal.modify_roster_status.assert_called_once_with(idea_id, user_id, False)
    mock_dal.invalidate_votes.assert_called_once_with(idea_id, user_id)

def test_modify_roster_activation_does_not_invalidate_votes(manager_al1_4):
    """
    Tests that activating a user does NOT trigger vote invalidation.
    """
    manager, mock_dal = manager_al1_4
    idea_id, user_id = 1, "user_to_add"

    manager.modify_roster(idea_id, user_id, new_active_status=True)

    # Check that only roster modification was called
    mock_dal.modify_roster_status.assert_called_once_with(idea_id, user_id, True)
    mock_dal.invalidate_votes.assert_not_called()
```

---
### AL2. Blinded Data Presentation and Randomization (The `DataPresenter`)

#### **AL2.1, AL2.2, AL2.3, AL2.4: Combined Data Retrieval, Filtering, Randomization, and Context**

> **Requirement Statements:**
> *   **AL2.1 CRITICAL: Information Control and Filtering (BRD F3.3):** The module MUST actively filter the internal `Concept_Pool` to produce the `BlindedConceptView`.
>     *   **AL2.1.1 Mandatory Exclusions (F3.3.2):** MUST strictly exclude the `Agreement_Level` and `Contributing_Arms`.
> *   **AL2.2 CRITICAL: Randomized Sequencing (BRD F3.2.1):** The sequence of Delta concepts MUST be randomized.
>     *   **AL2.2.1 Sequence Stability:** The randomization MUST utilize the `Session_RNG_Seed` provided in the `UserContext`.
> *   **AL2.3 Delta Retrieval (`GetConceptsForReview`):** Provides the interface to retrieve the randomized and sanitized concept list.
> *   **AL2.4 Clinical Idea Context (BRD F3.1):** Provide the standardized "Clinical Description" for context.

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/presenter.py`
*   **Class:** `DataPresenter`
*   **Method:** `get_concepts_for_review(self, clinical_idea_id: int, user_context: UserContext) -> AdjudicationDataPackage`

**Detailed Explanation:**
The `get_concepts_for_review` method holistically addresses all requirements for presenting data to an adjudicator.
1.  **Retrieval and Context (AL2.3, AL2.4):** It begins by fetching the raw concept pool and the clinical idea's description from the Data Access Layer (DAL).
2.  **Randomization (AL2.2):** Crucially, it instantiates a dedicated `random.Random` object using the `session_rng_seed` from the `UserContext`. This ensures that the randomization is both session-specific and deterministic, fulfilling the sequence stability requirement without affecting the global random state. It then shuffles a *copy* of the concept list.
3.  **Filtering and Blinding (AL2.1):** After shuffling, the method iterates through the randomized list and transforms each full `Concept` object into a `BlindedConceptView`. This transformation is the critical step for blinding; the `BlindedConceptView`'s constructor only accepts `concept_id`, `name`, and `description`, thereby guaranteeing that sensitive fields like `agreement_level` and `contributing_arms` are physically excluded from the data structure sent to the user.
4.  **Packaging:** Finally, it bundles the clinical description and the list of blinded, randomized concepts into an `AdjudicationDataPackage` for delivery.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/presenter.py

def get_concepts_for_review(
    self,
    clinical_idea_id: int,
    user_context: UserContext,
) -> AdjudicationDataPackage:
    """
    Retrieves, filters, and randomizes concepts for an adjudication session.
    ...
    """
    # AL2.4 & AL2.3: Fetch data from the DAL
    description = self._dal.get_clinical_idea_description(clinical_idea_id)
    concepts = self._dal.get_all_concepts_for_idea(clinical_idea_id)

    concepts_copy = list(concepts)

    # AL2.2: Use a dedicated Random instance with the session-specific seed
    session_randomizer = random.Random(user_context.session_rng_seed)
    session_randomizer.shuffle(concepts_copy)

    # AL2.1: Transform into the sanitized BlindedConceptView
    blinded_concepts = [
        BlindedConceptView(
            concept_id=c.concept_id,
            name=c.name,
            description=c.description,
        )
        for c in concepts_copy
    ]

    # Package the description and concepts together
    return AdjudicationDataPackage(
        clinical_idea_description=description,
        concepts_for_review=blinded_concepts,
    )
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al2.py
from unittest.mock import MagicMock
from codeeval_adjudication_engine.presenter import DataPresenter
from codeeval_adjudication_engine.models import Concept, UserContext
from codeeval_adjudication_engine.interfaces import DataAccessLayer

# 1. Set up mock DAL and DataPresenter
mock_dal = MagicMock(spec=DataAccessLayer)
presenter = DataPresenter(dal=mock_dal)
clinical_idea_id = 505

# 2. Mock the DAL return values
mock_dal.get_clinical_idea_description.return_value = "A sample clinical description."
mock_dal.get_all_concepts_for_idea.return_value = [
    Concept(concept_id=1, name="A", description="Desc A", agreement_level=3, contributing_arms=["X"]),
    Concept(concept_id=2, name="B", description="Desc B", agreement_level=2, contributing_arms=["Y"]),
    Concept(concept_id=3, name="C", description="Desc C", agreement_level=1, contributing_arms=["Z"]),
]

# 3. Simulate two different user sessions with the same seed
rng_seed = 123
user1_context = UserContext(user_id="user1", session_rng_seed=rng_seed, roles=[])
user2_context = UserContext(user_id="user2", session_rng_seed=rng_seed, roles=[])
user3_context = UserContext(user_id="user3", session_rng_seed=456, roles=[]) # Different seed

# 4. Get the data package for each user
package1 = presenter.get_concepts_for_review(clinical_idea_id, user1_context)
package2 = presenter.get_concepts_for_review(clinical_idea_id, user2_context)
package3 = presenter.get_concepts_for_review(clinical_idea_id, user3_context)

# 5. Print results and verify blinding and randomization
print(f"Clinical Idea Description: {package1.clinical_idea_description}\n")

print("User 1's Randomized/Blinded List (Seed: 123):")
for concept in package1.concepts_for_review:
    print(f"  - {concept}")
    assert not hasattr(concept, 'agreement_level'), "Blinding failed!"

print("\nUser 2's Randomized/Blinded List (Seed: 123):")
for concept in package2.concepts_for_review:
    print(f"  - {concept}")

print("\nUser 3's Randomized/Blinded List (Seed: 456):")
for concept in package3.concepts_for_review:
    print(f"  - {concept}")

# Verify randomization stability
user1_ids = [c.concept_id for c in package1.concepts_for_review]
user2_ids = [c.concept_id for c in package2.concepts_for_review]
user3_ids = [c.concept_id for c in package3.concepts_for_review]
print(f"\nUser 1 and 2 lists are identical: {user1_ids == user2_ids}")
print(f"User 1 and 3 lists are different: {user1_ids != user3_ids}")

# Expected Output:
# Clinical Idea Description: A sample clinical description.
#
# User 1's Randomized/Blinded List (Seed: 123):
#   - BlindedConceptView(concept_id=3, name='C', description='Desc C')
#   - BlindedConceptView(concept_id=2, name='B', description='Desc B')
#   - BlindedConceptView(concept_id=1, name='A', description='Desc A')
#
# User 2's Randomized/Blinded List (Seed: 123):
#   - BlindedConceptView(concept_id=3, name='C', description='Desc C')
#   - BlindedConceptView(concept_id=2, name='B', description='Desc B')
#   - BlindedConceptView(concept_id=1, name='A', description='Desc A')
#
# User 3's Randomized/Blinded List (Seed: 456):
#   - BlindedConceptView(concept_id=1, name='A', description='Desc A')
#   - BlindedConceptView(concept_id=2, name='B', description='Desc B')
#   - BlindedConceptView(concept_id=3, name='C', description='Desc C')
#
# User 1 and 2 lists are identical: True
# User 1 and 3 lists are different: True
```

**Test Case Example:**
```python
# From: tests/test_presenter_data_blinding.py

def test_blinding_strips_sensitive_fields(
    sample_concepts_for_blinding: List[Concept],
):
    """
    CRITICAL (NFR-AL1, AL2.1.1): Verifies that the `get_concepts_for_review`
    method strictly removes the `agreement_level` and `contributing_arms`
    fields from the data sent to the user, ensuring compliance with the
    blinding protocol.
    """
    clinical_idea_id = 1
    user_context = UserContext(user_id="test_user", session_rng_seed=123)
    mock_dal = MockDataAccessLayer(
        concepts_by_idea={clinical_idea_id: sample_concepts_for_blinding}
    )
    presenter = DataPresenter(dal=mock_dal)

    # Act
    result = presenter.get_concepts_for_review(clinical_idea_id, user_context)

    # Assert
    assert len(result.concepts_for_review) > 0, "Test setup failed: No concepts returned."

    for concept_view in result.concepts_for_review:
        # 1. Verify it's the correct, sanitized data model
        assert isinstance(
            concept_view, BlindedConceptView
        ), "Returned object is not a BlindedConceptView."

        # 2. CRITICAL: Verify sensitive fields are absent
        assert not hasattr(
            concept_view, "agreement_level"
        ), "Blinding failed: 'agreement_level' was exposed."
        assert not hasattr(
            concept_view, "contributing_arms"
        ), "Blinding failed: 'contributing_arms' were exposed."

        # 3. Verify that non-sensitive fields are present
        assert hasattr(
            concept_view, "concept_id"
        ), "Data integrity failed: 'concept_id' is missing."
        assert hasattr(
            concept_view, "name"
        ), "Data integrity failed: 'name' is missing."
        assert hasattr(
            concept_view, "description"
        ), "Data integrity failed: 'description' is missing."
```

---
### AL3. Vote Recording and Management (The `VoteRecorder`)

#### **AL3.1-AL3.5: Combined Vote Submission, Validation, Persistence, and Transaction Management**

> **Requirement Statements:**
> *   **AL3.1 Vote Submission (`SubmitVote`):** Interface to accept a vote (Include/Exclude).
> *   **AL3.2 Validation:** Validate the Adjudicator is authorized (AL1.1) and the Clinical Idea State is not `FINALIZED`.
> *   **AL3.3 Persistence and Auditing:** Successful votes must be persisted, including the timestamp.
> *   **AL3.4 Vote Updates:** Support Adjudicators changing their vote.
> *   **AL3.5 CRITICAL: Transaction Management and Locking (C4):** The entire process...MUST occur within a single, ACID-compliant database transaction.
>     *   **AL3.5.1 Pessimistic Locking Mandate:** This transaction MUST acquire a Pessimistic Lock (e.g., `SELECT FOR UPDATE`) on the corresponding `ConceptStatus` row.
>     *   **AL3.5.2 Error Handling:** The logic must handle potential locking failures or timeouts gracefully.

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/recorder.py`
*   **Class:** `VoteRecorder`
*   **Method:** `submit_vote(self, user_id: str, concept_id: int, decision: VoteDecision, clinical_idea_id: int) -> None`

**Detailed Explanation:**
The `submit_vote` method is a critical, multi-responsibility method that fulfills all requirements of section AL3 within a single, robust transaction.
1.  **Validation (AL3.2):** It first delegates validation to the `WorkflowManager`. It calls `start_adjudication` to ensure the clinical idea is in a valid state (`IN_PROGRESS`) and then retrieves the definitive roster to perform an authorization check, raising an `AuthorizationError` if the user is not an active adjudicator.
2.  **Auditing (AL3.3):** An audit trail is immediately created by calling `self._audit_logger.log_vote_action`, ensuring that every vote attempt is logged.
3.  **Vote Update Handling (AL3.4):** The method checks if a vote from the user for the specific concept already exists by calling `self._dal.get_vote_by_user_and_concept`. This determines whether to perform a `create_vote` or `update_vote` operation later.
4.  **Transaction and Locking (AL3.5):** The core logic is wrapped in a `with self._dal.transaction():` block, guaranteeing ACID compliance. The very first action inside the transaction is `self._dal.get_concept_status_for_update(concept_id)`, which explicitly acquires a pessimistic lock on the concept's status row in the database, preventing race conditions from concurrent votes.
5.  **Persistence (AL3.3):** A new `AdjudicationVote` object is created, crucially generating a server-side UTC timestamp at the moment of creation (`datetime.now(timezone.utc)`). The vote is then persisted using either `create_vote` or `update_vote`.
6.  **Consensus Trigger:** After the vote is successfully recorded, it immediately triggers the `ConsensusCalculator` and the `TGSFactory` to re-evaluate the state of the clinical idea in real-time, all within the same transaction.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/recorder.py

def submit_vote(
    self, user_id: str, concept_id: int, decision: VoteDecision, clinical_idea_id: int
) -> None:
    # ... (Validation and Auditing logic shown in detail in the file) ...

    # Check for existing vote (AL3.4)
    existing_vote = self._dal.get_vote_by_user_and_concept(
        user_id=user_id, concept_id=concept_id
    )

    # Transaction Management and Locking (AL3.5)
    with self._dal.transaction():
        # Acquire lock before any writes (AL3.5.1)
        self._dal.get_concept_status_for_update(concept_id)

        # Create the vote object with an authoritative timestamp (AL3.3)
        vote_to_persist = AdjudicationVote(
            user_id=user_id,
            concept_id=concept_id,
            decision=decision,
            timestamp=datetime.now(timezone.utc),
        )

        # Persist the vote (AL3.3, AL3.4)
        if existing_vote:
            self._dal.update_vote(vote_to_persist)
        else:
            self._dal.create_vote(vote_to_persist)

        # Consensus Recalculation (AL4.1.1)
        all_votes = self._dal.get_all_votes(clinical_idea_id)
        new_consensus = self._consensus_calculator.calculate_consensus(...)
        self._dal.update_concept_status(concept_id, new_consensus)

        # Check for Clinical Idea Finalization
        self._tgs_factory.check_and_finalize(clinical_idea_id)
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al3.py
from unittest.mock import MagicMock, call
from datetime import datetime
from codeeval_adjudication_engine.recorder import VoteRecorder
from codeeval_adjudication_engine.models import VoteDecision, AdjudicatorRoster, ConceptConsensusStatus
# Import all required components for instantiation
from codeeval_adjudication_engine.interfaces import DataAccessLayer, AuditLogger
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

# 1. Set up all mock dependencies
mock_dal = MagicMock(spec=DataAccessLayer)
mock_consensus = MagicMock(spec=ConsensusCalculator)
mock_tgs = MagicMock(spec=TGSFactory)
mock_audit = MagicMock(spec=AuditLogger)
mock_workflow = MagicMock(spec=WorkflowManager)

# 2. Instantiate the VoteRecorder
recorder = VoteRecorder(mock_dal, mock_consensus, mock_tgs, mock_audit, mock_workflow)

# 3. Configure mock behaviors
user_id, concept_id, idea_id = "user1", 101, 1
mock_workflow.get_roster.return_value = [AdjudicatorRoster("user1", is_active=True)]
mock_dal.get_vote_by_user_and_concept.return_value = None # Simulate a new vote
mock_consensus.calculate_consensus.return_value = ConceptConsensusStatus.PENDING

# 4. Simulate a vote submission
print(f"Submitting a new 'INCLUDE' vote for concept {concept_id}...")
recorder.submit_vote(user_id, concept_id, VoteDecision.INCLUDE, idea_id)
print("Vote submitted successfully.")

# 5. Verify the sequence of events
print("\nVerifying execution flow:")
# a. Validation was called
mock_workflow.start_adjudication.assert_called_with(idea_id)
mock_workflow.get_roster.assert_called_with(idea_id)
print("  - Validation and authorization checks passed.")

# b. Auditing was called
mock_audit.log_vote_action.assert_called()
print("  - Vote action was audited.")

# c. Transaction was initiated (we can't see inside, but we verify the calls within)
# d. Pessimistic lock was acquired
mock_dal.get_concept_status_for_update.assert_called_with(concept_id)
print("  - Pessimistic lock was acquired on the concept.")

# e. Vote was created (not updated)
mock_dal.create_vote.assert_called()
mock_dal.update_vote.assert_not_called()
print("  - A new vote was created in the DAL.")

# f. Consensus was recalculated
mock_consensus.calculate_consensus.assert_called()
print("  - Consensus was recalculated.")

# g. Finalization check was triggered
mock_tgs.check_and_finalize.assert_called_with(idea_id)
print("  - TGS finalization check was triggered.")

# Expected Output:
# Submitting a new 'INCLUDE' vote for concept 101...
# Vote submitted successfully.
#
# Verifying execution flow:
#   - Validation and authorization checks passed.
#   - Vote action was audited.
#   - Pessimistic lock was acquired on the concept.
#   - A new vote was created in the DAL.
#   - Consensus was recalculated.
#   - TGS finalization check was triggered.
```

**Test Case Example:**
```python
# test_case_al3.py
import pytest
from unittest.mock import MagicMock, ANY
from codeeval_adjudication_engine.recorder import VoteRecorder
from codeeval_adjudication_engine.models import VoteDecision, AdjudicatorRoster, AdjudicationVote, AuthorizationError
from codeeval_adjudication_engine.interfaces import DataAccessLayer, AuditLogger
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

@pytest.fixture
def recorder_components():
    return {
        "dal": MagicMock(spec=DataAccessLayer),
        "consensus_calculator": MagicMock(spec=ConsensusCalculator),
        "tgs_factory": MagicMock(spec=TGSFactory),
        "audit_logger": MagicMock(spec=AuditLogger),
        "workflow_manager": MagicMock(spec=WorkflowManager),
    }

def test_submit_new_vote_flow(recorder_components):
    """
    Tests the end-to-end flow for submitting a completely new vote. (AL3.1-3.5)
    """
    recorder = VoteRecorder(**recorder_components)
    dal = recorder_components['dal']

    # Arrange: User is authorized, it's a new vote
    recorder_components['workflow_manager'].get_roster.return_value = [AdjudicatorRoster("user1", True)]
    dal.get_vote_by_user_and_concept.return_value = None

    # Act
    recorder.submit_vote("user1", 101, VoteDecision.INCLUDE, 1)

    # Assert
    dal.get_concept_status_for_update.assert_called_once_with(101)
    dal.create_vote.assert_called_once()
    dal.update_vote.assert_not_called()
    recorder_components['consensus_calculator'].calculate_consensus.assert_called_once()

def test_submit_updated_vote_flow(recorder_components):
    """
    Tests the flow for a user changing their existing vote. (AL3.4)
    """
    recorder = VoteRecorder(**recorder_components)
    dal = recorder_components['dal']

    # Arrange: User is authorized, an existing vote is found
    recorder_components['workflow_manager'].get_roster.return_value = [AdjudicatorRoster("user1", True)]
    dal.get_vote_by_user_and_concept.return_value = MagicMock(spec=AdjudicationVote)

    # Act
    recorder.submit_vote("user1", 101, VoteDecision.EXCLUDE, 1)

    # Assert
    dal.get_concept_status_for_update.assert_called_once_with(101)
    dal.update_vote.assert_called_once()
    dal.create_vote.assert_not_called()

def test_submit_vote_unauthorized_user(recorder_components):
    """
    Tests that an unauthorized user submission is blocked. (AL3.2)
    """
    recorder = VoteRecorder(**recorder_components)
    # Arrange: User 'user2' is not in the active roster
    recorder_components['workflow_manager'].get_roster.return_value = [AdjudicatorRoster("user1", True)]

    # Act & Assert
    with pytest.raises(AuthorizationError):
        recorder.submit_vote("user2", 101, VoteDecision.INCLUDE, 1)
```

**Verification Note on Transactional Atomicity:**
The test suite includes a critical test, `test_submit_vote_rolls_back_on_downstream_error`, which is marked with `pytest.mark.xfail` to formally document a bug in the system's transactional behavior.

The test simulates a failure *inside* the transaction block (by forcing the `ConsensusCalculator` to raise an error) after the vote has already been saved to the mock database. The test then asserts that the vote has been rolled back (i.e., the vote count in the database is zero). The test fails because this assertion is not met, indicating that the vote remains in the database despite the subsequent error. This reveals a violation of the ACID atomicity guarantee required by AL3.5. The `xfail` marker ensures this known issue is documented within the test suite itself without failing the entire build.

**Test Case Example (Documents a Known Bug):**
```python
# From: tests/test_recorder.py

@pytest.mark.xfail(
    reason="BUG: Transactional rollback is not working correctly.", strict=True
)
def test_submit_vote_rolls_back_on_downstream_error(self):
    """
    Verify that if a downstream operation like consensus calculation fails,
    the vote creation is rolled back, ensuring atomicity.
    """
    # Arrange: Mock the consensus calculator to fail.
    error_message = "Consensus calculation failed!"
    # Refactor to avoid long line issue.
    calc_consensus_spec = create_autospec(
        self.consensus_calculator.calculate_consensus,
        side_effect=ValueError(error_message),
    )
    self.consensus_calculator.calculate_consensus = calc_consensus_spec

    # ... (re-initialize recorder) ...

    # Act & Assert: The exception from the mocked calculator should propagate
    with self.assertRaisesRegex(ValueError, error_message):
        self.vote_recorder.submit_vote(...)

    # CRITICAL: Assert that no vote was persisted in the DAL.
    # This confirms the rollback behavior of the transaction.
    # THIS ASSERTION CURRENTLY FAILS, HENCE THE XFAIL.
    self.assertEqual(len(self.mock_dal._votes), 0)
```

---
### AL4. Consensus Determination Engine (The `ConsensusCalculator`)

#### **AL4.1-AL4.4: Combined Consensus Evaluation, Rule Implementation, and Status Update**

> **Requirement Statements:**
> *   **AL4.1 Real-Time Evaluation:** Consensus status must be re-evaluated upon:
>     *   AL4.1.1 Every successful vote transaction (triggered by AL3.5).
>     *   AL4.1.2 Any change to the Adjudicator Roster (triggered by AL7.3).
> *   **AL4.2 CRITICAL: Unanimity Rule Implementation (Protocol C.3):** A concept is included ONLY IF 100% of the *active* Adjudicator Roster (AL1.4) have submitted an active "Include" vote.
> *   **AL4.3 Dynamic Required Voter Count:** The engine must use the current count of the active `AdjudicatorRoster` (AL1.4) to determine the threshold for unanimity.
> *   **AL4.4 Consensus Status Update:** If consensus is reached, update the `ConceptStatus`.
>     *   AL4.4.1 Optimization: If an "Exclude" vote is received, the status can immediately be set to `CONSENSUS_EXCLUDE`.

**Implementation Mapping:**
*   **Calculator Module:** `src/codeeval_adjudication_engine/consensus.py`
    *   **Class:** `ConsensusCalculator`
    *   **Method:** `calculate_consensus(...)`
*   **Trigger Modules (AL4.1):**
    *   `src/codeeval_adjudication_engine/recorder.py` (`VoteRecorder.submit_vote`)
    *   `src/codeeval_adjudication_engine/overrides.py` (`OverrideManager.recalculate_consensus_for_idea`)

**Detailed Explanation:**
The consensus logic is split between the calculator and the triggers, adhering to the Single Responsibility Principle.

**Calculation (AL4.2, AL4.3, AL4.4):**
The `ConsensusCalculator.calculate_consensus` method is the core implementation of the Unanimity Rule.
1.  **Dynamic Roster (AL4.3):** It first determines the set of `active_adjudicator_ids` by filtering the `active_roster` passed into it. This ensures the voter threshold is dynamically calculated on every call.
2.  **Exclude Optimization (AL4.4.1):** It immediately checks for any "Exclude" vote from an active adjudicator. If one is found, it instantly returns `CONSENSUS_EXCLUDE`, short-circuiting further checks as unanimity is impossible.
3.  **Unanimity Rule (AL4.2):** If no "Exclude" votes are found, it compiles a set of all users who voted "Include". It then performs a strict equality check (`==`) between the set of "Include" voters and the set of active adjudicators. Only if these sets are identical is `CONSENSUS_INCLUDE` returned. Otherwise, the status remains `PENDING`.

**Real-Time Evaluation Triggers (AL4.1):**
The `calculate_consensus` method is not self-triggering. It is explicitly called by:
*   The `VoteRecorder` at the end of a successful `submit_vote` transaction (fulfilling AL4.1.1).
*   The `OverrideManager` after the adjudicator roster is modified (fulfilling AL4.1.2).

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/consensus.py

class ConsensusCalculator:
    def calculate_consensus(
        self,
        concept_id: int,
        all_votes: List[AdjudicationVote],
        active_roster: List[AdjudicatorRoster],
    ) -> ConceptConsensusStatus:
        # AL4.3: Dynamically determine the required set of voters
        active_adjudicator_ids: Set[str] = {
            roster_member.user_id
            for roster_member in active_roster
            if roster_member.is_active
        }
        if not active_adjudicator_ids:
            return ConceptConsensusStatus.PENDING

        active_votes_for_concept = [ ... ] # Filter for relevant votes

        # AL4.4.1: Optimization for "Exclude"
        for vote in active_votes_for_concept:
            if (
                vote.user_id in active_adjudicator_ids
                and vote.decision == VoteDecision.EXCLUDE
            ):
                return ConceptConsensusStatus.CONSENSUS_EXCLUDE

        # AL4.2: Check for Unanimity "Include"
        include_voter_ids: Set[str] = {
            vote.user_id
            for vote in active_votes_for_concept
            if vote.decision == VoteDecision.INCLUDE
        }
        if include_voter_ids == active_adjudicator_ids:
            return ConceptConsensusStatus.CONSENSUS_INCLUDE

        return ConceptConsensusStatus.PENDING
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al4.py
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.models import AdjudicatorRoster, AdjudicationVote, VoteDecision, ConceptConsensusStatus
from datetime import datetime, timezone

# Helper to create a mock vote with a timestamp
def make_vote(user_id, decision):
    return AdjudicationVote(user_id, 101, decision, timestamp=datetime.now(timezone.utc))

# 1. Instantiate the calculator
calculator = ConsensusCalculator()
concept_id = 101

# 2. Define a scenario: 2 active adjudicators, 1 inactive
active_roster = [
    AdjudicatorRoster("user1", is_active=True),
    AdjudicatorRoster("user2", is_active=True),
    AdjudicatorRoster("user3", is_active=False),
]

# 3. Scenario 1: Pending (one vote missing)
votes1 = [make_vote("user1", VoteDecision.INCLUDE)]
status1 = calculator.calculate_consensus(concept_id, votes1, active_roster)
print(f"Scenario 1 (1/2 'Include' votes): {status1.name}")

# 4. Scenario 2: Consensus Include (unanimity reached)
votes2 = [
    make_vote("user1", VoteDecision.INCLUDE),
    make_vote("user2", VoteDecision.INCLUDE),
]
status2 = calculator.calculate_consensus(concept_id, votes2, active_roster)
print(f"Scenario 2 (2/2 'Include' votes): {status2.name}")

# 5. Scenario 3: Consensus Exclude (one 'Exclude' vote)
votes3 = [
    make_vote("user1", VoteDecision.INCLUDE),
    make_vote("user2", VoteDecision.EXCLUDE),
]
status3 = calculator.calculate_consensus(concept_id, votes3, active_roster)
print(f"Scenario 3 (1 'Include', 1 'Exclude'): {status3.name}")

# 6. Scenario 4: Pending (inactive user's vote is ignored)
votes4 = [
    make_vote("user1", VoteDecision.INCLUDE),
    make_vote("user3", VoteDecision.INCLUDE), # Inactive vote
]
status4 = calculator.calculate_consensus(concept_id, votes4, active_roster)
print(f"Scenario 4 (1 active 'Include', 1 inactive 'Include'): {status4.name}")

# Expected Output:
# Scenario 1 (1/2 'Include' votes): PENDING
# Scenario 2 (2/2 'Include' votes): CONSENSUS_INCLUDE
# Scenario 3 (1 'Include', 1 'Exclude'): CONSENSUS_EXCLUDE
# Scenario 4 (1 active 'Include', 1 inactive 'Include'): PENDING
```

**Test Case Example:**
```python
# test_case_al4.py
import pytest
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.models import AdjudicatorRoster, AdjudicationVote, VoteDecision, ConceptConsensusStatus

@pytest.fixture
def calculator():
    return ConsensusCalculator()

# Helper to create vote objects
def make_vote(user_id, decision):
    return AdjudicationVote(user_id, 1, decision, "2023-01-01T12:00:00Z")

def test_unanimity_include(calculator):
    """Tests that consensus is INCLUDE when all active adjudicators vote Include. (AL4.2)"""
    roster = [AdjudicatorRoster("u1", True), AdjudicatorRoster("u2", True)]
    votes = [make_vote("u1", VoteDecision.INCLUDE), make_vote("u2", VoteDecision.INCLUDE)]
    status = calculator.calculate_consensus(1, votes, roster)
    assert status == ConceptConsensusStatus.CONSENSUS_INCLUDE

def test_one_exclude_vote_causes_exclude_consensus(calculator):
    """Tests that a single Exclude vote from an active user results in EXCLUDE consensus. (AL4.4.1)"""
    roster = [AdjudicatorRoster("u1", True), AdjudicatorRoster("u2", True)]
    votes = [make_vote("u1", VoteDecision.INCLUDE), make_vote("u2", VoteDecision.EXCLUDE)]
    status = calculator.calculate_consensus(1, votes, roster)
    assert status == ConceptConsensusStatus.CONSENSUS_EXCLUDE

def test_pending_status_if_not_all_votes_are_in(calculator):
    """Tests that status is PENDING if not all active adjudicators have voted."""
    roster = [AdjudicatorRoster("u1", True), AdjudicatorRoster("u2", True)]
    votes = [make_vote("u1", VoteDecision.INCLUDE)]
    status = calculator.calculate_consensus(1, votes, roster)
    assert status == ConceptConsensusStatus.PENDING

def test_dynamic_roster_is_respected(calculator):
    """Tests that an inactive adjudicator's vote does not count. (AL4.3)"""
    # u2 is inactive, so their vote should be ignored. Unanimity among active
    # adjudicators (just u1) should result in CONSENSUS_INCLUDE.
    roster = [AdjudicatorRoster("u1", True), AdjudicatorRoster("u2", False)]
    votes = [make_vote("u1", VoteDecision.INCLUDE), make_vote("u2", VoteDecision.INCLUDE)]
    status = calculator.calculate_consensus(1, votes, roster)
    assert status == ConceptConsensusStatus.CONSENSUS_INCLUDE
```

---
### AL5. True Gold Standard (TGS) Construction (The `TGSFactory`)

#### **AL5.1-AL5.4: Combined TGS Finalization, Assembly, Persistence, and Notification**

> **Requirement Statements:**
> *   **AL5.1 TGS Finalization Trigger:** The TGS is finalized when 100% of the concepts in the Delta have a consensus state (not `PENDING`).
> *   **AL5.2 TGS Assembly (BRD F4.2):** TGS = Intersection + (Delta concepts where Status = `CONSENSUS_INCLUDE`).
> *   **AL5.3 TGS Persistence and State Locking:** Persist the `TGS_Definition` and set `ClinicalIdeaStatus` to `FINALIZED`.
> *   **AL5.4 Downstream Notification:** Signal the `sap_engine` that the TGS is ready.

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/tgs_factory.py`
*   **Class:** `TGSFactory`
*   **Method:** `check_and_finalize(self, clinical_idea_id: int) -> None`

**Detailed Explanation:**
The `check_and_finalize` method in the `TGSFactory` orchestrates the entire finalization process. It is designed to be called within a transaction by upstream modules like `VoteRecorder` or `OverrideManager`.
1.  **Finalization Trigger (AL5.1):** The method first fetches the status of all concepts for the clinical idea. It then evaluates the trigger condition by checking if `all()` concepts have a status other than `PENDING`. If this condition is not met, the method exits early.
2.  **TGS Assembly (AL5.2):** If the trigger condition is met, it proceeds to assemble the TGS. It fetches two sets of data from the DAL: the baseline "Intersection" concepts and the list of "Delta" concepts that achieved `CONSENSUS_INCLUDE` status. It combines these two lists and uses a `set` to ensure uniqueness before sorting the final list of concept IDs.
3.  **Persistence and State Locking (AL5.3):** The newly created `TGS_Definition` object is passed to `self._dal.save_tgs()` for persistence. Immediately after, it calls the `WorkflowManager` to update the clinical idea's status to `FINALIZED`. This transition acts as a lock, preventing any further votes or roster changes, as enforced by the `WorkflowManager` and `VoteRecorder`.
4.  **Auditing and Notification (AL5.4):** Before persisting, it logs the finalization event and the complete TGS definition using the `AuditLogger`. After successful persistence, it calls `self._notifier.notify_tgs_ready(clinical_idea_id)` to signal to downstream systems (like the `sap_engine`) that the TGS is complete and ready for consumption.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/tgs_factory.py

def check_and_finalize(self, clinical_idea_id: int) -> None:
    # ...
    concept_statuses = self._dal.get_all_concept_statuses(clinical_idea_id)

    # AL5.1: Check if all concepts have moved out of the PENDING state.
    all_concepts_resolved = all(
        status.status != ConceptConsensusStatus.PENDING for status in concept_statuses
    )

    if all_concepts_resolved:
        # AL5.2: TGS Assembly
        intersection_ids = self._dal.get_intersection_concepts(clinical_idea_id)
        delta_include_ids = [
            status.concept_id
            for status in concept_statuses
            if status.status == ConceptConsensusStatus.CONSENSUS_INCLUDE
        ]
        final_tgs_ids = sorted(list(set(intersection_ids + delta_include_ids)))
        tgs_definition = TGS_Definition(
            clinical_idea_id=clinical_idea_id,
            concept_ids=final_tgs_ids,
        )

        # ... (Auditing) ...

        # AL5.3: TGS Persistence and State Locking
        self._dal.save_tgs(tgs_definition)
        self._workflow_manager.update_clinical_idea_status(
            clinical_idea_id, ClinicalIdeaStatus.FINALIZED
        )

        # AL5.4: Downstream Notification
        self._notifier.notify_tgs_ready(clinical_idea_id)
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al5.py
from unittest.mock import MagicMock, call
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.models import ConceptStatus, ConceptConsensusStatus, ClinicalIdeaStatus, TGS_Definition
from codeeval_adjudication_engine.interfaces import DataAccessLayer, TGSFinalizationNotifier, AuditLogger
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

# 1. Set up all mock dependencies
mock_dal = MagicMock(spec=DataAccessLayer)
mock_notifier = MagicMock(spec=TGSFinalizationNotifier)
mock_audit = MagicMock(spec=AuditLogger)
mock_workflow = MagicMock(spec=WorkflowManager)
factory = TGSFactory(mock_dal, mock_notifier, mock_audit, mock_workflow)
idea_id = 1

# 2. Scenario 1: Not all concepts are resolved
print("Scenario 1: Finalization check when concepts are still PENDING.")
mock_dal.get_all_concept_statuses.return_value = [
    ConceptStatus(1, ConceptConsensusStatus.CONSENSUS_INCLUDE),
    ConceptStatus(2, ConceptConsensusStatus.PENDING), # Not resolved
]
factory.check_and_finalize(idea_id)
mock_dal.save_tgs.assert_not_called()
print("  - Result: TGS not finalized, as expected.\n")

# 3. Scenario 2: All concepts are resolved, finalization proceeds
print("Scenario 2: Finalization check when all concepts are resolved.")
mock_dal.reset_mock()
mock_dal.get_all_concept_statuses.return_value = [
    ConceptStatus(10, ConceptConsensusStatus.CONSENSUS_INCLUDE),
    ConceptStatus(11, ConceptConsensusStatus.CONSENSUS_EXCLUDE),
    ConceptStatus(12, ConceptConsensusStatus.CONSENSUS_INCLUDE),
]
mock_dal.get_intersection_concepts.return_value = [5, 10] # 10 is a duplicate

factory.check_and_finalize(idea_id)

# 4. Verify the entire finalization workflow
# TGS Assembly (AL5.2)
final_tgs_ids = [5, 10, 12]
expected_tgs_def = TGS_Definition(idea_id, final_tgs_ids)
mock_dal.save_tgs.assert_called_once_with(expected_tgs_def)
print(f"  - TGS Assembled with correct concepts: {final_tgs_ids}")

# Auditing
mock_audit.log_tgs_finalization.assert_called_once_with(
    clinical_idea_id=idea_id, final_tgs_concept_ids=final_tgs_ids
)
print("  - Finalization was correctly audited.")

# State Locking (AL5.3)
mock_workflow.update_clinical_idea_status.assert_called_once_with(idea_id, ClinicalIdeaStatus.FINALIZED)
print("  - Clinical Idea status was set to FINALIZED.")

# Notification (AL5.4)
mock_notifier.notify_tgs_ready.assert_called_once_with(idea_id)
print("  - Downstream systems were notified.")

# Expected Output:
# Scenario 1: Finalization check when concepts are still PENDING.
#   - Result: TGS not finalized, as expected.
#
# Scenario 2: Finalization check when all concepts are resolved.
#   - TGS Assembled with correct concepts: [5, 10, 12]
#   - Finalization was correctly audited.
#   - Clinical Idea status was set to FINALIZED.
#   - Downstream systems were notified.
```

**Test Case Example:**
```python
# test_case_al5.py
import pytest
from unittest.mock import MagicMock
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.models import ConceptStatus, ConceptConsensusStatus, TGS_Definition, ClinicalIdeaStatus
from codeeval_adjudication_engine.interfaces import DataAccessLayer, TGSFinalizationNotifier, AuditLogger
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

@pytest.fixture
def factory_components():
    return {
        "dal": MagicMock(spec=DataAccessLayer),
        "notifier": MagicMock(spec=TGSFinalizationNotifier),
        "audit_logger": MagicMock(spec=AuditLogger),
        "workflow_manager": MagicMock(spec=WorkflowManager),
    }

def test_finalization_is_skipped_if_concepts_are_pending(factory_components):
    """Tests that finalization does not occur if any concept is PENDING. (AL5.1)"""
    factory = TGSFactory(**factory_components)
    dal = factory_components['dal']
    dal.get_all_concept_statuses.return_value = [ConceptStatus(1, ConceptConsensusStatus.PENDING)]

    factory.check_and_finalize(1)

    dal.save_tgs.assert_not_called()
    factory_components['notifier'].notify_tgs_ready.assert_not_called()

def test_finalization_proceeds_when_all_concepts_are_resolved(factory_components):
    """Tests that finalization occurs when all concepts are resolved. (AL5.1)"""
    factory = TGSFactory(**factory_components)
    dal = factory_components['dal']
    dal.get_all_concept_statuses.return_value = [
        ConceptStatus(1, ConceptConsensusStatus.CONSENSUS_INCLUDE),
        ConceptStatus(2, ConceptConsensusStatus.CONSENSUS_EXCLUDE),
    ]
    dal.get_intersection_concepts.return_value = [] # Simplify test

    factory.check_and_finalize(1)

    dal.save_tgs.assert_called_once()
    factory_components['notifier'].notify_tgs_ready.assert_called_once()

def test_tgs_assembly_is_correct(factory_components):
    """Tests that TGS assembly correctly combines intersection and delta. (AL5.2)"""
    factory = TGSFactory(**factory_components)
    dal = factory_components['dal']
    dal.get_all_concept_statuses.return_value = [
        ConceptStatus(1, ConceptConsensusStatus.CONSENSUS_INCLUDE),
        ConceptStatus(2, ConceptConsensusStatus.CONSENSUS_EXCLUDE),
        ConceptStatus(3, ConceptConsensusStatus.CONSENSUS_INCLUDE),
    ]
    dal.get_intersection_concepts.return_value = [0, 3] # 3 is duplicate

    factory.check_and_finalize(1)

    expected_tgs = TGS_Definition(clinical_idea_id=1, concept_ids=[0, 1, 3])
    dal.save_tgs.assert_called_once_with(expected_tgs)
```

---
### AL6. Progress Tracking and Monitoring

#### **AL6.1 Adjudicator Progress (BRD F3.5)**

> **Requirement Statement:** Provide metrics for individual Adjudicators (X of Y reviewed).

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/tracker.py`
*   **Class:** `ProgressTracker`
*   **Method:** `get_individual_progress(self, clinical_idea_id: int, user_id: str) -> IndividualProgress`

**Detailed Explanation:**
This requirement is met by the `get_individual_progress` method. It calculates an adjudicator's personal progress by fetching two pieces of data from the DAL: the list of all votes cast by that specific `user_id` for the given `clinical_idea_id`, and the total list of all concepts associated with that idea. The progress metric is then constructed by taking the `len()` of the user's votes (the "X" value, or `reviewed_count`) and the `len()` of the total concepts (the "Y" value, or `total_count`). This data is returned in a structured `IndividualProgress` object.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/tracker.py

def get_individual_progress(
    self, clinical_idea_id: int, user_id: str
) -> IndividualProgress:
    """
    Provides metrics for an individual adjudicator's progress.
    FRD AL6.1
    ...
    """
    user_votes = self._dal.get_votes_by_user(clinical_idea_id, user_id)
    all_concepts = self._dal.get_all_concepts_for_idea(clinical_idea_id)

    return IndividualProgress(
        reviewed_count=len(user_votes), total_count=len(all_concepts)
    )
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al6_1.py
from unittest.mock import MagicMock
from codeeval_adjudication_engine.tracker import ProgressTracker
from codeeval_adjudication_engine.interfaces import DataAccessLayer
from codeeval_adjudication_engine.models import AdjudicationVote, Concept, VoteDecision
from datetime import datetime, timezone

# 1. Set up mock DAL and ProgressTracker
mock_dal = MagicMock(spec=DataAccessLayer)
tracker = ProgressTracker(dal=mock_dal)
idea_id, user_id = 1, "user_test"

# 2. Mock the DAL return values
# User has voted on 2 concepts
mock_dal.get_votes_by_user.return_value = [
    AdjudicationVote(user_id, 101, VoteDecision.INCLUDE, timestamp=datetime.now(timezone.utc)),
    AdjudicationVote(user_id, 102, VoteDecision.EXCLUDE, timestamp=datetime.now(timezone.utc)),
]
# There are 5 total concepts in the idea
mock_dal.get_all_concepts_for_idea.return_value = [
    Concept(101, "c1", "d1", 1, []),
    Concept(102, "c2", "d2", 1, []),
    Concept(103, "c3", "d3", 1, []),
    Concept(104, "c4", "d4", 1, []),
    Concept(105, "c5", "d5", 1, []),
]

# 3. Get the individual progress
progress = tracker.get_individual_progress(idea_id, user_id)

# 4. Print the result
print(f"User '{user_id}' Progress:")
print(f"  - Reviewed: {progress.reviewed_count}")
print(f"  - Total: {progress.total_count}")
print(f"  - Display: {progress.reviewed_count} of {progress.total_count} reviewed")

# Expected Output:
# User 'user_test' Progress:
#   - Reviewed: 2
#   - Total: 5
#   - Display: 2 of 5 reviewed
```

**Test Case Example:**
```python
# test_case_al6_1.py
import pytest
from unittest.mock import MagicMock
from codeeval_adjudication_engine.tracker import ProgressTracker
from codeeval_adjudication_engine.interfaces import DataAccessLayer
from codeeval_adjudication_engine.models import IndividualProgress

@pytest.fixture
def tracker_al6_1():
    mock_dal = MagicMock(spec=DataAccessLayer)
    tracker = ProgressTracker(dal=mock_dal)
    return tracker, mock_dal

def test_get_individual_progress(tracker_al6_1):
    """
    Tests the calculation of individual progress metrics.
    """
    tracker, mock_dal = tracker_al6_1
    idea_id, user_id = 1, "test_user"

    # Arrange: Mock DAL to return 3 votes for the user and 10 total concepts
    mock_dal.get_votes_by_user.return_value = [MagicMock()] * 3
    mock_dal.get_all_concepts_for_idea.return_value = [MagicMock()] * 10

    # Act
    progress = tracker.get_individual_progress(idea_id, user_id)

    # Assert
    assert isinstance(progress, IndividualProgress)
    assert progress.reviewed_count == 3
    assert progress.total_count == 10
    mock_dal.get_votes_by_user.assert_called_once_with(idea_id, user_id)
    mock_dal.get_all_concepts_for_idea.assert_called_once_with(idea_id)
```

---
#### **AL6.2 Session Lead Dashboard Metrics (BRD F5.1)**

> **Requirement Statement:** Provide aggregated metrics (Overall progress, Status per Clinical Idea).

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/tracker.py`
*   **Class:** `ProgressTracker`
*   **Method:** `get_aggregated_dashboard_metrics(self, clinical_idea_id: int) -> AggregatedProgress`

**Detailed Explanation:**
This requirement is fulfilled by the `get_aggregated_dashboard_metrics` method. It compiles a high-level summary of a clinical idea's progress. First, it fetches the consensus status for every concept within the idea from the DAL. It uses `collections.Counter` to efficiently tally the number of concepts in each status category (`PENDING`, `CONSENSUS_INCLUDE`, `CONSENSUS_EXCLUDE`). It then calculates the overall progress percentage by dividing the number of resolved concepts (Include + Exclude) by the total number of concepts. All of this information is packaged into the `AggregatedProgress` data model for use in a dashboard.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/tracker.py

def get_aggregated_dashboard_metrics(
    self, clinical_idea_id: int
) -> AggregatedProgress:
    """
    Provides aggregated metrics for a Session Lead's dashboard.
    FRD AL6.2
    ...
    """
    concept_statuses = self._dal.get_all_concept_statuses(clinical_idea_id)
    all_concepts = self._dal.get_all_concepts_for_idea(clinical_idea_id)

    status_counts = Counter(cs.status for cs in concept_statuses)

    total_concepts = len(all_concepts)
    include_count = status_counts[ConceptConsensusStatus.CONSENSUS_INCLUDE]
    exclude_count = status_counts[ConceptConsensusStatus.CONSENSUS_EXCLUDE]

    completed_count = include_count + exclude_count
    progress_percentage = (
        (completed_count / total_concepts) * 100.0 if total_concepts > 0 else 0.0
    )

    return AggregatedProgress(
        total_concepts=total_concepts,
        pending_count=status_counts[ConceptConsensusStatus.PENDING],
        consensus_include_count=include_count,
        consensus_exclude_count=exclude_count,
        overall_progress_percentage=progress_percentage,
    )
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al6_2.py
from unittest.mock import MagicMock
from collections import Counter
from codeeval_adjudication_engine.tracker import ProgressTracker
from codeeval_adjudication_engine.interfaces import DataAccessLayer
from codeeval_adjudication_engine.models import Concept, ConceptStatus, ConceptConsensusStatus

# 1. Set up mock DAL and ProgressTracker
mock_dal = MagicMock(spec=DataAccessLayer)
tracker = ProgressTracker(dal=mock_dal)
idea_id = 1

# 2. Mock the DAL return values for a scenario
# Total of 10 concepts
mock_dal.get_all_concepts_for_idea.return_value = [MagicMock()] * 10
# Status breakdown: 5 PENDING, 3 INCLUDE, 2 EXCLUDE
mock_dal.get_all_concept_statuses.return_value = (
    [ConceptStatus(1, ConceptConsensusStatus.PENDING)] * 5 +
    [ConceptStatus(2, ConceptConsensusStatus.CONSENSUS_INCLUDE)] * 3 +
    [ConceptStatus(3, ConceptConsensusStatus.CONSENSUS_EXCLUDE)] * 2
)

# 3. Get the aggregated metrics
metrics = tracker.get_aggregated_dashboard_metrics(idea_id)

# 4. Print the results
print(f"Aggregated Metrics for Clinical Idea {idea_id}:")
print(f"  - Total Concepts: {metrics.total_concepts}")
print(f"  - Pending: {metrics.pending_count}")
print(f"  - Consensus Include: {metrics.consensus_include_count}")
print(f"  - Consensus Exclude: {metrics.consensus_exclude_count}")
print(f"  - Overall Progress: {metrics.overall_progress_percentage:.1f}%")

# Expected Output:
# Aggregated Metrics for Clinical Idea 1:
#   - Total Concepts: 10
#   - Pending: 5
#   - Consensus Include: 3
#   - Consensus Exclude: 2
#   - Overall Progress: 50.0%
```

**Test Case Example:**
```python
# test_case_al6_2.py
import pytest
from unittest.mock import MagicMock
from codeeval_adjudication_engine.tracker import ProgressTracker
from codeeval_adjudication_engine.interfaces import DataAccessLayer
from codeeval_adjudication_engine.models import AggregatedProgress, ConceptStatus, ConceptConsensusStatus

@pytest.fixture
def tracker_al6_2():
    mock_dal = MagicMock(spec=DataAccessLayer)
    tracker = ProgressTracker(dal=mock_dal)
    return tracker, mock_dal

def test_get_aggregated_metrics(tracker_al6_2):
    """
    Tests the calculation of aggregated dashboard metrics.
    """
    tracker, mock_dal = tracker_al6_2
    idea_id = 1

    # Arrange: 20 total concepts. 10 PENDING, 8 INCLUDE, 2 EXCLUDE.
    mock_dal.get_all_concepts_for_idea.return_value = [MagicMock()] * 20
    mock_dal.get_all_concept_statuses.return_value = (
        [ConceptStatus(1, ConceptConsensusStatus.PENDING)] * 10 +
        [ConceptStatus(2, ConceptConsensusStatus.CONSENSUS_INCLUDE)] * 8 +
        [ConceptStatus(3, ConceptConsensusStatus.CONSENSUS_EXCLUDE)] * 2
    )

    # Act
    metrics = tracker.get_aggregated_dashboard_metrics(idea_id)

    # Assert
    assert isinstance(metrics, AggregatedProgress)
    assert metrics.total_concepts == 20
    assert metrics.pending_count == 10
    assert metrics.consensus_include_count == 8
    assert metrics.consensus_exclude_count == 2
    # (8 + 2) / 20 = 0.5 * 100 = 50.0
    assert metrics.overall_progress_percentage == 50.0

def test_get_aggregated_metrics_no_concepts(tracker_al6_2):
    """
    Tests the edge case where a clinical idea has no concepts.
    """
    tracker, mock_dal = tracker_al6_2
    idea_id = 2

    # Arrange: Zero concepts
    mock_dal.get_all_concepts_for_idea.return_value = []
    mock_dal.get_all_concept_statuses.return_value = []

    # Act
    metrics = tracker.get_aggregated_dashboard_metrics(idea_id)

    # Assert
    assert metrics.total_concepts == 0
    assert metrics.pending_count == 0
    assert metrics.overall_progress_percentage == 0.0
```

---
### AL7. Operational Override Module (The `OverrideManager`)

#### **AL7.1-AL7.6: Combined Roster Modification, Validation, Recalculation, and Auditing**

> **Requirement Statements:**
> *   **AL7.1 Adjudicator Roster Modification Interface:** Provide a function to allow removal/replacement of an Adjudicator.
> *   **AL7.2 Authorization and Validation:** Strictly for "Session Lead" role; must verify Clinical Idea is not `FINALIZED`.
> *   **AL7.3 CRITICAL: Immediate Consensus Recalculation Trigger:** Upon successful modification...re-evaluate the consensus status for all non-finalized concepts.
> *   **AL7.4 Vote Invalidation:** If an Adjudicator is removed/deactivated, their active votes must be logically invalidated.
> *   **AL7.5 Transaction Integrity:** The override process must be executed within a robust transaction boundary, utilizing appropriate locking.
> *   **AL7.6 Auditing:** All override actions must be rigorously audited.

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/overrides.py`
*   **Class:** `OverrideManager`
*   **Method:** `modify_adjudicator_roster(...)`

**Detailed Explanation:**
The `modify_adjudicator_roster` method is a critical transactional function that holistically implements all operational override requirements.
1.  **Authorization and Validation (AL7.2):** The method first performs crucial upfront checks. It verifies that the `current_user_context` contains the "Session Lead" role, raising an `AuthorizationError` if not. It then checks if the clinical idea is already `FINALIZED`, raising an `InvalidStateError` to prevent changes to a locked-down idea.
2.  **Auditing (AL7.6):** It immediately logs the override action by calling `self._audit_logger.log_override_action`, recording who made the change, who was affected, and what the action was.
3.  **Transaction and Locking (AL7.5):** The core logic is wrapped in a `with self._dal.transaction():` block. The first step inside the transaction is to call `get_all_concept_statuses_for_update`, which acquires a pessimistic lock on *all concept status rows* for the clinical idea. This is a crucial step to prevent any concurrent votes from interfering while the full recalculation is in progress.
4.  **Roster Modification and Vote Invalidation (AL7.1, AL7.4):** The method delegates the actual roster change to the `WorkflowManager`'s `modify_roster` method. As established in AL1.4, this centralized method handles both updating the adjudicator's active status and, critically, invalidating all of their existing votes if they are being deactivated.
5.  **Full Consensus Recalculation (AL7.3):** After the roster is updated, the method fetches the new roster and all votes for the idea. It then iterates through every concept that was locked at the beginning of the transaction, calling the `ConsensusCalculator` for each one to determine its new status based on the modified roster. If the status changes, it's updated in the DAL.
6.  **Finalization Check:** Finally, it calls `self._tgs_factory.check_and_finalize` to determine if the roster change has resulted in the clinical idea becoming fully resolved, potentially finalizing the TGS.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/overrides.py

def modify_adjudicator_roster(
    self,
    clinical_idea_id: int,
    user_id_to_modify: str,
    new_active_status: bool,
    current_user_context: UserContext,
) -> None:
    # AL7.2: Authorization and Validation
    if "Session Lead" not in current_user_context.roles:
        raise AuthorizationError("Only 'Session Lead' role can modify the roster.")
    # ... validation for FINALIZED status ...

    # AL7.6: Auditing
    self._audit_logger.log_override_action(...)

    # AL7.5: Transactional Execution
    with self._dal.transaction():
        # Lock all concepts for the idea
        concept_statuses = self._dal.get_all_concept_statuses_for_update(
            clinical_idea_id
        )

        # AL7.1 & AL7.4: Roster Update and Vote Invalidation (delegated)
        self._workflow_manager.modify_roster(
            clinical_idea_id, user_id_to_modify, new_active_status
        )

        # AL7.3: Full Consensus Recalculation
        new_roster = self._workflow_manager.get_roster(clinical_idea_id)
        all_votes = self._dal.get_all_votes(clinical_idea_id)
        for concept_status in concept_statuses:
            new_consensus = self._consensus_calculator.calculate_consensus(...)
            self._dal.update_concept_status(...)

        self._tgs_factory.check_and_finalize(clinical_idea_id)
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_al7.py
from unittest.mock import MagicMock, call
from codeeval_adjudication_engine.overrides import OverrideManager
from codeeval_adjudication_engine.models import UserContext, AuthorizationError
# Import all dependencies for instantiation
from codeeval_adjudication_engine.interfaces import DataAccessLayer, AuditLogger
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

# 1. Setup all mock dependencies
mock_dal = MagicMock(spec=DataAccessLayer)
mock_consensus = MagicMock(spec=ConsensusCalculator)
mock_tgs = MagicMock(spec=TGSFactory)
mock_audit = MagicMock(spec=AuditLogger)
mock_workflow = MagicMock(spec=WorkflowManager)
manager = OverrideManager(mock_dal, mock_consensus, mock_tgs, mock_audit, mock_workflow)

# 2. Define contexts and scenario parameters
lead_context = UserContext("lead1", 0, ["Session Lead"])
regular_user_context = UserContext("user1", 0, ["Adjudicator"])
idea_id = 1
user_to_deactivate = "adj2"

# 3. Scenario 1: Unauthorized user attempts override
print("Scenario 1: Unauthorized user attempts modification.")
try:
    manager.modify_adjudicator_roster(idea_id, user_to_deactivate, False, regular_user_context)
except AuthorizationError as e:
    print(f"  - Failed as expected: {e}\n")

# 4. Scenario 2: Authorized user performs deactivation
print("Scenario 2: Authorized Session Lead deactivates an adjudicator.")
# Mock DAL/Manager returns for the sequence of events
mock_dal.get_clinical_idea_status.return_value = "IN_PROGRESS"
mock_dal.get_all_concept_statuses_for_update.return_value = [MagicMock()] * 5 # 5 concepts

manager.modify_adjudicator_roster(idea_id, user_to_deactivate, False, lead_context)
print("  - Roster modification successful.")

# 5. Verify the sequence of calls
print("\nVerifying execution flow:")
# Auditing (AL7.6)
mock_audit.log_override_action.assert_called_once()
print("  - Override was audited.")
# Transactional Locking (AL7.5)
mock_dal.get_all_concept_statuses_for_update.assert_called_once_with(idea_id)
print("  - All concepts were locked for update.")
# Roster modification and vote invalidation (AL7.1, AL7.4)
mock_workflow.modify_roster.assert_called_once_with(idea_id, user_to_deactivate, False)
print("  - WorkflowManager was called to modify roster and invalidate votes.")
# Full recalculation (AL7.3)
assert mock_consensus.calculate_consensus.call_count == 5
print("  - Consensus was recalculated for all 5 concepts.")
# Finalization check
mock_tgs.check_and_finalize.assert_called_once_with(idea_id)
print("  - TGS finalization was checked.")

# Expected Output:
# Scenario 1: Unauthorized user attempts modification.
#   - Failed as expected: Only 'Session Lead' role can modify the roster.
#
# Scenario 2: Authorized Session Lead deactivates an adjudicator.
#   - Roster modification successful.
#
# Verifying execution flow:
#   - Override was audited.
#   - All concepts were locked for update.
#   - WorkflowManager was called to modify roster and invalidate votes.
#   - Consensus was recalculated for all 5 concepts.
#   - TGS finalization was checked.
```

**Test Case Example:**
```python
# From: tests/test_overrides.py

def test_consensus_changes_after_deactivating_blocking_voter(
    session_lead_context,
    mock_dal,
    # ... other fixtures
):
    """
    A complex scenario showing that consensus is recalculated correctly when an
    adjudicator with a deciding 'Exclude' vote is removed. This verifies
    AL7.3 (Recalculation) and AL7.4 (Vote Invalidation) work together.
    """
    # Arrange:
    # - Roster has 3 active members, including 'adj_blocking'.
    # - 'adj_blocking' has cast an 'EXCLUDE' vote.
    # - The other 2 have cast 'INCLUDE' votes.
    # - The initial concept status is CONSENSUS_EXCLUDE.
    mock_dal._roster = [AdjudicatorRoster("adj_1"), AdjudicatorRoster("adj_blocking"), ...]
    mock_dal._votes = [
        AdjudicationVote("adj_1", 101, VoteDecision.INCLUDE, ...),
        AdjudicationVote("adj_blocking", 101, VoteDecision.EXCLUDE, ...),
        AdjudicationVote("adj_3", 101, VoteDecision.INCLUDE, ...),
    ]
    mock_dal._concept_statuses = {
        101: ConceptStatus(101, ConceptConsensusStatus.CONSENSUS_EXCLUDE)
    }
    # ... (full setup)
    manager = OverrideManager(...)

    # Act: Deactivate the adjudicator who cast the deciding 'Exclude' vote.
    manager.modify_adjudicator_roster(
        clinical_idea_id=1,
        user_id_to_modify="adj_blocking",
        new_active_status=False,
        current_user_context=session_lead_context
    )

    # Assert: The status should now flip to CONSENSUS_INCLUDE because the
    # 'Exclude' vote has been invalidated along with its voter, and the
    # remaining active voters are unanimously 'Include'.
    final_status = mock_dal._concept_statuses[101].status
    assert final_status == ConceptConsensusStatus.CONSENSUS_INCLUDE
```

---
## V. Non-Functional Requirements

### NFR-AL1. Security and Blinding Integrity (BRD NFR7)

> **Requirement Statement:** The data filtering logic (AL2.1) is security-critical. Comprehensive testing MUST validate that restricted fields are never included in the `BlindedConceptView`. Authorization for overrides (AL7.2) must be strictly enforced.

This critical requirement is addressed through two primary enforcement points: data-model-level blinding in the `DataPresenter` and role-based authorization in the `OverrideManager`.

---
#### **Data Blinding (AL2.1)**

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/presenter.py`
*   **Class:** `DataPresenter`
*   **Method:** `get_concepts_for_review`
*   **Data Model:** `BlindedConceptView`

**Detailed Explanation:**
The system guarantees blinding by transforming the full internal `Concept` data model into a sanitized `BlindedConceptView` before it is ever sent to a user. The `DataPresenter.get_concepts_for_review` method is responsible for this transformation. It fetches the complete `Concept` objects from the data layer, but then explicitly constructs new `BlindedConceptView` objects, which, by design, only have fields for `concept_id`, `name`, and `description`. This ensures that sensitive information like `agreement_level` and `contributing_arms` is physically absent from the data structure that leaves the backend, providing a robust and easily verifiable blinding mechanism.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/presenter.py

# ... inside get_concepts_for_review method ...
# AL2.1: Transform into the sanitized BlindedConceptView
blinded_concepts = [
    BlindedConceptView(
        concept_id=c.concept_id,
        name=c.name,
        description=c.description,
    )
    for c in concepts_copy
]
# ...
```

**Verifiable Examples:**
**Test Case Example:**
```python
# From: tests/test_presenter_data_blinding.py

def test_blinding_strips_sensitive_fields(
    sample_concepts_for_blinding: List[Concept],
):
    """
    CRITICAL (NFR-AL1, AL2.1.1): Verifies that the `get_concepts_for_review`
    method strictly removes the `agreement_level` and `contributing_arms`
    fields from the data sent to the user, ensuring compliance with the
    blinding protocol.
    """
    # ... (Arrange)
    presenter = DataPresenter(dal=mock_dal)

    result = presenter.get_concepts_for_review(clinical_idea_id, user_context)

    for concept_view in result.concepts_for_review:
        # CRITICAL: Verify sensitive fields are absent
        assert not hasattr(
            concept_view, "agreement_level"
        ), "Blinding failed: 'agreement_level' was exposed."
        assert not hasattr(
            concept_view, "contributing_arms"
        ), "Blinding failed: 'contributing_arms' were exposed."
```

---
#### **Override Authorization (AL7.2)**

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/overrides.py`
*   **Class:** `OverrideManager`
*   **Method:** `modify_adjudicator_roster`

**Detailed Explanation:**
The `OverrideManager.modify_adjudicator_roster` method, which performs a highly sensitive operation, is strictly protected by a role-based authorization check. The very first action in the method is to inspect the `UserContext` of the caller. It checks for the presence of the "Session Lead" role in the user's role list. If the role is not present, it immediately raises an `AuthorizationError`, preventing any further execution. This ensures that only explicitly authorized users can perform operational overrides.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/overrides.py

def modify_adjudicator_roster(...):
    # 1. Authorization and Validation (AL7.2)
    if "Session Lead" not in current_user_context.roles:
        raise AuthorizationError("Only 'Session Lead' role can modify the roster.")

    # ... (rest of the method)
```

**Verifiable Examples:**
**Test Case Example:**
```python
# From: tests/test_overrides.py

def test_authorization_failure(
    regular_user_context, # A fixture providing a user without the 'Session Lead' role
    ...
):
    """
    Tests that non-Session Leads cannot modify the roster.
    FRD AL7.2.1
    """
    manager = OverrideManager(...)

    with pytest.raises(AuthorizationError):
        manager.modify_adjudicator_roster(1, "user_1", False, regular_user_context)

    # Assert that no changes were made
    assert len(mock_audit_logger.logged_actions) == 0
    mock_workflow_manager.modify_roster.assert_not_called()
```
---
### NFR-AL2. Performance and Scalability (BRD NFR2/NFR3)

> **Requirement Statement:** Must support 50+ concurrent users. `SubmitVote` (AL3.1) and consensus calculation (AL4.1) latency must be < 1 second, despite the overhead of Pessimistic Locking.

**Implementation Mapping:**
*   **Vote Locking Strategy:** `src/codeeval_adjudication_engine/recorder.py` -> `get_concept_status_for_update`
*   **Override Locking Strategy:** `src/codeeval_adjudication_engine/overrides.py` -> `get_all_concept_statuses_for_update`
*   **Architecture:** Dependency Injection and stateless services.

**Detailed Explanation:**
The system is architected to meet the performance requirements through a combination of appropriate locking strategies and standard scalable design patterns.

1.  **Fine-Grained Locking for High-Frequency Operations:** The most common and performance-critical operation is `submit_vote`. The implementation intelligently minimizes lock contention by acquiring a pessimistic lock on only a single row: the specific `ConceptStatus` being voted on. This fine-grained locking strategy is highly performant and scalable, as it ensures that adjudicators voting on *different* concepts will not block each other, allowing for high concurrency.

2.  **Appropriate Lock Escalation for Low-Frequency Operations:** The `modify_adjudicator_roster` operation is an infrequent administrative task. The system correctly recognizes that this action requires a full recalculation of consensus and therefore escalates the lock to cover all concept statuses within the clinical idea. This is a sound architectural trade-off, prioritizing data consistency for a rare, sensitive operation while preserving high performance for the common path.

3.  **Stateless, Decoupled Services:** The business logic is encapsulated in stateless service classes (e.g., `VoteRecorder`, `DataPresenter`) that receive their dependencies via constructor injection. This is a fundamental design pattern for building scalable applications, as stateless services can be easily replicated and load-balanced.

**Code Implementation Snippet:**
This requirement is demonstrated by the *choice* of locking calls in different scenarios.

**Fine-Grained Lock for Voting:**
```python
# From: src/codeeval_adjudication_engine/recorder.py
# This locks only one concept's status row.
self._dal.get_concept_status_for_update(concept_id)
```

**Wide Lock for Overrides:**
```python
# From: src/codeeval_adjudication_engine/overrides.py
# This locks all concept status rows for the entire clinical idea.
concept_statuses = self._dal.get_all_concept_statuses_for_update(
    clinical_idea_id
)
```

**Verifiable Examples:**
Performance verification requires dedicated load testing, which is outside the scope of this static audit. However, the architectural choices can be verified by inspection and are aligned with industry best practices for building performant systems. A load testing script could be designed to simulate 50+ concurrent users calling the `submit_vote` method on a variety of concepts and measure the response times.

---
### NFR-AL3. CRITICAL: Reliability and Data Integrity (C4)

> **Requirement Statement:** The mandatory use of robust transaction management and Pessimistic Locking (AL3.5) is required to prevent race conditions and ensure the absolute integrity of the TGS.

This critical requirement is fulfilled by wrapping all state-modifying operations in both the `VoteRecorder` and `OverrideManager` within robust transactional boundaries that include explicit pessimistic locking. This ensures atomicity and protects against race conditions in high-concurrency environments.

---
#### **Transactional Vote Recording (AL3.5)**

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/recorder.py`
*   **Class:** `VoteRecorder`
*   **Method:** `submit_vote`
*   **Implementation:** `with self._dal.transaction():` and `self._dal.get_concept_status_for_update(concept_id)`

**Detailed Explanation:**
The `submit_vote` method guarantees data integrity by executing its core logic within a `with self._dal.transaction():` block. This ensures that all database operations—creating/updating a vote, calculating consensus, and updating the concept's status—are treated as a single, atomic, ACID-compliant unit. Critically, the very first operation *inside* this transaction is `self._dal.get_concept_status_for_update(concept_id)`. This call instructs the database to acquire a pessimistic lock (e.g., `SELECT FOR UPDATE`) on the specific `ConceptStatus` row. This lock prevents any other concurrent transaction from reading or writing to that same row until the current transaction is complete, thereby serializing votes for the same concept and eliminating the risk of race conditions corrupting the consensus calculation.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/recorder.py

# ... inside submit_vote method ...

# 4. Transaction Management and Locking (AL3.5)
with self._dal.transaction():
    # Acquire lock before any writes (AL3.5.1)
    self._dal.get_concept_status_for_update(concept_id)

    # Create the vote object with an authoritative timestamp (AL3.3)
    vote_to_persist = AdjudicationVote(...)

    # Persist the vote (AL3.3, AL3.4)
    if existing_vote:
        self._dal.update_vote(vote_to_persist)
    else:
        self._dal.create_vote(vote_to_persist)

    # ... (Consensus Recalculation and Status Update) ...
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_nfr_al3_vote.py
from unittest.mock import create_autospec
from codeeval_adjudication_engine.recorder import VoteRecorder
from codeeval_adjudication_engine.models import VoteDecision, AdjudicatorRoster, ConcurrencyConflictError
from codeeval_adjudication_engine.interfaces import DataAccessLayer, AuditLogger
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager


# 1. Set up dependencies
mock_dal = create_autospec(DataAccessLayer)
mock_consensus = create_autospec(ConsensusCalculator)
mock_tgs = create_autospec(TGSFactory)
mock_audit = create_autospec(AuditLogger)
mock_workflow = create_autospec(WorkflowManager)

# 2. Configure mock DAL to simulate a locking failure
mock_dal.get_concept_status_for_update.side_effect = ConcurrencyConflictError("Failed to acquire lock on concept 101.")

# 3. Instantiate the recorder
recorder = VoteRecorder(mock_dal, mock_consensus, mock_tgs, mock_audit, mock_workflow)

# 4. Configure workflow manager to authorize the user
mock_workflow.get_roster.return_value = [AdjudicatorRoster("test_user", is_active=True)]

# 5. Attempt to submit a vote, expecting a concurrency error
print("Attempting to vote on a locked concept...")
try:
    recorder.submit_vote("test_user", 101, VoteDecision.INCLUDE, 1)
except ConcurrencyConflictError as e:
    print(f"  - Caught expected error: {e}")
    # Verify that despite the error, the transaction was attempted
    mock_dal.transaction.assert_called_once()
    # Verify no vote was actually created
    mock_dal.create_vote.assert_not_called()
    print("  - Verified that the vote was not saved.")

# Expected Output:
# Attempting to vote on a locked concept...
#   - Caught expected error: Failed to acquire lock on concept 101.
#   - Verified that the vote was not saved.
```

**Test Case Example:**
```python
# From: tests/test_recorder.py

# This test simulates a locking failure and verifies the system's response.
def test_concurrency_conflict_error_is_raised(self):
    """Verify a concurrency error still audits but does not save the vote."""
    self.mock_dal.get_concept_status_for_update = create_autospec(
        self.mock_dal.get_concept_status_for_update,
        side_effect=ConcurrencyConflictError("Failed to acquire lock"),
    )

    # ... (re-initialize recorder with the mock) ...

    with self.assertRaises(ConcurrencyConflictError):
        self.vote_recorder.submit_vote(...)

    # The transaction should be attempted and failed
    self.mock_dal.transaction_context.__enter__.assert_called_once()
    self.mock_dal.transaction_context.__exit__.assert_called_once()

    # No vote should have been persisted
    self.assertEqual(len(self.mock_dal._votes), 0)
```

---
#### **Transactional Roster Modification (AL7.5)**

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/overrides.py`
*   **Class:** `OverrideManager`
*   **Method:** `modify_adjudicator_roster`
*   **Implementation:** `with self._dal.transaction():` and `self._dal.get_all_concept_statuses_for_update(clinical_idea_id)`

**Detailed Explanation:**
The `OverrideManager` employs an even more robust locking strategy for roster modifications. The entire operation is wrapped in a `with self._dal.transaction():` block. The first action inside this block is `self._dal.get_all_concept_statuses_for_update(clinical_idea_id)`. This is a critical design choice: it pessimistically locks **all concept status rows** for the entire clinical idea. This comprehensive lock is necessary because a change to the roster (e.g., removing an adjudicator) requires a full recalculation of consensus for every single concept. By locking all relevant rows upfront, the system prevents any concurrent `submit_vote` operations from interfering while this sensitive, wide-ranging recalculation is in progress, thus guaranteeing data consistency.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/overrides.py

# ... inside modify_adjudicator_roster method ...

# 3. Transactional Execution (AL7.5)
with self._dal.transaction():
    # Lock all concepts for this clinical idea to prevent race conditions
    # with concurrent voting during the recalculation.
    concept_statuses = self._dal.get_all_concept_statuses_for_update(
        clinical_idea_id
    )

    # 3. Roster Update and Vote Invalidation (AL7.1, AL7.4) via WorkflowManager
    self._workflow_manager.modify_roster(...)

    # 4. Full Consensus Recalculation (AL7.3)
    # ...
```

**Verifiable Examples:**

**Usage Example:**
The following example demonstrates the successful execution path, which relies on the underlying transaction and locking mechanism being called correctly.
```python
# usage_example_nfr_al3_override.py
from unittest.mock import create_autospec
from codeeval_adjudication_engine.overrides import OverrideManager
from codeeval_adjudication_engine.models import UserContext, ClinicalIdeaStatus
from codeeval_adjudication_engine.interfaces import DataAccessLayer, AuditLogger
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

# 1. Set up dependencies
mock_dal = create_autospec(DataAccessLayer)
mock_consensus = create_autospec(ConsensusCalculator)
mock_tgs = create_autospec(TGSFactory)
mock_audit = create_autospec(AuditLogger)
mock_workflow = create_autospec(WorkflowManager)

# 2. Configure mock DAL to allow the operation
mock_dal.get_clinical_idea_status.return_value = ClinicalIdeaStatus.IN_PROGRESS
# Mock the locking call to return an empty list, simulating success
mock_dal.get_all_concept_statuses_for_update.return_value = []

# 3. Instantiate the manager
manager = OverrideManager(mock_dal, mock_consensus, mock_tgs, mock_audit, mock_workflow)
lead_context = UserContext("lead1", 0, ["Session Lead"])

# 4. Perform the override
print("Performing a roster modification...")
manager.modify_adjudicator_roster(1, "adj_to_mod", False, lead_context)
print("Modification complete.")

# 5. Verify that the transaction and locking were initiated
print("\nVerifying data integrity calls:")
mock_dal.transaction.assert_called_once()
print("  - Transaction was initiated.")
mock_dal.get_all_concept_statuses_for_update.assert_called_once_with(1)
print("  - All concept statuses were locked for update.")

# Expected Output:
# Performing a roster modification...
# Modification complete.
#
# Verifying data integrity calls:
#   - Transaction was initiated.
#   - All concept statuses were locked for update.
```

**Test Case Example:**
The test suite for `OverrideManager` verifies the successful workflow, which implicitly relies on the transaction and locking calls being made correctly. The following snippet from a successful test run demonstrates the sequence.
```python
# From: tests/test_overrides.py

def test_modify_adjudicator_roster_deactivation_success(...):
    # ... (Arrange)
    manager = OverrideManager(...)
    mock_dal = ... # Get the mock DAL from the test setup

    # Act
    manager.modify_adjudicator_roster(...)

    # Assert
    # We can explicitly check that the locking call was made.
    mock_dal.get_all_concept_statuses_for_update.assert_called_once_with(
        clinical_idea_id # The ID used in the test
    )
```
---
### NFR-AL4. Accuracy

> **Requirement Statement:** The Consensus Engine (AL4), including the dynamic recalculation logic (AL7.3) and vote invalidation (AL7.4), and TGS Construction (AL5) must be mathematically precise. 100% unit test coverage is required, including complex scenarios involving dynamic overrides.

**Implementation Mapping:**
*   **Consensus Logic Tests:** `tests/test_consensus.py`
*   **TGS Construction Tests:** `tests/test_tgs_factory.py`
*   **Dynamic Recalculation Tests:** `tests/test_overrides.py`

**Detailed Explanation:**
Compliance with this requirement is demonstrated through a comprehensive and multi-layered testing strategy that validates the mathematical precision of the system's core logic at every stage. The accuracy is ensured across three primary components:

1.  **Consensus Engine (`ConsensusCalculator`):** The test suite in `test_consensus.py` rigorously validates the Unanimity Rule. It includes specific tests for successful unanimity, immediate exclusion upon receiving an "Exclude" vote, and correct handling of edge cases like missing votes. Critically, it also contains tests that prove the logic correctly handles dynamic rosters by ignoring votes from adjudicators who have been deactivated or whose votes have been invalidated (AL7.4).

2.  **TGS Construction (`TGSFactory`):** The `test_tgs_factory.py` suite validates the TGS assembly formula (TGS = Intersection + Delta Includes). The tests confirm that the final set of concept IDs is correctly calculated, including scenarios where concepts might exist in both the intersection and the delta (ensuring uniqueness) and that the final list is properly formed.

3.  **Dynamic Override Recalculation (`OverrideManager`):** The `test_overrides.py` suite contains complex, end-to-end scenario tests that verify the accuracy of the entire workflow after a roster modification. The test `test_consensus_changes_after_deactivating_blocking_voter` provides a powerful example: it sets up a scenario where a concept's status is `CONSENSUS_EXCLUDE`, then removes the single adjudicator responsible for that status, and asserts that the system correctly recalculates the status to `CONSENSUS_INCLUDE`. This verifies the accuracy of the most complex interaction in the system.

**Code Implementation Snippet:**
The implementation is demonstrated through the tests that enforce it.

**Consensus Rule Test:**
```python
# From: tests/test_consensus.py
def test_unanimous_include_yields_consensus_include(
    calculator: ConsensusCalculator, active_roster: List[AdjudicatorRoster]
):
    """
    Tests AL4.2: A concept is included ONLY IF 100% of the active
    Adjudicator Roster have submitted an active 'Include' vote.
    """
    # ... (setup votes for all active roster members to be INCLUDE)
    result = calculator.calculate_consensus(concept_id, votes, active_roster)
    assert result == ConceptConsensusStatus.CONSENSUS_INCLUDE
```

**TGS Assembly Test:**
```python
# From: tests/test_tgs_factory.py
def test_tgs_factory_finalizes_when_all_concepts_resolved(...):
    # ... (setup mock DAL with intersection and delta concepts)
    mock_dal._intersection_concepts = [901, 902]
    mock_dal._concept_statuses = {
        101: ConceptStatus(status=ConceptConsensusStatus.CONSENSUS_INCLUDE),
        102: ConceptStatus(status=ConceptConsensusStatus.CONSENSUS_EXCLUDE),
        103: ConceptStatus(status=ConceptConsensusStatus.CONSENSUS_INCLUDE),
    }
    factory = TGSFactory(...)

    # Act
    factory.check_and_finalize(TEST_CLINICAL_IDEA_ID)

    # Assert
    # Verifies that the final TGS combines intersection and delta-include, handling duplicates
    assert mock_dal.saved_tgs.concept_ids == [101, 103, 901, 902]
```

**Dynamic Recalculation Test:**
```python
# From: tests/test_overrides.py
def test_consensus_changes_after_deactivating_blocking_voter(...):
    """
    A complex scenario showing that consensus is recalculated correctly when an
    adjudicator with a deciding 'Exclude' vote is removed.
    """
    # Arrange: Setup a concept that is CONSENSUS_EXCLUDE due to one voter
    mock_dal._concept_statuses = {
        concept_id: ConceptStatus(concept_id, ConceptConsensusStatus.CONSENSUS_EXCLUDE)
    }
    # ... (full setup)
    manager = OverrideManager(...)

    # Act: Deactivate the adjudicator who cast the 'Exclude' vote
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_deactivate, False, session_lead_context
    )

    # Assert: The status should flip to CONSENSUS_INCLUDE
    final_status = mock_dal._concept_statuses[concept_id].status
    assert final_status == ConceptConsensusStatus.CONSENSUS_INCLUDE
```

**Verifiable Examples:**

The verifiable example for this requirement is the successful execution of the entire test suite. The project is configured to use `pytest`.

**Verification Steps:**
1.  Ensure development dependencies are installed: `pip install .[test]`
2.  Run the test suite from the root of the project:
    ```bash
    hatch run test:run
    ```
3.  A successful run, with all tests passing, verifies that the mathematical logic of the core components is accurate as per the scenarios defined in the test suite.
---
### NFR-AL5. Auditability (BRD NFR12)

> **Requirement Statement:** Every vote (AL3.3) and every operational override (AL7.6) MUST be logged with full context.

This requirement is addressed in two key areas: the `VoteRecorder` for individual vote actions and the `OverrideManager` for roster modifications.

---
#### **Vote Auditing (AL3.3)**

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/recorder.py`
*   **Class:** `VoteRecorder`
*   **Method:** `submit_vote`
*   **Logger Call:** `self._audit_logger.log_vote_action(...)`

**Detailed Explanation:**
The `VoteRecorder.submit_vote` method ensures that every vote attempt is audited. Immediately after validating the user's authorization but *before* entering the main database transaction, it calls `self._audit_logger.log_vote_action`. This placement is critical: it guarantees that even if the subsequent database transaction fails (e.g., due to a concurrency conflict), the initial intent to vote is still recorded, providing a complete audit trail of all system interactions. The log includes the user ID, concept ID, clinical idea ID, and the specific decision, fulfilling the "full context" requirement.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/recorder.py

# ... inside submit_vote method, after validation ...

# 2. Auditing (NFR-AL5)
self._audit_logger.log_vote_action(
    user_id=user_id,
    concept_id=concept_id,
    clinical_idea_id=clinical_idea_id,
    decision=decision,
)

# 3. Check for existing vote (AL3.4)
# ...
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_nfr_al5_vote.py
from unittest.mock import create_autospec
from datetime import datetime, timezone
from typing import List, Dict, Any

from codeeval_adjudication_engine.recorder import VoteRecorder
from codeeval_adjudication_engine.models import VoteDecision, AdjudicatorRoster
from codeeval_adjudication_engine.interfaces import DataAccessLayer, AuditLogger
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

# Define a simple, concrete implementation of AuditLogger for this example.
class InMemoryAuditLogger(AuditLogger):
    def __init__(self):
        self.logs: List[Dict[str, Any]] = []

    def _log(self, event_type: str, details: Dict[str, Any]):
        log_entry = {
            'event_type': event_type,
            'timestamp': datetime.now(timezone.utc),
            'details': details
        }
        self.logs.append(log_entry)

    def log_vote_action(self, user_id: str, concept_id: int, clinical_idea_id: int, decision: VoteDecision):
        details = {'user_id': user_id, 'concept_id': concept_id, 'clinical_idea_id': clinical_idea_id, 'decision': decision}
        self._log('VOTE_ACTION', details)

    def log_override_action(self, session_lead_id: str, affected_adjudicator_id: str, action: str, clinical_idea_id: int):
        details = {'session_lead_id': session_lead_id, 'affected_adjudicator_id': affected_adjudicator_id, 'action': action, 'clinical_idea_id': clinical_idea_id}
        self._log('OVERRIDE_ACTION', details)

    def log_tgs_finalization(self, clinical_idea_id: int, final_tgs_concept_ids: List[int]):
        details = {'clinical_idea_id': clinical_idea_id, 'final_tgs_concept_ids': final_tgs_concept_ids}
        self._log('TGS_FINALIZATION', details)

    def get_log_entries(self):
        return self.logs

# 1. Set up mock dependencies and our in-memory AuditLogger
mock_dal = create_autospec(DataAccessLayer, instance=True)
mock_consensus = create_autospec(ConsensusCalculator, instance=True)
mock_tgs = create_autospec(TGSFactory, instance=True)
mock_workflow = create_autospec(WorkflowManager, instance=True)
audit_logger = InMemoryAuditLogger()

# 2. Configure mock workflow manager to authorize the user
mock_workflow.get_roster.return_value = [AdjudicatorRoster("test_user", is_active=True)]

# 3. Instantiate the VoteRecorder
recorder = VoteRecorder(mock_dal, mock_consensus, mock_tgs, audit_logger, mock_workflow)

# 4. Submit a vote
print("Submitting a vote...")
recorder.submit_vote(
    user_id="test_user",
    concept_id=101,
    decision=VoteDecision.INCLUDE,
    clinical_idea_id=1
)
print("Vote submitted.")

# 5. Verify the audit log
print("\nVerifying audit log contents:")
assert len(audit_logger.get_log_entries()) == 1
log_entry = audit_logger.get_log_entries()[0]
# For verification, we will just check the content, not the exact timestamp
print(f"  - Log entry found with event type: {log_entry['event_type']}")
print(f"  - Log details: {log_entry['details']}")
assert log_entry['details']['user_id'] == "test_user"
assert log_entry['details']['decision'] == VoteDecision.INCLUDE
print("  - Audit log verified successfully.")

# Expected Output:
# Submitting a vote...
# Vote submitted.
#
# Verifying audit log contents:
#   - Log entry found with event type: VOTE_ACTION
#   - Log details: {'user_id': 'test_user', 'concept_id': 101, 'clinical_idea_id': 1, 'decision': <VoteDecision.INCLUDE: 1>}
#   - Audit log verified successfully.
```

**Test Case Example:**
```python
# From: tests/test_recorder.py

# This test uses a mock logger to intercept and verify the audit call.
def test_submit_vote_success_audits_action(self):
    """Verify that a successful vote submission is correctly audited."""
    self.vote_recorder.submit_vote(
        user_id="adj1",
        concept_id=1,
        decision=VoteDecision.EXCLUDE,
        clinical_idea_id=TEST_CLINICAL_IDEA_ID,
    )
    self.assertEqual(len(self.mock_audit_logger.logged_actions), 1)
    log_entry = self.mock_audit_logger.logged_actions[0]
    self.assertEqual(log_entry["type"], "VOTE")
    self.assertEqual(log_entry["user_id"], "adj1")
    self.assertEqual(log_entry["concept_id"], 1)
    self.assertEqual(log_entry["clinical_idea_id"], TEST_CLINICAL_IDEA_ID)
    self.assertEqual(log_entry["decision"], VoteDecision.EXCLUDE)
```

---
#### **Operational Override Auditing (AL7.6)**

**Implementation Mapping:**
*   **Module:** `src/codeeval_adjudication_engine/overrides.py`
*   **Class:** `OverrideManager`
*   **Method:** `modify_adjudicator_roster`
*   **Logger Call:** `self._audit_logger.log_override_action(...)`

**Detailed Explanation:**
The `OverrideManager.modify_adjudicator_roster` method addresses this requirement. As soon as the initial authorization (verifying "Session Lead" role) and state validation checks pass, it calls `self._audit_logger.log_override_action`. This call records the ID of the Session Lead performing the action, the ID of the adjudicator being modified, the specific action taken ("ACTIVATE" or "DEACTIVATE"), and the relevant clinical idea ID. This provides a clear, comprehensive, and immediate audit trail for every operational override, as mandated by the FRD.

**Code Implementation Snippet:**
```python
# From: src/codeeval_adjudication_engine/overrides.py

# ... inside modify_adjudicator_roster, after validation ...

# 2. Auditing (AL7.6)
action = "ACTIVATE" if new_active_status else "DEACTIVATE"
self._audit_logger.log_override_action(
    session_lead_id=current_user_context.user_id,
    affected_adjudicator_id=user_id_to_modify,
    action=action,
    clinical_idea_id=clinical_idea_id,
)

# 3. Transactional Execution (AL7.5)
# ...
```

**Verifiable Examples:**

**Usage Example:**
```python
# usage_example_nfr_al5_override.py
from unittest.mock import create_autospec
from datetime import datetime, timezone
from typing import List, Dict, Any

from codeeval_adjudication_engine.overrides import OverrideManager
from codeeval_adjudication_engine.models import UserContext, ClinicalIdeaStatus, VoteDecision
from codeeval_adjudication_engine.interfaces import DataAccessLayer, AuditLogger
from codeeval_adjudication_engine.consensus import ConsensusCalculator
from codeeval_adjudication_engine.tgs_factory import TGSFactory
from codeeval_adjudication_engine.workflow_manager import WorkflowManager

# Define a simple, concrete implementation of AuditLogger for this example.
class InMemoryAuditLogger(AuditLogger):
    def __init__(self):
        self.logs: List[Dict[str, Any]] = []

    def _log(self, event_type: str, details: Dict[str, Any]):
        log_entry = {
            'event_type': event_type,
            'timestamp': datetime.now(timezone.utc),
            'details': details
        }
        self.logs.append(log_entry)

    def log_vote_action(self, user_id: str, concept_id: int, clinical_idea_id: int, decision: VoteDecision):
        details = {'user_id': user_id, 'concept_id': concept_id, 'clinical_idea_id': clinical_idea_id, 'decision': decision}
        self._log('VOTE_ACTION', details)

    def log_override_action(self, session_lead_id: str, affected_adjudicator_id: str, action: str, clinical_idea_id: int):
        details = {'session_lead_id': session_lead_id, 'affected_adjudicator_id': affected_adjudicator_id, 'action': action, 'clinical_idea_id': clinical_idea_id}
        self._log('OVERRIDE_ACTION', details)

    def log_tgs_finalization(self, clinical_idea_id: int, final_tgs_concept_ids: List[int]):
        details = {'clinical_idea_id': clinical_idea_id, 'final_tgs_concept_ids': final_tgs_concept_ids}
        self._log('TGS_FINALIZATION', details)

    def get_log_entries(self):
        return self.logs

# 1. Set up dependencies
mock_dal = create_autospec(DataAccessLayer, instance=True)
mock_consensus = create_autospec(ConsensusCalculator, instance=True)
mock_tgs = create_autospec(TGSFactory, instance=True)
mock_workflow = create_autospec(WorkflowManager, instance=True)
audit_logger = InMemoryAuditLogger()

# 2. Configure mock DAL to allow the operation
mock_dal.get_clinical_idea_status.return_value = ClinicalIdeaStatus.IN_PROGRESS
# Mock the locking mechanism to return an empty list of concepts
mock_dal.get_all_concept_statuses_for_update.return_value = []

# 3. Instantiate the OverrideManager
manager = OverrideManager(mock_dal, mock_consensus, mock_tgs, audit_logger, mock_workflow)

# 4. Define user context for an authorized "Session Lead"
lead_context = UserContext("lead_user", 1, ["Session Lead"])

# 5. Perform an override action
print("Deactivating adjudicator 'adj_to_remove'...")
manager.modify_adjudicator_roster(
    clinical_idea_id=5,
    user_id_to_modify="adj_to_remove",
    new_active_status=False,
    current_user_context=lead_context
)
print("Override action complete.")

# 6. Verify the audit log
print("\nVerifying audit log contents:")
assert len(audit_logger.get_log_entries()) == 1
log_entry = audit_logger.get_log_entries()[0]
print(f"  - Log entry found: {log_entry['event_type']}")
print(f"  - Log details: {log_entry['details']}")
assert log_entry['event_type'] == 'OVERRIDE_ACTION'
assert log_entry['details']['session_lead_id'] == "lead_user"
assert log_entry['details']['affected_adjudicator_id'] == "adj_to_remove"
assert log_entry['details']['action'] == "DEACTIVATE"
print("  - Audit log verified successfully.")

# Expected Output:
# Deactivating adjudicator 'adj_to_remove'...
# Override action complete.
#
# Verifying audit log contents:
#   - Log entry found: OVERRIDE_ACTION
#   - Log details: {'session_lead_id': 'lead_user', 'affected_adjudicator_id': 'adj_to_remove', 'action': 'DEACTIVATE', 'clinical_idea_id': 5}
#   - Audit log verified successfully.
```

**Test Case Example:**
```python
# From: tests/test_overrides.py

def test_auditing_occurs_on_roster_modification(
    session_lead_context,
    mock_dal,
    mock_tgs_notifier,
    mock_workflow_manager,
    mock_audit_logger,
):
    """
    Verifies that modifying a roster correctly logs the action to the database.
    FRD AL7.6
    """
    # ... (Arrange steps) ...
    manager = OverrideManager(...)

    # Act
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_modify, False, session_lead_context
    )
    manager.modify_adjudicator_roster(
        clinical_idea_id, user_to_modify, True, session_lead_context
    )

    # Assert
    assert len(mock_audit_logger.logged_actions) == 2
    assert mock_audit_logger.logged_actions[0]["action"] == "DEACTIVATE"
    assert mock_audit_logger.logged_actions[1]["action"] == "ACTIVATE"
```

---
### NFR-AL6. Code Quality (BRD NFR14)

> **Requirement Statement:** Strict adherence to PEP standards, full type hinting, and comprehensive test coverage are required.

**Implementation Mapping:**
*   **Tooling Configuration:** `pyproject.toml`
*   **Code Style Enforcement:** `black`, `isort`, `flake8`
*   **Static Typing:** Consistent use of Python type hints throughout the codebase.
*   **Test Coverage Measurement:** `pytest-cov`

**Detailed Explanation:**
The project ensures high code quality through a combination of automated tooling, coding standards, and a robust testing culture.

1.  **Automated Formatting and Linting:** The `pyproject.toml` file defines `black`, `isort`, and `flake8` as development dependencies. This indicates a standardized toolchain for automatically formatting code, sorting imports, and checking for common style violations (linting), ensuring consistent adherence to PEP standards across the project.

2.  **Full Type Hinting:** A manual review of the source code (e.g., `recorder.py`, `presenter.py`, `models.py`) confirms the pervasive use of Python's type hints for function arguments, return values, and variable declarations. This improves code readability, maintainability, and allows for static analysis tools to catch potential errors before runtime.

3.  **Comprehensive Test Coverage:** The project includes a dedicated `tests/` directory with a test file for each corresponding module in the source code. The inclusion of `pytest-cov` in the test dependencies demonstrates an established practice of measuring test coverage, which is a key component in verifying that the logic is thoroughly tested.

**Code Implementation Snippet:**
Evidence for this requirement is found in the project's configuration and code structure.

**Tooling Definition in `pyproject.toml`:**
```toml
# From: pyproject.toml
[project.optional-dependencies]
test = [
    "pytest",
    "pytest-cov",
]
dev = [
    "black",
    "isort",
    "flake8",
]
```

**Example of Full Type Hinting:**
```python
# From: src/codeeval_adjudication_engine/presenter.py
def get_concepts_for_review(
    self,
    clinical_idea_id: int,
    user_context: UserContext,
) -> AdjudicationDataPackage:
    # ...
    blinded_concepts: List[BlindedConceptView] = [
        BlindedConceptView(...) for c in concepts_copy
    ]
    # ...
```

**Verifiable Examples:**
Compliance can be verified by running the code quality tools.

**Verification Steps:**
1.  Ensure development dependencies are installed: `pip install .[dev]`
2.  Run the tools from the project's root directory:
    ```bash
    # Check formatting (black and isort)
    black --check .
    isort --check .
    # Run linter
    flake8 .
    ```
3.  A successful run of these commands with no errors indicates compliance with the configured code quality standards.