class DataQuality:

    from typing import List, Dict, Optional
    
    @classmethod
    def save_data_quality_results(
        cls,
        results: List[Dict],
        table_name: Optional[str] = None
    ) -> None:
        """
        Save data quality validation results into a Spark table.

        Parameters
        ----------

        results : list[dict]
            A list of dictionaries, where each dictionary contains:
            {

                "job_name": str
                "expectation_type": str,
                "rule": str,
                "condition": str,
                "total_records": int,
                "passed_records": int,
                "failed_records": int,
                "status": str
            }

        table_name : str, optional
            Name of the Spark table where results will be stored (default: data_quality_results).
        """
        from pyspark.sql import Row, DataFrame
        from pyspark.sql.functions import current_timestamp

        row_results = [Row(**r) for r in results]
        results_df = spark.createDataFrame(row_results)
        results_df = results_df.withColumn("_timestamp", current_timestamp())
        results_df.write.mode("append").saveAsTable(table_name)
        print(f" Data quality results appended to table `{table_name}`")



    from typing import Dict
    @staticmethod
    def expect(rules: Dict[str, str], job_name: Optional[str] = None,  dq_table_name: Optional[str] = None):
        """
        A decorator to validate Spark DataFrames against data quality rules.

        Parameters
        ----------
        rules : dict[str, str]
            A dictionary where keys are human-readable rule descriptions
            and values are SQL filter expressions to validate.

            Example:
            --------
            rules = {
                "Employee ID should be greater than 2": "emp_id > 2",
                "Name should not be null": "fname IS NOT NULL"
            }
        job_name : str, optional
            Name of the job where data quality rules are applied.
            This is used to identify the job in the data quality results table.

        dq_table_name : str, optional
                    Name of the table where data quality results will be stored.
        Returns
        -------
        function
            A decorated function that returns the DataFrame with
            validation results printed for each rule.

        Usage
        -----
        @DataQuality.expect(rules)
        def load_employee_df() -> DataFrame:
            return spark.read.table("employee")

        df = load_employee_df()
        """
        from pyspark.sql import DataFrame
        from pyspark.sql.functions import expr
        from typing import Callable

        def decorator(func: Callable[..., DataFrame]) -> Callable[..., DataFrame]:
            def wrapper(*args, **kwargs) -> DataFrame:
                df: DataFrame = func(*args, **kwargs)
                total_count = df.count()
                validation_results = {}
                for description, condition in rules.items():
                    failed_count = df.filter(expr(f"NOT ({condition})")).count()
                    passed_count = total_count - failed_count
                    validation_results[description] = {
                        "rule": condition,
                        "passed": passed_count,
                        "failed": failed_count,
                        "total": total_count,
                        "status": "PASSED" if failed_count == 0 else "FAILED"
                    }


                # Print results in a framework-style report
                print("="*50)
                print(" DATA QUALITY VALIDATION REPORT ")
                print("="*50)
                dq_input = []
                for desc, result in validation_results.items():
                    print(f"Rule: {desc}")
                    print(f" - Condition: {result['rule']}")
                    print(f" - Total: {result['total']} | Passed: {result['passed']} | Failed: {result['failed']}")
                    print(f" - Status: {result['status']}")
                    print("-"*50)
                    if dq_table_name and job_name:    
                        dq_input.append(
                            {
                                "job_name": job_name,
                                "expectation_type": 'expect',
                                "rule": desc,
                                "condition": result['rule'],
                                "total_records": result['total'],
                                "passed_records": result['passed'],
                                "failed_records": result['failed'],
                                "status": result['status']
                            })
                if dq_table_name and job_name:
                    DataQuality.save_data_quality_results(dq_input, dq_table_name)

                return df
            return wrapper
        return decorator
    


    from typing import Dict
    @staticmethod
    def expect_drop(rules: Dict[str, str], job_name: Optional[str] = None,  dq_table_name: Optional[str] = None):
        """
        A decorator to validate Spark DataFrames against data quality rules.

        Parameters
        ----------
        rules : dict[str, str]
            A dictionary where keys are human-readable rule descriptions
            and values are SQL filter expressions to validate.

            Example:
            --------
            rules = {
                "Employee ID should be greater than 2": "emp_id > 2",
                "Name should not be null": "fname IS NOT NULL"
            }
        job_name : str, optional
            Name of the job where data quality rules are applied.
            This is used to identify the job in the data quality results table.

        dq_table_name : str, optional
                    Name of the table where data quality results will be stored.
        Returns
        -------
        function
            A decorated function that returns the filtered DataFrame with
            validation results printed for each rule.

        Usage
        -----
        @DataQuality.expect_drop(rules)
        def load_employee_df() -> DataFrame:
            return spark.read.table("employee")

        df = load_employee_df()
        """
        from pyspark.sql import DataFrame
        from pyspark.sql.functions import expr
        from typing import Callable

        def decorator(func: Callable[..., DataFrame]) -> Callable[..., DataFrame]:
            def wrapper(*args, **kwargs) -> DataFrame:
                df: DataFrame = func(*args, **kwargs)
                total_count = df.count()
                validation_results = {}
                for description, condition in rules.items():
                    failed_count = df.filter(expr(f"NOT ({condition})")).count()
                    passed_count = total_count - failed_count
                    validation_results[description] = {
                        "rule": condition,
                        "passed": passed_count,
                        "failed": failed_count,
                        "total": total_count,
                        "status": "PASSED" if failed_count == 0 else "FAILED"
                    }

                # Print results in a framework-style report
                print("="*50)
                print(" DATA QUALITY VALIDATION REPORT ")
                print("="*50)

                dq_input=[]
                for desc, result in validation_results.items():
                    print(f"Rule: {desc}")
                    print(f" - Condition: {result['rule']}")
                    print(f" - Total: {result['total']} | Passed: {result['passed']} | Failed: {result['failed']}")
                    print(f" - Status: {result['status']}")
                    print("-"*50)
                    if dq_table_name and job_name:    
                        dq_input.append(
                            {
                                "job_name": job_name,
                                "expectation_type": 'expect_drop',
                                "rule": desc,
                                "condition": result['rule'],
                                "total_records": result['total'],
                                "passed_records": result['passed'],
                                "failed_records": result['failed'],
                                "status": result['status']
                            })
                if dq_table_name and job_name:
                    DataQuality.save_data_quality_results(dq_input, dq_table_name)

                combined_condition = " AND ".join([f"({condition})" for condition in rules.values()])
                filtered_df = df.filter(expr(f"({combined_condition})"))

                return filtered_df
            return wrapper
        return decorator




    from typing import Dict
    @staticmethod
    def expect_fail(rules: Dict[str, str], job_name: Optional[str] = None,  dq_table_name: Optional[str] = None):
        """
        A decorator to validate Spark DataFrames against data quality rules.

        Parameters
        ----------
        rules : dict[str, str]
            A dictionary where keys are human-readable rule descriptions
            and values are SQL filter expressions to validate.

            Example:
            --------
            rules = {
                "Employee ID should be greater than 2": "emp_id > 2",
                "Name should not be null": "fname IS NOT NULL"
            }

        job_name : str, optional
            Name of the job where data quality rules are applied.
            This is used to identify the job in the data quality results table.

        dq_table_name : str, optional
                    Name of the table where data quality results will be stored.
        Returns
        -------
        function
            A decorated function that returns the DataFrame with
            validation results printed for each rule if any rule not fails.

        Usage
        -----
        @DataQuality.expect_drop(rules)
        def load_employee_df() -> DataFrame:
            return spark.read.table("employee")

        df = load_employee_df()
        """
        from pyspark.sql import DataFrame
        from pyspark.sql.functions import expr
        from typing import Callable

        def decorator(func: Callable[..., DataFrame]) -> Callable[..., DataFrame]:
            def wrapper(*args, **kwargs) -> DataFrame:
                df: DataFrame = func(*args, **kwargs)
                total_count = df.count()
                validation_results = {}
                for description, condition in rules.items():
                    failed_count = df.filter(expr(f"NOT ({condition})")).count()
                    passed_count = total_count - failed_count
                    validation_results[description] = {
                        "rule": condition,
                        "passed": passed_count,
                        "failed": failed_count,
                        "total": total_count,
                        "status": "PASSED" if failed_count == 0 else "FAILED"
                    }

                # Print results in a framework-style report
                dq_input=[]
                print("="*50)
                print(" DATA QUALITY VALIDATION REPORT ")
                print("="*50)
                for desc, result in validation_results.items():
                    print(f"Rule: {desc}")
                    print(f" - Condition: {result['rule']}")
                    print(f" - Total: {result['total']} | Passed: {result['passed']} | Failed: {result['failed']}")
                    print(f" - Status: {result['status']}")
                    print("-"*50)
                    
                    if dq_table_name and job_name:
                        dq_input.append(
                            {
                                "job_name": job_name,
                                "expectation_type": 'expect_fail',
                                "rule": desc,
                                "condition": result['rule'],
                                "total_records": result['total'],
                                "passed_records": result['passed'],
                                "failed_records": result['failed'],
                                "status": result['status']
                            })
                if dq_table_name and job_name:
                    DataQuality.save_data_quality_results(dq_input, dq_table_name)

                combined_condition = " AND ".join([f"({condition})" for condition in rules.values()])
                
                if df.filter(expr(f"({combined_condition})")).count() != df.count():
                    raise Exception("Pipeline execution stopped!")

                return df
            return wrapper
        return decorator



    from typing import Dict, Optional
    @staticmethod
    def expect_quarantine(
        rules: Dict[str, str],
        job_name: Optional[str] = None,  
        dq_table_name: Optional[str] = None,
        quarantine_location: Optional[str] = None,
        quarantine_table: Optional[str] = None,
        quarantine_format: str = "parquet"   # default format
    ):
        """
        A decorator to validate Spark DataFrames against data quality rules,
        with optional quarantine handling for failed records.

        Exactly one of `quarantine_location` or `quarantine_table` can be provided.

        Parameters
        ----------
        rules : dict[str, str]
            Validation rules in form {description: sql_condition}.
        quarantine_location : str, optional
            Path to store failed records. Default format is Parquet, but can
            be overridden with `quarantine_format`.
        quarantine_table : str, optional
            Table name to store failed records.
        quarantine_format : str, default 'parquet'
            File format for quarantine data. Options:
              - 'parquet'
              - 'delta'
              - 'iceberg'
        job_name : str, optional
            Name of the job where data quality rules are applied.
            This is used to identify the job in the data quality results table.

        dq_table_name : str, optional
                    Name of the table where data quality results will be stored.
        Returns
        -------
        function
            A decorated function that:
              - Prints validation results.
              - Quarantines failed records (if configured).
              - Returns the DataFrame with only the **valid (passed) records**.

        Raises
        ------
        ValueError
            If both `quarantine_location` and `quarantine_table` are provided.
            If `quarantine_format` is not one of ['parquet', 'delta', 'iceberg'].

        Usage
        -----
        >>> rules = {"Employee ID > 2": "emp_id > 2"}

        # Example 1: Quarantine to path as Delta
        >>> @DataQuality.expect_quarantine(rules, quarantine_location="/mnt/quarantine/employees", quarantine_format="delta")
        ... def load_employee_df():
        ...     return spark.read.table("employee")
        >>> df_valid = load_employee_df()

        # Example 2: Quarantine to table as Iceberg
        >>> @DataQuality.expect_quarantine(rules, quarantine_table="quarantine_employees", quarantine_format="iceberg")
        ... def load_employee_df():
        ...     return spark.read.table("employee")
        >>> df_valid = load_employee_df()
        """
        from pyspark.sql import DataFrame
        from pyspark.sql.functions import expr, current_timestamp, lit
        from typing import Callable

        if quarantine_location and quarantine_table:
            raise ValueError("Provide only one of `quarantine_location` or `quarantine_table`.")

        if quarantine_format not in ["parquet", "delta", "iceberg"]:
            raise ValueError("`quarantine_format` must be one of ['parquet', 'delta', 'iceberg'].")

        def decorator(func: Callable[..., DataFrame]) -> Callable[..., DataFrame]:
            def wrapper(*args, **kwargs) -> DataFrame:
                df: DataFrame = func(*args, **kwargs)
                total_count = df.count()

                valid_df = df
                
                # Print results in a framework-style report
                dq_input=[]
                print("="*50)
                print(" DATA QUALITY VALIDATION REPORT ")
                print("="*50)
                for desc, condition in rules.items():
                    failed_df = valid_df.filter(expr(f"NOT ({condition})"))
                    passed_df = valid_df.filter(expr(condition))

                    failed_count = failed_df.count()
                    passed_count = passed_df.count()

                    print(f"Rule: {desc}")
                    print(f" - Condition: {condition}")
                    print(f" - Total: {total_count} | Passed: {passed_count} | Failed: {failed_count}")
                    print(f" - Status: {'PASSED' if failed_count == 0 else 'FAILED'}")
                    print("-"*50)
                    
                    if dq_table_name and job_name:
                        dq_input.append(
                            {
                                "job_name": job_name,
                                "expectation_type": 'expect_quarentine',
                                "rule": desc,
                                "condition": condition,
                                "total_records": total_count,
                                "passed_records":passed_count,
                                "failed_records": failed_count,
                                "status": 'PASSED' if failed_count == 0 else 'FAILED'
                            })
                
                    # quarantine failed records if configured
                    if failed_count > 0:

                        # Add quarantine metadata
                        failed_df = (
                            failed_df
                            .withColumn("_quarantine_reason", lit(desc))
                            .withColumn("_quarantine_ts", current_timestamp())
                        )

                        if quarantine_location:
                            failed_df.write.format(quarantine_format).mode("append").save(quarantine_location)
                            print(f"Quarantined {failed_count} records to path: {quarantine_location} ({quarantine_format})")
                            print("-"*50)

                        if quarantine_table:
                            failed_df.write.format(quarantine_format).mode("append").saveAsTable(quarantine_table)
                            print(f"Quarantined {failed_count} records to table: {quarantine_table} ({quarantine_format})")
                            print("-"*50)

                    # continue only with passed records
                    valid_df = passed_df
                if dq_table_name and job_name:
                    DataQuality.save_data_quality_results(dq_input, dq_table_name)
                    
                return valid_df
            return wrapper
        return decorator