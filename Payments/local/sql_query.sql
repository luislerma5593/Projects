SELECT * FROM python_db2.payments;

SELECT id_cliente, id_contrato, SUM(monto) AS Monto_Acumulado
FROM python_db2.payments
WHERE MONTH(fecha) = 10 AND
	activo = TRUE
GROUP BY id_cliente, id_contrato
