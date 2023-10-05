-- DROP DATABASE IF EXISTS beautytime;

--CREATE DATABASE beautyTime
--	WITH 
--	OWNER = root
--	ENCODING = 'UTF8'
--	LC_COLLATE = 'ru_RU.UTF-8'
--	LC_CTYPE = 'ru_RU.UTF-8'
--	TABLESPACE = pg_default
--	CONNECTION LIMIT = -1
--	IS_TEMPLATE = False;

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE "user" (
  "id" serial PRIMARY KEY,
  "login" varchar(30) NOT NULL,
  "password" varchar(256) NOT NULL
);
ALTER TABLE "user" DROP CONSTRAINT IF EXISTS "login_unique";
ALTER TABLE "user" ADD CONSTRAINT "login_unique" UNIQUE ("login");
CREATE UNIQUE INDEX IF NOT EXISTS "login_idx" ON "user" ("login");

CREATE TABLE "client" (
  "id" serial PRIMARY KEY,
  "user_id" integer NOT NULL,
  "email" varchar(30) NOT NULL,
  "first_name" varchar(20) NOT NULL,
  "second_name" varchar(20) NOT NULL,
  "surname" varchar(20),
  "phone" varchar(17),
    CONSTRAINT "email_unique" UNIQUE ("email")
);
ALTER TABLE "client" DROP CONSTRAINT IF EXISTS "user_fk";
ALTER TABLE "client" ADD CONSTRAINT "user_fk" FOREIGN KEY ("user_id") REFERENCES "user" ("id");


CREATE TABLE "service" (
  "id" serial PRIMARY KEY,
  "name" varchar(30) NOT NULL,
  "alias" varchar NOT NULL,
  "description" text,
  "cost" real NOT NULL
);
ALTER TABLE "service" DROP CONSTRAINT IF EXISTS "alias_unique";
ALTER TABLE "service" ADD CONSTRAINT "alias_unique" UNIQUE ("alias");
CREATE UNIQUE INDEX IF NOT EXISTS "service_idx" ON "service" ("alias");


CREATE TABLE "staff" (
  "id" serial PRIMARY KEY,
  "user_id" integer NOT NULL,
  "first_name" varchar(20) NOT NULL,
  "second_name" varchar(20) NOT NULL,
  "email" varchar(30) NOT NULL,
  "position" varchar(20),
  "phone" varchar(17)
);
ALTER TABLE "staff" DROP CONSTRAINT IF EXISTS "user_fk";
ALTER TABLE "staff" ADD CONSTRAINT "user_fk" FOREIGN KEY ("user_id") REFERENCES "user" ("id");


CREATE TABLE "schedule" (
  "id" serial PRIMARY KEY,
  "client_id" integer NOT NULL,
  "service_id" integer NOT NULL,
  "staff_id" integer,
  "start_date" timestamp with time zone NOT NULL,
  "duration" real NOT NULL,
  "notes" text
);
ALTER TABLE "schedule" DROP CONSTRAINT IF EXISTS "client_schedule_fk";
ALTER TABLE "schedule" DROP CONSTRAINT IF EXISTS "service_schedule_fk";
ALTER TABLE "schedule" DROP CONSTRAINT IF EXISTS "staff_schedule_fk";
ALTER TABLE "schedule" ADD CONSTRAINT "client_schedule_fk" FOREIGN KEY ("client_id") REFERENCES "client" ("id");
ALTER TABLE "schedule" ADD CONSTRAINT "service_schedule_fk" FOREIGN KEY ("service_id") REFERENCES "service" ("id");
ALTER TABLE "schedule" ADD CONSTRAINT "staff_schedule_fk" FOREIGN KEY ("staff_id") REFERENCES "staff" ("id");


CREATE TABLE "admin" (
  "id" serial PRIMARY KEY,
  "user_id" integer NOT NULL,
  "unique_id" varchar UNIQUE NOT NULL
);
ALTER TABLE "admin" DROP CONSTRAINT IF EXISTS "user_fk";
ALTER TABLE "admin" ADD CONSTRAINT "user_fk" FOREIGN KEY ("user_id") REFERENCES "user" ("id");

CREATE TABLE "product" (
  "id" serial PRIMARY KEY,
  "name" varchar NOT NULL,
  "alias" varchar UNIQUE NOT NULL,
  "quantity" integer NOT NULL,
  "supply_date" timestamp with time zone NOT NULL,
  "client_cost" real NOT NULL,
  "supply_cost" real NOT NULL,
  "cost_diff" real NOT NULL
);
ALTER TABLE "product" DROP CONSTRAINT IF EXISTS "alias_unique";
ALTER TABLE "product" ADD CONSTRAINT "alias_unique" UNIQUE ("alias");
CREATE UNIQUE INDEX IF NOT EXISTS "product_idx" ON "product" ("alias");

CREATE TABLE "sale" (
  "id" serial PRIMARY KEY,
  "client_id" integer NOT NULL,
  "product_id" integer NOT NULL,
  "quantity" integer NOT NULL,
  "sale_date" timestamp with time zone NOT NULL
);
ALTER TABLE "sale" DROP CONSTRAINT IF EXISTS "client_sale_fk";
ALTER TABLE "sale" DROP CONSTRAINT IF EXISTS "product_sale_fk";
ALTER TABLE "sale" ADD CONSTRAINT "client_sale_fk" FOREIGN KEY ("client_id") REFERENCES "client" ("id");
ALTER TABLE "sale" ADD CONSTRAINT "product_sale_fk" FOREIGN KEY ("product_id") REFERENCES "product" ("id");


CREATE TABLE "review" (
  "id" serial PRIMARY KEY,
  "schedule_id" integer NOT NULL,
  "client_id" integer NOT NULL,
  "rating" integer NOT NULL,
  "comment" text
);
ALTER TABLE "review" DROP CONSTRAINT IF EXISTS "schedule_review_fk";
ALTER TABLE "review" DROP CONSTRAINT IF EXISTS "client_review_fk";
ALTER TABLE "review" ADD CONSTRAINT "schedule_review_fk" FOREIGN KEY ("schedule_id") REFERENCES "schedule" ("id");
ALTER TABLE "review" ADD CONSTRAINT "client_review_fk" FOREIGN KEY ("client_id") REFERENCES "client" ("id");

CREATE TABLE "finance" (
  "id" serial PRIMARY KEY,
  "type" varchar NOT NULL,
  "sum" real NOT NULL,
  "date" timestamp with time zone NOT NULL,
  "sale_id" integer,
  "schedule_id" integer,
  "supply_id" integer,
  "notes" text
);
ALTER TABLE "finance" DROP CONSTRAINT IF EXISTS "finance_sale_fk";
ALTER TABLE "finance" DROP CONSTRAINT IF EXISTS "finance_schedule_fk";
ALTER TABLE "finance" DROP CONSTRAINT IF EXISTS "finance_supply_fk";
ALTER TABLE "finance" ADD CONSTRAINT "finance_sale_fk" FOREIGN KEY ("sale_id") REFERENCES "sale" ("id");
ALTER TABLE "finance" ADD CONSTRAINT "finance_schedule_fk" FOREIGN KEY ("schedule_id") REFERENCES "schedule" ("id");
ALTER TABLE "finance" ADD CONSTRAINT "finance_supply_fk" FOREIGN KEY ("supply_id") REFERENCES "supply" ("id");

CREATE TABLE "supply" (
  "id" serial PRIMARY KEY,
  "product_id" integer,
  "type" integer,
  "quantity" integer NOT NULL,
  "sum" real NOT NULL
);
ALTER TABLE "supply" DROP CONSTRAINT IF EXISTS "product_supply_fk";
ALTER TABLE "product_supply" ADD CONSTRAINT "product_supply_fk" FOREIGN KEY ("product_id") REFERENCES "product" ("id");


CREATE TABLE "log" (
  "id" serial PRIMARY KEY,
  "date" timestamp with time zone NOT NULL,
  "client_id" integer NOT NULL,
  "info" text NOT NULL
);
ALTER TABLE "log" DROP CONSTRAINT IF EXISTS "log_client_fk";
ALTER TABLE "log" ADD CONSTRAINT "log_client_fk" FOREIGN KEY ("client_id") REFERENCES "client" ("id");
