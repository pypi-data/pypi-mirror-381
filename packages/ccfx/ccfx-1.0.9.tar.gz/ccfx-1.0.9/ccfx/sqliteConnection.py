'''
a module that helps ease the management of sqlite databases

Author  : Celray James CHAWANDA
Email   : celray.chawanda@outlook.com
Licence : MIT 2023
Repo    : https://github.com/celray

Date    : 2023-07-20
'''

# imports
import sys
import sqlite3
import sys
import pandas

# classes
class sqliteConnection:
    def __init__(self, sqlite_database, connect = False) -> None:
        self.db_name = sqlite_database
        self.connection = None
        self.cursor = None

        if connect:
            self.connect()

    def connect(self, v=True) -> None:
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        if v:
            self.report("\t-> connection to " + self.db_name + " established...")

    def updateValue(self, table_name, col_name, new_value, col_where1, val_1, v=False) -> None:
        """
        Updates a single value in a specified table where the condition matches.
        
        Args:
            table_name (str): Name of the table to update
            col_name (str): Name of the column to update
            new_value: Value to set (can be None)
            col_where1 (str): Column name for WHERE clause
            val_1: Value to match in WHERE clause
            v (bool): Verbose flag for logging
        """
        try:
            # Use parameterized queries for ALL cases to prevent SQL injection
            query = f"UPDATE {table_name} SET {col_name} = ? WHERE {col_where1} = ?"
            self.cursor.execute(query, (new_value, val_1))
            
            if v:
                self.report(f"\t -> updated value in {self.db_name} table: {table_name}")
            
            
        except Exception as e:
            raise Exception(f"Error updating value: {str(e)}")
        

    def createTable(self, table_name, initial_field_name, data_type) -> None:
        '''
        can be text, real, etc
        '''
        try:
            self.cursor.execute('''CREATE TABLE ''' + table_name +
                                '(' + initial_field_name + ' ' + data_type + ')')
            self.report("\t-> created table " + table_name + " in " + self.db_name)
        except:
            self.report("\t! table exists")

    def newTable(self, tableName, columnsDict, columnOrder=None, notNull=None, foreignKeys=None) -> None:
        """
        Create a new table based on dictionary of columns and types.
        
        Args:
            tableName (str): Name of the table to create
            columnsDict (dict): Dictionary with column names as keys and data types as values
                                options:
                                INTEGER, REAL, TEXT, BLOB, etc.
                                Example: {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'}

            columnOrder (list, optional): List specifying the order of columns
                                Example: ['name', 'age', 'id']

            notNull (list, optional): List of column names that should have NOT NULL constraint
                                Example: ['name', 'age']

            foreignKeys (dict, optional): Dictionary defining foreign key constraints
                                Format Option 1: {currentTableField: {foreignTable: foreignField}, 'onDelete': 'CASCADE'}
                                Format Option 2: {currentTableField: {foreignTable: foreignField, 'onDelete': 'CASCADE'}}
                
                                onDelete options: CASCADE, SET NULL, RESTRICT, NO ACTION, SET DEFAULT
                                Examples: 
                                {'user_id': {'users': 'id'}, 'onDelete': 'CASCADE'}
                                {'user_id': {'users': 'id', 'onDelete': 'SET NULL'}}

        """
        try:
            # Determine column order
            if columnOrder:
                # Use specified order, but include any columns not in the order list at the end
                orderedColumns = []
                for col in columnOrder:
                    if col in columnsDict:
                        orderedColumns.append(col)
                # Add any remaining columns not in the order list
                for col in columnsDict:
                    if col not in orderedColumns:
                        orderedColumns.append(col)
            else:
                orderedColumns = list(columnsDict.keys())
            
            # Build column definitions
            columnDefinitions = []
            for col in orderedColumns:
                definition = f"{col} {columnsDict[col]}"
                
                # Add NOT NULL constraint if specified
                if notNull and col in notNull:
                    definition += " NOT NULL"
                
                columnDefinitions.append(definition)
            
            # Handle foreign key constraints
            if foreignKeys:
                onDeleteClause = ""
                if 'onDelete' in foreignKeys:
                    onDeleteClause = f" ON DELETE {foreignKeys['onDelete']}"
                
                for currentField, foreignRef in foreignKeys.items():
                    if currentField != 'onDelete':  # Skip the onDelete key
                        if isinstance(foreignRef, dict):
                            # Check if onDelete is specified at field level
                            if 'onDelete' in foreignRef:
                                fieldOnDelete = f" ON DELETE {foreignRef['onDelete']}"
                                # Get the actual foreign table and field (skip onDelete key)
                                foreignTable = None
                                foreignField = None
                                for key, value in foreignRef.items():
                                    if key != 'onDelete':
                                        foreignTable = key
                                        foreignField = value
                                        break
                            else:
                                # Use global onDelete clause and assume dict format {table: field}
                                fieldOnDelete = onDeleteClause
                                foreignTable = list(foreignRef.keys())[0]
                                foreignField = foreignRef[foreignTable]
                            
                            if foreignTable and foreignField:
                                foreignKeyDef = f"FOREIGN KEY ({currentField}) REFERENCES {foreignTable}({foreignField}){fieldOnDelete}"
                                columnDefinitions.append(foreignKeyDef)
            
            # Create the SQL statement
            columnsSQL = ', '.join(columnDefinitions)
            sql = f"CREATE TABLE {tableName} ({columnsSQL})"
            
            self.cursor.execute(sql)
            self.report(f"\t-> created table {tableName} in {self.db_name}")
            
        except Exception as e:
            self.report(f"\t! error creating table {tableName}: {str(e)}")

    def renameTable(self, old_table_name, new_table_name, v=False) -> None:
        """
        this function gives a new name to an existing table and saves the changes
        """
        self.cursor.execute("ALTER TABLE " + old_table_name +
                            " RENAME TO " + new_table_name)
        if v:
            self.report("\t-> renamed " + old_table_name + " to " + new_table_name)
        self.commitChanges()

    def tableExists(self, table_name) -> bool:
        self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(
            table_name=table_name))
        if self.cursor.fetchone()[0] == 1:
            return True
        else:
            return False

    def deleteRows(self, table_to_clean, col_where=None, col_where_value=None, v=False) -> None:
        """

        """

        if (col_where is None) and (col_where_value is None):
            self.connection.execute("DELETE FROM " + table_to_clean)

        elif (not col_where is None) and (not col_where_value is None):
            self.connection.execute(
                "DELETE FROM " + table_to_clean + " WHERE " + col_where + " = " + col_where_value + ";")

        else:
            raise ("\t! not all arguments were provided for selective row deletion")

        if v:
            self.report("\t-> removed all rows from " + table_to_clean)

    def deleteTable(self, table_name) -> None:
        """
        this function deletes the specified table
        """
        self.cursor.execute('''DROP TABLE ''' + table_name)
        self.report("\t-> deleted table " + table_name + " from " + self.db_name)

    def dropTable(self, table_name) -> None:
        self.deleteTable(table_name)

    def undoChanges(self) -> None:
        """
        This function reverts the database to status before last commit
        """
        self.report("\t-> undoing changes to " + self.db_name + " then saving")
        self.connection.rollback()
        self.commitChanges()

    def readTableAsDict(self, table_name, key_column: str = 'id') -> dict:
        # Execute a SQL query to fetch all rows from your table
        self.cursor = self.connection.execute(f"SELECT * FROM {table_name}")

        # Fetch all rows as dictionaries
        rows = [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]

        # Convert the list of dictionaries to a dictionary of dictionaries, 
        # using the 'id' field as the key
        data = {row[key_column]: row for row in rows}

        return data

    def getColumnsWithTypes(self, table_name) -> dict:
        c = self.cursor

        # Prepare and execute a PRAGMA table_info statement
        c.execute(f'PRAGMA table_info({table_name})')

        # Fetch all rows and extract the column names and types
        columns_with_types = {row[1]: row[2] for row in c.fetchall()}

        return columns_with_types

    def insertDictPartial(self, table_name, data_dict) -> None:
        c = self.cursor

        # Get the column names from the table
        c.execute(f"PRAGMA table_info({table_name})")
        columns = [row[1] for row in c.fetchall()]

        # Filter the dictionary keys to match the column names
        filtered_data = {k: v for k, v in data_dict.items() if k in columns}

        # Prepare an INSERT INTO statement
        fields = ', '.join(filtered_data.keys())
        placeholders = ', '.join('?' for _ in filtered_data)
        values = list(filtered_data.values())
        sql = f'INSERT INTO {table_name} ({fields}) VALUES ({placeholders})'

        # Execute the statement
        c.execute(sql, values)

        # Commit the changes
        self.commitChanges()


    def report(self, string, printing=False) -> None:
        if printing:
            print(f"\t> {string}")
        else:
            sys.stdout.write("\r" + string)
            sys.stdout.flush()


    def createTableFromDict(self, table_name, columns_with_types) -> None:

        # Prepare a CREATE TABLE statement
        fields = ', '.join(f'{column} {data_type}' for column, data_type in columns_with_types.items())
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({fields})'

        # Execute the statement
        self.connection.execute(sql)
        self.commitChanges()


    def insertDict(self, table_name, data) -> None:
        
        # Prepare an INSERT INTO statement for each dictionary
        for id, row in data.items():
            fields = ', '.join(row.keys())
            placeholders = ', '.join('?' for _ in row)
            values = list(row.values())
            sql = f'INSERT INTO {table_name} ({fields}) VALUES ({placeholders})'

            # Execute the statement
            self.cursor.execute(sql, values)

        # Commit the changes
        self.connection.commit()



    def readTableColumns(self, table_name, column_list="all") -> list:
        """
        this function takes a list to be a string separated by commmas and
        a table and puts the columns in the table into a variable

        "all" to select all columns
        """
        if column_list == "all":
            self.cursor = self.connection.execute(
                "SELECT * from " + table_name)
        else:
            self.cursor = self.connection.execute(
                "SELECT " + ",".join(column_list) + " from " + table_name)

        list_of_tuples = []
        for row in self.cursor:
            list_of_tuples.append(row)
        self.cursor = self.connection.cursor()
        self.report("\t-> read selected table columns from " + table_name)
        return list_of_tuples

    def insertField(self, table_name, field_name, data_type, to_new_line=False, messages=True) -> None:
        """
        This will insert a new field into your sqlite database

        table_name: an existing table
        field_name: the field you want to add
        data_type : text, integer, float or real
        """
        self.cursor.execute("alter table " + table_name +
                            " add column " + field_name + " " + data_type)
        if messages:
            if to_new_line:
                self.report(
                    "\t-> inserted into table {0} field {1}".format(table_name, field_name))
            else:
                sys.stdout.write(
                    "\r\t-> inserted into table {0} field {1}            ".format(table_name, field_name))
                sys.stdout.flush()

    def insertRow(self, table_name, ordered_content_list = [], dictionary_obj = {}, messages=False) -> None:
        """
        ordered_list such as ['ha','he','hi']
        list should have data as strings
        """
        if len(ordered_content_list) > 0:
            values_placeholder = ','.join(['?' if value is None else '?' for value in ordered_content_list])
            values = [None if value is None else value for value in ordered_content_list]
            self.cursor.execute("INSERT INTO " + table_name + " VALUES(" + values_placeholder + ")", values)
        
        elif len(dictionary_obj) > 0:
            question_marks = ','.join(list('?'*len(dictionary_obj)))
            keys = ','.join(dictionary_obj.keys())
            values = tuple(dictionary_obj.values())
            self.cursor.execute('INSERT INTO '+table_name+' ('+keys+') VALUES ('+question_marks+')', values)

        if messages:
            self.report("\t-> inserted row into " + table_name)

    def insertRows(self, table_name, list_of_tuples, messages=False) -> None:
        """
        list_of_tuples such as [('ha','he','hi')'
                                ('ha','he','hi')]
        not limited to string data
        """
        self.cursor.executemany('INSERT INTO ' + table_name + ' VALUES (?{qmarks})'.format(
            qmarks=",?" * (len(list_of_tuples[0]) - 1)), list_of_tuples)
        if messages:
            self.report("\t-> inserted rows into " + table_name)

    def dumpCSV(self, table_name, file_name, index=False, v=False) -> None:
        '''
        save table to csv
        '''
        tmp_conn = sqlite3.connect(self.db_name)
        df = pandas.read_sql_query(
            "SELECT * FROM {tn}".format(tn=table_name), tmp_conn)
        if index:
            df.to_csv(file_name)
        else:
            df.to_csv(file_name, index=False)

        if v:
            self.report(
                "\t-> dumped table {0} to {1}".format(table_name, file_name))

    def commitChanges(self, v=False):
        '''
        save changes to the database.
        '''
        self.connection.commit()
        number_of_changes = self.connection.total_changes
        if v:
            self.report(
                "\t-> saved {0} changes to ".format(number_of_changes) + self.db_name)

    def commit(self, v=False) -> None:
        '''proxy to commitChanges'''
        self.commitChanges(v)

    def closeConnection(self, commit=True) -> None:
        '''
        disconnects from the database
        '''
        if commit:
            self.commitChanges()
        self.connection.close()
        self.report("\t-> closed connection to " + self.db_name)

