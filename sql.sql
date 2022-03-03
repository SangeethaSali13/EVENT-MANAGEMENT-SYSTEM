/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - ems
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ems` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ems`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `booking_date` varchar(50) DEFAULT NULL,
  `booking_time` varchar(50) DEFAULT NULL,
  `booking_venue` varchar(50) DEFAULT NULL,
  `booking_status` varchar(50) DEFAULT NULL,
  `booking_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`event_id`,`customer_id`,`booking_date`,`booking_time`,`booking_venue`,`booking_status`,`booking_type`) values (1,10,3,'2022-01-20','11:44','hbvhfgvc','pending','event package'),(2,8,3,'2022-01-20','20:59','mnmbv','pending','event package'),(3,10,3,'2022-01-20','02:08','ggfgff','pending','event package'),(4,13,3,'2022-01-21','10:22',' n,mn','pending','event package'),(5,13,3,'2022-01-21','10:23','mnb','pending','event package'),(6,17,3,'2022-01-31','11:14','fgth','pending','event package'),(7,21,6,'2022-02-11','19:17','rey','Paid','event package');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(50) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `complaint_date` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`complaint`,`customer_id`,`complaint_date`,`reply`) values (3,' bn ',3,'2022-01-20','pending'),(2,'mmhbjgb',3,'2022-01-20','fd'),(4,'fdgdf',3,'2022-01-20','pending'),(5,'retrr',3,'2022-01-31','pending'),(6,'fgdrg',3,'2022-01-31','pending'),(7,'hmgfc',3,'2022-01-31','pending'),(8,'mjhgbfd',3,'2022-01-31','pending');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`login_id`,`first_name`,`last_name`,`gender`,`house_name`,`place`,`pincode`,`email`,`phone`) values (1,3,'ammu','appu','Female','jkhmgtyghf','jkhg','687632','ammu123@gmail.com','8765436823'),(4,6,'ammu','j','Female','dsfdgfh','mnbhg','679834','ammu123@gmail.com','9873214786'),(3,5,'appu','kumar','Male','hngfncxgdftfh','hmgf','675432','appu123@gmail.com','9754321947'),(5,7,'ammu','j','Female','sdfgftyjhkj','gdfrdtf','956213','ammu123@gmail.com','7894561237'),(6,8,'anu','s','Female','ddsefsfs','dsfsf','674321','anu345@gmail.com','9786350921'),(7,9,'anu','s','Female','sadssef','fregrt','686503','anu345@gmail.com','9756432109'),(8,10,'Anupama','ks','Female','anhbtyhui','gdfgf','567803','anupama916@gmail.com','732180909034576768'),(9,11,'A','B','Male','cdfgfhyg','fhghj','987456','ammu123@gmail.com','85451565262262652'),(10,12,'achu','k','Female','jmgvgb','jhjmbv','632145','achu45@gmail.com','9821368123');

/*Table structure for table `customevent` */

DROP TABLE IF EXISTS `customevent`;

CREATE TABLE `customevent` (
  `custom_event_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `custom_event_title` varchar(50) DEFAULT NULL,
  `budget_amount` varchar(50) DEFAULT NULL,
  `custom_event_date` varchar(50) DEFAULT NULL,
  `custom_event_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`custom_event_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `customevent` */

insert  into `customevent`(`custom_event_id`,`customer_id`,`custom_event_title`,`budget_amount`,`custom_event_date`,`custom_event_status`) values (8,3,'fghgfhf','30000','15-01-2022','ftgrytuyi'),(6,3,'aewrtrfg','40000','15-01-2022','pending'),(4,3,',mnbvfgbbn n','20000','15-01-2022','pending'),(12,3,'hgfdnbv','30000','2022-01-31','pending'),(11,3,'hgtfr','50000','2022-01-31','pending'),(10,3,'xfddfsdfg','4000','2022-01-21','pending');

/*Table structure for table `customeventdetails` */

DROP TABLE IF EXISTS `customeventdetails`;

CREATE TABLE `customeventdetails` (
  `custom_event_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `custom_event_id` int(11) DEFAULT NULL,
  `feature_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`custom_event_details_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `customeventdetails` */

insert  into `customeventdetails`(`custom_event_details_id`,`custom_event_id`,`feature_id`) values (1,6,7),(2,4,7),(3,12,7);

/*Table structure for table `eventcategories` */

DROP TABLE IF EXISTS `eventcategories`;

CREATE TABLE `eventcategories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=63 DEFAULT CHARSET=latin1;

/*Data for the table `eventcategories` */

insert  into `eventcategories`(`category_id`,`category_name`) values (62,'fdgtgrtgr vmb'),(2,'sddsf ,nmb'),(45,'jmhgvgn h'),(28,'dfrjuytdcsfdrg'),(5,'dscsddfzdfdg'),(61,'jhg'),(33,'nnbhjhgt'),(55,'m,nbhn nbhgbv '),(57,'mnxz,mcz,kjuhj'),(59,'cxvcvcbcvcv');

/*Table structure for table `eventpackages` */

DROP TABLE IF EXISTS `eventpackages`;

CREATE TABLE `eventpackages` (
  `package_id` int(11) NOT NULL AUTO_INCREMENT,
  `package_title` varchar(50) DEFAULT NULL,
  `package_amount` varchar(50) DEFAULT NULL,
  `package_description` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`package_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `eventpackages` */

insert  into `eventpackages`(`package_id`,`package_title`,`package_amount`,`package_description`,`status`) values (10,'nbhngfcvbgbff','30000','hgfhnh',NULL),(8,'jgtf vcbg bghbv','7800','nmnm',NULL),(13,'jkmbhgthfgfdx','50000',' hjnb  hn n n',NULL),(14,'zczxvxdgdhgf','70000','dsfgfhgj',NULL),(20,'pack','0','pack',NULL),(21,'pack2','300','pack2','available');

/*Table structure for table `features` */

DROP TABLE IF EXISTS `features`;

CREATE TABLE `features` (
  `feature_id` int(11) NOT NULL AUTO_INCREMENT,
  `feature_title` varchar(50) DEFAULT NULL,
  `feature_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feature_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `features` */

insert  into `features`(`feature_id`,`feature_title`,`feature_description`) values (5,'m,nbhnb b n  mhfds','n,jhnbvhgmnh nmk,'),(2,'jhgvhkjmj  kljhbghfngybhjm','mhbyhtrtfcr'),(7,' bnvbyhght','bnbfgd,jm ngbvvgrbg'),(10,'mnbgb vbmj','mnjbhgn vbbhj'),(14,'hjgfrxdfgh','hyjgf'),(15,'hntftngyhtgf','nhgytgrd');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(50) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `feedback_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`feedback`,`customer_id`,`feedback_date`) values (1,'nbhngh',3,'2022-01-20'),(2,',hjmb',3,'2022-01-20'),(3,',jhghtfbfdctggnh',3,'2022-01-20'),(4,'m mnb',3,'2022-01-20'),(5,'nnb',3,'2022-01-31');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `login_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`login_type`) values (1,'admin','admin','admin'),(7,'paruathi','paru143','customer'),(6,'ammu','ammu','customer'),(5,'appu','appu','customer'),(8,'anu','anu','customer'),(12,'achuk','achu@123','customer');

/*Table structure for table `packagedetails` */

DROP TABLE IF EXISTS `packagedetails`;

CREATE TABLE `packagedetails` (
  `package_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `package_id` int(11) DEFAULT NULL,
  `feature_id` int(11) DEFAULT NULL,
  `amt` int(11) DEFAULT NULL,
  PRIMARY KEY (`package_details_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `packagedetails` */

insert  into `packagedetails`(`package_details_id`,`package_id`,`feature_id`,`amt`) values (4,21,7,300);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `payment_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount`,`payment_date`) values (1,1,'30000','2022-01-20'),(3,2,'7800','2022-01-20'),(4,4,'50000','2022-01-27'),(5,5,'50000','2022-01-31'),(6,7,'300','2022-02-25');

/*Table structure for table `proposal` */

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL AUTO_INCREMENT,
  `custom_event_id` int(11) DEFAULT NULL,
  `proposal_date` varchar(50) DEFAULT NULL,
  `proposal_amount` varchar(50) DEFAULT NULL,
  `proposal_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `proposal` */

insert  into `proposal`(`proposal_id`,`custom_event_id`,`proposal_date`,`proposal_amount`,`proposal_status`) values (1,6,'2022-01-21','3000','Paid'),(2,8,'2022-01-21','40000','Paid'),(3,4,'2022-01-21','50000','Paid'),(4,10,'2022-01-21','30000','Paid'),(8,8,'2022-01-21','20000','Paid'),(7,8,'2022-01-21','4000','Paid'),(9,8,'2022-01-21','3000','Paid'),(10,6,'2022-01-21','50000','pending'),(11,6,'2022-01-21','25000','pending'),(12,8,'2022-01-31','7000','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
