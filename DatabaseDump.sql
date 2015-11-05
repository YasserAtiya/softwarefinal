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
-- Table structure for table `Resume`
--

DROP TABLE IF EXISTS `Resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Resume` (
  `Author` int(11) NOT NULL,
  `File` blob,
  PRIMARY KEY (`Author`),
  KEY `fk_Resume_1` (`Author`),
  CONSTRAINT `fk_Resume_1` FOREIGN KEY (`Author`) REFERENCES `Student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Resume`
--

LOCK TABLES `Resume` WRITE;
/*!40000 ALTER TABLE `Resume` DISABLE KEYS */;
/*!40000 ALTER TABLE `Resume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internship`
--

DROP TABLE IF EXISTS `Internship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internship` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Position` varchar(100) DEFAULT NULL,
  `Company` int(11) NOT NULL,
  `Span` varchar(45) DEFAULT NULL,
  `Requirements` varchar(1000) DEFAULT NULL,
  `Applicants` varchar(45) DEFAULT NULL,
  `ApplicationLink` varchar(45) DEFAULT NULL,
  `About` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_Internship_1` (`Company`),
  CONSTRAINT `fk_Internship_1` FOREIGN KEY (`Company`) REFERENCES `Company` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internship`
--

LOCK TABLES `Internship` WRITE;
/*!40000 ALTER TABLE `Internship` DISABLE KEYS */;
/*!40000 ALTER TABLE `Internship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Company`
--

DROP TABLE IF EXISTS `Company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Company` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `Name` varchar(45) DEFAULT NULL,
  `Website` varchar(100) DEFAULT NULL,
  `About` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `UserID` (`ID`),
  CONSTRAINT `UserID` FOREIGN KEY (`ID`) REFERENCES `User` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Company`
--

LOCK TABLES `Company` WRITE;
/*!40000 ALTER TABLE `Company` DISABLE KEYS */;
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
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PossibleInterest`
--

LOCK TABLES `PossibleInterest` WRITE;
/*!40000 ALTER TABLE `PossibleInterest` DISABLE KEYS */;
INSERT INTO `PossibleInterest` VALUES ('C#',1),('C++',2),('Java',3),('SQL',4);
/*!40000 ALTER TABLE `PossibleInterest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Messages`
--

DROP TABLE IF EXISTS `Messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Messages` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FromUser` int(11) DEFAULT NULL,
  `ToUser` int(11) DEFAULT NULL,
  `Message` varchar(1000) DEFAULT NULL,
  `Subject` varchar(100) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `Read` tinyint(4) DEFAULT NULL,
  `ContactingID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_Messages_1` (`FromUser`),
  KEY `fk_Messages_2` (`ToUser`),
  KEY `fk_Messages_3` (`ContactingID`),
  CONSTRAINT `fk_Messages_3` FOREIGN KEY (`ContactingID`) REFERENCES `Contacting` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Messages_1` FOREIGN KEY (`FromUser`) REFERENCES `User` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Messages_2` FOREIGN KEY (`ToUser`) REFERENCES `User` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Messages`
--

LOCK TABLES `Messages` WRITE;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StudentInterest`
--

DROP TABLE IF EXISTS `StudentInterest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StudentInterest` (
  `UserID` int(11) DEFAULT NULL,
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `InterestID` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_StudentInterest_1` (`UserID`),
  KEY `fk_StudentInterest_2` (`InterestID`),
  CONSTRAINT `fk_StudentInterest_2` FOREIGN KEY (`InterestID`) REFERENCES `PossibleInterest` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_StudentInterest_1` FOREIGN KEY (`UserID`) REFERENCES `User` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StudentInterest`
--

LOCK TABLES `StudentInterest` WRITE;
/*!40000 ALTER TABLE `StudentInterest` DISABLE KEYS */;
/*!40000 ALTER TABLE `StudentInterest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(45) DEFAULT NULL,
  `Role` varchar(45) DEFAULT NULL,
  `Authenticated` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (2,'yatiya@cs.fsu.edu',NULL,'Student',NULL),(3,'cpatino@cs.fsu.edu',NULL,'Student',NULL),(4,'jake@statefarm.com',NULL,'Company',NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Student` (
  `ID` int(11) NOT NULL DEFAULT '0',
  `FName` varchar(45) DEFAULT NULL,
  `LName` varchar(45) DEFAULT NULL,
  `PreviousLogin` tinyint(4) DEFAULT NULL,
  `About` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_Student_1` (`ID`),
  CONSTRAINT `fk_Student_1` FOREIGN KEY (`ID`) REFERENCES `User` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES (2,'Yasser','Atiya',0,NULL);
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contacting`
--

DROP TABLE IF EXISTS `Contacting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Contacting` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `UserID` int(11) DEFAULT NULL,
  `ContactID` int(11) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `LatestDate` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_Contacting_1` (`UserID`),
  KEY `fk_Contacting_2` (`ContactID`),
  CONSTRAINT `fk_Contacting_1` FOREIGN KEY (`UserID`) REFERENCES `User` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Contacting_2` FOREIGN KEY (`ContactID`) REFERENCES `User` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contacting`
--

LOCK TABLES `Contacting` WRITE;
/*!40000 ALTER TABLE `Contacting` DISABLE KEYS */;
/*!40000 ALTER TABLE `Contacting` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-05 12:31:22
