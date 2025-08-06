--user
--TRUNCATE TABLE records_user;
INSERT INTO records_user(id, email, username, password)
VALUES(1, 'admin@admin.com', 'admin', 'admin'),
(2, 'test@test.com', 'admin', 'pbkdf2_sha256$720000$DtXaZlG3Fzp8$Q0ImyJhk0rc9VLHre68Bg8xy0cdiQ0cQKvHyGCw3ddU=');


--category
TRUNCATE TABLE records_category;
INSERT INTO records_category(id, user_id, category, balance)
VALUES(1, 1, '光熱費/携帯', TRUE),
(2, 1, '食費', TRUE),
(3, 1, '交際費', TRUE),
(4, 1, '雑費', TRUE),
(5, 1, '固定費', TRUE);


--budget
TRUNCATE TABLE records_budget;
INSERT INTO records_budget(id, user_id, category_id, amount)
VALUES(1, 1, 1, 10000),
(2, 1, 2, 25000),
(3, 1, 3, 20000),
(4, 1, 4, 10000),
(5, 1, 5, 100000);


--kakeibo
TRUNCATE TABLE records_kakeibo;
INSERT INTO records_kakeibo(id, user_id, category_id, type, name, amount, memo, day)
VALUES(1, 1, 1, 2, '電気代', 3345, NULL, '2025-08-01'),
(2, 1, 1, 2, 'ガス代', 4350, NULL, '2025-08-01'),
(3, 1, 1, 2, '携帯', 4912, NULL, '2025-08-01'),
(4, 1, 2, 2, 'アイコス', 530, NULL, '2025-08-01'),
(5, 1, 2, 2, 'コンビニ', 638, NULL, '2025-08-01'),
(6, 1, 2, 2, '飲み物', 152, NULL, '2025-08-01'),
(7, 1, 2, 2, '肉屋', 1170, NULL, '2025-08-01'),
(8, 1, 2, 2, '八百屋', 255, NULL, '2025-08-01'),
(9, 1, 2, 2, 'ヨーク', 777, NULL, '2025-08-01'),
(10, 1, 2, 2, 'モンスター', 230, NULL, '2025-08-01'),
(11, 1, 3, 2, '物販', 4300, NULL, '2025-08-01'),
(12, 1, 3, 2, '居酒屋', 5000, NULL, '2025-08-01'),
(13, 1, 4, 2, '漂白剤', 218, NULL, '2025-08-01');

--subscription
TRUNCATE TABLE records_subscription;
INSERT INTO records_subscription(id, user_id, category_id, type, name, day, amount)
VALUES(1, 1, 5, 2, '家賃', 1, 71770),
(2, 1, 5, 2, '奨学金', 1, 10530),
(3, 1, 5, 2, 'ジム', 1, 3300),
(4, 1, 5, 2, '保険', 1, 10000),
(5, 1, 5, 2, 'Apple Music', 1, 1000),
(6, 1, 5, 2, 'Amazon Prime', 1, 600);