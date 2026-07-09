"""
MongoDB Connection

Provides a singleton MongoDB connection for the application.

Responsibilities
----------------
- Create MongoDB client
- Return database
- Return collections

Does NOT
--------
- Perform CRUD operations
"""

from pymongo import MongoClient

from review_engine.config.mongodb_constants import (
    MONGODB_URI,
    DATABASE_NAME,
    SERVER_SELECTION_TIMEOUT_MS,
    CONNECT_TIMEOUT_MS,
    SOCKET_TIMEOUT_MS,
)


class MongoDB:

    _client = None
    _database = None

    @classmethod
    def connect(cls):
        """
        Create MongoDB connection once.
        """

        if cls._client is None:

            cls._client = MongoClient(
                MONGODB_URI,
                serverSelectionTimeoutMS=SERVER_SELECTION_TIMEOUT_MS,
                connectTimeoutMS=CONNECT_TIMEOUT_MS,
                socketTimeoutMS=SOCKET_TIMEOUT_MS,
            )

            # Verify connection
            cls._client.admin.command("ping")

            cls._database = cls._client[
                DATABASE_NAME
            ]

        return cls._database

    @classmethod
    def get_database(cls):
        """
        Return database instance.
        """

        if cls._database is None:
            cls.connect()

        return cls._database

    @classmethod
    def get_collection(cls, collection_name):
        """
        Return MongoDB collection.
        """

        database = cls.get_database()

        return database[
            collection_name
        ]

    @classmethod
    def close(cls):
        """
        Close MongoDB connection.
        """

        if cls._client:

            cls._client.close()

            cls._client = None
            cls._database = None