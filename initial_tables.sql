CREATE DATABASE IF NOT EXISTS `Oco-WhereIncomeGo`;

USE `Oco-WhereIncomeGo`;
CREATE TABLE us_zip_codes (
    zip_code VARCHAR(5) PRIMARY KEY,
    city VARCHAR(50),
    state_id VARCHAR(2),
    state_name VARCHAR(50),
    county_name VARCHAR(50),
    timezone VARCHAR(50)
);

CREATE TABLE federal_tax_brackets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    filing_status VARCHAR(50),
    income_min DECIMAL(10,2),
    income_max DECIMAL(10,2),
    tax_rate DECIMAL(10,2)
);

CREATE TABLE state_tax_brackets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id VARCHAR(2),
    filing_status VARCHAR(50),
    income_min DECIMAL(10,2),
    income_max DECIMAL(10,2),
    tax_rate DECIMAL(10,2)
);
