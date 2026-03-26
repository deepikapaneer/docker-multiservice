CREATE TABLE IF NOT EXISTS skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50)
);

INSERT INTO skills (name, category) VALUES
    ('Docker', 'DevOps'),
    ('GitHub Actions', 'CI/CD'),
    ('Flask', 'Backend'),
    ('PostgreSQL', 'Database'),
    ('Linux', 'OS'),
    ('AWS', 'Cloud'),
    ('nginx', 'Web Server'),
    ('Kubernetes', 'DevOps');