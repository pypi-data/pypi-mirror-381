import logging
import os
import re
import warnings
from typing import Any, Dict, List, Optional, Set, Union
from urllib.parse import quote_plus

import sqlalchemy

# To support key pair authentication
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from snowflake.sqlalchemy import URL

from tundra.logger import GLOBAL_LOGGER as logger

# Don't show all the info log messages from Snowflake
for logger_name in ["snowflake.connector", "bot", "boto3"]:
    log = logging.getLogger(logger_name)
    log.setLevel(logging.WARNING)


class SnowflakeConnector:
    def __init__(self, config: Optional[Dict] = None) -> None:
        if not config:
            config = {
                "user": os.getenv("PERMISSION_BOT_USER"),
                "password": quote_plus(os.getenv("PERMISSION_BOT_PASSWORD", "")),
                "account": os.getenv("PERMISSION_BOT_ACCOUNT"),
                "database": os.getenv("PERMISSION_BOT_DATABASE"),
                "role": os.getenv("PERMISSION_BOT_ROLE"),
                "warehouse": os.getenv("PERMISSION_BOT_WAREHOUSE"),
                "oauth_token": os.getenv("PERMISSION_BOT_OAUTH_TOKEN"),
                "key_path": os.getenv("PERMISSION_BOT_KEY_PATH"),
                "key_passphrase": os.getenv("PERMISSION_BOT_KEY_PASSPHRASE"),
                "authenticator": os.getenv("PERMISSION_BOT_AUTHENTICATOR"),
            }

        if config["oauth_token"] is not None:
            self.engine = sqlalchemy.create_engine(
                URL(
                    user=config["user"],
                    account=config["account"],
                    authenticator="oauth",
                    token=config["oauth_token"],
                    warehouse=config["warehouse"],
                )
            )
        elif config["key_path"] is not None:
            pkb = self.generate_private_key(
                config["key_path"], config.get("key_passphrase")
            )
            self.engine = sqlalchemy.create_engine(
                URL(
                    user=config["user"],
                    account=config["account"],
                    database=config["database"],
                    role=config["role"],
                    warehouse=config["warehouse"],
                ),
                connect_args={"private_key": pkb},
            )

        elif config["authenticator"] is not None:
            self.engine = sqlalchemy.create_engine(
                URL(
                    user=config["user"],
                    account=config["account"],
                    database=config["database"],
                    role=config["role"],
                    warehouse=config["warehouse"],
                    authenticator=config["authenticator"],
                ),
            )
        else:
            if not config["user"]:
                raise Exception(
                    "Validation Error: PERMISSION_BOT_USER not set. Please ensure environment variables are set."
                )
            self.engine = sqlalchemy.create_engine(
                URL(
                    user=config["user"],
                    password=config["password"],
                    account=config["account"],
                    database=config["database"],
                    role=config["role"],
                    warehouse=config["warehouse"],
                    # Enable the insecure_mode if you get OCSP errors while testing
                    # insecure_mode=True,
                )
            )

    @staticmethod
    def generate_private_key(
            key_path: str, key_passphrase: Union[str, None]
    ) -> bytes:
        with open(key_path, "rb") as key:
            encoded_key = None
            if key_passphrase:
                encoded_key = key_passphrase.encode()
            p_key = serialization.load_pem_private_key(
                key.read(), password=encoded_key, backend=default_backend()
            )

        return p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

    def show_query(self, entity) -> List[str]:
        names = []

        query = f"SHOW {entity}"
        results = self.run_query(query).fetchall()

        for result in results:
            # lowercase the entity if alphanumeric plus _ else leave as is
            names.append(
                result["name"].lower()
                if bool(re.match("^[a-zA-Z0-9_]*$", result["name"]))
                else result["name"]
            )

        return names

    def show_databases(self) -> List[str]:
        return self.show_query("DATABASES")

    def show_warehouses(self) -> List[str]:
        return self.show_query("WAREHOUSES")

    def show_integrations(self) -> List[str]:
        return self.show_query("INTEGRATIONS")

    def show_external_volumes(self) -> List[str]:
        return self.show_query("EXTERNAL VOLUMES")

    def show_iceberg_tables(
        self, database: Optional[str] = None, schema: Optional[str] = None
    ) -> List[str]:
        names = []

        if schema:
            query = f"SHOW ICEBERG TABLES IN SCHEMA {schema}"
        elif database:
            query = f"SHOW ICEBERG TABLES IN DATABASE {database}"
        else:
            query = "SHOW ICEBERG TABLES IN ACCOUNT"

        results = self.run_query(query).fetchall()

        for result in results:
            table_identifier = (
                f"{result['database_name']}.{result['schema_name']}.{result['name']}"
            )
            names.append(SnowflakeConnector.snowflaky(table_identifier))

        return names

    def show_users(self) -> List[str]:
        return self.show_query("USERS")

    def show_schemas(self, database: Optional[str] = None) -> List[str]:
        names = []

        if database:
            query = f"SHOW TERSE SCHEMAS IN DATABASE {database}"
        else:
            query = "SHOW TERSE SCHEMAS IN ACCOUNT"

        results = self.run_query(query).fetchall()

        for result in results:
            schema_identifier = f"{result['database_name']}.{result['name']}"
            names.append(SnowflakeConnector.snowflaky(schema_identifier))

        return names

    def show_tables(
        self, database: Optional[str] = None, schema: Optional[str] = None
    ) -> List[str]:
        names = []

        if schema:
            query = f"SHOW TERSE TABLES IN SCHEMA {schema}"
        elif database:
            query = f"SHOW TERSE TABLES IN DATABASE {database}"
        else:
            query = "SHOW TERSE TABLES IN ACCOUNT"

        results = self.run_query(query).fetchall()

        for result in results:
            table_identifier = (
                f"{result['database_name']}.{result['schema_name']}.{result['name']}"
            )
            names.append(SnowflakeConnector.snowflaky(table_identifier))

        return names

    def show_views(
        self, database: Optional[str] = None, schema: Optional[str] = None
    ) -> List[str]:
        names = []

        if schema:
            query = f"SHOW TERSE VIEWS IN SCHEMA {schema}"
        elif database:
            query = f"SHOW TERSE VIEWS IN DATABASE {database}"
        else:
            query = "SHOW TERSE VIEWS IN ACCOUNT"

        results = self.run_query(query).fetchall()

        for result in results:
            view_identifier = (
                f"{result['database_name']}.{result['schema_name']}.{result['name']}"
            )
            names.append(SnowflakeConnector.snowflaky(view_identifier))

        return names

    def show_future_grants(
        self, database: Optional[str] = None, schema: Optional[str] = None
    ) -> Dict[str, Dict[str, Dict[str, List[str]]]]:
        future_grants: Dict[str, Any] = {}

        if schema:
            query = f"SHOW FUTURE GRANTS IN SCHEMA {schema}"
        elif database:
            query = f"SHOW FUTURE GRANTS IN DATABASE {database}"
        else:
            pass

        results = self.run_query(query).fetchall()

        for result in results:
            if result["grant_to"] == "ROLE":
                role = result["grantee_name"].lower()
                privilege = result["privilege"].lower()
                granted_on = result["grant_on"].lower()

                if bool(re.match("^[a-zA-Z0-9_]*$", result["name"])):
                    clean_name = result["name"].lower()
                else:
                    clean_name = result["name"]

                future_grants.setdefault(role, {}).setdefault(privilege, {}).setdefault(
                    granted_on, []
                ).append(SnowflakeConnector.snowflaky(result["name"]))

            else:
                continue

        return future_grants

    def show_grants_to_role(self, role) -> Dict[str, Any]:
        grants: Dict[str, Any] = {}
        if role in ["*", '"*"']:
            return grants

        query = f"SHOW GRANTS TO ROLE {SnowflakeConnector.snowflaky_user_role(role)}"

        results = self.run_query(query).fetchall()

        for result in results:
            privilege = result["privilege"].lower()
            granted_on = result["granted_on"].lower()

            if bool(re.match("^[a-zA-Z0-9_]*$", result["name"])):
                clean_name = result["name"].lower()
            else:
                clean_name = result["name"]

            grants.setdefault(privilege, {}).setdefault(granted_on, []).append(
                SnowflakeConnector.snowflaky(clean_name)
            )

        return grants

    def show_grants_to_role_with_grant_option(self, role) -> Dict[str, Any]:
        grants: Dict[str, Any] = {}

        query = f"SHOW GRANTS TO ROLE {SnowflakeConnector.snowflaky(role)}"
        results = self.run_query(query).fetchall()

        for result in results:
            privilege = result["privilege"].lower()
            granted_on = result["granted_on"].lower()
            grant_option = result["grant_option"].lower() == "true"

            if bool(re.match("^[a-zA-Z0-9_]*$", result["name"])):
                clean_name = SnowflakeConnector.snowflaky(result["name"].lower())
            else:
                clean_name = SnowflakeConnector.snowflaky(result["name"])

            grants.setdefault(privilege, {}).setdefault(granted_on, {}).setdefault(
                clean_name, {}
            ).update({"grant_option": grant_option})

        return grants

    def show_roles_granted_to_user(self, user) -> List[str]:
        roles = []

        query = f"SHOW GRANTS TO USER {SnowflakeConnector.snowflaky_user_role(user)}"
        results = self.run_query(query).fetchall()

        for result in results:
            if bool(re.match("^[a-zA-Z0-9_]*$", result["role"])):
                clean_role = SnowflakeConnector.snowflaky(result["role"].lower())
            else:
                clean_role = SnowflakeConnector.snowflaky(result["role"])
            roles.append(clean_role)

        return roles

    def get_current_user(self) -> str:
        query = "SELECT CURRENT_USER() AS USER"
        result = self.run_query(query).fetchone()
        return result["user"].lower()

    def get_current_role(self) -> str:
        query = "SELECT CURRENT_ROLE() AS ROLE"
        result = self.run_query(query).fetchone()
        return result["role"].lower()

    def show_roles(self) -> Dict[str, str]:
        roles = {}

        query = "SHOW ROLES"
        results = self.run_query(query).fetchall()

        for result in results:
            roles[
                SnowflakeConnector.snowflaky(result["name"])
            ] = SnowflakeConnector.snowflaky(result["owner"])
        return roles

    def run_query(self, query: str):
        from sqlalchemy import text
        with self.engine.connect() as connection:
            logger.debug(f"Running query: {query}")
            result = connection.execute(text(query))

        return result

    def full_schema_list(self, schema: str) -> List[str]:
        """
        For a given schema name, get all schemas it may be referencing.

        For example, if <db>.* is given then all schemas in the database
        will be returned. If <db>.<schema_partial>_* is given, then all
        schemas that match the schema partial pattern will be returned.
        If a full schema name is given, it will return that single schema
        as a list.

        This function can be enhanced in the future to handle more
        complicated schema names if necessary.

        Returns a list of schema names.
        """
        # Generate the information_schema identifier for that database
        # in order to be able to filter it out
        name_parts = schema.split(".")

        info_schema = f"{name_parts[0]}.information_schema"

        fetched_schemas = []

        # All Schemas
        if name_parts[1] == "*":
            db_schemas = self.show_schemas(name_parts[0])
            for db_schema in db_schemas:
                if db_schema != info_schema:
                    fetched_schemas.append(db_schema)

        # Prefix and suffix schema matches
        elif "*" in name_parts[1]:
            db_schemas = self.show_schemas(name_parts[0])
            for db_schema in db_schemas:
                schema_name = db_schema.split(".", 1)[1].lower()
                if name_parts[1].endswith("*") and schema_name.startswith(
                    name_parts[1].split("*", 1)[0]
                ):
                    if db_schema != info_schema:
                        fetched_schemas.append(db_schema)
                elif name_parts[1].startswith("*") and schema_name.endswith(
                    name_parts[1].split("*", 1)[1]
                ):
                    if db_schema != info_schema:
                        fetched_schemas.append(db_schema)

        # TODO: Handle more complicated matches

        else:
            # If no * in name, then return provided schema name
            fetched_schemas = [schema]

        return fetched_schemas

    @staticmethod
    def snowflaky(name: str) -> str:
        """
        Convert an entity name to an object identifier that will most probably be
        the proper name for Snowflake.

        e.g. gitlab-ci --> "gitlab-ci"
             527-INVESTIGATE$ISSUES.ANALYTICS.COUNTRY_CODES -->
             --> "527-INVESTIGATE$ISSUES".ANALYTICS.COUNTRY_CODES;
             DEPARTMENT - DATA --> "DEPARTMENT - DATA"

        Pronounced /snəʊfleɪkɪ/ like saying very fast snowflak[e and clarif]y
        Permission granted to use snowflaky as a verb.
        """
        if name is not None:
            name_parts = name.split(".")
        else:
            name_parts = []

        # We do not currently support identifiers that include periods (i.e. db_1.schema_1."table.with.period")
        if len(name_parts) > 3:
            warnings.warn(
                f"Unsupported object identifier: {name} contains additional periods within identifier.",
                SyntaxWarning,
            )

        if len(name_parts) == 0:
            warnings.warn(
                "Object identifier is Null",
                SyntaxWarning,
            )

        new_name_parts = []

        for part in name_parts:
            # If already quoted, return as-is
            if re.match('^".*"$', part) is not None:
                new_name_parts.append(part)

            # If a future object, return in lower case - no need to quote
            elif re.match("<(table|view|schema)>", part, re.IGNORECASE) is not None:
                new_name_parts.append(part.lower())

            # If does not meet requirements for unquoted object identifiers or collides with reserved keywords,
            # add double-quotes. See https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html for what
            # those requirements are and https://docs.snowflake.com/en/sql-reference/reserved-keywords for keywords
            elif (
                re.match("^[a-z_][0-9a-z_$]*$", part) is None
                and re.match("^[A-Z_][0-9A-Z_$]*$", part) is None
            ) or part.lower() in SnowflakeConnector.reserved_keywords():
                new_name_parts.append(f'"{part}"')

            else:
                new_name_parts.append(part.lower())

        return ".".join(new_name_parts)

    @staticmethod
    def snowflaky_user_role(name: str) -> str:
        """
        Convert users/roles to an object identifier that will most probably be
        the proper name for Snowflake.

        e.g. gitlab-ci --> "gitlab-ci"
             blake.enyart@gmail.com --> "blake.enyart@gmail.com"

        Pronounced /snəʊfleɪkɪ/ like saying very fast snowflak[e and clarif]y
        Permission granted to use snowflaky as a verb.
        """
        if (
            re.match("^[0-9a-zA-Z_]*$", name) is None  # Proper formatting
            and re.match('^".*"$', name) is None  # Already quoted
        ):
            name = f'"{name}"'

        return name

    @staticmethod
    def reserved_keywords() -> Set[str]:
        return {
            "account",
            "all",
            "alter",
            "and",
            "any",
            "as",
            "between",
            "by",
            "case",
            "cast",
            "check",
            "column",
            "connect",
            "connection",
            "constraint",
            "create",
            "cross",
            "current",
            "current_date",
            "current_time",
            "current_timestamp",
            "current_user",
            "database",
            "delete",
            "distinct",
            "drop",
            "else",
            "exists",
            "false",
            "following",
            "for",
            "from",
            "full",
            "grant",
            "group",
            "gscluster",
            "having",
            "ilike",
            "in",
            "increment",
            "inner",
            "insert",
            "intersect",
            "into",
            "is",
            "issue",
            "join",
            "lateral",
            "left",
            "like",
            "localtime",
            "localtimestamp",
            "minus",
            "natural",
            "not",
            "null",
            "of",
            "on",
            "or",
            "order",
            "organization",
            "qualify",
            "regexp",
            "revoke",
            "right",
            "rlike",
            "row",
            "rows",
            "sample",
            "schema",
            "select",
            "set",
            "some",
            "start",
            "table",
            "tablesample",
            "then",
            "to",
            "trigger",
            "true",
            "try_cast",
            "union",
            "unique",
            "update",
            "using",
            "values",
            "view",
            "when",
            "whenever",
            "where",
            "with",
        }
