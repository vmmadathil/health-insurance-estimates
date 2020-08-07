CREATE TABLE health_insurance_modeling.children_data AS (
SELECT *
FROM health_insurance_modeling.ipums_data_raw
WHERE CONVERT(`AGE`, SIGNED INTEGER) < 18 )
