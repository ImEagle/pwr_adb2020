-- -----------------------------------------------------
-- Table employees
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS employees (
  employee_id VARCHAR(36) NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  access_code VARCHAR(4) NOT NULL,
  gender VARCHAR(1) NOT NULL,
  employment_DATE DATE NOT NULL,
  type VARCHAR(45) NOT NULL,
  PRIMARY KEY (employee_id))
;


-- -----------------------------------------------------
-- Table customers
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
  customer_id VARCHAR(36) NOT NULL,
  gender VARCHAR(1) NOT NULL,
  date_of_birth DATE NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (customer_id))
;


-- -----------------------------------------------------
-- Table vendors_categories
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS vendors_categories (
  vendor_category_id VARCHAR(36) NOT NULL,
  name VARCHAR(45) NOT NULL,
  is_seasonal BOOLEAN NOT NULL,
  adults_only BOOLEAN NOT NULL,
  created_at VARCHAR(45) NOT NULL,
  PRIMARY KEY (vendor_category_id))
;


-- -----------------------------------------------------
-- Table locations
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS locations (
  location_id VARCHAR(36) NOT NULL,
  name VARCHAR(45) NOT NULL,
  location_type VARCHAR(45) NOT NULL,
  country VARCHAR(45) NOT NULL,
  address VARCHAR(45) NOT NULL,
  latitude VARCHAR(45) NOT NULL,
  longitude VARCHAR(45) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  PRIMARY KEY (location_id))
;


-- -----------------------------------------------------
-- Table vendors
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS vendors (
  vendor_id VARCHAR(36) NOT NULL,
  vendor_category_id VARCHAR(36) NOT NULL,
  location_id VARCHAR(36) NOT NULL,
  name VARCHAR(45) NOT NULL,
  delivery_charge DECIMAL(2) NOT NULL,
  is_open BOOLEAN NOT NULL,
  created_at TIMESTAMP NOT NULL,
  PRIMARY KEY (vendor_id))
;


-- -----------------------------------------------------
-- Table promotions
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS promotions (
  promotion_id VARCHAR(36) NOT NULL,
  vendor_id VARCHAR(36) NOT NULL,
  name VARCHAR(45) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NULL,
  type VARCHAR(45) NOT NULL,
  discount_amount DECIMAL(2) NULL,
  discount_percent DECIMAL(2) NULL,
  PRIMARY KEY (promotion_id))
;


-- -----------------------------------------------------
-- Table orders
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS orders (
  order_id VARCHAR(36) NOT NULL,
  customer_id VARCHAR(36) NOT NULL,
  employee_id VARCHAR(36) NOT NULL,
  vendor_id VARCHAR(36) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  status VARCHAR(45) NOT NULL,
  items_count INT NULL,
  total_amount DECIMAL(2) NULL,
  promotion_id INT NULL,
  prepared_at TIMESTAMP NULL,
  PRIMARY KEY (order_id))
;


-- -----------------------------------------------------
-- Table ratings
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ratings (
  rating_id VARCHAR(36) NOT NULL,
  order_id VARCHAR(36) NOT NULL,
  opinion VARCHAR(45) NOT NULL,
  rating INT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  PRIMARY KEY (rating_id))
;


-- -----------------------------------------------------
-- Table items
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS items (
  item_id VARCHAR(36) NOT NULL,
  vendor_id VARCHAR(36) NOT NULL,
  name VARCHAR(45) NOT NULL,
  price DECIMAL(2) NOT NULL,
  created_at VARCHAR(45) NOT NULL,
  PRIMARY KEY (item_id, vendor_id))
;


-- -----------------------------------------------------
-- Table orders_has_items
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS orders_has_items (
  order_id VARCHAR(36) NOT NULL,
  item_id VARCHAR(36) NOT NULL,
  quantity INT NOT NULL,
  comment VARCHAR(255) NULL,
  PRIMARY KEY (order_id, item_id))
;


-- -----------------------------------------------------
-- Table delivery
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS delivery (
  delivery_id VARCHAR(36) NOT NULL,
  order_id VARCHAR(36) NOT NULL,
  employee_id VARCHAR(36) NOT NULL,
  pick_up_at TIMESTAMP NOT NULL,
  delivered_at TIMESTAMP NULL,
  type VARCHAR(45) NOT NULL,
  tip DECIMAL(2) NULL,
  PRIMARY KEY (delivery_id))
;


-- -----------------------------------------------------
-- Table customers_location
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS customers_location (
  customer_id VARCHAR(36) NOT NULL,
  location_id VARCHAR(36) NOT NULL,
  created_at TIMESTAMP NULL,
  PRIMARY KEY (customer_id, location_id))
;


-- -----------------------------------------------------
-- Table promotions_items
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS promotions_items (
  promotion_id VARCHAR(36) NOT NULL,
  items_id VARCHAR(36) NOT NULL,
  type VARCHAR(45) NOT NULL,
  min_items_count INT NULL,
  max_items_count INT NULL,
  discount_amount DECIMAL(2) NULL,
  discount_percent DECIMAL(2) NULL,
  PRIMARY KEY (promotion_id, items_id))
;
