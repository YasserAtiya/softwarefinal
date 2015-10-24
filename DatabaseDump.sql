CREATE DATABASE  IF NOT EXISTS `Intern` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `Intern`;
-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: Intern
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `StudentInterest`
--

DROP TABLE IF EXISTS `StudentInterest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StudentInterest` (
  `StudentID` varchar(40) NOT NULL,
  `InterestName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`StudentID`),
  KEY `InterestLink` (`InterestName`),
  KEY `StudentIDLink` (`StudentID`),
  CONSTRAINT `StudentIDLink` FOREIGN KEY (`StudentID`) REFERENCES `StudentInfo` (`StudentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `InterestLink` FOREIGN KEY (`InterestName`) REFERENCES `PossibleInterest` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StudentInterest`
--

LOCK TABLES `StudentInterest` WRITE;
/*!40000 ALTER TABLE `StudentInterest` DISABLE KEYS */;
INSERT INTO `StudentInterest` VALUES ('yatiya@cs.fsu.edu','C#'),('cpatino@cs.fsu.edu','SQL');
/*!40000 ALTER TABLE `StudentInterest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `UserId` varchar(45) NOT NULL DEFAULT '',
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('cpatino@cs.fsu.edu'),('pn12@cs.fsu.edu'),('sfarm'),('yatiya@cs.fsu.edu');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StudentInfo`
--

DROP TABLE IF EXISTS `StudentInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StudentInfo` (
  `StudentID` varchar(40) NOT NULL,
  `FName` varchar(45) DEFAULT NULL,
  `LName` varchar(45) DEFAULT NULL,
  `GPA` double DEFAULT NULL,
  `PreviousLogin` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`StudentID`),
  KEY `Username` (`StudentID`),
  CONSTRAINT `Username` FOREIGN KEY (`StudentID`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StudentInfo`
--

LOCK TABLES `StudentInfo` WRITE;
/*!40000 ALTER TABLE `StudentInfo` DISABLE KEYS */;
INSERT INTO `StudentInfo` VALUES ('cpatino@cs.fsu.edu','Christian','Patino',3.85,1),('pn12@cs.fsu.edu',NULL,NULL,NULL,0),('yatiya@cs.fsu.edu','Yasser','Atiya',2.9,1);
/*!40000 ALTER TABLE `StudentInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Resume`
--

DROP TABLE IF EXISTS `Resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Resume` (
  `Author` varchar(40) NOT NULL,
  `File` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Author`),
  KEY `AuthorName` (`Author`),
  CONSTRAINT `AuthorName` FOREIGN KEY (`Author`) REFERENCES `StudentInfo` (`StudentID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Resume`
--

LOCK TABLES `Resume` WRITE;
/*!40000 ALTER TABLE `Resume` DISABLE KEYS */;
INSERT INTO `Resume` VALUES ('cpatino@cs.fsu.edu',NULL),('yatiya@cs.fsu.edu',NULL);
/*!40000 ALTER TABLE `Resume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internship`
--

DROP TABLE IF EXISTS `Internship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internship` (
  `Position` varchar(100) NOT NULL,
  `Company` varchar(45) NOT NULL,
  `Span` varchar(45) NOT NULL,
  `Requirements` varchar(45) DEFAULT NULL,
  `Applicants` varchar(45) DEFAULT NULL,
  `ApplicationLink` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Position`,`Company`),
  KEY `Provider` (`Company`),
  CONSTRAINT `Provider` FOREIGN KEY (`Company`) REFERENCES `Company` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internship`
--

LOCK TABLES `Internship` WRITE;
/*!40000 ALTER TABLE `Internship` DISABLE KEYS */;
INSERT INTO `Internship` VALUES ('C# Developer','sfarm','Spring 2014','GPA > 3.0',NULL,'www.statefarm.com');
/*!40000 ALTER TABLE `Internship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Company`
--

DROP TABLE IF EXISTS `Company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Company` (
  `ID` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Contact` varchar(45) NOT NULL,
  `Website` varchar(100) DEFAULT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_Company_1` (`ID`),
  CONSTRAINT `fk_Company_1` FOREIGN KEY (`ID`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Company`
--

LOCK TABLES `Company` WRITE;
/*!40000 ALTER TABLE `Company` DISABLE KEYS */;
INSERT INTO `Company` VALUES ('sfarm','State Farm','jake@statefarm.com','statefarm.com','');
/*!40000 ALTER TABLE `Company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PossibleInterest`
--

DROP TABLE IF EXISTS `PossibleInterest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PossibleInterest` (
  `Name` varchar(100) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PossibleInterest`
--

LOCK TABLES `PossibleInterest` WRITE;
/*!40000 ALTER TABLE `PossibleInterest` DISABLE KEYS */;
INSERT INTO `PossibleInterest` VALUES ('C#'),('C++'),('Java'),('SQL');
/*!40000 ALTER TABLE `PossibleInterest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-23  6:24:23
