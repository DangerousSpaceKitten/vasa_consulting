SELECT `week`, worker_id, shift, department
FROM schedules
WHERE `week` = 0
EXCEPT
SELECT `week`, worker_id, shift, department
FROM schedules
WHERE `week` = 1
ORDER BY WORKER_ID;

SELECT WEEK, DAY, department, COUNT(*) FROM SCHEDULES WHERE WEEK IN (0,1) GROUP BY WEEK, DAY, DEPARTMENT;

SELECT WEEK, DAY, SHIFT, WORKER_ID, DEPARTMENT FROM schedules WHERE WEEK = 0 order by DAY, SHIFT, WORKER_ID;


SELECT
	a.WEEK
    , c.article_name
	, SUM(a.PURCHASE_AMOUNTS) 
    , d.amount
    , b.ARTICLE_PRICE
FROM transactions as a
LEFT JOIN prices as b
ON a.article_id = b.article_id
LEFT JOIN articles as c
ON a.ARTICLE_ID = c.ARTICLE_ID
LEFT JOIN purchases as d
ON d.ARTICLE_ID = a.ARTICLE_ID
WHERE a.week = 0 AND b.WEEK = 0 AND d.WEEK = 0
group by a.week, a.ARTICLE_ID, c.article_name, b.ARTICLE_PRICE
order by a.ARTICLE_ID;


SELECT * FROM TRANSACTIONS WHERE WEEK = 4 AND ARTICLE_ID = 5;
SELECT * FROM SCHEDULES WHERE WEEK = 4 and DAY = "sunday" and WORKER_ID = "w_8a912f92-d7a8-4352-b86b-51cebacc1371";

SELECT * FROM SUPPLIER_PRICES;