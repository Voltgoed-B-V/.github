# install mypy to see typing errors
from typing import NewType
# WRONG ********************************************************************


def create_table_in_database(table_name: str, database_name: str):
    print("Creating table", table_name, "in database", database_name)


first_table1 = "first_table"
my_db1 = "my_own_db"

create_table_in_database(table_name=my_db1, database_name=first_table1)

# CORRECT ******************************************************************
TableName = NewType("TableName", str)
DatabaseName = NewType("DatabaseName", str)


def create_table_in_database_typed(table_name: TableName, database_name: DatabaseName):
    print("Creating table", table_name, "in database", database_name)


# adding type hint after variable declaration is optional,
# in my opinion it's a bit too verbose as typing should be obvious from assignment
first_table2: TableName = TableName("first_table")
my_db2 = DatabaseName("my_own_db")

create_table_in_database_typed(table_name=my_db2, database_name=first_table2)
