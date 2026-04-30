-- 01_create_dw_tables.sql
-- Objetivo: criar as tabelas dimensionais e a tabela fato do Data Warehouse bancário.

DROP TABLE IF EXISTS dim_customers;
DROP TABLE IF EXISTS dim_branches;
DROP TABLE IF EXISTS dim_accounts;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS fact_transactions;

CREATE TABLE dim_customers AS
SELECT
    customer_id,
    customer_name,
    city,
    state,
    customer_segment,
    registration_date
FROM customers;

CREATE TABLE dim_branches AS
SELECT
    branch_id,
    branch_name,
    city,
    state,
    branch_type
FROM branches;

CREATE TABLE dim_accounts AS
SELECT
    account_id,
    customer_id,
    branch_id,
    account_type,
    opening_date,
    status
FROM accounts;

CREATE TABLE dim_date AS
SELECT DISTINCT
    transaction_date AS date_id,
    CAST(strftime('%Y', transaction_date) AS INTEGER) AS year,
    CAST(strftime('%m', transaction_date) AS INTEGER) AS month,
    CAST(strftime('%d', transaction_date) AS INTEGER) AS day,
    strftime('%Y-%m', transaction_date) AS year_month
FROM transactions;

CREATE TABLE fact_transactions AS
SELECT
    transaction_id,
    account_id,
    transaction_date AS date_id,
    transaction_type,
    channel,
    amount,
    CASE
        WHEN amount > 0 THEN amount
        ELSE 0
    END AS inflow_amount,
    CASE
        WHEN amount < 0 THEN ABS(amount)
        ELSE 0
    END AS outflow_amount
FROM transactions;