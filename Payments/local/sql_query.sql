SELECT * FROM python_db2.payments;


SELECT * FROM python_db2.payments;

SELECT id_cliente, id_contrato, MONTH(curdate()) - 1 AS Mes, SUM(monto) AS Monto_Acumulado
FROM python_db2.payments
WHERE MONTH(fecha) = MONTH(curdate()) - 1 AND
	activo = TRUE
GROUP BY id_cliente, id_contrato
