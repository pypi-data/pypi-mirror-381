from peliqan.exceptions import PeliqanClientException, OperationNotSupported
from peliqan.client.base import BaseClient
from peliqan.utils import empty, _check_record_byte_size

import pandas as pd
import json


class DBClient(BaseClient):
    is_trino = False

    def __init__(self, connection, jwt, backend_url):
        super(DBClient, self).__init__(jwt, backend_url)
        self.connection = connection

    def db_via_proxy(self, db_name, schema_name, table_name, pk, action, kwargs=None):
        # pk has same identity as empty declared above
        if pk is empty:
            raise PeliqanClientException("'pk' must be provided.")

        if kwargs is None:
            kwargs = {}
    
        payload = {
            "connection": self.connection,
            "dbName": db_name,
            "schemaName": schema_name,
            "tableName": table_name,
            "pk": pk,
            "action": action,
            "kwargs": kwargs
        }
        url = f"{self.BACKEND_URL}/api/proxy/db/"
        return self.call_backend('post', url, json=payload)

    def create_schema(self, db_name, schema_name):
        response = self.db_via_proxy(db_name, schema_name, None, None, 'create_schema')
        return response

    def create_table(self, db_name, schema_name, table_name, fields=None, pk=None):
        response = self.db_via_proxy(
            db_name,
            schema_name,
            table_name,
            pk,
            'create_table',
            kwargs={'fields': fields}
        )
        return response

    def insert(self, db_name, schema_name, table_name, *args, **kwargs):
        # allow using both keyword arguments or a dict as argument:
        # pq.insert("my_db", "my_table", name='John', city='NY') or pq.insert("my_db", "my_table", contact_obj)
        kwargs = self.args_to_kwargs(args, kwargs)
        response = self.db_via_proxy(db_name, schema_name, table_name, None, 'insert', kwargs=kwargs)
        return response

    def update(self, db_name, schema_name, table_name, pk=empty, *args, **kwargs):
        # allow using both keyword arguments or a dict as argument:
        # pq.update("my_db", "my_table", id=1, name='John', city='NY') or pq.update("my_db", "my_table", contact_obj)
        kwargs = self.args_to_kwargs(args, kwargs)
        response = self.db_via_proxy(db_name, schema_name, table_name, pk, 'update', kwargs=kwargs)
        return response

    def upsert(self, db_name, schema_name, table_name, pk=empty, *args, **kwargs):
        # allow using both keyword arguments or a dict as argument:
        # pq.update("my_db", "my_table", id=1, name='John', city='NY') or pq.update("my_db", "my_table", contact_obj)
        kwargs = self.args_to_kwargs(args, kwargs)
        response = self.db_via_proxy(db_name, schema_name, table_name, pk, 'upsert', kwargs=kwargs)
        return response
    def materialize(self,db_name, **kwargs):
        """
        Materialize a table in Trino.
        :param table_config_list: List of table configurations.
        :param target_schema: The schema where the materialized table will be created.
        :return: Response from the backend.
        """
        # kwargs for generate_lineage will be set as true
        kwargs['generate_lineage'] = True
        response = self.db_via_proxy(
            db_name=db_name,
            schema_name=None,
            table_name=None,
            pk=None,
            action='materialize',
            kwargs=kwargs,
        )
        return response
    def _to_dtype(self, column_type, tz, enable_datetime_as_string):
        if (
            column_type[0:6].lower() == "double" or
            column_type[0:5].lower() == "float" or
            column_type[0:7].lower() == "decimal" or
            column_type[0:7].lower() == "numeric"
        ):
            type_name = pd.Float64Dtype()

        elif (
            column_type[0:3].lower() == "int" or
            column_type[0:6].lower() == "bigint" or
            column_type[0:3].lower() == "num"
        ):  # todo add more field types
            type_name = pd.Int64Dtype()

        elif column_type[0:4].lower() == "bool":
            type_name = pd.BooleanDtype()

        elif not enable_datetime_as_string and (
            column_type == "date" or
            column_type[0:9].lower() == "timestamp" or
            column_type[0:8].lower() == "datetime"
        ):
            type_name = pd.DatetimeTZDtype(tz=tz)

        elif column_type[0:4].lower() == "json" and self.is_trino:
            type_name = 'json_str'

        elif column_type[0:4].lower() == "json":
            type_name = 'json'

        else:
            type_name = pd.StringDtype()

        return type_name

    def _convert_result_to_df(self, json_response, error, df=False, fillna_with=None, fillnat_with=None,
                              enable_python_types=True, enable_datetime_as_string=True, tz='UTC'):
        if error:
            raise PeliqanClientException(f"Client encountered a error while fetching records.\n{error}")

        records = json_response['records']
        column_data = json_response['columns']

        columns = []
        dtypes = []
        for column in column_data:
            dtypes.append((column[0], self._to_dtype(column[1], tz, enable_datetime_as_string)))
            columns.append(column[0])

        # Create dataframe
        dataframe = pd.DataFrame(records, columns=columns)
        if enable_python_types:
            for dtype in dtypes:
                if dtype[1] == 'json_str':
                    try:
                        dataframe[dtype[0]] = dataframe[dtype[0]].apply(json.loads)
                    except Exception:
                        pass

                elif dtype[1] != 'json':
                    dataframe[dtype[0]] = dataframe[dtype[0]].astype(dtype[1])

        dataframe.replace({pd.NaT: fillnat_with, pd.NA: fillna_with}, inplace=True)

        if df:
            return dataframe

        else:
            return dataframe.to_dict('records')

    def fetch(
        self, db_name, schema_name=None, table_name=None, query=None, df=False, fillna_with=None,
        fillnat_with=None, enable_python_types=True, enable_datetime_as_string=True, tz='UTC'
    ):
        json_response = self.db_via_proxy(
            db_name,
            schema_name,
            table_name,
            None,
            'fetch',
            kwargs={'query': query}
        )
        detail = json_response['detail']
        error = json_response['status'] == 'failed'
        if error:
            error = detail or error
        return self._convert_result_to_df(detail, error, df, fillna_with, fillnat_with, enable_python_types,
                                          enable_datetime_as_string, tz)

    def delete(self, db_name, schema_name, table_name, pk):
        response = self.db_via_proxy(db_name, schema_name, table_name, pk, 'delete')
        return response

    def execute(self, db_name, query):
        kwargs = {'query': query}
        response = self.db_via_proxy(
            db_name,
            None,
            None,
            None,
            'execute',
            kwargs=kwargs
        )
        return response

    def write(
        self,
        schema_name,
        table_name,
        records,
        object_schema=None,
        pk=None,
        db_name=None,
        transformer_mode='lossless',
        decimal_separator='.'
    ):
        if pk is None:
            pk = []

        if isinstance(records, pd.DataFrame):
            records.replace({pd.NaT: None, pd.NA: None}, inplace=True)
            records = records.to_dict('records')

        if isinstance(records, pd.Series):
            records.replace({pd.NaT: None, pd.NA: None}, inplace=True)
            records = records.to_dict()

        if not isinstance(records, (list, tuple)):
            if isinstance(records, dict):
                records = [records]
            else:
                raise PeliqanClientException("records must be a dataframe, a series, a list or a dict")

        if not isinstance(pk, list):
            if isinstance(pk, str):
                pk = [pk]
            else:
                raise PeliqanClientException("pk has to be either a string or a list")

        _check_record_byte_size(records)
        kwargs = {
            'records': records,
            'object_schema': object_schema,
            'transformer_mode': transformer_mode,
            'decimal_separator': decimal_separator
        }
        response = self.db_via_proxy(db_name, schema_name, table_name, pk, 'write_records', kwargs=kwargs)
        return response


class PeliqanTrinoDBClient(DBClient):
    is_trino = True

    def create_schema(self, db_name, schema_name):
        raise OperationNotSupported("'create_schema' operation is not support by Peliqan Trino")

    def create_table(self, db_name, schema_name, table_name, fields=None, pk=None):
        raise OperationNotSupported("'create_table' operation is not support by Peliqan Trino")

    def insert(self, db_name, schema_name, table_name, *args, **kwargs):
        raise OperationNotSupported("'insert' operation is not support by Peliqan Trino")

    def update(self, db_name, schema_name, table_name, pk=empty, *args, **kwargs):
        raise OperationNotSupported("'update' operation is not support by Peliqan Trino")

    def upsert(self, db_name, schema_name, table_name, pk=empty, *args, **kwargs):
        raise OperationNotSupported("'update' operation is not support by Peliqan Trino")

    def write(
        self,
        schema_name,
        table_name,
        records,
        object_schema=None,
        pk=None,
        db_name=None,
        transformer_mode='lossless',
        decimal_separator='.'
    ):
        raise OperationNotSupported("'write' operation is not support by Peliqan Trino")

    def execute(self, query, *args, **kwargs):
        """
        Execute a query on the Trino server.
        :param query:
        :return:
        """

        body = {
            "query": query
        }

        url = f"{self.BACKEND_URL}/api/database/resource/trino/execute/"
        response_dict = self.call_backend("post", url, json=body)
        return response_dict

    def fetch(
        self, db_name=None, schema_name=None, table_name=None,
        query=None, table_id=None, df=False,
        fillna_with=None, fillnat_with=None,
        enable_python_types=True, enable_datetime_as_string=True, tz='UTC'
    ):
        """
            Return the records in a table.
            :param db_name: The name of a database.
            :param schema_name: The name of a schema a table belongs to.
            :param table_name: The name of a table.
            :param query: A valid Trino sql query.
            :param table_id: An integer value that uniquely identifies a table.
            :param df: This flag decides what should be returned by this function. df=True returns a dataframe. df=False returns an array of dicts, where each item represents a row with column name as the key.
            :param fillna_with: Replace empty/invalid values (NA) with a default value. This will also replace NaN values.
            :param fillnat_with: Replace invalid time/datetime values (NaT) with a default value.
            :param enable_python_types: This flag will cause the record's values to be returned as python types
            :param enable_datetime_as_string: This flag will cause date/time/datetime objects to be converted to string.
            :param tz: This is the timezone that will be used to convert date and datetime strings
            to timezone aware datetime objects. This value defaults to 'UTC'.

            :return:
        """

        # table_id will return the raw table data.
        # This causes multiple select and single select to be returned as json objects

        # query and table_name will return the data as if the queried table is a prepended statement.
        # This causes multiple select and single select to be returned as strings instead of a json object

        if not table_id and not table_name and not query:
            raise PeliqanClientException("Input 'table_name' (table or view name), 'query' or 'table_id' must be set.")

        body = {
            'db_name': db_name,
            'schema_name': schema_name,
            'table_name': table_name,
            'table_id': table_id,
            'query': query,
        }

        # Fetch Trino catalog and SQL query with all CDC changes applied
        url = f"{self.BACKEND_URL}/api/database/resource/trino/records/"
        response_dict = self.call_backend("post", url, json=body)
        json_response = response_dict

        error = json_response['error']
        return self._convert_result_to_df(json_response, error, df, fillna_with, fillnat_with, enable_python_types,
                                          enable_datetime_as_string, tz)
