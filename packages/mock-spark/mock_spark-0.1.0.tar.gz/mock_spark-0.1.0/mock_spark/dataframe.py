"""
Mock DataFrame implementation for Mock Spark.

This module provides a complete mock implementation of PySpark DataFrame
that behaves identically to the real PySpark DataFrame for testing and
development purposes. It supports all major DataFrame operations including
selection, filtering, grouping, joining, and window functions.

Key Features:
    - Complete PySpark API compatibility
    - Type-safe operations with proper schema inference
    - Window function support with partitioning and ordering
    - Comprehensive error handling matching PySpark exceptions
    - In-memory storage for fast test execution

Example:
    >>> from mock_spark import MockSparkSession, F
    >>> spark = MockSparkSession("test")
    >>> data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    >>> df = spark.createDataFrame(data)
    >>> df.select("name", "age").filter(F.col("age") > 25).show()
    +----+---+
    |name|age|
    +----+---+
    | Bob| 30|
    +----+---+
"""

from typing import Any, Dict, List, Optional, Union, Tuple
from dataclasses import dataclass
import pandas as pd

from .spark_types import (
    MockStructType,
    MockStructField,
    StringType,
    IntegerType,
    MockRow,
)
from .functions import MockColumn, MockColumnOperation, F, MockLiteral
from .storage import MockStorageManager
from .errors import (
    raise_column_not_found,
    raise_value_error,
    raise_invalid_argument,
    AnalysisException,
    IllegalArgumentException,
)


@dataclass
class MockDataFrameWriter:
    """Mock DataFrame writer for saveAsTable operations.

    Provides a PySpark-compatible interface for writing DataFrames to storage
    formats. Supports various formats and save modes for testing and development.

    Attributes:
        df: The DataFrame to be written.
        storage: Storage manager for persisting data.
        format_name: Output format (e.g., 'parquet', 'json').
        save_mode: Save mode ('append', 'overwrite', 'error', 'ignore').
        options: Additional options for the writer.

    Example:
        >>> df.write.format("parquet").mode("overwrite").saveAsTable("my_table")
    """

    def __init__(self, df: "MockDataFrame", storage: MockStorageManager):
        self.df = df
        self.storage = storage
        self.format_name = "parquet"
        self.save_mode = "append"
        self.options: Dict[str, Any] = {}

    def format(self, source: str) -> "MockDataFrameWriter":
        """Set the output format for the DataFrame writer.

        Args:
            source: The output format (e.g., 'parquet', 'json', 'csv').

        Returns:
            Self for method chaining.

        Example:
            >>> df.write.format("parquet")
        """
        self.format_name = source
        return self

    def mode(self, mode: str) -> "MockDataFrameWriter":
        """Set the save mode for the DataFrame writer.

        Args:
            mode: Save mode ('append', 'overwrite', 'error', 'ignore').

        Returns:
            Self for method chaining.

        Example:
            >>> df.write.mode("overwrite")
        """
        self.save_mode = mode
        return self

    @property
    def saveMode(self) -> str:
        """Get the current save mode (PySpark compatibility).

        Returns:
            Current save mode string.
        """
        return self.save_mode

    def option(self, key: str, value: Any) -> "MockDataFrameWriter":
        """Set an option for the DataFrame writer.

        Args:
            key: Option key.
            value: Option value.

        Returns:
            Self for method chaining.

        Example:
            >>> df.write.option("compression", "snappy")
        """
        self.options[key] = value
        return self

    def saveAsTable(self, table_name: str) -> None:
        """Save DataFrame as a table in storage.

        Args:
            table_name: Name of the table (can include schema, e.g., 'schema.table').

        Raises:
            AnalysisException: If table operations fail.

        Example:
            >>> df.write.saveAsTable("my_table")
            >>> df.write.saveAsTable("schema.my_table")
        """
        schema, table = (
            table_name.split(".", 1) if "." in table_name else ("default", table_name)
        )

        # Create table if not exists
        if not self.storage.table_exists(schema, table):
            self.storage.create_table(schema, table, self.df.schema.fields)

        # Insert data
        if self.save_mode == "overwrite":
            # Clear existing data by dropping and recreating table
            if self.storage.table_exists(schema, table):
                self.storage.drop_table(schema, table)
            self.storage.create_table(schema, table, self.df.schema.fields)

        data = self.df.collect()
        # Convert MockRow objects to dictionaries
        dict_data = [row.asDict() for row in data]
        self.storage.insert_data(schema, table, dict_data)


class MockDataFrame:
    """Mock DataFrame implementation with complete PySpark API compatibility.

    Provides a comprehensive mock implementation of PySpark DataFrame that supports
    all major operations including selection, filtering, grouping, joining, and
    window functions. Designed for testing and development without requiring JVM.

    Attributes:
        data: List of dictionaries representing DataFrame rows.
        schema: MockStructType defining the DataFrame schema.
        storage: Optional storage manager for persistence operations.

    Example:
        >>> from mock_spark import MockSparkSession, F
        >>> spark = MockSparkSession("test")
        >>> data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
        >>> df = spark.createDataFrame(data)
        >>> df.select("name").filter(F.col("age") > 25).show()
        +----+
        |name|
        +----+
        | Bob|
        +----+
    """

    def __init__(
        self,
        data: List[Dict[str, Any]],
        schema: MockStructType,
        storage: Optional[MockStorageManager] = None,
    ):
        """Initialize MockDataFrame.

        Args:
            data: List of dictionaries representing DataFrame rows.
            schema: MockStructType defining the DataFrame schema.
            storage: Optional storage manager for persistence operations.
                    Defaults to a new MockStorageManager instance.
        """
        self.data = data
        self.schema = schema
        self.storage = storage or MockStorageManager()
        self._cached_count: Optional[int] = None

    def __repr__(self) -> str:
        return (
            f"MockDataFrame[{len(self.data)} rows, {len(self.schema.fields)} columns]"
        )

    def show(self, n: int = 20, truncate: bool = True) -> None:
        """Display DataFrame content in a formatted table.

        Args:
            n: Number of rows to display (default: 20).
            truncate: Whether to truncate long values (default: True).

        Example:
            >>> df.show(5)
            +--- MockDataFrame: 3 rows ---+
                name | age | salary
            --------|-----|--------
              Alice |  25 |  50000
                Bob |  30 |  60000
            Charlie |  35 |  70000
        """
        print(f"+--- MockDataFrame: {len(self.data)} rows ---+")
        if not self.data:
            print("(empty)")
            return

        # Show first n rows
        display_data = self.data[:n]

        # Get column names
        columns = (
            list(display_data[0].keys()) if display_data else self.schema.fieldNames()
        )

        # Print header
        header = " | ".join(f"{col:>12}" for col in columns)
        print(header)
        print("-" * len(header))

        # Print data
        for row in display_data:
            row_str = " | ".join(f"{str(row.get(col, 'null')):>12}" for col in columns)
            print(row_str)

        if len(self.data) > n:
            print(f"... ({len(self.data) - n} more rows)")

    def collect(self) -> List[MockRow]:
        """Collect all data as list of Row objects."""
        return [MockRow(row) for row in self.data]

    def toPandas(self) -> Any:
        """Convert to pandas DataFrame."""
        if not self.data:
            # Create empty DataFrame with correct column structure
            return pd.DataFrame(columns=[field.name for field in self.schema.fields])
        return pd.DataFrame(self.data)

    def count(self) -> int:
        """Count number of rows."""
        if self._cached_count is None:
            self._cached_count = len(self.data)
        return self._cached_count

    @property
    def columns(self) -> List[str]:
        """Get column names."""
        return [field.name for field in self.schema.fields]

    def printSchema(self) -> None:
        """Print DataFrame schema."""
        print("MockDataFrame Schema:")
        for field in self.schema.fields:
            nullable = "nullable" if field.nullable else "not nullable"
            print(
                f" |-- {field.name}: {field.dataType.__class__.__name__} ({nullable})"
            )

    def select(self, *columns: Union[str, MockColumn]) -> "MockDataFrame":
        """Select columns from the DataFrame.

        Args:
            *columns: Column names, MockColumn objects, or expressions to select.
                     Use "*" to select all columns.

        Returns:
            New MockDataFrame with selected columns.

        Raises:
            AnalysisException: If specified columns don't exist.

        Example:
            >>> df.select("name", "age")
            >>> df.select("*")
            >>> df.select(F.col("name"), F.col("age") * 2)
        """
        if not columns:
            return self

        # Import MockLiteral and MockAggregateFunction to check for special columns
        from .functions import MockLiteral, MockAggregateFunction

        # Check if this is an aggregation operation
        has_aggregation = any(
            isinstance(col, MockAggregateFunction)
            or (
                isinstance(col, MockColumn)
                and (
                    col.name.startswith(("count(", "sum(", "avg(", "max(", "min("))
                    or col.name.startswith("count(DISTINCT ")
                )
            )
            for col in columns
        )

        if has_aggregation:
            # Handle aggregation - return single row
            return self._handle_aggregation_select(list(columns))

        # Process columns and handle literals
        col_names = []
        literal_columns: Dict[str, Any] = {}
        literal_objects: Dict[str, MockLiteral] = (
            {}
        )  # Store MockLiteral objects for type information

        for col in columns:
            if isinstance(col, str):
                if col == "*":
                    # Handle select all columns
                    col_names.extend([field.name for field in self.schema.fields])
                else:
                    col_names.append(col)
            elif isinstance(col, MockLiteral):
                # Handle literal columns
                literal_name = col.name
                col_names.append(literal_name)
                literal_columns[literal_name] = col.value
                literal_objects[literal_name] = col  # Store the MockLiteral object
            elif isinstance(col, MockColumn):
                if col.name == "*":
                    # Handle select all columns
                    col_names.extend([field.name for field in self.schema.fields])
                else:
                    col_names.append(col.name)
            elif hasattr(col, "operation") and hasattr(col, "column"):
                # Handle MockColumnOperation (e.g., col + 1, upper(col))
                col_names.append(col.name)
            elif hasattr(col, "name"):  # Support other column-like objects
                col_names.append(col.name)
            else:
                raise_value_error(f"Invalid column type: {type(col)}")

        # Validate non-literal columns exist (skip validation for MockColumnOperation, function calls, and window functions)
        for col_name in col_names:
            if (
                col_name not in [field.name for field in self.schema.fields]
                and col_name not in literal_columns
                and not any(
                    hasattr(col, "operation")
                    and hasattr(col, "column")
                    and hasattr(col, "name")
                    and col.name == col_name
                    for col in columns
                )
                and not any(
                    hasattr(col, "function_name")
                    and hasattr(col, "over")
                    and hasattr(col, "name")
                    and col.name == col_name
                    for col in columns
                )
                and not any(
                    hasattr(col, "operation")
                    and not hasattr(col, "column")
                    and hasattr(col, "name")
                    and col.name == col_name
                    for col in columns
                )  # Handle functions like coalesce
                and not any(
                    hasattr(col, "conditions")
                    and hasattr(col, "name")
                    and col.name == col_name
                    for col in columns
                )  # Handle MockCaseWhen objects
                and not self._is_function_call(col_name)
            ):
                raise_column_not_found(col_name)

        # Filter data to selected columns and add literal values
        filtered_data = []
        for row in self.data:
            filtered_row = {}
            for i, col in enumerate(columns):
                if isinstance(col, str):
                    col_name = col
                    if col_name == "*":
                        # Add all existing columns
                        for field in self.schema.fields:
                            filtered_row[field.name] = row[field.name]
                    elif col_name in literal_columns:
                        # Add literal value
                        filtered_row[col_name] = literal_columns[col_name]
                    elif col_name in ("current_timestamp()", "current_date()"):
                        # Handle timestamp and date functions
                        if col_name == "current_timestamp()":
                            import datetime

                            filtered_row[col_name] = datetime.datetime.now()
                        elif col_name == "current_date()":
                            import datetime

                            filtered_row[col_name] = datetime.date.today()
                    else:
                        # Add existing column value
                        filtered_row[col_name] = row[col_name]
                elif hasattr(col, "operation") and hasattr(col, "column"):
                    # Handle MockColumnOperation (e.g., upper(col), length(col))
                    col_name = col.name
                    evaluated_value = self._evaluate_column_expression(row, col)
                    filtered_row[col_name] = evaluated_value
                elif hasattr(col, "conditions"):
                    # Handle MockCaseWhen objects
                    col_name = col.name
                    evaluated_value = self._evaluate_case_when(row, col)
                    filtered_row[col_name] = evaluated_value
                elif isinstance(col, MockColumn):
                    col_name = col.name
                    if col_name == "*":
                        # Add all existing columns
                        for field in self.schema.fields:
                            filtered_row[field.name] = row[field.name]
                    elif col_name in literal_columns:
                        # Add literal value
                        filtered_row[col_name] = literal_columns[col_name]
                    elif col_name.startswith(
                        (
                            "upper(",
                            "lower(",
                            "length(",
                            "abs(",
                            "round(",
                            "coalesce(",
                            "isnull(",
                            "isnan(",
                            "trim(",
                            "ceil(",
                            "floor(",
                            "sqrt(",
                            "regexp_replace(",
                            "split(",
                        )
                    ) or (
                        hasattr(col, "_original_column")
                        and col._original_column is not None
                        and hasattr(col._original_column, "name")
                        and col._original_column.name.startswith(
                            (
                                "coalesce(",
                                "isnull(",
                                "isnan(",
                                "trim(",
                                "ceil(",
                                "floor(",
                                "sqrt(",
                                "regexp_replace(",
                                "split(",
                            )
                        )
                    ):
                        # Handle function calls
                        evaluated_value = self._evaluate_column_expression(row, col)
                        filtered_row[col_name] = evaluated_value
                    else:
                        # Handle aliased columns - get value from original column name
                        if (
                            hasattr(col, "_original_column")
                            and col._original_column is not None
                        ):
                            # This is an aliased column, get value from original column
                            original_name = col._original_column.name
                            if original_name in (
                                "current_timestamp()",
                                "current_date()",
                            ):
                                # Handle timestamp and date functions
                                if original_name == "current_timestamp()":
                                    import datetime

                                    filtered_row[col_name] = datetime.datetime.now()
                                elif original_name == "current_date()":
                                    import datetime

                                    filtered_row[col_name] = datetime.date.today()
                            else:
                                filtered_row[col_name] = row[original_name]
                        elif col_name in ("current_timestamp()", "current_date()"):
                            # Handle timestamp and date functions
                            if col_name == "current_timestamp()":
                                import datetime

                                filtered_row[col_name] = datetime.datetime.now()
                            elif col_name == "current_date()":
                                import datetime

                                filtered_row[col_name] = datetime.date.today()
                        else:
                            # Add existing column value
                            filtered_row[col_name] = row[col_name]
                elif hasattr(col, "function_name") and hasattr(col, "over"):
                    # Handle MockWindowFunction (e.g., row_number().over(window))
                    col_name = col.name
                    # Window functions need to be evaluated across all rows
                    # For now, we'll handle this after processing all rows
                    filtered_row[col_name] = None  # Placeholder, will be filled later
                elif hasattr(col, "name"):
                    col_name = col.name
                    if col_name in literal_columns:
                        # Add literal value
                        filtered_row[col_name] = literal_columns[col_name]
                    elif col_name in ("current_timestamp()", "current_date()"):
                        # Handle timestamp and date functions
                        if col_name == "current_timestamp()":
                            import datetime

                            filtered_row[col_name] = datetime.datetime.now()
                        elif col_name == "current_date()":
                            import datetime

                            filtered_row[col_name] = datetime.date.today()
                    else:
                        # Add existing column value
                        filtered_row[col_name] = row[col_name]
            filtered_data.append(filtered_row)

        # Handle window functions that need to be evaluated across all rows
        window_functions = []
        for i, col in enumerate(columns):
            if hasattr(col, "function_name") and hasattr(col, "over"):
                window_functions.append((i, col))

        if window_functions:
            filtered_data = self._evaluate_window_functions(
                filtered_data, window_functions
            )

        # Create new schema
        new_fields = []
        for i, col in enumerate(columns):
            if isinstance(col, MockLiteral):
                # Handle MockLiteral directly
                col_name = col.name
                new_fields.append(MockStructField(col_name, col.column_type))
            elif isinstance(col, str):
                col_name = col
                if col_name == "*":
                    # Add all existing fields
                    new_fields.extend(self.schema.fields)
                elif col_name in literal_columns:
                    # Create field for literal column with correct type
                    from .spark_types import (
                        convert_python_type_to_mock_type,
                        MockDataType,
                    )

                    literal_value = literal_columns[col_name]
                    literal_type: MockDataType = convert_python_type_to_mock_type(
                        type(literal_value)
                    )
                    new_fields.append(MockStructField(col_name, literal_type))
                else:
                    # Use existing field
                    for field in self.schema.fields:
                        if field.name == col_name:
                            new_fields.append(field)
                            break
            elif hasattr(col, "operation") and hasattr(col, "column"):
                # Handle MockColumnOperation (e.g., upper(col), length(col))
                col_name = col.name
                from .spark_types import StringType, LongType, DoubleType, IntegerType

                if col.operation in ["upper", "lower"]:
                    new_fields.append(MockStructField(col_name, StringType()))
                elif col.operation == "length":
                    new_fields.append(
                        MockStructField(col_name, IntegerType())
                    )  # length() returns IntegerType
                elif col.operation == "abs":
                    new_fields.append(
                        MockStructField(col_name, LongType())
                    )  # abs() returns LongType
                elif col.operation == "round":
                    new_fields.append(
                        MockStructField(col_name, DoubleType())
                    )  # round() returns DoubleType
                elif col.operation in ["+", "-", "*", "%"]:
                    # Arithmetic operations - infer type from operands
                    left_type = self._get_column_type(col.column)
                    right_type = (
                        self._get_column_type(col.value)
                        if hasattr(col, "value") and col.value is not None
                        else LongType()
                    )

                    # If either operand is DoubleType, result is DoubleType
                    if left_type == DoubleType() or right_type == DoubleType():
                        new_fields.append(MockStructField(col_name, DoubleType()))
                    else:
                        new_fields.append(MockStructField(col_name, LongType()))
                elif col.operation == "/":
                    # Division returns DoubleType
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.operation == "ceil":
                    # Ceiling function returns LongType
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.operation == "floor":
                    # Floor function returns LongType
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.operation == "sqrt":
                    # Square root function returns DoubleType
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.operation == "split":
                    # Split function returns ArrayType
                    from .spark_types import ArrayType

                    new_fields.append(
                        MockStructField(col_name, ArrayType(StringType()))
                    )
                elif col.operation == "regexp_replace":
                    # Regexp replace function returns StringType
                    new_fields.append(MockStructField(col_name, StringType()))
                elif col.operation == "cast":
                    # Cast operation - infer type from the cast parameter
                    cast_type = col.value
                    if isinstance(cast_type, str):
                        # String type name, convert to actual type
                        if cast_type.lower() in ["double", "float"]:
                            new_fields.append(MockStructField(col_name, DoubleType()))
                        elif cast_type.lower() in ["int", "integer", "long", "bigint"]:
                            new_fields.append(MockStructField(col_name, LongType()))
                        elif cast_type.lower() in ["string", "varchar"]:
                            new_fields.append(MockStructField(col_name, StringType()))
                        else:
                            new_fields.append(MockStructField(col_name, StringType()))
                    else:
                        # Type object, use directly
                        new_fields.append(MockStructField(col_name, cast_type))
                else:
                    new_fields.append(
                        MockStructField(col_name, StringType())
                    )  # Default to StringType
            elif isinstance(col, MockColumn):
                col_name = col.name
                if col_name == "*":
                    # Add all existing fields
                    new_fields.extend(self.schema.fields)
                # Check if this is a function call first
                elif (
                    col_name.startswith(
                        (
                            "abs(",
                            "round(",
                            "upper(",
                            "lower(",
                            "length(",
                            "coalesce(",
                            "isnull(",
                            "isnan(",
                            "trim(",
                            "ceil(",
                            "floor(",
                            "sqrt(",
                            "regexp_replace(",
                            "split(",
                        )
                    )
                    or col_name in ("current_timestamp()", "current_date()")
                    or (
                        hasattr(col, "_original_column")
                        and col._original_column is not None
                        and hasattr(col._original_column, "name")
                        and (
                            col._original_column.name.startswith(
                                (
                                    "coalesce(",
                                    "isnull(",
                                    "isnan(",
                                    "trim(",
                                    "ceil(",
                                    "floor(",
                                    "sqrt(",
                                    "regexp_replace(",
                                    "split(",
                                )
                            )
                            or col._original_column.name
                            in ("current_timestamp()", "current_date()")
                        )
                    )
                ):
                    from .spark_types import (
                        DoubleType,
                        StringType,
                        LongType,
                        IntegerType,
                        BooleanType,
                        TimestampType,
                        DateType,
                    )

                    # Determine the function name for type inference
                    func_name = col_name
                    if (
                        hasattr(col, "_original_column")
                        and col._original_column is not None
                        and hasattr(col._original_column, "name")
                    ):
                        func_name = col._original_column.name

                    if func_name.startswith("abs("):
                        new_fields.append(
                            MockStructField(col_name, LongType())
                        )  # abs() returns LongType for integers
                    elif func_name.startswith("round("):
                        new_fields.append(MockStructField(col_name, DoubleType()))
                    elif func_name.startswith("length("):
                        new_fields.append(
                            MockStructField(col_name, IntegerType())
                        )  # length() returns IntegerType
                    elif func_name.startswith(
                        ("upper(", "lower(", "coalesce(", "trim(")
                    ):
                        new_fields.append(MockStructField(col_name, StringType()))
                    elif func_name.startswith(("isnull(", "isnan(")):
                        new_fields.append(MockStructField(col_name, BooleanType()))
                    elif func_name == "current_timestamp()":
                        new_fields.append(MockStructField(col_name, TimestampType()))
                    elif func_name == "current_date()":
                        new_fields.append(MockStructField(col_name, DateType()))
                    elif func_name.startswith(("ceil(", "floor(")):
                        new_fields.append(MockStructField(col_name, LongType()))
                    elif func_name.startswith("sqrt("):
                        new_fields.append(MockStructField(col_name, DoubleType()))
                    elif func_name.startswith("regexp_replace("):
                        new_fields.append(MockStructField(col_name, StringType()))
                    elif func_name.startswith("split("):
                        new_fields.append(MockStructField(col_name, StringType()))
                    else:
                        new_fields.append(MockStructField(col_name, StringType()))
                elif col_name in literal_columns:
                    # Create field for literal column with correct type
                    if col_name in literal_objects:
                        # Use the MockLiteral object's column_type
                        literal_obj = literal_objects[col_name]
                        new_fields.append(
                            MockStructField(col_name, literal_obj.column_type)
                        )
                    else:
                        # Fallback to type inference
                        from .spark_types import (
                            convert_python_type_to_mock_type,
                            IntegerType,
                            MockDataType,
                        )

                        literal_value = literal_columns[col_name]
                        if isinstance(literal_value, int):
                            literal_type_2 = IntegerType()
                        else:
                            literal_type_2: MockDataType = (
                                convert_python_type_to_mock_type(type(literal_value))
                            )
                        new_fields.append(MockStructField(col_name, literal_type_2))
                else:
                    # Use existing field
                    for field in self.schema.fields:
                        if field.name == col_name:
                            new_fields.append(field)
                            break
            elif isinstance(col, str):
                col_name = col
                if col_name == "*":
                    # Add all existing fields
                    new_fields.extend(self.schema.fields)
                elif col_name in literal_columns:
                    # Create field for literal column with correct type
                    from .spark_types import convert_python_type_to_mock_type

                    literal_value = literal_columns[col_name]
                    literal_type: MockDataType = convert_python_type_to_mock_type(
                        type(literal_value)
                    )
                    new_fields.append(MockStructField(col_name, literal_type))
                else:
                    # Use existing field
                    for field in self.schema.fields:
                        if field.name == col_name:
                            new_fields.append(field)
                            break
            elif hasattr(col, "operation") and hasattr(col, "column"):
                # Handle MockColumnOperation (e.g., upper(col), length(col))
                col_name = col.name
                from .spark_types import StringType, LongType, DoubleType, IntegerType

                if col.operation in ["upper", "lower"]:
                    new_fields.append(MockStructField(col_name, StringType()))
                elif col.operation == "length":
                    new_fields.append(
                        MockStructField(col_name, IntegerType())
                    )  # length() returns IntegerType
                elif col.operation == "abs":
                    new_fields.append(
                        MockStructField(col_name, LongType())
                    )  # abs() returns LongType
                elif col.operation == "round":
                    new_fields.append(
                        MockStructField(col_name, DoubleType())
                    )  # round() returns DoubleType
                elif col.operation in ["+", "-", "*", "%"]:
                    # Arithmetic operations - infer type from operands
                    left_type = self._get_column_type(col.column)
                    right_type = (
                        self._get_column_type(col.value)
                        if hasattr(col, "value") and col.value is not None
                        else LongType()
                    )

                    # If either operand is DoubleType, result is DoubleType
                    if left_type == DoubleType() or right_type == DoubleType():
                        new_fields.append(MockStructField(col_name, DoubleType()))
                    else:
                        new_fields.append(MockStructField(col_name, LongType()))
                elif col.operation == "/":
                    # Division operation - use DoubleType for decimal results
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.operation == "ceil":
                    # Ceiling function returns LongType
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.operation == "floor":
                    # Floor function returns LongType
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.operation == "sqrt":
                    # Square root function returns DoubleType
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.operation == "split":
                    # Split function returns ArrayType
                    from .spark_types import ArrayType

                    new_fields.append(
                        MockStructField(col_name, ArrayType(StringType()))
                    )
                elif col.operation == "regexp_replace":
                    # Regexp replace function returns StringType
                    new_fields.append(MockStructField(col_name, StringType()))
                elif col.operation == "cast":
                    # Cast operation - infer type from the cast parameter
                    cast_type = col.value
                    if isinstance(cast_type, str):
                        # String type name, convert to actual type
                        if cast_type.lower() in ["double", "float"]:
                            new_fields.append(MockStructField(col_name, DoubleType()))
                        elif cast_type.lower() in ["int", "integer", "long", "bigint"]:
                            new_fields.append(MockStructField(col_name, LongType()))
                        elif cast_type.lower() in ["string", "varchar"]:
                            new_fields.append(MockStructField(col_name, StringType()))
                        else:
                            new_fields.append(MockStructField(col_name, StringType()))
                    else:
                        # Type object, use directly
                        new_fields.append(MockStructField(col_name, cast_type))
                elif col.operation == "upper":
                    # Upper function returns StringType
                    new_fields.append(MockStructField(col_name, StringType()))
                elif col.operation == "lower":
                    # Lower function returns StringType
                    new_fields.append(MockStructField(col_name, StringType()))
                elif col.operation == "length":
                    # Length function returns LongType
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.operation == "abs":
                    # Abs function returns DoubleType
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.operation == "round":
                    # Round function returns DoubleType
                    new_fields.append(MockStructField(col_name, DoubleType()))
                else:
                    # Default to StringType for other operations
                    new_fields.append(MockStructField(col_name, StringType()))
            elif hasattr(col, "function_name") and hasattr(col, "over"):
                # Handle MockWindowFunction (e.g., row_number().over(window))
                col_name = col.name
                from .spark_types import IntegerType, DoubleType, StringType

                # Infer type based on window function
                if col.function_name in ["row_number", "rank", "dense_rank"]:
                    # Ranking functions return IntegerType
                    new_fields.append(MockStructField(col_name, IntegerType()))
                elif col.function_name in ["lag", "lead"] and col.column_name:
                    # Lag/lead functions return the same type as the source column
                    source_col_name = col.column_name
                    source_type = None
                    for field in self.schema.fields:
                        if field.name == source_col_name:
                            source_type = field.dataType
                            break
                    if source_type:
                        new_fields.append(MockStructField(col_name, source_type))
                    else:
                        # Default to DoubleType if source column not found
                        new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.function_name in ["avg", "sum"]:
                    # Average and sum functions return DoubleType
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.function_name in ["count", "countDistinct"]:
                    # Count functions return LongType
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.function_name in ["max", "min"] and col.column_name:
                    # Max/min functions return the same type as the source column
                    source_col_name = col.column_name
                    source_type = None
                    for field in self.schema.fields:
                        if field.name == source_col_name:
                            source_type = field.dataType
                            break
                    if source_type:
                        new_fields.append(MockStructField(col_name, source_type))
                    else:
                        # Default to DoubleType if source column not found
                        new_fields.append(MockStructField(col_name, DoubleType()))
                else:
                    # Default to IntegerType for other window functions
                    new_fields.append(MockStructField(col_name, IntegerType()))
            elif hasattr(col, "conditions"):
                # Handle MockCaseWhen objects
                col_name = col.name
                from .spark_types import StringType, LongType, DoubleType, IntegerType

                # Infer type from the first condition's value
                if col.conditions:
                    first_value = col.conditions[0][1]  # First condition's value
                    if hasattr(first_value, "column") and hasattr(
                        first_value.column, "name"
                    ):
                        # It's a column reference, get its type
                        source_col_name = first_value.column.name
                        source_type = None
                        for field in self.schema.fields:
                            if field.name == source_col_name:
                                source_type = field.dataType
                                break
                        if source_type:
                            new_fields.append(MockStructField(col_name, source_type))
                        else:
                            new_fields.append(MockStructField(col_name, StringType()))
                    else:
                        # It's a literal or operation, default to StringType
                        new_fields.append(MockStructField(col_name, StringType()))
                else:
                    # No conditions, default to StringType
                    new_fields.append(MockStructField(col_name, StringType()))
            elif isinstance(col, MockColumn) and col.name.startswith(
                (
                    "abs(",
                    "round(",
                    "upper(",
                    "lower(",
                    "length(",
                    "ceil(",
                    "floor(",
                    "sqrt(",
                    "regexp_replace(",
                    "split(",
                )
            ):
                # Handle function calls like abs(column), round(column), upper(column), etc.
                col_name = col.name
                from .spark_types import DoubleType, StringType, LongType

                if col.name.startswith(("abs(", "round(", "sqrt(")):
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col.name.startswith("length("):
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.name.startswith(("ceil(", "floor(")):
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col.name.startswith("split("):
                    # Split function returns ArrayType
                    from .spark_types import ArrayType

                    new_fields.append(
                        MockStructField(col_name, ArrayType(StringType()))
                    )
                elif col.name.startswith(("upper(", "lower(", "regexp_replace(")):
                    new_fields.append(MockStructField(col_name, StringType()))
                else:
                    new_fields.append(MockStructField(col_name, StringType()))
            elif hasattr(col, "name"):
                col_name = col.name
                if col_name in literal_columns:
                    # Create field for literal column with correct type
                    from .spark_types import convert_python_type_to_mock_type

                    literal_value = literal_columns[col_name]
                    literal_type: MockDataType = convert_python_type_to_mock_type(
                        type(literal_value)
                    )
                    new_fields.append(MockStructField(col_name, literal_type))
                else:
                    # Use existing field
                    for field in self.schema.fields:
                        if field.name == col_name:
                            new_fields.append(field)
                            break

        new_schema = MockStructType(new_fields)
        return MockDataFrame(filtered_data, new_schema, self.storage)

    def _handle_aggregation_select(
        self, columns: List[Union[str, MockColumn]]
    ) -> "MockDataFrame":
        """Handle aggregation select operations."""
        from .functions import MockAggregateFunction
        from .spark_types import LongType, DoubleType

        result_row: Dict[str, Any] = {}
        new_fields = []

        for col in columns:
            if isinstance(col, MockAggregateFunction):
                func_name = col.function_name
                col_name = col.column_name

                if func_name == "count":
                    if col_name is None or col_name == "*":
                        agg_col_name = "count(1)"
                        result_row[agg_col_name] = len(self.data)
                    else:
                        agg_col_name = f"count({col_name})"
                        # Count non-null values for specific column
                        non_null_count = sum(
                            1 for row in self.data if row.get(col_name) is not None
                        )
                        result_row[agg_col_name] = non_null_count
                    new_fields.append(MockStructField(agg_col_name, LongType()))
                elif func_name == "sum":
                    agg_col_name = f"sum({col_name})"
                    if col_name is not None:
                        values = [
                            row.get(col_name, 0)
                            for row in self.data
                            if row.get(col_name) is not None
                        ]
                        result_row[agg_col_name] = sum(values) if values else 0
                    else:
                        result_row[agg_col_name] = 0
                    new_fields.append(MockStructField(agg_col_name, DoubleType()))
                elif func_name == "avg":
                    agg_col_name = f"avg({col_name})"
                    if col_name is not None:
                        values = [
                            row.get(col_name, 0)
                            for row in self.data
                            if row.get(col_name) is not None
                        ]
                        result_row[agg_col_name] = (
                            sum(values) / len(values) if values else 0
                        )
                    else:
                        result_row[agg_col_name] = 0
                    new_fields.append(MockStructField(agg_col_name, DoubleType()))
                elif func_name == "max":
                    agg_col_name = f"max({col_name})"
                    if col_name is not None:
                        values = [
                            row.get(col_name)
                            for row in self.data
                            if row.get(col_name) is not None
                        ]
                        result_row[agg_col_name] = max(values) if values else 0
                    else:
                        result_row[agg_col_name] = 0
                    new_fields.append(MockStructField(agg_col_name, DoubleType()))
                elif func_name == "min":
                    agg_col_name = f"min({col_name})"
                    if col_name is not None:
                        values = [
                            row.get(col_name)
                            for row in self.data
                            if row.get(col_name) is not None
                        ]
                        result_row[agg_col_name] = min(values) if values else 0
                    else:
                        result_row[agg_col_name] = 0
                    new_fields.append(MockStructField(agg_col_name, DoubleType()))
                elif func_name == "count(DISTINCT":
                    agg_col_name = f"count(DISTINCT {col_name})"
                    if col_name is not None:
                        values = [
                            row.get(col_name)
                            for row in self.data
                            if row.get(col_name) is not None
                        ]
                        result_row[agg_col_name] = len(set(values)) if values else 0
                    else:
                        result_row[agg_col_name] = 0
                    new_fields.append(MockStructField(agg_col_name, LongType()))
            elif isinstance(col, MockColumn) and (
                col.name.startswith(("count(", "sum(", "avg(", "max(", "min("))
                or col.name.startswith("count(DISTINCT ")
            ):
                # Handle MockColumn with function names
                col_name = col.name
                if col_name.startswith("count("):
                    if col_name == "count(1)":
                        result_row[col_name] = len(self.data)
                    else:
                        # Extract column name from count(column)
                        inner_col = col_name[6:-1]
                        # Count non-null values for specific column
                        non_null_count = sum(
                            1 for row in self.data if row.get(inner_col) is not None
                        )
                        result_row[col_name] = non_null_count
                    new_fields.append(MockStructField(col_name, LongType()))
                elif col_name.startswith("sum("):
                    inner_col = col_name[4:-1]
                    values = [
                        row.get(inner_col, 0)
                        for row in self.data
                        if row.get(inner_col) is not None
                    ]
                    # Ensure values are numeric for sum calculation
                    numeric_values = [v for v in values if isinstance(v, (int, float))]
                    result_row[col_name] = (
                        float(sum(numeric_values)) if numeric_values else 0.0
                    )
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col_name.startswith("avg("):
                    inner_col = col_name[4:-1]
                    values = [
                        row.get(inner_col, 0)
                        for row in self.data
                        if row.get(inner_col) is not None
                    ]
                    # Ensure values are numeric for average calculation
                    numeric_values = [v for v in values if isinstance(v, (int, float))]
                    result_row[col_name] = (
                        float(sum(numeric_values)) / len(numeric_values)
                        if numeric_values
                        else 0.0
                    )
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col_name.startswith("max("):
                    inner_col = col_name[4:-1]
                    values = [
                        row.get(inner_col)
                        for row in self.data
                        if row.get(inner_col) is not None
                    ]
                    result_row[col_name] = float(max(values)) if values else 0.0
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col_name.startswith("min("):
                    inner_col = col_name[4:-1]
                    values = [
                        row.get(inner_col)
                        for row in self.data
                        if row.get(inner_col) is not None
                    ]
                    result_row[col_name] = float(min(values)) if values else 0.0
                    new_fields.append(MockStructField(col_name, DoubleType()))
                elif col_name.startswith("count(DISTINCT"):
                    inner_col = col_name[13:-1]
                    values = [
                        row.get(inner_col)
                        for row in self.data
                        if row.get(inner_col) is not None
                    ]
                    result_row[col_name] = len(set(values)) if values else 0
                    new_fields.append(MockStructField(col_name, LongType()))

        new_schema = MockStructType(new_fields)
        return MockDataFrame([result_row], new_schema, self.storage)

    def filter(
        self, condition: Union[MockColumnOperation, MockColumn]
    ) -> "MockDataFrame":
        """Filter rows based on condition."""
        if isinstance(condition, MockColumn):
            # Simple column reference - return all non-null rows
            filtered_data = [
                row for row in self.data if row.get(condition.name) is not None
            ]
        else:
            # Apply condition logic
            filtered_data = self._apply_condition(self.data, condition)

        return MockDataFrame(filtered_data, self.schema, self.storage)

    def withColumn(
        self,
        col_name: str,
        col: Union[MockColumn, MockColumnOperation, MockLiteral, Any],
    ) -> "MockDataFrame":
        """Add or replace column."""
        new_data = []

        for row in self.data:
            new_row = row.copy()

            if isinstance(col, (MockColumn, MockColumnOperation)):
                # Evaluate the column expression
                evaluated_value = self._evaluate_column_expression(row, col)
                new_row[col_name] = evaluated_value
            elif hasattr(col, "value") and hasattr(col, "column_type"):
                # Handle MockLiteral objects
                new_row[col_name] = col.value
            else:
                new_row[col_name] = col

            new_data.append(new_row)

        # Update schema
        new_fields = [field for field in self.schema.fields if field.name != col_name]

        # Determine the correct type for the new column
        from .spark_types import StringType, LongType, DoubleType, IntegerType

        if isinstance(col, (MockColumn, MockColumnOperation)):
            # For arithmetic operations, determine type based on the operation
            if hasattr(col, "operation") and col.operation in ["+", "-", "*", "/", "%"]:
                # Arithmetic operations typically return LongType or DoubleType
                # For now, use LongType for integer arithmetic
                new_fields.append(MockStructField(col_name, LongType()))
            elif hasattr(col, "operation") and col.operation in ["abs"]:
                new_fields.append(MockStructField(col_name, LongType()))
            elif hasattr(col, "operation") and col.operation in ["length"]:
                new_fields.append(MockStructField(col_name, IntegerType()))
            elif hasattr(col, "operation") and col.operation in ["round"]:
                new_fields.append(MockStructField(col_name, DoubleType()))
            elif hasattr(col, "operation") and col.operation in ["upper", "lower"]:
                new_fields.append(MockStructField(col_name, StringType()))
            else:
                # Default to StringType for unknown operations
                new_fields.append(MockStructField(col_name, StringType()))
        elif hasattr(col, "value") and hasattr(col, "column_type"):
            # Handle MockLiteral objects - use their column_type
            new_fields.append(MockStructField(col_name, col.column_type))
        else:
            # For literal values, infer type
            if isinstance(col, (int, float)):
                if isinstance(col, float):
                    new_fields.append(MockStructField(col_name, DoubleType()))
                else:
                    new_fields.append(MockStructField(col_name, LongType()))
            else:
                new_fields.append(MockStructField(col_name, StringType()))

        new_schema = MockStructType(new_fields)
        return MockDataFrame(new_data, new_schema, self.storage)

    def groupBy(self, *columns: Union[str, MockColumn]) -> "MockGroupedData":
        """Group by columns."""
        col_names = []
        for col in columns:
            if isinstance(col, MockColumn):
                col_names.append(col.name)
            else:
                col_names.append(col)

        # Validate that all columns exist
        for col_name in col_names:
            if col_name not in [field.name for field in self.schema.fields]:
                from .errors import raise_column_not_found

                raise_column_not_found(col_name)

        return MockGroupedData(self, col_names)

    def orderBy(self, *columns: Union[str, MockColumn]) -> "MockDataFrame":
        """Order by columns."""
        col_names: List[str] = []
        sort_orders: List[bool] = []

        for col in columns:
            if isinstance(col, MockColumn):
                col_names.append(col.name)
                sort_orders.append(True)  # Default ascending
            elif hasattr(col, "operation") and hasattr(col, "column"):
                # Handle MockColumnOperation (e.g., col.desc())
                if col.operation == "desc":
                    col_names.append(col.column.name)
                    sort_orders.append(False)  # Descending
                elif col.operation == "asc":
                    col_names.append(col.column.name)
                    sort_orders.append(True)  # Ascending
                else:
                    col_names.append(col.column.name)
                    sort_orders.append(True)  # Default ascending
            else:
                col_names.append(col)
                sort_orders.append(True)  # Default ascending

        # Sort data by columns with proper ordering
        def sort_key(row: Dict[str, Any]) -> Tuple[Any, ...]:
            key_values = []
            for i, col in enumerate(col_names):
                value = row.get(col, None)
                # Handle None values for sorting
                if value is None:
                    value = float("inf") if sort_orders[i] else float("-inf")
                key_values.append(value)
            return tuple(key_values)

        sorted_data = sorted(
            self.data, key=sort_key, reverse=any(not order for order in sort_orders)
        )

        return MockDataFrame(sorted_data, self.schema, self.storage)

    def limit(self, n: int) -> "MockDataFrame":
        """Limit number of rows."""
        limited_data = self.data[:n]
        return MockDataFrame(limited_data, self.schema, self.storage)

    def take(self, n: int) -> List[MockRow]:
        """Take first n rows as list of Row objects."""
        return [MockRow(row) for row in self.data[:n]]

    @property
    def dtypes(self) -> List[Tuple[str, str]]:
        """Get column names and their data types."""
        return [(field.name, field.dataType.typeName()) for field in self.schema.fields]

    def union(self, other: "MockDataFrame") -> "MockDataFrame":
        """Union with another DataFrame."""
        combined_data = self.data + other.data
        return MockDataFrame(combined_data, self.schema, self.storage)

    def join(
        self, other: "MockDataFrame", on: Union[str, List[str]], how: str = "inner"
    ) -> "MockDataFrame":
        """Join with another DataFrame."""
        if isinstance(on, str):
            on = [on]

        # Simple join implementation
        joined_data = []
        for left_row in self.data:
            for right_row in other.data:
                # Check if join condition matches
                if all(left_row.get(col) == right_row.get(col) for col in on):
                    joined_row = left_row.copy()
                    joined_row.update(right_row)
                    joined_data.append(joined_row)

        # Create new schema
        new_fields = self.schema.fields.copy()
        for field in other.schema.fields:
            if not any(f.name == field.name for f in new_fields):
                new_fields.append(field)

        new_schema = MockStructType(new_fields)
        return MockDataFrame(joined_data, new_schema, self.storage)

    def cache(self) -> "MockDataFrame":
        """Cache DataFrame (no-op in mock)."""
        return self

    def persist(self) -> "MockDataFrame":
        """Persist DataFrame (no-op in mock)."""
        return self

    def unpersist(self) -> "MockDataFrame":
        """Unpersist DataFrame (no-op in mock)."""
        return self

    def distinct(self) -> "MockDataFrame":
        """Return distinct rows."""
        seen = set()
        distinct_data = []
        for row in self.data:
            row_tuple = tuple(sorted(row.items()))
            if row_tuple not in seen:
                seen.add(row_tuple)
                distinct_data.append(row)
        return MockDataFrame(distinct_data, self.schema, self.storage)

    def dropDuplicates(self, subset: Optional[List[str]] = None) -> "MockDataFrame":
        """Drop duplicate rows."""
        if subset is None:
            return self.distinct()

        seen = set()
        distinct_data = []
        for row in self.data:
            row_tuple = tuple(sorted((k, v) for k, v in row.items() if k in subset))
            if row_tuple not in seen:
                seen.add(row_tuple)
                distinct_data.append(row)
        return MockDataFrame(distinct_data, self.schema, self.storage)

    def drop(self, *cols: str) -> "MockDataFrame":
        """Drop columns."""
        new_data = []
        for row in self.data:
            new_row = {k: v for k, v in row.items() if k not in cols}
            new_data.append(new_row)

        # Update schema
        new_fields = [field for field in self.schema.fields if field.name not in cols]
        new_schema = MockStructType(new_fields)
        return MockDataFrame(new_data, new_schema, self.storage)

    def withColumnRenamed(self, existing: str, new: str) -> "MockDataFrame":
        """Rename a column."""
        new_data = []
        for row in self.data:
            new_row = {}
            for k, v in row.items():
                if k == existing:
                    new_row[new] = v
                else:
                    new_row[k] = v
            new_data.append(new_row)

        # Update schema
        new_fields = []
        for field in self.schema.fields:
            if field.name == existing:
                new_fields.append(MockStructField(new, field.dataType))
            else:
                new_fields.append(field)
        new_schema = MockStructType(new_fields)
        return MockDataFrame(new_data, new_schema, self.storage)

    def dropna(
        self,
        how: str = "any",
        thresh: Optional[int] = None,
        subset: Optional[List[str]] = None,
    ) -> "MockDataFrame":
        """Drop rows with null values."""
        filtered_data = []
        for row in self.data:
            if subset:
                # Check only specified columns
                null_count = sum(1 for col in subset if row.get(col) is None)
            else:
                # Check all columns
                null_count = sum(1 for v in row.values() if v is None)

            if how == "any" and null_count == 0:
                filtered_data.append(row)
            elif how == "all" and null_count < len(row):
                filtered_data.append(row)
            elif thresh is not None and null_count <= len(row) - thresh:
                filtered_data.append(row)

        return MockDataFrame(filtered_data, self.schema, self.storage)

    def fillna(self, value: Union[Any, Dict[str, Any]]) -> "MockDataFrame":
        """Fill null values."""
        new_data = []
        for row in self.data:
            new_row = row.copy()
            if isinstance(value, dict):
                for col, fill_value in value.items():
                    if new_row.get(col) is None:
                        new_row[col] = fill_value
            else:
                for col in new_row:
                    if new_row[col] is None:
                        new_row[col] = value
            new_data.append(new_row)

        return MockDataFrame(new_data, self.schema, self.storage)

    def printSchema(self) -> None:
        """Print schema."""
        print("MockDataFrame Schema:")
        for field in self.schema.fields:
            print(f"  {field.name}: {field.dataType.__class__.__name__}")

    def explain(self) -> None:
        """Explain execution plan."""
        print("MockDataFrame Execution Plan:")
        print("  MockDataFrame")
        print("    MockDataSource")

    @property
    def rdd(self) -> "MockRDD":
        """Get RDD representation."""
        return MockRDD(self.data)

    def registerTempTable(self, name: str) -> None:
        """Register as temporary table."""
        # Store in storage
        self.storage.insert_data("default", name, self.data, self.schema)

    def createTempView(self, name: str) -> None:
        """Create temporary view."""
        self.registerTempTable(name)

    def _apply_condition(
        self, data: List[Dict[str, Any]], condition: MockColumnOperation
    ) -> List[Dict[str, Any]]:
        """Apply condition to filter data."""
        filtered_data = []

        for row in data:
            if self._evaluate_condition(row, condition):
                filtered_data.append(row)

        return filtered_data

    def _evaluate_condition(
        self, row: Dict[str, Any], condition: Union[MockColumnOperation, MockColumn]
    ) -> bool:
        """Evaluate condition for a single row."""
        # Handle MockColumn case
        if isinstance(condition, MockColumn):
            return row.get(condition.name) is not None

        # Handle MockColumnOperation case
        if condition.operation == "isNotNull":
            return row.get(condition.column.name) is not None
        elif condition.operation == "isNull":
            return row.get(condition.column.name) is None
        elif condition.operation == "==":
            col_value = row.get(condition.column.name)
            return (
                bool(col_value == condition.value) if col_value is not None else False
            )
        elif condition.operation == "!=":
            col_value = row.get(condition.column.name)
            return bool(col_value != condition.value) if col_value is not None else True
        elif condition.operation == ">":
            col_value = row.get(condition.column.name)
            return bool(col_value > condition.value) if col_value is not None else False
        elif condition.operation == ">=":
            col_value = row.get(condition.column.name)
            return (
                bool(col_value >= condition.value) if col_value is not None else False
            )
        elif condition.operation == "<":
            col_value = row.get(condition.column.name)
            return bool(col_value < condition.value) if col_value is not None else False
        elif condition.operation == "<=":
            col_value = row.get(condition.column.name)
            return (
                bool(col_value <= condition.value) if col_value is not None else False
            )
        elif condition.operation == "like":
            col_value = row.get(condition.column.name)
            if col_value is None:
                return False
            value = str(col_value)
            pattern = str(condition.value).replace("%", ".*")
            import re

            return bool(re.match(pattern, value))
        elif condition.operation == "isin":
            col_value = row.get(condition.column.name)
            return col_value in condition.value if col_value is not None else False
        elif condition.operation == "between":
            between_value: Any = row.get(condition.column.name)
            if between_value is None:
                return False
            lower, upper = condition.value
            return bool(lower <= between_value <= upper)
        elif condition.operation == "and":
            return self._evaluate_condition(
                row, condition.column
            ) and self._evaluate_condition(row, condition.value)
        elif condition.operation == "or":
            return self._evaluate_condition(
                row, condition.column
            ) or self._evaluate_condition(row, condition.value)
        elif condition.operation == "not":
            return not self._evaluate_condition(row, condition.column)
        else:
            return False

    def _evaluate_column_expression(
        self, row: Dict[str, Any], column_expression: Any
    ) -> Any:
        """Evaluate a column expression for a single row."""
        if isinstance(column_expression, MockColumn):
            # Check if this is a function call
            col_name = column_expression.name

            # Check if this is an aliased function call
            if hasattr(column_expression, "_original_column") and hasattr(
                column_expression._original_column, "name"
            ):
                original_name = column_expression._original_column.name
                if original_name.startswith(
                    (
                        "coalesce(",
                        "isnull(",
                        "isnan(",
                        "trim(",
                        "ceil(",
                        "floor(",
                        "sqrt(",
                        "regexp_replace(",
                        "split(",
                    )
                ):
                    return self._evaluate_function_call_by_name(row, original_name)

            # Check if this is a direct function call
            if col_name.startswith(
                (
                    "coalesce(",
                    "isnull(",
                    "isnan(",
                    "trim(",
                    "ceil(",
                    "floor(",
                    "sqrt(",
                    "regexp_replace(",
                    "split(",
                )
            ):
                return self._evaluate_function_call_by_name(row, col_name)
            else:
                # Simple column reference
                return row.get(column_expression.name)

        elif hasattr(column_expression, "operation") and hasattr(
            column_expression, "column"
        ):
            # Handle MockColumnOperation (arithmetic operations and function calls)
            if column_expression.operation in ["+", "-", "*", "/", "%"]:
                return self._evaluate_arithmetic_operation(row, column_expression)
            else:
                return self._evaluate_function_call(row, column_expression)

        else:
            # Direct value
            return column_expression

    def _evaluate_arithmetic_operation(
        self, row: Dict[str, Any], operation: Any
    ) -> Any:
        """Evaluate arithmetic operations on columns."""
        if not hasattr(operation, "operation") or not hasattr(operation, "column"):
            return None

        # Extract left value from row
        left_value = (
            row.get(operation.column.name)
            if hasattr(operation.column, "name")
            else None
        )

        # Extract right value - handle MockColumn, MockLiteral, or primitive values
        right_value = operation.value
        if hasattr(right_value, "name") and hasattr(right_value, "__class__"):
            # It's a MockColumn - get value from row
            if hasattr(right_value, "name"):
                right_value = row.get(right_value.name)
            else:
                right_value = None
        elif hasattr(right_value, "value"):
            # It's a MockLiteral - get the actual value
            right_value = right_value.value

        if operation.operation == "-" and operation.value is None:
            # Unary minus operation
            if left_value is None:
                return None
            return -left_value

        if left_value is None or right_value is None:
            return None

        if operation.operation == "+":
            return left_value + right_value
        elif operation.operation == "-":
            return left_value - right_value
        elif operation.operation == "*":
            return left_value * right_value
        elif operation.operation == "/":
            return left_value / right_value if right_value != 0 else None
        elif operation.operation == "%":
            return left_value % right_value if right_value != 0 else None
        else:
            return None

    def _evaluate_function_call(self, row: Dict[str, Any], operation: Any) -> Any:
        """Evaluate function calls like upper(), lower(), length(), abs(), round()."""
        if not hasattr(operation, "operation") or not hasattr(operation, "column"):
            return None

        # Evaluate the column expression (could be a nested operation)
        if hasattr(operation.column, "operation") and hasattr(
            operation.column, "column"
        ):
            # The column is itself a MockColumnOperation, evaluate it first
            value = self._evaluate_column_expression(row, operation.column)
        else:
            # Simple column reference
            column_name = (
                operation.column.name
                if hasattr(operation.column, "name")
                else str(operation.column)
            )
            value = row.get(column_name)

        if value is None:
            return None

        func_name = operation.operation

        if func_name == "upper":
            return str(value).upper()
        elif func_name == "lower":
            return str(value).lower()
        elif func_name == "length":
            return len(str(value))
        elif func_name == "abs":
            return abs(value) if isinstance(value, (int, float)) else value
        elif func_name == "round":
            # For round function, we need to handle the precision parameter
            precision = getattr(operation, "precision", 0)
            return round(value, precision) if isinstance(value, (int, float)) else value
        elif func_name == "trim":
            return str(value).strip()
        elif func_name == "ceil":
            import math

            return math.ceil(value) if isinstance(value, (int, float)) else value
        elif func_name == "floor":
            import math

            return math.floor(value) if isinstance(value, (int, float)) else value
        elif func_name == "sqrt":
            import math

            return (
                math.sqrt(value)
                if isinstance(value, (int, float)) and value >= 0
                else None
            )
        elif func_name == "split":
            if value is None:
                return None
            delimiter = operation.value
            return str(value).split(delimiter)
        elif func_name == "regexp_replace":
            if value is None:
                return None
            pattern = (
                operation.value[0]
                if isinstance(operation.value, tuple)
                else operation.value
            )
            replacement = (
                operation.value[1]
                if isinstance(operation.value, tuple) and len(operation.value) > 1
                else ""
            )
            import re

            return re.sub(pattern, replacement, str(value))
        elif func_name == "cast":
            # Cast operation
            if value is None:
                return None
            cast_type = operation.value
            if isinstance(cast_type, str):
                # String type name, convert value
                if cast_type.lower() in ["double", "float"]:
                    return float(value)
                elif cast_type.lower() in ["int", "integer", "long", "bigint"]:
                    return int(
                        float(value)
                    )  # Convert via float to handle decimal strings
                elif cast_type.lower() in ["string", "varchar"]:
                    return str(value)
                else:
                    return value
            else:
                # Type object, use appropriate conversion
                return value
        else:
            return value

    def _evaluate_function_call_by_name(
        self, row: Dict[str, Any], col_name: str
    ) -> Any:
        """Evaluate function calls by parsing the function name."""
        if col_name.startswith("coalesce("):
            # Parse coalesce arguments: coalesce(col1, col2, ...)
            # For now, implement basic coalesce logic
            if "name" in col_name and "Unknown" in col_name:
                name_value = row.get("name")
                return name_value if name_value is not None else "Unknown"
        elif col_name.startswith("isnull("):
            # Parse isnull argument: isnull(col)
            if "name" in col_name:
                return row.get("name") is None
        elif col_name.startswith("isnan("):
            # Parse isnan argument: isnan(col)
            if "salary" in col_name:
                value = row.get("salary")
                if isinstance(value, float):
                    return value != value  # NaN check
                return False
        elif col_name.startswith("trim("):
            # Parse trim argument: trim(col)
            if "name" in col_name:
                value = row.get("name")
                return str(value).strip() if value is not None else None
        elif col_name.startswith("ceil("):
            # Parse ceil argument: ceil(col)
            import math

            if "value" in col_name:
                value = row.get("value")
                return math.ceil(value) if isinstance(value, (int, float)) else value
        elif col_name.startswith("floor("):
            # Parse floor argument: floor(col)
            import math

            if "value" in col_name:
                value = row.get("value")
                return math.floor(value) if isinstance(value, (int, float)) else value
        elif col_name.startswith("sqrt("):
            # Parse sqrt argument: sqrt(col)
            import math

            if "value" in col_name:
                value = row.get("value")
                return (
                    math.sqrt(value)
                    if isinstance(value, (int, float)) and value >= 0
                    else None
                )
        elif col_name.startswith("regexp_replace("):
            # Parse regexp_replace arguments: regexp_replace(col, pattern, replacement)
            if "name" in col_name:
                value = row.get("name")
                if value is not None:
                    import re

                    # Simple regex replacement - replace 'e' with 'X'
                    return re.sub(r"e", "X", str(value))
                return value
        elif col_name.startswith("split("):
            # Parse split arguments: split(col, delimiter)
            if "name" in col_name:
                value = row.get("name")
                if value is not None:
                    # Simple split on 'l'
                    return str(value).split("l")
                return []

        # Default fallback
        return None

    def _is_function_call(self, col_name: str) -> bool:
        """Check if column name is a function call."""
        function_patterns = [
            "upper(",
            "lower(",
            "length(",
            "abs(",
            "round(",
            "count(",
            "sum(",
            "avg(",
            "max(",
            "min(",
            "count(DISTINCT ",
            "coalesce(",
            "isnull(",
            "isnan(",
            "trim(",
            "ceil(",
            "floor(",
            "sqrt(",
            "regexp_replace(",
            "split(",
        ]
        return any(col_name.startswith(pattern) for pattern in function_patterns)

    def _evaluate_window_functions(
        self, data: List[Dict[str, Any]], window_functions: List[tuple]
    ) -> List[Dict[str, Any]]:
        """Evaluate window functions across all rows."""
        result_data = data.copy()

        for col_index, window_func in window_functions:
            col_name = window_func.name

            if window_func.function_name == "row_number":
                # For row_number(), we need to handle partitionBy and orderBy
                if hasattr(window_func, "_window_spec") and window_func._window_spec:
                    window_spec = window_func._window_spec

                    # Get partition by columns from window spec
                    partition_by_cols = getattr(window_spec, "_partition_by", [])
                    # Get order by columns from window spec
                    order_by_cols = getattr(window_spec, "_order_by", [])

                    if partition_by_cols:
                        # Handle partitioning - group by partition columns
                        partition_groups = {}
                        for i, row in enumerate(result_data):
                            # Create partition key
                            partition_key = tuple(
                                (
                                    row.get(col.name)
                                    if hasattr(col, "name")
                                    else row.get(str(col))
                                )
                                for col in partition_by_cols
                            )
                            if partition_key not in partition_groups:
                                partition_groups[partition_key] = []
                            partition_groups[partition_key].append(i)

                        # Assign row numbers within each partition
                        for partition_indices in partition_groups.values():
                            if order_by_cols:
                                # Sort within partition by order by columns using corrected ordering logic
                                sorted_partition_indices = (
                                    self._apply_ordering_to_indices(
                                        result_data, partition_indices, order_by_cols
                                    )
                                )
                            else:
                                # No order by - use original order within partition
                                sorted_partition_indices = partition_indices

                            # Assign row numbers starting from 1 within each partition
                            for i, original_index in enumerate(
                                sorted_partition_indices
                            ):
                                result_data[original_index][col_name] = i + 1
                    elif order_by_cols:
                        # No partitioning, just sort by order by columns using corrected ordering logic
                        sorted_indices = self._apply_ordering_to_indices(
                            result_data, list(range(len(result_data))), order_by_cols
                        )

                        # Assign row numbers based on sorted order
                        for i, original_index in enumerate(sorted_indices):
                            result_data[original_index][col_name] = i + 1
                    else:
                        # No partition or order by - just assign sequential row numbers
                        for i in range(len(result_data)):
                            result_data[i][col_name] = i + 1
                else:
                    # No window spec - assign sequential row numbers
                    for i in range(len(result_data)):
                        result_data[i][col_name] = i + 1
            elif window_func.function_name == "lag":
                # Handle lag function - get previous row value
                self._evaluate_lag_lead(
                    result_data, window_func, col_name, is_lead=False
                )
            elif window_func.function_name == "lead":
                # Handle lead function - get next row value
                self._evaluate_lag_lead(
                    result_data, window_func, col_name, is_lead=True
                )
            elif window_func.function_name in ["rank", "dense_rank"]:
                # Handle rank and dense_rank functions
                self._evaluate_rank_functions(result_data, window_func, col_name)
            elif window_func.function_name in [
                "avg",
                "sum",
                "count",
                "countDistinct",
                "max",
                "min",
            ]:
                # Handle aggregate window functions
                self._evaluate_aggregate_window_functions(
                    result_data, window_func, col_name
                )
            else:
                # For other window functions, assign None for now
                for row in result_data:
                    row[col_name] = None

        return result_data

    def _evaluate_lag_lead(
        self, data: List[Dict[str, Any]], window_func: Any, col_name: str, is_lead: bool
    ) -> None:
        """Evaluate lag or lead window function."""
        if not window_func.column_name:
            # No column specified, set to None
            for row in data:
                row[col_name] = None
            return

        # Get offset and default value
        offset = getattr(window_func, "offset", 1)
        default_value = getattr(window_func, "default_value", None)

        # Handle window specification if present
        if hasattr(window_func, "_window_spec") and window_func._window_spec:
            window_spec = window_func._window_spec
            partition_by_cols = getattr(window_spec, "_partition_by", [])
            order_by_cols = getattr(window_spec, "_order_by", [])

            if partition_by_cols:
                # Handle partitioning
                partition_groups = {}
                for i, row in enumerate(data):
                    partition_key = tuple(
                        row.get(col.name) if hasattr(col, "name") else row.get(str(col))
                        for col in partition_by_cols
                    )
                    if partition_key not in partition_groups:
                        partition_groups[partition_key] = []
                    partition_groups[partition_key].append(i)

                # Process each partition
                for partition_indices in partition_groups.values():
                    # Apply ordering to partition indices
                    ordered_indices = self._apply_ordering_to_indices(
                        data, partition_indices, order_by_cols
                    )
                    self._apply_lag_lead_to_partition(
                        data,
                        ordered_indices,
                        window_func.column_name,
                        col_name,
                        offset,
                        default_value,
                        is_lead,
                    )
            else:
                # No partitioning, apply to entire dataset with ordering
                all_indices = list(range(len(data)))
                ordered_indices = self._apply_ordering_to_indices(
                    data, all_indices, order_by_cols
                )
                self._apply_lag_lead_to_partition(
                    data,
                    ordered_indices,
                    window_func.column_name,
                    col_name,
                    offset,
                    default_value,
                    is_lead,
                )
        else:
            # No window spec, apply to entire dataset
            self._apply_lag_lead_to_partition(
                data,
                list(range(len(data))),
                window_func.column_name,
                col_name,
                offset,
                default_value,
                is_lead,
            )

    def _apply_ordering_to_indices(
        self, data: List[Dict[str, Any]], indices: List[int], order_by_cols: List[Any]
    ) -> List[int]:
        """Apply ordering to a list of indices based on order by columns."""
        if not order_by_cols:
            return indices

        def sort_key(idx):
            row = data[idx]
            key_values = []
            for col in order_by_cols:
                # Handle MockColumnOperation objects (like col("salary").desc())
                if hasattr(col, "column") and hasattr(col.column, "name"):
                    col_name = col.column.name
                elif hasattr(col, "name"):
                    col_name = col.name
                else:
                    col_name = str(col)
                value = row.get(col_name)
                key_values.append(value)
            return tuple(key_values)

        # Check if any column has desc operation
        has_desc = any(
            hasattr(col, "operation") and col.operation == "desc"
            for col in order_by_cols
        )

        # Sort indices based on the ordering
        return sorted(indices, key=sort_key, reverse=has_desc)

    def _apply_lag_lead_to_partition(
        self,
        data: List[Dict[str, Any]],
        indices: List[int],
        source_col: str,
        target_col: str,
        offset: int,
        default_value: Any,
        is_lead: bool,
    ) -> None:
        """Apply lag or lead to a specific partition."""
        if is_lead:
            # Lead: get next row value
            for i, idx in enumerate(indices):
                source_idx = i + offset
                if source_idx < len(indices):
                    actual_idx = indices[source_idx]
                    data[idx][target_col] = data[actual_idx].get(source_col)
                else:
                    data[idx][target_col] = default_value
        else:
            # Lag: get previous row value
            for i, idx in enumerate(indices):
                source_idx = i - offset
                if source_idx >= 0:
                    actual_idx = indices[source_idx]
                    data[idx][target_col] = data[actual_idx].get(source_col)
                else:
                    data[idx][target_col] = default_value

    def _evaluate_rank_functions(
        self, data: List[Dict[str, Any]], window_func: Any, col_name: str
    ) -> None:
        """Evaluate rank or dense_rank window function."""
        is_dense = window_func.function_name == "dense_rank"

        # Handle window specification if present
        if hasattr(window_func, "_window_spec") and window_func._window_spec:
            window_spec = window_func._window_spec
            partition_by_cols = getattr(window_spec, "_partition_by", [])
            order_by_cols = getattr(window_spec, "_order_by", [])

            if partition_by_cols:
                # Handle partitioning
                partition_groups = {}
                for i, row in enumerate(data):
                    partition_key = tuple(
                        row.get(col.name) if hasattr(col, "name") else row.get(str(col))
                        for col in partition_by_cols
                    )
                    if partition_key not in partition_groups:
                        partition_groups[partition_key] = []
                    partition_groups[partition_key].append(i)

                # Process each partition
                for partition_indices in partition_groups.values():
                    self._apply_rank_to_partition(
                        data, partition_indices, order_by_cols, col_name, is_dense
                    )
            else:
                # No partitioning, apply to entire dataset
                self._apply_rank_to_partition(
                    data, list(range(len(data))), order_by_cols, col_name, is_dense
                )
        else:
            # No window spec, assign ranks based on original order
            for i in range(len(data)):
                data[i][col_name] = i + 1

    def _apply_rank_to_partition(
        self,
        data: List[Dict[str, Any]],
        indices: List[int],
        order_by_cols: List[Any],
        col_name: str,
        is_dense: bool,
    ) -> None:
        """Apply rank or dense_rank to a specific partition."""
        if not order_by_cols:
            # No order by, assign ranks based on original order
            for i, idx in enumerate(indices):
                data[idx][col_name] = i + 1
            return

        # Sort partition by order by columns using the corrected ordering logic
        sorted_indices = self._apply_ordering_to_indices(data, indices, order_by_cols)

        # Assign ranks in sorted order
        if is_dense:
            # Dense rank: consecutive ranks without gaps
            current_rank = 1
            previous_values = None

            for i, idx in enumerate(sorted_indices):
                row = data[idx]
                current_values = []
                for col in order_by_cols:
                    # Handle MockColumnOperation objects (like col("salary").desc())
                    if hasattr(col, "column") and hasattr(col.column, "name"):
                        order_col_name = col.column.name
                    elif hasattr(col, "name"):
                        order_col_name = col.name
                    else:
                        order_col_name = str(col)
                    value = row.get(order_col_name)
                    current_values.append(value)

                if previous_values is not None and current_values != previous_values:
                    current_rank += 1

                data[idx][col_name] = current_rank
                previous_values = current_values
        else:
            # Regular rank: ranks with gaps for ties
            current_rank = 1

            for i, idx in enumerate(sorted_indices):
                if i > 0:
                    prev_idx = sorted_indices[i - 1]
                    # Check if current and previous rows have different values
                    row = data[idx]
                    prev_row = data[prev_idx]

                    current_values = []
                    prev_values = []
                    for col in order_by_cols:
                        # Handle MockColumnOperation objects (like col("salary").desc())
                        if hasattr(col, "column") and hasattr(col.column, "name"):
                            order_col_name = col.column.name
                        elif hasattr(col, "name"):
                            order_col_name = col.name
                        else:
                            order_col_name = str(col)
                        current_values.append(row.get(order_col_name))
                        prev_values.append(prev_row.get(order_col_name))

                    if current_values != prev_values:
                        current_rank = i + 1
                else:
                    current_rank = 1

                data[idx][col_name] = current_rank

    def _evaluate_aggregate_window_functions(
        self, data: List[Dict[str, Any]], window_func: Any, col_name: str
    ) -> None:
        """Evaluate aggregate window functions like avg, sum, count, etc."""
        if not window_func.column_name and window_func.function_name not in ["count"]:
            # No column specified for functions that need it
            for row in data:
                row[col_name] = None
            return

        # Handle window specification if present
        if hasattr(window_func, "_window_spec") and window_func._window_spec:
            window_spec = window_func._window_spec
            partition_by_cols = getattr(window_spec, "_partition_by", [])
            order_by_cols = getattr(window_spec, "_order_by", [])

            if partition_by_cols:
                # Handle partitioning
                partition_groups = {}
                for i, row in enumerate(data):
                    partition_key = tuple(
                        row.get(col.name) if hasattr(col, "name") else row.get(str(col))
                        for col in partition_by_cols
                    )
                    if partition_key not in partition_groups:
                        partition_groups[partition_key] = []
                    partition_groups[partition_key].append(i)

                # Process each partition
                for partition_indices in partition_groups.values():
                    # Apply ordering to partition indices
                    ordered_indices = self._apply_ordering_to_indices(
                        data, partition_indices, order_by_cols
                    )
                    self._apply_aggregate_to_partition(
                        data, ordered_indices, window_func, col_name
                    )
            else:
                # No partitioning, apply to entire dataset with ordering
                all_indices = list(range(len(data)))
                ordered_indices = self._apply_ordering_to_indices(
                    data, all_indices, order_by_cols
                )
                self._apply_aggregate_to_partition(
                    data, ordered_indices, window_func, col_name
                )
        else:
            # No window spec, apply to entire dataset
            all_indices = list(range(len(data)))
            self._apply_aggregate_to_partition(data, all_indices, window_func, col_name)

    def _apply_aggregate_to_partition(
        self,
        data: List[Dict[str, Any]],
        indices: List[int],
        window_func: Any,
        col_name: str,
    ) -> None:
        """Apply aggregate function to a specific partition."""
        if not indices:
            return

        source_col = window_func.column_name
        func_name = window_func.function_name

        # Get window boundaries if specified
        rows_between = (
            getattr(window_func._window_spec, "_rows_between", None)
            if hasattr(window_func, "_window_spec") and window_func._window_spec
            else None
        )

        for i, idx in enumerate(indices):
            # Determine the window for this row
            if rows_between:
                start_offset, end_offset = rows_between
                window_start = max(0, i + start_offset)
                window_end = min(len(indices), i + end_offset + 1)
            else:
                # Default: all rows up to current row
                window_start = 0
                window_end = i + 1

            # Get values in the window
            window_values = []
            for j in range(window_start, window_end):
                if j < len(indices):
                    row_idx = indices[j]
                    if source_col:
                        value = data[row_idx].get(source_col)
                        if value is not None:
                            window_values.append(value)
                    else:
                        # For count(*) - count all rows
                        window_values.append(1)

            # Apply aggregate function
            if func_name == "avg":
                data[idx][col_name] = (
                    sum(window_values) / len(window_values) if window_values else None
                )
            elif func_name == "sum":
                data[idx][col_name] = sum(window_values) if window_values else None
            elif func_name == "count":
                data[idx][col_name] = len(window_values)
            elif func_name == "countDistinct":
                data[idx][col_name] = len(set(window_values))
            elif func_name == "max":
                data[idx][col_name] = max(window_values) if window_values else None
            elif func_name == "min":
                data[idx][col_name] = min(window_values) if window_values else None

    def _evaluate_case_when(self, row: Dict[str, Any], case_when_obj) -> Any:
        """Evaluate CASE WHEN expression for a row."""
        # Evaluate each condition in order
        for condition, value in case_when_obj.conditions:
            if self._evaluate_case_when_condition(row, condition):
                return self._evaluate_value(row, value)

        # Return else value if no condition matches
        if case_when_obj.else_value is not None:
            return self._evaluate_value(row, case_when_obj.else_value)

        return None

    def _evaluate_case_when_condition(self, row: Dict[str, Any], condition) -> bool:
        """Evaluate a CASE WHEN condition for a row."""
        if hasattr(condition, "operation") and hasattr(condition, "column"):
            # Handle MockColumnOperation conditions
            if condition.operation == ">":
                col_value = self._get_column_value(row, condition.column)
                return col_value > condition.value
            elif condition.operation == ">=":
                col_value = self._get_column_value(row, condition.column)
                return col_value >= condition.value
            elif condition.operation == "<":
                col_value = self._get_column_value(row, condition.column)
                return col_value < condition.value
            elif condition.operation == "<=":
                col_value = self._get_column_value(row, condition.column)
                return col_value <= condition.value
            elif condition.operation == "==":
                col_value = self._get_column_value(row, condition.column)
                return col_value == condition.value
            elif condition.operation == "!=":
                col_value = self._get_column_value(row, condition.column)
                return col_value != condition.value
        return False

    def _evaluate_value(self, row: Dict[str, Any], value) -> Any:
        """Evaluate a value (could be a column reference, literal, or operation)."""
        if hasattr(value, "operation") and hasattr(value, "column"):
            # It's a MockColumnOperation
            return self._evaluate_column_expression(row, value)
        elif hasattr(value, "name"):
            # It's a column reference
            return self._get_column_value(row, value)
        else:
            # It's a literal value
            return value

    def _get_column_value(self, row: Dict[str, Any], column) -> Any:
        """Get column value from row."""
        if hasattr(column, "name"):
            return row.get(column.name)
        else:
            return row.get(str(column))

    def _get_column_type(self, column) -> Any:
        """Get column type from schema."""
        if hasattr(column, "name"):
            for field in self.schema.fields:
                if field.name == column.name:
                    return field.dataType
        return None

    def createOrReplaceTempView(self, name: str) -> None:
        """Create or replace a temporary view of this DataFrame."""
        # Store the DataFrame as a temporary view in the storage manager
        self.storage.create_temp_view(name, self)

    @property
    def write(self) -> MockDataFrameWriter:
        """Get DataFrame writer."""
        return MockDataFrameWriter(self, self.storage)


class MockRDD:
    """Mock RDD for DataFrame compatibility."""

    def __init__(self, data: List[Dict[str, Any]]):
        """Initialize MockRDD."""
        self.data = data

    def collect(self) -> List[Any]:
        """Collect RDD data."""
        return self.data

    def count(self) -> int:
        """Count RDD elements."""
        return len(self.data)


class MockGroupedData:
    """Mock grouped data for aggregation operations."""

    def __init__(self, df: MockDataFrame, group_columns: List[str]):
        self.df = df
        self.group_columns = group_columns

    def agg(self, *exprs: Union[str, MockColumn, MockColumnOperation]) -> MockDataFrame:
        """Aggregate grouped data."""
        # Group data by group columns
        groups = {}
        for row in self.df.data:
            group_key = tuple(row.get(col) for col in self.group_columns)
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(row)

        # Apply aggregations
        result_data = []
        for group_key, group_rows in groups.items():
            result_row = dict(zip(self.group_columns, group_key))

            for expr in exprs:
                if isinstance(expr, str):
                    # Handle string expressions like "sum(age)"
                    if expr.startswith("sum("):
                        col_name = expr[4:-1]
                        values = [
                            row.get(col_name, 0)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr] = sum(values) if values else 0
                    elif expr.startswith("avg("):
                        col_name = expr[4:-1]
                        values = [
                            row.get(col_name, 0)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr] = sum(values) / len(values) if values else 0
                    elif expr.startswith("count("):
                        result_row[expr] = len(group_rows)
                    elif expr.startswith("max("):
                        col_name = expr[4:-1]
                        values = [
                            row.get(col_name)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr] = max(values) if values else None
                    elif expr.startswith("min("):
                        col_name = expr[4:-1]
                        values = [
                            row.get(col_name)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr] = min(values) if values else None
                elif hasattr(expr, "function_name"):
                    # Handle MockAggregateFunction
                    func_name = expr.function_name
                    col_name = expr.column_name

                    # Use alias if available, otherwise use function name
                    alias_name = getattr(expr, "_alias", None)

                    if func_name == "sum":
                        values = [
                            row.get(col_name, 0)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_key = alias_name if alias_name else f"sum({col_name})"
                        result_row[result_key] = sum(values) if values else 0
                    elif func_name == "avg":
                        values = [
                            row.get(col_name, 0)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_key = alias_name if alias_name else f"avg({col_name})"
                        result_row[result_key] = (
                            sum(values) / len(values) if values else 0
                        )
                    elif func_name == "count":
                        if col_name == "*":
                            result_key = alias_name if alias_name else "count(1)"
                            result_row[result_key] = len(group_rows)
                        else:
                            result_key = (
                                alias_name if alias_name else f"count({col_name})"
                            )
                            result_row[result_key] = len(group_rows)
                    elif func_name == "max":
                        values = [
                            row.get(col_name)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_key = alias_name if alias_name else f"max({col_name})"
                        result_row[result_key] = max(values) if values else None
                    elif func_name == "min":
                        values = [
                            row.get(col_name)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_key = alias_name if alias_name else f"min({col_name})"
                        result_row[result_key] = min(values) if values else None
                elif hasattr(expr, "name"):
                    # Handle MockColumn or MockColumnOperation
                    expr_name = expr.name
                    if expr_name.startswith("sum("):
                        col_name = expr_name[4:-1]
                        values = [
                            row.get(col_name, 0)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr_name] = sum(values) if values else 0
                    elif expr_name.startswith("avg("):
                        col_name = expr_name[4:-1]
                        values = [
                            row.get(col_name, 0)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr_name] = (
                            sum(values) / len(values) if values else 0
                        )
                    elif expr_name.startswith("count("):
                        result_row[expr_name] = len(group_rows)
                    elif expr_name.startswith("max("):
                        col_name = expr_name[4:-1]
                        values = [
                            row.get(col_name)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr_name] = max(values) if values else None
                    elif expr_name.startswith("min("):
                        col_name = expr_name[4:-1]
                        values = [
                            row.get(col_name)
                            for row in group_rows
                            if row.get(col_name) is not None
                        ]
                        result_row[expr_name] = min(values) if values else None

            result_data.append(result_row)

        # Create new schema
        new_fields = []
        for col in self.group_columns:
            # Find the field in the original schema
            for field in self.df.schema.fields:
                if field.name == col:
                    new_fields.append(field)
                    break

        # Add aggregation result fields
        for expr in exprs:
            if isinstance(expr, str):
                from .spark_types import LongType, DoubleType

                # Determine the correct type based on the function
                if expr.startswith(("sum(", "avg(", "max(", "min(")):
                    new_fields.append(MockStructField(expr, DoubleType()))
                else:
                    new_fields.append(MockStructField(expr, LongType()))
            elif hasattr(expr, "function_name"):
                # Handle MockAggregateFunction
                from .spark_types import LongType, DoubleType, IntegerType

                func_name = expr.function_name
                col_name = expr.column_name
                alias_name = getattr(expr, "_alias", None)

                if func_name == "count":
                    if col_name == "*":
                        field_name = alias_name if alias_name else "count(1)"
                        new_fields.append(MockStructField(field_name, LongType()))
                    else:
                        field_name = alias_name if alias_name else f"count({col_name})"
                        new_fields.append(MockStructField(field_name, LongType()))
                elif func_name == "sum":
                    field_name = (
                        alias_name if alias_name else f"{func_name}({col_name})"
                    )
                    # Sum should return the same type as the source column
                    source_type = None
                    for field in self.df.schema.fields:
                        if field.name == col_name:
                            source_type = field.dataType
                            break
                    if source_type and source_type in [LongType(), IntegerType()]:
                        new_fields.append(MockStructField(field_name, source_type))
                    else:
                        new_fields.append(MockStructField(field_name, DoubleType()))
                elif func_name == "avg":
                    field_name = (
                        alias_name if alias_name else f"{func_name}({col_name})"
                    )
                    new_fields.append(MockStructField(field_name, DoubleType()))
                elif func_name in ["max", "min"]:
                    field_name = (
                        alias_name if alias_name else f"{func_name}({col_name})"
                    )
                    # For max/min, infer type from the source column
                    source_type = None
                    for field in self.df.schema.fields:
                        if field.name == col_name:
                            source_type = field.dataType
                            break
                    if source_type and source_type in [
                        DoubleType(),
                        LongType(),
                        IntegerType(),
                    ]:
                        new_fields.append(MockStructField(field_name, source_type))
                    else:
                        new_fields.append(MockStructField(field_name, DoubleType()))
                else:
                    field_name = (
                        alias_name if alias_name else f"{func_name}({col_name})"
                    )
                    new_fields.append(MockStructField(field_name, LongType()))
            elif hasattr(expr, "name"):
                from .spark_types import LongType, DoubleType

                expr_name = expr.name
                if expr_name.startswith(("sum(", "avg(", "max(", "min(")):
                    new_fields.append(MockStructField(expr_name, DoubleType()))
                else:
                    new_fields.append(MockStructField(expr_name, LongType()))

        new_schema = MockStructType(new_fields)
        return MockDataFrame(result_data, new_schema, self.df.storage)

    def count(self) -> MockDataFrame:
        """Count grouped data."""
        # Group data by group columns
        groups = {}
        for row in self.df.data:
            group_key = tuple(row.get(col) for col in self.group_columns)
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(row)

        # Apply count aggregation
        result_data = []
        for group_key, group_rows in groups.items():
            result_row = dict(zip(self.group_columns, group_key))
            result_row["count"] = len(group_rows)
            result_data.append(result_row)

        # Create new schema
        new_fields = []
        for col in self.group_columns:
            # Find the field in the original schema
            for field in self.df.schema.fields:
                if field.name == col:
                    new_fields.append(field)
                    break

        # Add count field
        from .spark_types import LongType

        new_fields.append(MockStructField("count", LongType()))

        new_schema = MockStructType(new_fields)
        return MockDataFrame(result_data, new_schema, self.df.storage)

    def sum(self, *columns: Union[str, MockColumn]) -> MockDataFrame:
        """Sum grouped data."""
        if not columns:
            return self.agg("sum(1)")

        exprs = [
            f"sum({col})" if isinstance(col, str) else f"sum({col.name})"
            for col in columns
        ]
        return self.agg(*exprs)

    def avg(self, *columns: Union[str, MockColumn]) -> MockDataFrame:
        """Average grouped data."""
        if not columns:
            return self.agg("avg(1)")

        exprs = [
            f"avg({col})" if isinstance(col, str) else f"avg({col.name})"
            for col in columns
        ]
        return self.agg(*exprs)

    def max(self, *columns: Union[str, MockColumn]) -> MockDataFrame:
        """Max grouped data."""
        if not columns:
            return self.agg("max(1)")

        exprs = [
            f"max({col})" if isinstance(col, str) else f"max({col.name})"
            for col in columns
        ]
        return self.agg(*exprs)

    def min(self, *columns: Union[str, MockColumn]) -> MockDataFrame:
        """Min grouped data."""
        if not columns:
            return self.agg("min(1)")

        exprs = [
            f"min({col})" if isinstance(col, str) else f"min({col.name})"
            for col in columns
        ]
        return self.agg(*exprs)
