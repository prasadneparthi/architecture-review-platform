"""
Review Repository

Handles all MongoDB operations related to architecture reviews.

Responsibilities
----------------
- Save review
- Get review
- Get all reviews
- Delete review

Does NOT
--------
- Build review documents
- Perform business logic
"""

from review_engine.database.mongodb import (
    MongoDB,
)

from review_engine.models import (
    ReviewDocument,
)

from review_engine.config.mongodb_constants import (
    REVIEW_COLLECTION,
)

from review_engine.exceptions.custom_exceptions import (
    DatabaseError,
)
from review_engine.logging.logger import (
    logger,
)
logger = logger.get_logger()


class ReviewRepository:

    def __init__(self):

        self.collection = MongoDB.get_collection(
            REVIEW_COLLECTION
        )

    # =====================================================
    # Save
    # =====================================================

    def save_review(
        self,
        user,
        architecture: dict,
        review_result: dict,
    ):
        """
        Save architecture review.
        """

        try:

            document = ReviewDocument.build(
                user=user,
                architecture=architecture,
                review_result=review_result,
            )

            self.collection.insert_one(
                document
            )
            logger.info(f"MongoDb insert successful. Review ID: {document['review_id']}")

            return document

        except Exception as exc:
            logger.exception("Unable to save review.")

            raise DatabaseError(
                f"Unable to save review. {str(exc)}"
            )

    # =====================================================
    # Get by Review ID
    # =====================================================

    def get_review(
        self,
        user,
        review_id: str,
    ):
        """
        Fetch review using review_id.
        """
        logger.info(f"Fetching review {review_id}")

        try:

            return self.collection.find_one(
                {
                    "review_id": review_id,
                    "user_id":user.id,
                },
                {
                    "_id": 0
                },
            )

        except Exception as exc:
            logger.exception(f"Unable to fetch review {review_id}")

            raise DatabaseError(
                f"Unable to fetch review. {str(exc)}"
            )

    # =====================================================
    # Get All Reviews
    # =====================================================

    def get_all_reviews(self,user):
        """
        Fetch all reviews.
        """
        logger.info("Fetching all reviews")
        try:

            cursor = self.collection.find(
                {
                    "user_id":user.id
                },
                {
                    "_id": 0
                },
            )

            return list(cursor)

        except Exception as exc:
            logger.exception("Unable to fetch reviews.")

            raise DatabaseError(
                f"Unable to fetch reviews. {str(exc)}"
            )

    # =====================================================
    # Delete Review
    # =====================================================

    def delete_review(
        self,
        user,
        review_id: str,
    ):
        """
        Delete review.
        """
        logger.info(f"Deleting review {review_id}")
        try:

            result = self.collection.delete_one(
                {
                    "review_id": review_id,
                    "user_id":user.id,
                }
            )

            return result.deleted_count > 0

        except Exception as exc:
            logger.exception("Unable to delete review.")

            raise DatabaseError(
                f"Unable to delete review. {str(exc)}"
            )

    # =====================================================
    # Count Reviews
    # =====================================================

    def count_reviews(self):
        """
        Total reviews.
        """

        try:

            return self.collection.count_documents(
                {}
            )

        except Exception as exc:

            logger.exception("Unable to count reviews.")

            raise DatabaseError(
                f"Unable to count reviews. {str(exc)}"
            )