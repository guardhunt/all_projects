-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 23, 2015 at 08:30 PM
-- Server version: 5.5.46-0ubuntu0.14.04.2
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `development`
--

-- --------------------------------------------------------

--
-- Table structure for table `academic_p`
--

CREATE TABLE IF NOT EXISTS `academic_p` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ap_name` varchar(50) DEFAULT NULL,
  `division` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=32 ;

--
-- Dumping data for table `academic_p`
--

INSERT INTO `academic_p` (`ID`, `ap_name`, `division`) VALUES
(1, 'Biology', 'I'),
(2, 'Chemistry', 'I'),
(3, 'Mathematics', 'I'),
(5, 'Physics', 'I'),
(6, 'Agriculture and Natural Resources', 'II'),
(7, 'Computer Science', 'II'),
(8, 'Economics and Business', 'II'),
(9, 'Sustainability and Environmental Studies', 'II'),
(10, 'Technology and Applied Design', 'II'),
(11, 'Child and Family Studies', 'III'),
(12, 'Health and Human Performance ', 'III'),
(13, 'Psychology', 'III'),
(14, 'Sociology', 'III'),
(15, 'Communication', 'IV'),
(16, 'English', 'IV'),
(17, 'Foreign Languages', 'IV'),
(18, 'Music', 'IV'),
(19, 'Theater', 'IV'),
(20, 'Art and Art History', 'V'),
(21, 'Asian Studies', 'V'),
(22, 'History', 'V'),
(23, 'Philosophy', 'V'),
(24, 'Political Science', 'V'),
(25, 'Religion', 'V'),
(26, 'African and African American Studies', 'VI'),
(27, 'Appalachian Studies', 'VI'),
(28, 'Educational Studies', 'VI'),
(29, 'Peace and Social Justice Studies', 'VI'),
(30, 'Women and Gender Studies', 'VI'),
(31, 'Nursing', 'I');

-- --------------------------------------------------------

--
-- Table structure for table `Activities_t`
--

CREATE TABLE IF NOT EXISTS `Activities_t` (
  `ID` int(100) NOT NULL AUTO_INCREMENT,
  `Title` varchar(100) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time NOT NULL,
  `Location` int(20) NOT NULL,
  `Type` int(20) NOT NULL,
  `Goal` int(20) NOT NULL,
  `Description` text,
  `Narrative` text,
  PRIMARY KEY (`ID`),
  KEY `Goal` (`Goal`),
  KEY `Type` (`Type`),
  KEY `Location` (`Location`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `Activities_t`
--

INSERT INTO `Activities_t` (`ID`, `Title`, `Date`, `Time`, `Location`, `Type`, `Goal`, `Description`, `Narrative`) VALUES
(1, 'Understanding Student Stress', '2015-11-17', '15:30:00', 2, 2, 1, ' Donec ac nisl imperdiet, pellentesque odio et, tincidunt neque. Cras vel quam et justo tempus scelerisque. Morbi vehicula nulla id velit facilisis laoreet. Curabitur nunc dui, malesuada vitae lorem at, laoreet laoreet nisi. Quisque tincidunt dolor ac est mattis sodales. Maecenas nec maximus magna, non porttitor diam. Pellentesque feugiat neque neque, nec feugiat diam semper vel. Duis pharetra fringilla odio, vel suscipit mauris varius ac. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas tempor eleifend lorem efficitur tristique. Donec turpis purus, commodo sit amet facilisis a, sodales non mi. In orci dolor, consequat id felis ullamcorper, vulputate laoreet lacus. Aenean nisl dolor, bibendum in leo ac, mattis sollicitudin mi. Duis ex orci, vehicula quis fermentum id, aliquet eget risus. Praesent eu imperdiet enim. Donec ex ligula, tempor nec neque sit amet, ornare aliquet metus.', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempor erat vitae erat varius consequat. Integer quam nunc, tincidunt nec purus quis, lobortis dictum leo. Donec porta vehicula tellus, at interdum nibh aliquet a. Aenean eu mi a tellus tempor bibendum sit amet sed purus. Sed luctus urna erat, non commodo libero tempor quis. Duis sed tellus congue tortor pellentesque ultrices. Integer venenatis dignissim dui gravida vulputate. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;'),
(5, 'Writing for Dummies', '2015-11-11', '20:15:00', 1, 2, 1, 'N/A', 'N/A'),
(22, 'Lorum Ipsum', '2016-02-09', '14:30:00', 1, 3, 2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tempor erat vitae erat varius consequat. Integer quam nunc, tincidunt nec purus quis, lobortis dictum leo. Donec porta vehicula tellus, at interdum nibh aliquet a. Aenean eu mi a tellus tempor bibendum sit amet sed purus. Sed luctus urna erat, non commodo libero tempor quis. Duis sed tellus congue tortor pellentesque ultrices. Integer venenatis dignissim dui gravida vulputate. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;', '		');

-- --------------------------------------------------------

--
-- Table structure for table `Attendance`
--

CREATE TABLE IF NOT EXISTS `Attendance` (
  `AttendID` int(20) NOT NULL AUTO_INCREMENT,
  `f_ID` varchar(9) NOT NULL,
  `a_ID` int(20) NOT NULL,
  PRIMARY KEY (`AttendID`),
  KEY `f_ID` (`f_ID`),
  KEY `a_ID` (`a_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=114 ;

--
-- Dumping data for table `Attendance`
--

INSERT INTO `Attendance` (`AttendID`, `f_ID`, `a_ID`) VALUES
(99, 'B00839257', 1),
(100, 'B00839257', 22),
(105, 'B00675123', 1),
(107, 'B00328837', 1),
(108, 'B00839276', 22),
(109, 'B00111111', 1),
(110, '00792846', 1),
(112, 'B00629835', 1),
(113, 'B00839257', 5);

-- --------------------------------------------------------

--
-- Table structure for table `ethnicity_T`
--

CREATE TABLE IF NOT EXISTS `ethnicity_T` (
  `ethnicityID` int(11) NOT NULL AUTO_INCREMENT,
  `ename` varchar(200) NOT NULL,
  PRIMARY KEY (`ethnicityID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `ethnicity_T`
--

INSERT INTO `ethnicity_T` (`ethnicityID`, `ename`) VALUES
(1, 'American Indian, Alaskan Native, or Aboriginal Canadian'),
(2, 'Black, African American, or African Diaspora'),
(3, 'Hispanic/Latino(a)'),
(4, 'Middle Eastern or Arabic'),
(5, 'Native Hawaiian, Samoan, Oceanian, or Pacific Islander'),
(6, 'South Asian, including the Diaspora'),
(7, 'Southeast Asian, East Asian, including the Diaspora'),
(8, 'White or Caucasian'),
(9, 'Multi-racial/multi-ethnic'),
(10, 'Other');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE IF NOT EXISTS `faculty` (
  `bnumber` varchar(9) NOT NULL,
  `title` varchar(20) DEFAULT NULL,
  `firstname` varchar(20) DEFAULT NULL,
  `mi` varchar(2) DEFAULT NULL,
  `lastname` varchar(20) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `cpo` int(20) DEFAULT NULL,
  `program` int(11) DEFAULT NULL,
  `ethnicity` int(20) NOT NULL,
  `gender` int(20) NOT NULL,
  `status` int(20) NOT NULL,
  `rank` int(20) NOT NULL,
  PRIMARY KEY (`bnumber`),
  UNIQUE KEY `bnumber` (`bnumber`),
  KEY `ethnicity` (`ethnicity`),
  KEY `gender` (`gender`),
  KEY `status` (`status`),
  KEY `ethnicity_2` (`ethnicity`),
  KEY `gender_2` (`gender`),
  KEY `status_2` (`status`),
  KEY `rank` (`rank`),
  KEY `program` (`program`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`bnumber`, `title`, `firstname`, `mi`, `lastname`, `email`, `cpo`, `program`, `ethnicity`, `gender`, `status`, `rank`) VALUES
('00792846', 'Mrs.', 'Dara', 'L', 'Kinger', 'darak@berea.edu', 953, 18, 2, 2, 2, 6),
('B00111111', 'Ms.', 'Nemo', NULL, 'Forester', 'nemof@berea.edu', 999, 1, 10, 2, 2, 2),
('B00123456', 'Dr.', 'Roger', 'Ba', 'Kirkston', 'RBK@berea.edu', 733, 17, 1, 2, 3, 1),
('B00328837', 'Ms', 'Levi', 'M', 'Biskerner', 'levib@berea.edu', 799, 13, 1, 2, 1, 2),
('B00629835', 'Dr.', 'Austin', 'H', 'Victor', 'austinv@berea.edu', 933, 21, 9, 3, 4, 1),
('B00675123', 'Prof.', 'Austin', 'S', 'McGlothlin', 'mcglothlina@berea.edu', 954, 7, 8, 1, 4, 1),
('B00839257', 'Prof.', 'Christopher', 'G', 'Hunt', 'myemail@berea.edu', 729, 7, 7, 1, 4, 6),
('B00839276', 'Dr.', 'Quentin', 'M.', 'Lambert', 'quentinl@berea.edu', 733, 7, 8, 1, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `gender_T`
--

CREATE TABLE IF NOT EXISTS `gender_T` (
  `genderID` int(11) NOT NULL AUTO_INCREMENT,
  `gname` varchar(20) NOT NULL,
  PRIMARY KEY (`genderID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `gender_T`
--

INSERT INTO `gender_T` (`genderID`, `gname`) VALUES
(1, 'Male'),
(2, 'Female'),
(3, 'Other'),
(4, 'Prefer Not to Answer');

-- --------------------------------------------------------

--
-- Table structure for table `goal_t`
--

CREATE TABLE IF NOT EXISTS `goal_t` (
  `ID` int(20) NOT NULL AUTO_INCREMENT,
  `g_name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `goal_t`
--

INSERT INTO `goal_t` (`ID`, `g_name`) VALUES
(1, 'To increase understanding'),
(2, 'Testing3');

-- --------------------------------------------------------

--
-- Table structure for table `IMPORT_TESTING`
--

CREATE TABLE IF NOT EXISTS `IMPORT_TESTING` (
  `ID` int(50) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `location_t`
--

CREATE TABLE IF NOT EXISTS `location_t` (
  `ID` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `location_t`
--

INSERT INTO `location_t` (`ID`, `name`) VALUES
(1, 'Baird Lounge'),
(2, 'Seabury Gym'),
(4, 'Testing'),
(5, 'Test Location');

-- --------------------------------------------------------

--
-- Table structure for table `rank_T`
--

CREATE TABLE IF NOT EXISTS `rank_T` (
  `rankID` int(11) NOT NULL AUTO_INCREMENT,
  `rname` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`rankID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `rank_T`
--

INSERT INTO `rank_T` (`rankID`, `rname`) VALUES
(1, 'Visiting Professor'),
(2, 'Instructor'),
(3, 'Post-Doctoral Fellow'),
(4, 'Assistant Professor'),
(5, 'Associate Professor'),
(6, 'Professor');

-- --------------------------------------------------------

--
-- Table structure for table `status_T`
--

CREATE TABLE IF NOT EXISTS `status_T` (
  `statusID` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(30) NOT NULL,
  PRIMARY KEY (`statusID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `status_T`
--

INSERT INTO `status_T` (`statusID`, `sname`) VALUES
(1, 'Full-Time Contract Faculty'),
(2, 'Full-Time Tenure-Track Faculty'),
(3, 'Full-Time Tenured Faculty'),
(4, 'Part-Time Faculty');

-- --------------------------------------------------------

--
-- Table structure for table `type_t`
--

CREATE TABLE IF NOT EXISTS `type_t` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `t_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `type_t`
--

INSERT INTO `type_t` (`ID`, `t_name`) VALUES
(2, 'Workshop'),
(3, 'Learning Community'),
(4, 'Presentation'),
(5, 'Conference'),
(6, 'Consultation with the Faculty Development Director'),
(7, 'Midterm Assessment of Teaching'),
(8, 'Educational Technology Presentation'),
(9, 'New Faculty Orientation'),
(10, 'New Faculty Seminar'),
(11, 'Faculty Reading Group'),
(12, 'Testing2');

-- --------------------------------------------------------

--
-- Table structure for table `USERS`
--

CREATE TABLE IF NOT EXISTS `USERS` (
  `UID` int(100) NOT NULL AUTO_INCREMENT,
  `FIRSTNAME` varchar(255) NOT NULL,
  `LASTNAME` varchar(255) NOT NULL,
  `USERNAME` varchar(255) NOT NULL,
  `EMAIL` varchar(255) NOT NULL,
  `PASSWORD` varchar(255) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `USERS`
--

INSERT INTO `USERS` (`UID`, `FIRSTNAME`, `LASTNAME`, `USERNAME`, `EMAIL`, `PASSWORD`) VALUES
(1, 'Leslie', 'Ortquist-Ahrens', 'leslieo', 'Leslie_Ortquist-Ahrens@berea.edu', '1234'),
(2, 'Channing', 'Francis', 'channingf', 'Channing_Francis@berea.edu', '5678');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Activities_t`
--
ALTER TABLE `Activities_t`
  ADD CONSTRAINT `Activities_t_ibfk_1` FOREIGN KEY (`Location`) REFERENCES `location_t` (`ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Activities_t_ibfk_2` FOREIGN KEY (`Type`) REFERENCES `type_t` (`ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Activities_t_ibfk_3` FOREIGN KEY (`Goal`) REFERENCES `goal_t` (`ID`) ON UPDATE CASCADE;

--
-- Constraints for table `Attendance`
--
ALTER TABLE `Attendance`
  ADD CONSTRAINT `Attendance_ibfk_2` FOREIGN KEY (`a_ID`) REFERENCES `Activities_t` (`ID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Attendance_ibfk_1` FOREIGN KEY (`f_ID`) REFERENCES `faculty` (`bnumber`) ON UPDATE CASCADE;

--
-- Constraints for table `faculty`
--
ALTER TABLE `faculty`
  ADD CONSTRAINT `facultyethnicity` FOREIGN KEY (`ethnicity`) REFERENCES `ethnicity_T` (`ethnicityID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `facultygender` FOREIGN KEY (`gender`) REFERENCES `gender_T` (`genderID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `facultyrank` FOREIGN KEY (`rank`) REFERENCES `rank_T` (`rankID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `facultystatus` FOREIGN KEY (`status`) REFERENCES `status_T` (`statusID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `faculty_ibfk_1` FOREIGN KEY (`program`) REFERENCES `academic_p` (`ID`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
