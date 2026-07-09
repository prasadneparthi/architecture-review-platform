"""
Review Document

Builds the MongoDB document for a completed architecture review.

Responsibilities
----------------
- Generate review_id
- Generate timestamp
- Standardize review document

Does NOT
--------
- Save to MongoDB
- Perform business logic
"""

from uuid import uuid4
from datetime import datetime, timezone

from review_engine.config.mongodb_constants import (
    REVIEW_VERSION,
)


class ReviewDocument:

    @staticmethod
    def build(
        user,
        architecture: dict,
        review_result: dict,
    ):
        """
        Build MongoDB review document.
        """

        return {

            "review_id": str(
                uuid4()
            ),
            "user_id":user.id,
            "username":user.username,

            "system_name": architecture[
                "system_name"
            ],

            "architecture_type": architecture[
                "architecture_type"
            ],

            "created_at": datetime.now(
                timezone.utc
            ),

            "review_version": REVIEW_VERSION,

            "input_architecture": architecture,

            "review_result": review_result,
        }