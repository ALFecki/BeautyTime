CREATE PROCEDURE supplyInsert AS
    @product_id INTEGER,
    @type INTEGER,
    @quantity INTEGER,
    @sum REAL
BEGIN 
    INSERT (product_id, type, quantity, sum) INTO supply
    VALUES (@product_id, @type, @quantity, @sum);
END

CREATE PROCEDURE insertFinance AS
    @type varchar,
    @sum real,
    @sale_id integer = NULL,
    @schedule_id integer = NULL,
    @supply_id integer = NULL
BEGIN 
    INSERT (type, sum, date, sale_id, schedule_id, supply_id) INTO finance 
    VALUES (@type, @sum, NOW(), @sale_id, @schedule_id, @supply_id);


CREATE PROCEDURE saleSum AS
    @product_id integer,
    @quantity integer,
    @sum REAL OUTPUT
BEGIN
    SET @sum = @quantity * (SELECT cost FROM product WHERE product.id == @product_id);
END