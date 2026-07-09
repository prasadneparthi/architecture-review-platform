"""
Architecture Review Output Schema

Defines the standard response returned after an architecture review.

No validation or business logic should be added here.
"""

from review_engine.config.constants import (
    REVIEW_CATEGORIES,
    RULE_STATUS,
    RULE_SEVERITIES,
    DEFAULT_LLM,
    DEFAULT_REVIEW_VERSION,
    DEFAULT_RULEBOOK_VERSION,
    DEFAULT_SCHEMA_VERSION,
)

# ==========================================================
# Category Scores
# ==========================================================

CATEGORY_SCORES = {
    "scalability": int,
    "security": int,
    "reliability": int,
    "performance": int,
    "maintainability": int,
    "cost_efficiency": int,
}

# ==========================================================
# Rule Result Schema
# ==========================================================

RULE_RESULT_SCHEMA = {
    "rule_id": str,
    "category": REVIEW_CATEGORIES,
    "status": RULE_STATUS,
    "severity": RULE_SEVERITIES,
    "score_change": int,
    "recommendation": str,
}

# ==========================================================
# Recommendation Schema
# ==========================================================

RECOMMENDATION_SCHEMA = {
    "rule_id": str,
    "title": str,
    "category": REVIEW_CATEGORIES,
    "severity": RULE_SEVERITIES,
    "description": str,
}

# ==========================================================
# Cost Analysis Schema
# ==========================================================

COST_ANALYSIS_SCHEMA = {
    "monthly_cost": float,
    "yearly_cost": float,
    "cost_score": int,
    "optimization_suggestions": [str],
}

# ==========================================================
# Review Metadata
# ==========================================================

REVIEW_METADATA_SCHEMA = {
    "reviewed_at": str,
    "llm_used": DEFAULT_LLM,
    "review_version": DEFAULT_REVIEW_VERSION,
    "rulebook_version": DEFAULT_RULEBOOK_VERSION,
    "schema_version": DEFAULT_SCHEMA_VERSION,
}

# ==========================================================
# Master Response Schema
# ==========================================================

RESPONSE_SCHEMA = {
    "review_id": str,
    "system_name": str,
    "overall_score": int,
    "category_scores": CATEGORY_SCORES,
    "rule_results": [RULE_RESULT_SCHEMA],
    "strengths": [str],
    "weaknesses": [str],
    "recommendations": [RECOMMENDATION_SCHEMA],
    "cost_analysis": COST_ANALYSIS_SCHEMA,
    "review_metadata": REVIEW_METADATA_SCHEMA,
}