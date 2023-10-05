SELECT * FROM "client" WHERE "email" = 'example@example.com';
SELECT * FROM "service" WHERE "cost" > 50;
SELECT * FROM "user";
SELECT * FROM "schedule" WHERE "duration" > 60 AND "cost" < 100;
SELECT * FROM "product" WHERE "quantity" > 10 AND "supply_date" > '2023-01-01';
SELECT "first_name", "surname" FROM "client";
SELECT * FROM "service" WHERE "name" IN ('Чистка лица', 'Массаж');
SELECT * FROM "product" WHERE "alias" NOT IN ('milk', 'conditioner');

SELECT * FROM "staff" ORDER BY "surname" ASC;
SELECT * FROM "sale" ORDER BY "sale_date" DESC LIMIT 5;

SELECT * FROM "schedule" WHERE "start_date" BETWEEN '2023-01-01' AND '2023-12-31';
SELECT * FROM "sale" WHERE "quantity" BETWEEN 10 AND 20;


DELETE FROM "review" WHERE "rating" < 3;
DELETE FROM "product" WHERE "id" = 1;
DELETE FROM "user" WHERE "id" = 1;
DELETE FROM "client" WHERE "surname" = 'Иваныч';
DELETE FROM "staff" WHERE "position" LIKE '%Manager%';
DELETE FROM "client" WHERE "email" LIKE '%@gmail.com';

UPDATE "client" SET "email" = 'newemail@example.com' WHERE "id" = 1;
UPDATE "service" SET "cost" = 100 WHERE "name" = 'Haircut';
UPDATE "client" SET "phone" = '+123456789' WHERE "first_name" LIKE 'John%';
UPDATE "product" SET "client_cost" = 10, "quantity" = 20 WHERE "name" = 'Shampoo';

UPDATE "staff" SET "position" = 'Supervisor' 
FROM "user" WHERE "staff"."user_id" = "user"."id" AND "user"."login" = 'johnsmith';

UPDATE "sale" SET "quantity" = 5, "sale_date" = '2023-10-01' 
FROM "product" WHERE "sale"."product_id" = "product"."id" AND "product"."name" = 'Молочко';