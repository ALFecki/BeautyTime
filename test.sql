INSERT INTO "user" 
    ("login", "password")
VALUES
    ('ivan123', 'password123'),
    ('petr456', 'password456'),
    ('sid789', 'password789');


INSERT INTO "client" 
    ("user_id", "email", "first_name", "second_name", "surname", "phone")
VALUES 
    (1, 'ivan@example.com', 'Иванов', 'Иван', 'Иваныч', '+1234567890'),
    (2, 'petr@example.com', 'Петров', 'Петр', 'Петрович', '+9876543210'),
    (3, 'sid@example.com', 'Сидрова', 'Сидора', NULL, '+5555555555');


INSERT INTO "service" 
    ("name", "alias", "description", "cost")
VALUES 
    ('Чистка лица', 'cleaning', NULL, 85),
    ('Уход Options', 'care_options', NULL, 98);
    ('Уход So delicate', 'care_so_delicate', NULL, 95);


INSERT INTO "staff" 
    ("user_id", "first_name", "second_name", "email", "position", "phone")
VALUES 
    (1, 'John', 'Doe', 'john.doe@example.com', 'Stylist', '+1234567890'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', 'Manicurist', '+9876543210');


INSERT INTO "schedule" 
    ("client_id", "service_id", "staff_id", "start_date", "duration", "notes")
VALUES 
    (1, 1, 1, '2023-10-05 10:00:00', 1.5, 'Notes for the appointment'),
    (2, 2, 2, '2023-10-06 15:30:00', 2, NULL);
INSERT INTO "schedule" 
    ("client_id", "service_id", "staff_id", "start_date", "duration", "notes")
VALUES 
    (1, 1, 1, '2023-10-05 10:00:00', 1.5, 'Notes for the appointment'),
    (2, 2, 1, '2023-10-06 15:30:00', 2, NULL);

INSERT INTO "schedule" 
    ("client_id", "service_id", "staff_id", "start_date", "duration", "notes")
VALUES 
    (3, 1, 1, '2023-10-05 10:00:00', 1.5, 'Notes for the appointment'),
    (3, 2, 1, '2023-10-06 15:30:00', 2, NULL);

INSERT INTO "schedule" 
    ("client_id", "service_id", "staff_id", "start_date", "duration", "notes")
VALUES 
    (2, 1, 1, '2023-10-05 10:00:00', 1.5, 'Notes for the appointment');


INSERT INTO "admin" 
    ("user_id", "unique_id")
VALUES 
    (1, 'admin123'),
    (2, 'admin456');


INSERT INTO "product" 
    ("name", "alias", "quantity", "supply_date", "client_cost", "supply_cost", "cost_diff")
VALUES 
    ('Молочко', 'milk', 50, '2023-10-01 08:00:00', 99, 80.99, 18.01),
    ('Тоник', 'tonic', 100, '2023-10-02 14:00:00', 5.99, 3.99, 2);
    ('Крем для лица', 'cream', 100, '2023-10-02 14:00:00', 5.99, 3.99, 2);


INSERT INTO "sale" 
    ("client_id", "product_id", "quantity", "sale_date")
VALUES 
    (1, 1, 2, '2023-10-03 09:30:00'),
    (2, 2, 1, '2023-10-04 16:45:00');


INSERT INTO "review" 
    ("schedule_id", "client_id", "rating", "comment")
VALUES 
    (1, 1, 4, 'Great service!'),
    (2, 2, 5, 'Highly recommend!');


INSERT INTO "finance"
    ("type", "sum", "date", "sale_id", "schedule_id", "supply_id", "notes")
VALUES 
    ('income', 50, '2023-10-03 10:00:00', 1, NULL, NULL, 'Payment for haircut'),
    ('expense', 10, '2023-10-04 17:00:00', NULL, 2, NULL, 'Payment for manicure');


INSERT INTO "supply" 
    ("product_id", "type", "quantity", "sum")
VALUES 
    (1, 1, 50, 399.50),
    (2, 2, 100, 299.00);


INSERT INTO "log" 
    ("date", "client_id", "info")
VALUES 
    ('2023-10-03 10:30:00', 1, 'Appointment booked'),
    ('2023-10-04 17:30:00', 2, 'Appointment cancelled');