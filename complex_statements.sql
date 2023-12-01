SELECT *
FROM client
WHERE first_name = 'Иванов'
  AND second_name = 'Иван'
  AND email = 'ivan@example.com';



SELECT *
FROM schedule
WHERE client_id IN (
  SELECT id
  FROM client
  WHERE first_name = 'Иванов'
    AND second_name = 'Иван'
    AND email = 'ivan@example.com'
);



SELECT s.id, s.start_date, c.first_name, c.second_name, p.name
FROM schedule s
JOIN client c ON s.client_id = c.id
JOIN service p ON s.service_id = p.id
WHERE s.start_date >= '2023-01-01'
  AND s.start_date <= '2023-12-31'
  AND p.cost >= 50.0
ORDER BY s.start_date ASC;


SELECT *
FROM client
INNER JOIN user ON client.user_id = user.id;

SELECT *
FROM client
LEFT JOIN schedule ON client.id = schedule.client_id;

CREATE OR REPLACE VIEW staff_schedule AS
SELECT staff.first_name, schedule.duration
FROM staff
RIGHT OUTER JOIN schedule ON staff.id = schedule.id;


SELECT *
FROM client
FULL OUTER JOIN schedule ON client.id = schedule.client_id;

SELECT *
FROM client
CROSS JOIN service;





WITH visits AS (
                SELECT c.id AS client_id, s.id AS staff_id, COUNT(*) AS visit_count
                FROM
                    client c
                    JOIN schedule sch ON c.id = sch.client_id
                    JOIN staff s ON sch.staff_id = s.id
                GROUP BY
                    c.id,
                    s.id
            )


SELECT c.first_name as client_name, s.first_name as staff_name,  COUNT(*) AS visit_count
FROM client c
JOIN schedule ON c.id = schedule.client_id
JOIN staff s ON schedule.staff_id = s.id
GROUP BY c.id, s.id

HAVING COUNT(*) = (
        SELECT MAX(visit_count)
        FROM visits
        WHERE visits.client_id = c.id
    );

