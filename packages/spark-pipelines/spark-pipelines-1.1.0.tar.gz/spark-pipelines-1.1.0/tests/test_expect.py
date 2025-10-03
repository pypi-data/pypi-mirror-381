import pytest
from pyspark.sql import SparkSession
from spark_pipelines.spark_pipelines import DataQuality

# Initialize Spark session for testing
@pytest.fixture(scope="module")
def spark():
    spark_session = SparkSession.builder \
        .appName("TestSparkPipelines") \
        .getOrCreate()
    yield spark_session
    spark_session.stop()

# Sample DataFrame for testing
@pytest.fixture
def sample_df(spark):
    data = [
        (1, "Alice"),
        (3, "Bob"),
        (2, None),
        (4, "Charlie"),
    ]
    return spark.createDataFrame(data, ["emp_id", "fname"])

# Test for the expect decorator
def test_expect(spark, sample_df):
    rules = {
        "Employee ID should be greater than 2": "emp_id > 2",
        "Name should not be null": "fname IS NOT NULL"
    }

    @DataQuality.expect(rules)
    def load_employee_df():
        return sample_df

    df = load_employee_df()
    assert df.count() == 2  # Only Bob and Charlie should pass

# Test for the expect_drop decorator
def test_expect_drop(spark, sample_df):
    rules = {
        "Employee ID should be greater than 2": "emp_id > 2",
        "Name should not be null": "fname IS NOT NULL"
    }

    @DataQuality.expect_drop(rules)
    def load_employee_df():
        return sample_df

    df = load_employee_df()
    assert df.count() == 2  # Only Bob and Charlie should remain

# Test for the expect_fail decorator
def test_expect_fail(spark, sample_df):
    rules = {
        "Employee ID should be greater than 2": "emp_id > 2",
        "Name should not be null": "fname IS NOT NULL"
    }

    @DataQuality.expect_fail(rules)
    def load_employee_df():
        return sample_df

    with pytest.raises(Exception):
        load_employee_df()  # Should raise an exception due to failed validation

# Test for the expect_quarantine decorator
def test_expect_quarantine(spark, sample_df):
    rules = {
        "Employee ID should be greater than 2": "emp_id > 2",
        "Name should not be null": "fname IS NOT NULL"
    }

    @DataQuality.expect_quarantine(rules, quarantine_location="/tmp/quarantine", quarantine_format="parquet")
    def load_employee_df():
        return sample_df

    df_valid = load_employee_df()
    assert df_valid.count() == 2  # Only Bob and Charlie should pass
    # Additional checks can be added to verify the quarantine location if needed.