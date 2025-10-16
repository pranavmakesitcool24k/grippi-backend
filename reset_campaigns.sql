CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    clicks INTEGER,
    cost REAL,
    impressions INTEGER
);

INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES
('Summer Sale', 'Active', 150, 45.99, 1000),
('Black Friday', 'Paused', 320, 89.50, 2500),
('Diwali Bonanza', 'Active', 200, 65.25, 1200),
('Spring Fling', 'Paused', 99, 25.75, 900),
('Back to School', 'Active', 180, 54.30, 1400),
('Holiday Rush', 'Paused', 400, 129.99, 3200),
('Tech Expo', 'Active', 295, 74.00, 2100),
('Flash Friday', 'Paused', 150, 60.00, 1100),
('Winter Gala', 'Active', 85, 32.10, 800),
('Mega Deals', 'Active', 500, 199.99, 3500);
