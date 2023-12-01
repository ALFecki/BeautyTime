CREATE OR REPLACE FUNCTION insertFinance ()
RETURNS TRIGGER AS $$
DECLARE 
	service_cost real;
BEGIN
		  SELECT cost INTO service_cost FROM service WHERE id = NEW.service_id;
		  INSERT INTO finance (type, service_cost, date, schedule_id)	
      VALUES ('INCOME', service_cost, NOW(), NEW.id);

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER schedule_INSERT_finance
  AFTER INSERT ON schedule
  FOR EACH ROW
  EXECUTE FUNCTION insertFinance();


CREATE OR REPLACE FUNCTION insertSupplyFinance ()
RETURNS TRIGGER AS $$
BEGIN
		  INSERT INTO finance (type, sum, date, supply_id)	
      VALUES ('OUTCOME', NEW.sum, NOW(), NEW.id);

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER supply_INSERT_finance
  AFTER INSERT ON supply
  FOR EACH ROW
  EXECUTE FUNCTION insertSupplyFinance();
	  

CREATE OR REPLACE FUNCTION calculateSaleSum(
    product_id integer,
    quantity integer,
    OUT sum REAL
) AS $$
BEGIN
    SELECT quantity * cost INTO sum FROM product WHERE product.id = product_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insertSaleFinance ()
RETURNS TRIGGER AS $$
DECLARE
    total_sum REAL;
BEGIN
      SELECT calculateSaleSum(NEW.product_id, NEW.quantity) INTO total_sum; 
		  INSERT INTO finance (type, sum, date, sale_id)	
      VALUES ('INCOME', total_sum, NOW(), NEW.id);

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER sale_INSERT_finance
  AFTER INSERT ON sale
  FOR EACH ROW
  EXECUTE FUNCTION insertSaleFinance();
	  

CREATE OR REPLACE FUNCTION updateProductQuantity()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE product 
  SET quantity = quantity + NEW.quantity 
  WHERE product_id = NEW.product_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER product_quantity_UPDATE
  AFTER INSERT ON supply
  FOR EACH ROW
  EXECUTE FUNCTION updateProductQuantity();


CREATE OR REPLACE PROCEDURE add_client(
  login varchar(30),
  password varchar(256),
  email varchar(30),
  first_name varchar(30),
  second_name varchar(20),
  surname varchar(20),
  phone varchar(17)
) AS $$
DECLARE 
	inserted_id integer;
BEGIN 
  INSERT INTO public.user (login, password) VALUES (login, password)
  RETURNING id INTO inserted_id;
  INSERT INTO client(user_id, email, first_name, second_name, surname, phone)
  VALUES (inserted_id, email, first_name, second_name, surname, phone);
END
$$ LANGUAGE plpgsql;

	  