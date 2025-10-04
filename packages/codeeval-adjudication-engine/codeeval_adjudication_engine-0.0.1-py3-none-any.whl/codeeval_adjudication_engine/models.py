# Copyright (c) 2025-2026 Gowtham A Rao MD PhD. All Rights Reserved.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
#
# Commercial use beyond a 30-day trial requires a separate license.
# Contact: rao@ohdsi.org

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from typing import List


class VoteDecision(Enum):
    """Represents the decision options for an adjudicator's vote."""

    INCLUDE = auto()
    EXCLUDE = auto()


class ConceptConsensusStatus(Enum):
    """Represents the consensus status of a concept after adjudication."""

    PENDING = auto()
    CONSENSUS_INCLUDE = auto()
    CONSENSUS_EXCLUDE = auto()


class ClinicalIdeaStatus(Enum):
    """Represents the overall status of a clinical idea in the adjudication workflow."""

    PENDING = auto()
    IN_PROGRESS = auto()
    FINALIZED = auto()


# --- Custom Exceptions ---


class AdjudicationError(Exception):
    """Base class for all adjudication-specific errors."""

    pass


class ConcurrencyConflictError(AdjudicationError):
    """
    Raised when a pessimistic lock cannot be acquired, indicating a race condition.
    FRD AL3.5.2: Must be handled gracefully.
    """

    pass


class AuthorizationError(AdjudicationError):
    """
    Raised when an action is attempted by an unauthorized user.
    FRD AL1.1: Used to enforce roster-based authorization.
    """

    pass


class InvalidStateError(AdjudicationError):
    """
    Raised when an action is attempted on an entity in an inappropriate state
    (e.g., voting on a FINALIZED clinical idea).
    FRD AL3.2: Used to protect the integrity of the workflow.
    """

    pass


# --- Data Models ---


@dataclass
class Concept:
    """
    Represents a concept from the Concept_Pool, including sensitive information.
    """

    concept_id: int
    name: str
    description: str
    agreement_level: int  # CRITICAL: Must be excluded from BlindedConceptView
    contributing_arms: List[str]  # CRITICAL: Must be excluded from BlindedConceptView


@dataclass
class BlindedConceptView:
    """
    The sanitized data structure served to the front-end, with sensitive fields removed.
    """

    concept_id: int
    name: str
    description: str


@dataclass
class AdjudicationDataPackage:
    """
    A data package containing all necessary information for an adjudication session,
    including the overall context and the list of items to be reviewed.
    """

    clinical_idea_description: str
    concepts_for_review: List[BlindedConceptView]


@dataclass
class UserContext:
    """
    Represents the user's session context, including the randomization seed.
    """

    user_id: str
    session_rng_seed: int
    roles: List[str] = field(default_factory=list)


@dataclass
class AdjudicatorRoster:
    """
    Defines an adjudicator's assignment and active status for a Clinical Idea.
    """

    user_id: str
    is_active: bool = True


@dataclass
class AdjudicationVote:
    """
    Represents a single vote cast by an adjudicator for a specific concept.
    """

    user_id: str
    concept_id: int
    decision: VoteDecision
    timestamp: datetime  # FRD AL3.3: Added for auditability.
    is_active: bool = True


@dataclass
class ConceptStatus:
    """
    Tracks the consensus status of a Delta concept. This is the primary
    target for pessimistic locking as per FRD C4.1.
    """

    concept_id: int
    status: ConceptConsensusStatus = ConceptConsensusStatus.PENDING


@dataclass
class ClinicalIdea:
    """Represents a clinical idea, the parent entity for adjudication."""

    clinical_idea_id: int
    status: ClinicalIdeaStatus = ClinicalIdeaStatus.PENDING


# --- Progress Tracking Models (FRD AL6) ---


@dataclass
class IndividualProgress:
    """
    Represents the progress of a single adjudicator for a clinical idea.
    FRD AL6.1
    """

    reviewed_count: int
    total_count: int


@dataclass
class AggregatedProgress:
    """
    Represents the aggregated progress for a clinical idea, suitable for a
    dashboard.
    FRD AL6.2
    """

    total_concepts: int
    pending_count: int
    consensus_include_count: int
    consensus_exclude_count: int
    overall_progress_percentage: float = 0.0


@dataclass
class TGS_Definition:
    """
    Represents the finalized True Gold Standard (TGS) for a clinical idea.
    FRD AL5.3
    """

    clinical_idea_id: int
    concept_ids: List[int]


@dataclass
class OverrideAuditLog:
    """
    Represents a persistent audit trail entry for an override action.
    FRD AL7.6
    """

    log_id: int
    session_lead_id: str
    affected_adjudicator_id: str
    action: str
    clinical_idea_id: int
    timestamp: datetime


@dataclass
class VoteAuditLog:
    """
    Represents a persistent audit trail entry for a vote action.
    Fulfills NFR-AL5.
    """

    log_id: int
    user_id: str
    concept_id: int
    clinical_idea_id: int
    decision: VoteDecision
    timestamp: datetime


@dataclass
class TGSFinalizationAuditLog:
    """
    Represents a persistent audit trail entry for a TGS finalization event.
    This is a new requirement to enhance auditability.
    """

    log_id: int
    clinical_idea_id: int
    timestamp: datetime
    final_tgs_concept_ids: List[int]
