-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.3.14-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- python_ex_db 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `python_ex_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `python_ex_db`;

-- 테이블 python_ex_db.point_table 구조 내보내기
CREATE TABLE IF NOT EXISTS `point_table` (
  `point_stu_idx` int(11) DEFAULT NULL,
  `point_stu_grade` varchar(50) DEFAULT NULL,
  `point_stu_kor` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 python_ex_db.point_table:~0 rows (대략적) 내보내기
DELETE FROM `point_table`;
/*!40000 ALTER TABLE `point_table` DISABLE KEYS */;
INSERT INTO `point_table` (`point_stu_idx`, `point_stu_grade`, `point_stu_kor`) VALUES
	(2, '2', '90'),
	(2, '3', '95'),
	(1, '1', '89');
/*!40000 ALTER TABLE `point_table` ENABLE KEYS */;

-- 테이블 python_ex_db.student_table 구조 내보내기
CREATE TABLE IF NOT EXISTS `student_table` (
  `stu_idx` int(11) NOT NULL AUTO_INCREMENT,
  `stu_name` varchar(50) DEFAULT NULL,
  `stu_age` varchar(3) DEFAULT NULL,
  `stu_addr` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stu_idx`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 테이블 데이터 python_ex_db.student_table:~1 rows (대략적) 내보내기
DELETE FROM `student_table`;
/*!40000 ALTER TABLE `student_table` DISABLE KEYS */;
INSERT INTO `student_table` (`stu_idx`, `stu_name`, `stu_age`, `stu_addr`) VALUES
	(1, '홍길동', '18', '서울시'),
	(2, '김개똥', '19', '서울시');
/*!40000 ALTER TABLE `student_table` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
