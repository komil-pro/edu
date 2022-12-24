-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.31 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for shop1
CREATE DATABASE IF NOT EXISTS `shop1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `shop1`;

-- Dumping structure for table shop1.catalog
CREATE TABLE IF NOT EXISTS `catalog` (
  `cat_id` int unsigned NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(200) NOT NULL DEFAULT '',
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table shop1.catalog: ~0 rows (approximately)
INSERT IGNORE INTO `catalog` (`cat_id`, `cat_name`) VALUES
	(1, 'Фрукты'),
	(2, 'Овощи'),
	(3, 'Напитки'),
	(4, 'Сладости');

-- Dumping structure for table shop1.products
CREATE TABLE IF NOT EXISTS `products` (
  `prod_id` int unsigned NOT NULL AUTO_INCREMENT,
  `catalog_id` int DEFAULT NULL,
  `supplier_id` int DEFAULT NULL,
  `prod_name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`prod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Dumping data for table shop1.products: ~0 rows (approximately)

-- Dumping structure for table shop1.suppliers
CREATE TABLE IF NOT EXISTS `suppliers` (
  `sup_id` int unsigned NOT NULL AUTO_INCREMENT,
  `sup_name` varchar(150) COLLATE utf8mb4_bin NOT NULL DEFAULT '0',
  PRIMARY KEY (`sup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Dumping data for table shop1.suppliers: ~0 rows (approximately)
INSERT IGNORE INTO `suppliers` (`sup_id`, `sup_name`) VALUES
	(1, 'ООО "Свежие фрукты"'),
	(2, 'ЧДММ "Сабзавоти бехтарин"'),
	(3, 'ЧДММ "Ширин"');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
