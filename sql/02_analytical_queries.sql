-- 02_analytical_queries.sql
-- Objetivo: análises sobre o Data Warehouse bancário


-- 1. Volume total de transações
SELECT 
    COUNT(*) AS total_transacoes
FROM fact_transactions;


-- 2. Volume financeiro total (entrada e saída)
SELECT
    SUM(inflow_amount) AS total_entradas,
    SUM(outflow_amount) AS total_saidas,
    SUM(amount) AS saldo_liquido
FROM fact_transactions;


-- 3. Volume por tipo de transação
SELECT
    transaction_type,
    COUNT(*) AS quantidade,
    SUM(amount) AS valor_total
FROM fact_transactions
GROUP BY transaction_type
ORDER BY valor_total DESC;


-- 4. Evolução mensal do volume financeiro
SELECT
    d.year,
    d.month,
    SUM(f.amount) AS valor_total
FROM fact_transactions f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;


-- 5. Top 10 clientes por volume movimentado
SELECT
    c.customer_name,
    SUM(f.amount) AS total_movimentado
FROM fact_transactions f
JOIN dim_accounts a ON f.account_id = a.account_id
JOIN dim_customers c ON a.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_movimentado DESC
LIMIT 10;


-- 6. Volume por agência
SELECT
    b.branch_name,
    SUM(f.amount) AS total_movimentado
FROM fact_transactions f
JOIN dim_accounts a ON f.account_id = a.account_id
JOIN dim_branches b ON a.branch_id = b.branch_id
GROUP BY b.branch_name
ORDER BY total_movimentado DESC;


-- 7. Volume por canal
SELECT
    channel,
    COUNT(*) AS quantidade,
    SUM(amount) AS total
FROM fact_transactions
GROUP BY channel
ORDER BY total DESC;