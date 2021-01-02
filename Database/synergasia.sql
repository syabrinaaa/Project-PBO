-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2021 at 02:11 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `synergasia`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `ID_Account` int(11) NOT NULL,
  `full_Name` varchar(40) NOT NULL,
  `email` varchar(35) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`ID_Account`, `full_Name`, `email`, `password`) VALUES
(1, 'Rizqi Syabrina Haq', 'rizqisyabrinahaq@yahoo.com', 'qwertyu'),
(2, 'Riyan Setiyadi', 'setiyariyan19@gmail.com', 'syabrina123'),
(3, 'wkwkwk', 'hello', 'hallo'),
(8, 'sbbd', 'bdshubuh', 'uydbubsdf'),
(9, 'uxshio', 'ncdxaoidaxm', 'uidhxins'),
(10, 'hciasuc', 'ckaopsj', 'andios'),
(11, 'dhsihdioa', 'cjdioh', 'hsuidbas'),
(12, 'IDSNDIL', 'chsfna', 'disoaodna'),
(13, 'cudbcaiidcna', 'adsiodjasidjsa', 'bsdbsan'),
(14, 'ndcncidianc', 'akdoasjda', 'adisahdn'),
(15, 'snudn', 'qid9w0pe', 'x8e2d287'),
(16, 'cbscbsiu', 'adusa', 'andus'),
(17, 'dnand', 'snu', 'AJDOS'),
(18, 'aaa', 'bbb', 'ccc'),
(19, 'aas', 'dsi', 'sod'),
(20, 'ajdial', 'oais', 'nxua'),
(21, '19usw', 'jw1iw', 's8wqs'),
(22, 'q111', 'w111', 'a1111'),
(23, 'lllll', 'ssss', 'iiiii'),
(24, 'nnoa', 'siq', 'ias'),
(25, 'alalala', 'sjjss', 'iqqqoqoqo'),
(26, 'ajdaposk', 'saoks', 'admsak'),
(27, 'oxci0a', 'jaiwpq', 'i9w6d8'),
(28, 'sjw', '123', 'nzan'),
(29, 'oqk8wyhs', 'sask9as', 'xm8asj'),
(30, 'apkdpas', 'iddsjs', 'mkxaa'),
(31, 'hsihda', 'skao', 'owu9s'),
(32, 'acusd', 'saojs', 'aixsa'),
(33, 'qwertyu', 'rizqisyabrinahaq@yahoo.com', '& \"C:/Users/HP NOTEB');

-- --------------------------------------------------------

--
-- Table structure for table `board`
--

CREATE TABLE `board` (
  `ID_Board` int(11) NOT NULL,
  `Board_Name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `board`
--

INSERT INTO `board` (`ID_Board`, `Board_Name`) VALUES
(1, 'aa'),
(2, 'aa'),
(3, 'a'),
(4, 'z'),
(5, 'q'),
(6, 'a'),
(7, 'm'),
(8, 'mm'),
(9, 'qq');

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `ID_Card` int(11) NOT NULL,
  `card_name` varchar(40) NOT NULL,
  `deadline` date DEFAULT NULL,
  `ID_List` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `card`
--

INSERT INTO `card` (`ID_Card`, `card_name`, `deadline`, `ID_List`) VALUES
(1, 'mm', '0000-00-00', 1),
(2, 'll', '0000-00-00', 1),
(3, 'mm', '0000-00-00', 1),
(4, 'a', '2021-01-01', 1),
(5, 'aa', '0000-00-00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `detail_board`
--

CREATE TABLE `detail_board` (
  `ID_Detail_Board` int(11) NOT NULL,
  `ID_Account` int(11) DEFAULT NULL,
  `ID_Board` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detail_board`
--

INSERT INTO `detail_board` (`ID_Detail_Board`, `ID_Account`, `ID_Board`) VALUES
(1, 18, 1),
(2, 18, 1),
(3, 18, 3),
(4, 18, 4),
(5, 18, 7),
(6, 18, 8),
(7, 18, 9);

-- --------------------------------------------------------

--
-- Table structure for table `list`
--

CREATE TABLE `list` (
  `ID_List` int(11) NOT NULL,
  `list_name` varchar(40) NOT NULL,
  `ID_Board` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `list`
--

INSERT INTO `list` (`ID_List`, `list_name`, `ID_Board`) VALUES
(1, 'q', 1),
(2, 'n', 1),
(3, 'a', 1),
(4, 'a', 1),
(5, 'a', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`ID_Account`);

--
-- Indexes for table `board`
--
ALTER TABLE `board`
  ADD PRIMARY KEY (`ID_Board`);

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`ID_Card`),
  ADD KEY `ID_List` (`ID_List`);

--
-- Indexes for table `detail_board`
--
ALTER TABLE `detail_board`
  ADD PRIMARY KEY (`ID_Detail_Board`),
  ADD KEY `ID_Account` (`ID_Account`),
  ADD KEY `ID_Board` (`ID_Board`);

--
-- Indexes for table `list`
--
ALTER TABLE `list`
  ADD PRIMARY KEY (`ID_List`),
  ADD KEY `ID_Board` (`ID_Board`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `ID_Account` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `board`
--
ALTER TABLE `board`
  MODIFY `ID_Board` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `card`
--
ALTER TABLE `card`
  MODIFY `ID_Card` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `detail_board`
--
ALTER TABLE `detail_board`
  MODIFY `ID_Detail_Board` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `list`
--
ALTER TABLE `list`
  MODIFY `ID_List` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `card`
--
ALTER TABLE `card`
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`ID_List`) REFERENCES `list` (`ID_List`);

--
-- Constraints for table `detail_board`
--
ALTER TABLE `detail_board`
  ADD CONSTRAINT `detail_board_ibfk_2` FOREIGN KEY (`ID_Account`) REFERENCES `account` (`ID_Account`),
  ADD CONSTRAINT `detail_board_ibfk_3` FOREIGN KEY (`ID_Board`) REFERENCES `board` (`ID_Board`);

--
-- Constraints for table `list`
--
ALTER TABLE `list`
  ADD CONSTRAINT `list_ibfk_1` FOREIGN KEY (`ID_Board`) REFERENCES `board` (`ID_Board`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
