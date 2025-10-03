from spark_pipelines import DataQuality

rules = {
    "Employee ID should be greater than 2": "emp_id > 2",
    "Name should not be null": "fname IS NOT NULL"
}

@DataQuality.expect(rules)
def load_employee_df():
    return spark.read.table("employee")

df = load_employee_df()