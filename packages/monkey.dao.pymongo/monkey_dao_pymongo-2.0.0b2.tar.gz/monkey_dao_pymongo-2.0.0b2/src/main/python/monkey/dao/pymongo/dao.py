# -*- coding: utf-8 -*-
"""
Provides implementation of the [Data Access Object (DAO)](https://en.wikipedia.org/wiki/Data_access_object) design model
based on [MongoDB PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/) as specified by
[monkey.dao](https://dao.monkey-python.org) project.

This module contains the [`PyMongoDAO`](#monkey.dao.pymongo.dao.PyMongoDAO) class, designed to abstract database
operations such as querying, inserting, updating, and deleting documents from a MongoDB collection.

The module supports flexible collection configuration with options such as codec options, read/write concerns, and read
preferences.

It also introduces a few extra features for the documents in the collection managed with an instance
of [`PyMongoDAO`](#monkey.dao.pymongo.dao.PyMongoDAO) like:

- A sequence number management mechanism.
- An auditability sub-document.

Sequence number counters are maintained in a collection referenced by the
[`seq_collection_name`](./#monkey.dao.pymongo.dao.PyMongoDAO.sequences) instantiation parameter. By default, this
collection is named `sequences`.
Each collection exploiting this mechanism is associated with a document identified by the name of this collection in the
 sequence number counter-management collection. In the sequence number counter-management collection, the last sequence
 number used for a given collection is stored in the field referenced by the
 [`seq_num_counter_field`](./#monkey.dao.pymongo.dao.PyMongoDAO.seq_num_counter_field) property of the DAO instance. By
 default, this field is named `seq`.
If sequence numbers are enabled for a collection, the sequence number of each document is stored in the field referenced
 by the [`seq_num_field`](./#monkey.dao.pymongo.dao.PyMongoDAO.seq_num_field) property of the DAO instance. By default,
 this field is named `_seq_num`.

If auditability is enabled, the DAO will manage a sub-document referenced by the name defined by the property
[`auditable_sub_doc_name`](./#monkey.dao.pymongo.dao.PyMongoDAO.auditable_sub_doc_name) in the instance of the
`PyMongoDAO` class. By default this sub-document is named `_auditable`.
The auditability sub-document will contain the following fields:

| Audit information | Default field name | Referenced by |
| ----------- | ----------- |----------- |
| Operation type | `operation` | [`auditable_sub_doc_operation_type_field`](./#monkey.dao.pymongo.dao.PyMongoDAO.auditable_sub_doc_operation_type_field) |
| Creation  date | `creation_date` | [`auditable_sub_doc_creation_date_field`](./#monkey.dao.pymongo.dao.PyMongoDAO.auditable_sub_doc_creation_date_field) |
| Modification date | `modification_date` | [`auditable_sub_doc_modification_date_field`](./#monkey.dao.pymongo.dao.PyMongoDAO.auditable_sub_doc_modification_date_field) |
| Creator | `creator` | [`auditable_sub_doc_creator_field`](./#monkey.dao.pymongo.dao.PyMongoDAO.auditable_sub_doc_creator_field) |
| Modifier | `modifier` | [`auditable_sub_doc_modifier_field`](./#monkey.dao.pymongo.dao.PyMongoDAO.auditable_sub_doc_modifier_field) |
"""

from datetime import datetime, timezone
from logging import Logger, getLogger
from typing import Any, Union, Iterable, Optional, List, Dict

from bson.objectid import ObjectId
from bson.codec_options import CodecOptions
from pymongo.collection import Collection, ReturnDocument
from pymongo.database import Database
from pymongo.errors import PyMongoError
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern
import pymongo.results

from monkey.dao.dao import DAO
from monkey.dao.errors import PersistenceError, ObjectNotFoundError
from monkey.dao.util import OperationType
from monkey.dao.pymongo.results import (
    DeleteResult,
    InsertResult,
    UpdateResult,
    ReplaceResult,
)

SEQUENCE_COLLECTION_DEFAULT_NAME: str = "sequences"
"""The default name used for the sequences counter collection."""

SEQUENCE_COUNTER_DEFAULT_FIELD: str = "seq"
"""The default field name used for counter value field in the sequence counter collection."""

SEQUENCE_NUMBER_DEFAULT_FIELD: str = "_seq_num"
"""The default field name used for sequence number in documents."""

_ID_FIELD: str = "_id"
"""The name used for the builtin id field."""

AUDITABLE_SUB_DOC_DEFAULT_NAME: str = "_auditable"
"""The default name used for the auditable sub-document."""

AUDITABLE_SUB_DOC_CREATOR_DEFAULT_FIELD: str = "creator"
"""The default field name used for the creator in the auditable sub-document."""

AUDITABLE_SUB_DOC_MODIFIER_DEFAULT_FIELD: str = "modifier"
"""The default field name used for the modifier in the auditable sub-document."""

AUDITABLE_SUB_DOC_CREATION_DATE_DEFAULT_FIELD: str = "creation_date"
"""The default field name used for the creation date in the auditable sub-document."""

AUDITABLE_SUB_DOC_MODIFICATION_DATE_DEFAULT_FIELD: str = "modification_date"
"""The default field name used for the modification date in the auditable sub-document."""

AUDITABLE_SUB_DOC_OPERATION_TYPE_DEFAULT_FIELD: str = "operation"
"""The default field name used for the operation type in the auditable sub-document."""


class PyMongoDAO(DAO):
    """
    Provides an implementation of a Data Access Object (DAO) for MongoDB using PyMongo.

    This class encapsulates operations for querying, inserting, updating, deleting,
    and counting documents within a specific MongoDB collection. It also provides
    support for sequence numbers on documents if enabled.

    The PyMongoDAO class is designed for ease of use and to abstract database
    persistence logic, allowing the rest of the application to interact with data
    without knowledge of MongoDB operations. Custom configurations such as sequence
    number handling and collection configuration are supported.

    :ivar collection: The collection to use.
    :ivar seq_enabled: If True, sequence numbering is enabled.
    :ivar sequences: The collection to use for the sequence number counters.
    :ivar seq_num_counter_field: The name of the field in the collection to store the sequence number.
    :ivar seq_num_field: The name of the field in the document to store the sequence number.
    :ivar auditable_sub_doc_name: The name of the sub-document to be used for auditable.
    :ivar auditable_sub_doc_operation_type_field: The name of the field to be used for the operation type in the auditable sub-document.
    :ivar auditable_sub_doc_creation_date_field: The name of the field to be used for the creation date in the auditable sub-document.
    :ivar auditable_sub_doc_modification_date_field: The name of the field to be used for the modification date in the auditable sub-document.
    :ivar auditable_sub_doc_creator_field: The name of the field to be used for the creator in the auditable sub-document.
    :ivar auditable_sub_doc_modifier_field: The name of the field to be used for the modifier in the auditable sub-document.
    """

    def __init__(
        self,
        database: Database,
        collection_name: str,
        seq_enabled: bool = False,
        seq_collection_name: str = SEQUENCE_COLLECTION_DEFAULT_NAME,
        seq_num_counter_field: str = SEQUENCE_NUMBER_DEFAULT_FIELD,
        seq_num_field: str = SEQUENCE_NUMBER_DEFAULT_FIELD,
        auditable: bool = False,
        auditable_sub_doc_name: str = AUDITABLE_SUB_DOC_DEFAULT_NAME,
        auditable_sub_doc_operation_type_field: str = AUDITABLE_SUB_DOC_OPERATION_TYPE_DEFAULT_FIELD,
        auditable_sub_doc_creation_date_field: str = AUDITABLE_SUB_DOC_CREATION_DATE_DEFAULT_FIELD,
        auditable_sub_doc_modification_date_field: str = AUDITABLE_SUB_DOC_MODIFICATION_DATE_DEFAULT_FIELD,
        auditable_sub_doc_creator_field: str = AUDITABLE_SUB_DOC_CREATOR_DEFAULT_FIELD,
        auditable_sub_doc_modifier_field: str = AUDITABLE_SUB_DOC_MODIFIER_DEFAULT_FIELD,
        codec_options: Optional[CodecOptions] = None,
        read_preference=None,
        write_concern: Optional[WriteConcern] = None,
        read_concern: Optional[ReadConcern] = None,
        indexes: Optional[List[Dict[str, Any]]] = None,
    ):
        """
        Instantiates a new PyMongo DAO.

        :param database: A MongoDB database provided by pymongo.MongoClient.
        :param collection_name: The name of the collection in which documents persist.
        :param seq_enabled: If True, DAO will add a sequence number to all newly inserted documents.
        :param seq_collection_name: The name of the collection in which the last sequence number is stored.
        :param seq_num_counter_field: The name of the field in the collection where the last sequence number is stored.
        :param seq_num_field: The name of the document field is used for the sequence number.
        ;param auditable: If True, the DAO will manage auditable sub-documents.
        :param auditable_sub_doc_name: The name of the sub-document to be used for auditability.
        :param auditable_sub_doc_operation_type_field: The name of the field to be used for the operation type in the auditability sub-document.
        :param auditable_sub_doc_creation_date_field: The name of the field to be used for the creation date in the auditability sub-document.
        :param auditable_sub_doc_modification_date_field: The name of the field to be used for the modification date in the auditability sub-document.
        :param auditable_sub_doc_creator_field: The name of the field to be used for the creator in the auditability sub-document.
        :param auditable_sub_doc_modifier_field: The name of the field to be used for the modifier in the auditability sub-document.
        :param codec_options: An instance of [`bson.codec_options.CodecOptions`] to configure the codec options for the collection. See :method: pymongo.database.Database.get_collection for more details.
        :param read_preference: The read preference to use. See :method: pymongo.database.Database.get_collection for more details.
        :param write_concern: The write concern to use. See [`pymongo.database.Database.get_collection`] for more details.
        :param read_concern: The read concern to use. See [`pymongo.database.Database.get_collection`] for more details.
        :param indexes: A list of indexes to use for this collection.
        """
        super().__init__()
        self.logger: Logger = getLogger(
            f"{self.__class__.__module__}.{self.__class__.__name__}.{collection_name}"
        )
        self.database: Database = database
        self.collection: Collection = database.get_collection(
            collection_name, codec_options, read_preference, write_concern, read_concern
        )
        self.seq_enabled: bool = seq_enabled
        if seq_enabled:
            self.sequence_name: str = collection_name
            self.seq_num_counter_field: str = seq_num_counter_field
            self.sequences: Collection = database.get_collection(seq_collection_name)
            self.seq_num_field: str = seq_num_field
        self.auditable: bool = auditable
        if auditable:
            self.auditable_sub_doc_name: str = auditable_sub_doc_name
            self.auditable_sub_doc_operation_type_field: str = (
                auditable_sub_doc_operation_type_field
            )
            self.auditable_sub_doc_creation_date_field: str = (
                auditable_sub_doc_creation_date_field
            )
            self.auditable_sub_doc_modification_date_field: str = (
                auditable_sub_doc_modification_date_field
            )
            self.auditable_sub_doc_creator_field: str = auditable_sub_doc_creator_field
            self.auditable_sub_doc_modifier_field: str = (
                auditable_sub_doc_modifier_field
            )
        if indexes:
            self._ensure_indexes(indexes)

    def _ensure_indexes(self, indexes: List[Dict[str, Any]]) -> None:
        """
        Ensures that the specified indexes exist on the collection. If an index does not already exist,
        it will be created. The method compares index definitions provided in the input with the
        existing indexes of the collection to determine if creation is necessary.

        :param indexes: A list of index definitions where each definition includes `key` for the index fields and
            `options` for additional index options.
        """
        for index_def in indexes:
            key = index_def["key"]
            options = index_def.get("options", {})
            index_name = options.get("name", "_".join([f"{k[0]}_{k[1]}" for k in key]))

            if index_name not in self.collection.index_information():
                self.logger.info(
                    f"Index {index_name} not found. Creating index {index_name}"
                )
                self.collection.create_index(key, **options)
            else:
                self.logger.info(f"Index {index_name} found. Index already exists")

    def find(
        self,
        query: Any = None,
        skip: int = 0,
        limit: int = 0,
        sort: Optional[Union[list[str], dict[str, int]]] = None,
        projection=None,
        **kwargs,
    ):
        """
        Finds documents matching the specified query.

        :param query: The filter used to query the data collection. If the query is None, all documents are returned.
        :param skip: The number of documents to omit (from the start of the result set) when returning the results.
        :param limit: The maximum number of documents to return.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction,
            use 1 for ascending and -1 for descending.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find`] for more details.
        :return: The list of query matching documents. Itv returns an empty list if no document is found.
        """
        cursor = None
        try:
            cursor = self.collection.find(
                filter=query,
                projection=projection,
                skip=skip,
                limit=limit,
                sort=sort,
                **kwargs,
            )
            result = [d for d in cursor]
            return result
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)
        finally:
            cursor.close()

    def find_one(self, query: Any = None, projection=None, **kwargs):
        """
        Finds a single document in the collection that matches the given query.

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param query: The filter used to query the data collection. If the query is None, the first found document is
            returned.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find_one`] for more
            details.
        :return: The document matching the query.
        :raises ObjectNotFoundError: If no document matches the given query.
        """
        try:
            doc = self.collection.find_one(query, projection=projection, **kwargs)
            if doc is not None:
                return doc
            else:
                raise ObjectNotFoundError(self.collection.name, query)
        except ObjectNotFoundError as e:
            self.logger.warning(
                f"No documents found in {self.collection.name} for query: {query}"
            )
            raise e
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def find_one_by_id(
        self, oid: Union[ObjectId, str, bytes], projection=None, **kwargs
    ):
        """
        Finds a document by its identifier (i.e. by filtering on the '_id' field of the document).

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param oid: The id of the document.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
            fields to include or exclude.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find_one`] for more
            details.
        :return: The found document (if there is one).
        :raises ObjectNotFoundError: If no documents match the specified key.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.find_one(query, projection, **kwargs)

    def find_one_by_key(
        self, key: Union[ObjectId, str, bytes], projection=None, **kwargs
    ):
        """
        Finds a document by its key (synonym of `find_one_by_id`).

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param key: The key of the document.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find_one`] for more
            details.
        :return: The found document (if there is one).
        :raises ObjectNotFoundError: If no documents match the specified key.
        """
        return self.find_one_by_id(key, projection, **kwargs)

    def find_one_by_seq_num(self, seq_num: int, projection=None, **kwargs):
        """
        Finds a document by its sequence number.

        If no matching document is found, the method may raise an ObjectNotFound error.

        :param seq_num: The sequence number of the document.
        :param projection: A list of field names that should be returned in the resultset or a dict specifying the
        fields to include or exclude.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find_one`] for more
            details.
        :return: The found document (if there is one).
        :raises ObjectNotFoundError: If no documents match the specified key.
        """
        if self.seq_enabled:
            return self.find_one({self.seq_num_field: seq_num}, projection, **kwargs)
        else:
            message = f"Sequence number is not enabled for {self.__class__} on '{self.collection.name}' collection"
            self.logger.error(message)
            raise NotImplementedError(message)

    def count(self, query: Any = None, **kwargs) -> int:
        """
        Counts the number of documents matching the query.

        :param query: The filter used to query the collection.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.count_documents`] for more
            details.
        :return: The total number of documents.
        """
        if not query:
            query = {}
        try:
            return self.collection.count_documents(query, **kwargs)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def count_all(self, fast_count: bool = False, **kwargs) -> int:
        """
        Counts the number of all documents.

        :param fast_count: If True, uses the estimated document count provided by MongoDB.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.estimated_document_count`]
            and [`pymongo.collection.Collection.count_documents`] for more details.
        :return: The total number of documents.
        """
        if fast_count:
            return self.collection.estimated_document_count(**kwargs)
        else:
            return self.count({}, **kwargs)

    def delete(self, query: Any = None, **kwargs) -> DeleteResult:
        """
        Deletes the document identified by the given key.

        If no matching document is found, the method returns 0. Otherwise, it returns the number of deleted documents.

        :param query: The query filter used to query the documents to delete from the collection.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.delete_many`] for more
            details.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            native_result: pymongo.results.DeleteResult = self.collection.delete_many(
                query, **kwargs
            )
            return DeleteResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def delete_one(
        self,
        query: Any = None,
        sort: Optional[Union[list[str], dict[str, int]]] = None,
        **kwargs,
    ) -> DeleteResult:
        """
        Deletes the first document matching the query.

        :param query: The query filter to select the document to be deleted from the data collection.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.delete_one`] for more
            details.
        :param sort: A list of (key, direction) pairs specifying the sort order for this list. For sort direction, use
            1 for ascending and -1 for descending.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            native_result: DeleteResult = self.collection.delete_one(query, **kwargs)
            return DeleteResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def delete_one_by_id(
        self, oid: Union[ObjectId, str, bytes], **kwargs
    ) -> DeleteResult:
        """
        Deletes the document matching the specified identifier.
        :param oid: The id of the document.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.delete_one`] for more
            details.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.delete_one(query, **kwargs)

    def delete_one_by_key(
        self, key: Union[ObjectId, str, bytes], **kwargs
    ) -> DeleteResult:
        """
        Deletes the document identified by the given key (synonym of `delete_one_by_id`).

        :param key: The key of the document is to delete.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.delete_one`] for more
            details.
        :return: An instance of DeleteResult.
        :raises PersistenceError: If the operation generates an error.
        """
        return self.delete_one_by_id(key, **kwargs)

    def insert(
        self, data: Iterable[Dict], user: Optional[Union[str, Dict]] = None, **kwargs
    ) -> InsertResult:
        """
        Inserts many new documents into the data collection.

        :param data: The list of data to insert as new documents.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.insert_many`] for more
            details.
        :return: An instance of InsertResult.
        :raises PersistenceError: If the operation generates an error.
        """
        next_seq_num = (
            self._reserve_seq_num(sum(1 for _ in data)) if self.seq_enabled else None
        )
        auditable_sub_doc = (
            self._build_auditable_sub_document(OperationType.INSERT, user)
            if self.auditable
            else None
        )
        docs = []
        for d in data:
            doc = {**d}
            if self.seq_enabled:
                doc[self.seq_num_field] = next_seq_num
                next_seq_num += 1
            if self.auditable:
                doc[self.auditable_sub_doc_name] = auditable_sub_doc
            docs.append(doc)
        try:
            native_result: pymongo.results.InsertManyResult = (
                self.collection.insert_many(docs)
            )
            return InsertResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def insert_one(
        self, data: Dict, user: Optional[Union[str, Dict]] = None, **kwargs
    ) -> InsertResult:
        """
        Inserts a new document into the data collection.

        :param data: The data to insert.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.insert_one`] for more
            details.
        :return: An instance of InsertResult.
        :raises PersistenceError: If the operation generates an error.
        """
        return self.insert([data], user=user, **kwargs)

    def update(
        self,
        query: Any,
        change_set: Dict,
        upsert: bool = False,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ) -> UpdateResult:
        """
        Updates many documents in the database matching the provided query. The
        method will apply the given modifications defined in the data parameter.

        :param query: The query filter used to filter documents to update. Must define the matching criteria to find desired documents.
        :param change_set: The modifications to apply to the matched documents. Can include new values or transformations.
        :param upsert: Determines whether to insert a new document if no matching document exists.
            Defaults to False.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.update_many`](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.update_many) for more details.
        :return: Returns an instance of UpdateResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            data = {**change_set}
            if self.auditable:
                auditable_sub_doc = self._build_auditable_sub_document(
                    OperationType.UPDATE, user
                )
                data.update(auditable_sub_doc)
            native_result: pymongo.results.UpdateResult = self.collection.update_many(
                query, {"$set": data}, upsert=upsert, **kwargs
            )
            return UpdateResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def update_one(
        self,
        query: Any,
        change_set: Dict,
        upsert: bool = False,
        sort: Optional[Union[List[str], Dict[str, int]]] = None,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ) -> UpdateResult:
        """
        Updates the first document found matching the query using provided data.

        :param query: The query filter used to filter documents to update. Must define the matching criteria to find
            desired documents.
        :param change_set: The data to update.
        :param upsert: If True, the document will be inserted if it does not exist.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction,
            use 1 for ascending and -1 for descending.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.update_one`] for more details.
        :return: The updated document.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            update_instr = {"$set": change_set}
            data = {**change_set}
            if self.auditable:
                auditable_sub_doc = self._build_auditable_sub_document(
                    OperationType.UPDATE, user
                )
                # data[self.auditable_sub_doc_name] = auditable_sub_doc
                update_instr = {
                    "$set": {
                        **change_set,
                        **{
                            f"{self.auditable_sub_doc_name}.{k}": v
                            for k, v in auditable_sub_doc.items()
                        },
                    }
                }
            # TODO: Check why introduction of `sort` parameter doesn't work (`TypeError`).
            # TODO: To be tested with a real database and not only with [mongomock](https://github.com/mongomock)
            # SEE: Changed in version 4.11 [pymongo.collection.Collection.update_one](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.update_one)
            # native_result: pymongo.results.UpdateResult = self.collection.update_one(query, {'$set': change_set},
            #                                                                         upsert=upsert, sort=sort, **kwargs)
            # WORKAROUND
            native_result: pymongo.results.UpdateResult = self.collection.update_one(
                query, update_instr, upsert=upsert, **kwargs
            )
            return UpdateResult(native_result)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def update_one_by_id(
        self,
        oid: Union[ObjectId, str, bytes],
        change_set: Dict,
        upsert: bool = False,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ) -> UpdateResult:
        """
        Updates the document associated with the given key using provided data.

        :param oid: The id of the document to update.
        :param change_set: The data to update.
        :param upsert: If True, the document will be inserted if it does not exist.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.update_one`] for more details.
        :return: The updated document.
        :raises PersistenceError: If the operation generates an error.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.update_one(query, change_set, upsert=upsert, user=user, **kwargs)

    def update_one_by_key(
        self,
        key: Union[ObjectId, str, bytes],
        change_set: Dict,
        upsert: bool = False,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ) -> UpdateResult:
        """
        Updates the document associated with the given key using provided data (synonym of `delete_one_by_id`).

        :param key: The key of the document is to update.
        :param change_set: The data to update.
        :param upsert: If True, the document will be inserted if it does not exist.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.update_one`] for more details.
        :return: An instance of UpdateResult.
        """
        return self.update_one_by_id(
            key, change_set, upsert=upsert, user=user, **kwargs
        )

    def replace(
        self,
        query: Any,
        data: Dict,
        upsert: bool = False,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ):
        """
        Replaces the documents matching the query with the provided data.

        Identifier and sequence number of the records have to be preserved during the replacement.

        :param query: The query filter used to locate the document that will be replaced. This
            determines the condition for document matching.
        :param data: The new data that will replace the matched document. This should be in an
            acceptable format for the database.
        :param upsert: If True, the document will be inserted if it does not exist.
            Defaults to False.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find`] and
            [`pymongo.collection.Collection.replace_one`] for more details.
        :return: An instance of ReplaceResult.
        :raises PersistenceError: If the operation generates an error.
        """
        try:
            matching_doc_ids = self.lookup(query, **kwargs)
            replace_count = 0
            upsert_count = 0
            replaced_ids = []
            inserted_ids = []
            native_results = []
            for doc_id in matching_doc_ids:
                result: ReplaceResult = self.replace_one_by_id(
                    doc_id, data, upsert=upsert, user=user, **kwargs
                )
                replace_count += result.replaced_count
                upsert_count += result.upsert_count
                replaced_ids.append(result.replaced_ids)
                inserted_ids.append(result.inserted_keys)
                native_results.append(result.native_result)
            return ReplaceResult(
                replace_count,
                upsert_count,
                replaced_keys=replaced_ids,
                inserted_keys=inserted_ids,
                native_result=native_results,
            )
        except PersistenceError as e:
            self.logger.error(f"Document replacement failure: {e}")
            raise PersistenceError("Document replacement failure.", e)
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error.", e)

    def replace_one(
        self,
        query: Any,
        data: Dict,
        upsert: bool = False,
        sort: Optional[Union[List[str], Dict[str, int]]] = None,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ) -> ReplaceResult:
        """
        Replaces the first document matching the query with the provided data.

        Identifier and sequence number of the records have to be preserved during the replacement.

        :param query: The query filter used to locate the document that will be replaced. This determines the condition
            for document matching.
        :param data: The new data that will replace the matched document. This should be in an acceptable format for the
            database.
        :param upsert: If True, the document will be inserted if it does not exist.
            Defaults to False.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction,
            use 1 for ascending and -1 for descending.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find`] for more details.
        :return: An instance of ReplaceResult.
        :raises PersistenceError: If the operation generates an error.
        """
        document = {**data}
        try:
            existing_doc = self.find_one(query, sort=sort, **kwargs)
            doc_id = str(existing_doc[_ID_FIELD])
            if self.seq_enabled:
                seq_num = existing_doc.get(self.seq_num_field, None)
                if seq_num:
                    document[self.seq_num_field] = seq_num
                else:
                    document[self.seq_num_field] = self._reserve_seq_num()
            if self.auditable:
                auditable_sub_doc = existing_doc.get(self.auditable_sub_doc_name, None)
                auditable_sub_doc_update = self._build_auditable_sub_document(
                    OperationType.REPLACE, user
                )
                if auditable_sub_doc:
                    auditable_sub_doc.update(auditable_sub_doc_update)
                else:
                    auditable_sub_doc = auditable_sub_doc_update
                    auditable_sub_doc[self.auditable_sub_doc_creation_date_field] = None
                    auditable_sub_doc[self.auditable_sub_doc_creator_field] = None
                document[self.auditable_sub_doc_name] = auditable_sub_doc
            query_filter = {_ID_FIELD: ObjectId(doc_id)}
            native_result: pymongo.results.UpdateResult = self.collection.replace_one(
                query_filter, document, upsert=False, **kwargs
            )

            return ReplaceResult(
                1,
                0,
                replaced_keys=[doc_id],
                inserted_keys=[],
                native_result=native_result,
            )
        except ObjectNotFoundError:
            res: InsertResult = self.insert_one(data, user=user, **kwargs)
            return ReplaceResult(
                0,
                res.inserted_count,
                replaced_keys=[],
                inserted_keys=res.inserted_ids,
                native_result=res.native_result,
            )
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def replace_one_by_id(
        self,
        oid: Union[ObjectId, str, bytes],
        data: Any,
        upsert: bool = False,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ) -> ReplaceResult:
        """
        Replaces the record associated with the given key using provided data.

        The identifier has to be preserved during the replacement.

        :param oid: The id of the record to replace.
        :param data: The data to replace.
        :param upsert: If True, the record will be inserted if it does not exist.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.replace_one for
            more details.
        :return: An instance of ReplaceResult.
        """
        query = {_ID_FIELD: ObjectId(oid)} if isinstance(oid, str) else {_ID_FIELD: oid}
        return self.replace_one(query, data, upsert=upsert, user=user, **kwargs)

    def replace_one_by_key(
        self,
        key: Union[ObjectId, str, bytes],
        data: Any,
        upsert: bool = False,
        user: Optional[Union[str, Dict]] = None,
        **kwargs,
    ) -> ReplaceResult:
        """
        Replaces the record associated with the given key using provided data.

        The identifier has to be preserved during the replacement.

        :param key: The key of the record to replace.
        :param data: The data to replace.
        :param upsert: If True, the record will be inserted if it does not exist.
        :param user: Information about the user performing the operation. This information will be included in the
            auditability sub-document if this behavior is enabled.
        :param kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.replace_one for
            more details.
        :return: An instance of ReplaceResult.
        """
        return self.replace_one_by_id(key, data, upsert=upsert, user=user, **kwargs)

    def lookup(
        self,
        query: Any = None,
        skip: int = 0,
        limit: int = 0,
        sort: Optional[Union[list[str], dict[str, int]]] = None,
        **kwargs,
    ) -> list[str]:
        """
        Retrieves ids of documents matching the specified query

        :param query: The filter used to query the data collection. If the query is None, all documents are returned.
        :param skip: The number of documents to omit (from the start of the result set) when returning the results.
        :param limit: The maximum number of documents to return.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction,
            use 1 for ascending and -1 for descending.
        :kwargs: Implementation specific arguments. See :method: pymongo.collection.Collection.find for more details.
        :return: List of matching document ids
        :raises PersistenceError: if an unexpected error occurs during the operation
        """
        docs = self.find(
            query,
            skip=skip,
            limit=limit,
            sort=sort,
            projection=[_ID_FIELD],
            **kwargs,
        )
        result = [str(doc[_ID_FIELD]) for doc in docs]
        return result

    def lookup_one(
        self, query=None, sort: Union[None, list[str], dict[str, int]] = None, **kwargs
    ) -> Optional[str]:
        """
        Retrieves the id of the first document found matching the specified query
        :param query: The filter used to query the data collection. If the query is None, all documents are returned.
        :param sort: A list of (field key, direction) pairs specifying the sort order for this list. For sort direction,
            use 1 for ascending and -1 for descending.
        :kwargs: Implementation specific arguments. See [`pymongo.collection.Collection.find_one`] for more details.
        :return: The id of the first document found matching the query
        :raises ObjectNotFoundError: if no document is found
        :raises PersistenceError: if an unexpected error occurs during the operation
        """
        try:
            doc = self.find_one(query, sort=sort, projection=[_ID_FIELD], **kwargs)
            if doc is not None:
                return str(doc[_ID_FIELD])
            else:
                raise ObjectNotFoundError(self.collection.name, query)
        except ObjectNotFoundError as e:
            self.logger.warning(
                f"No documents found in {self.collection.name} for query: {query}"
            )
            raise e
        except PyMongoError as e:
            self.logger.error(f"Database error: {e}")
            raise PersistenceError("Unexpected error", e)

    def _reserve_seq_num(self, count: int = 1) -> int:
        """
        Reserves the specified number of sequence numbers and returns the first sequence number reserved.

        :param count: The number of sequence numbers to reserve.
            Defaults to 1.
        :return: The first reserved sequence number (i.e., the next sequence number to use).
        """
        result = self.sequences.find_one_and_update(
            {_ID_FIELD: self.sequence_name},
            {"$inc": {self.seq_num_counter_field: count}},
            projection={
                self.seq_num_counter_field: True,
                _ID_FIELD: False,
            },
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )
        return result[self.seq_num_counter_field] - count + 1

    def _get_last_reserved_seq_num(self) -> int:
        """
        Retrieves the last reserved sequence number from a database.

        This method queries the *sequences* collection in the database to fetch the last
        reserved sequence number for the given sequence name. If no record is found,
        it defaults to returning 0.

        :return: The last reserved sequence number.
        """
        result = self.sequences.find_one(
            {_ID_FIELD: self.sequence_name},
            projection={self.seq_num_counter_field: True},
        )
        return result[SEQUENCE_COUNTER_DEFAULT_FIELD] if result is not None else 0

    def _build_auditable_sub_document(
        self, operation_type: OperationType, user: Optional[Union[str, Dict]] = None
    ) -> Dict:
        """
        Builds an auditable sub-document for tracking the operation type and timestamps.

        This function generates a dictionary that includes operation type and modification timestamp. If the operation
        type is an insert, it also includes the creation timestamp. Additionally, if a user is provided, it will include
         the creator information for insert operations.

        :param operation_type: Type of the operation to be recorded.
        :param user: Information about the user performing the operation. Can be
            a string representing the username or a dictionary containing user details.
        :return: Dictionary representing the auditable sub-document with operation and timestamp details.
        """
        ts = datetime.now(timezone.utc)
        auditable = {
            self.auditable_sub_doc_operation_type_field: operation_type.value,
            self.auditable_sub_doc_modification_date_field: ts,
        }
        if user is not None:
            auditable[self.auditable_sub_doc_modifier_field] = user
        if operation_type == OperationType.INSERT:
            auditable[self.auditable_sub_doc_creation_date_field] = ts
            if user is not None:
                auditable[self.auditable_sub_doc_creator_field] = user
        return auditable
