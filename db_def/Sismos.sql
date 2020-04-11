-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 11, 2020 at 03:05 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Sismos`
--

-- --------------------------------------------------------

--
-- Table structure for table `CHANNEL`
--

CREATE TABLE `CHANNEL` (
  `symbol` char(3) NOT NULL,
  `station` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `CHANNEL_EVENT`
--

CREATE TABLE `CHANNEL_EVENT` (
  `station` varchar(10) NOT NULL,
  `channel` char(3) NOT NULL,
  `event_id` int(10) UNSIGNED NOT NULL,
  `sample_rate` int(10) UNSIGNED NOT NULL,
  `waveform` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`waveform`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `EARTHQUAKE`
--

CREATE TABLE `EARTHQUAKE` (
  `id` int(10) UNSIGNED NOT NULL,
  `date_time` datetime NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `depth` float NOT NULL,
  `magnitude` float NOT NULL,
  `duration` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `STATION`
--

CREATE TABLE `STATION` (
  `symbol` varchar(10) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `elevation` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CHANNEL`
--
ALTER TABLE `CHANNEL`
  ADD PRIMARY KEY (`symbol`,`station`),
  ADD KEY `station` (`station`);

--
-- Indexes for table `CHANNEL_EVENT`
--
ALTER TABLE `CHANNEL_EVENT`
  ADD KEY `station` (`station`,`channel`),
  ADD KEY `event_id` (`event_id`);

--
-- Indexes for table `EARTHQUAKE`
--
ALTER TABLE `EARTHQUAKE`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `STATION`
--
ALTER TABLE `STATION`
  ADD PRIMARY KEY (`symbol`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `CHANNEL`
--
ALTER TABLE `CHANNEL`
  ADD CONSTRAINT `CHANNEL_ibfk_1` FOREIGN KEY (`station`) REFERENCES `STATION` (`symbol`);

--
-- Constraints for table `CHANNEL_EVENT`
--
ALTER TABLE `CHANNEL_EVENT`
  ADD CONSTRAINT `CHANNEL_EVENT_ibfk_1` FOREIGN KEY (`station`,`channel`) REFERENCES `CHANNEL` (`station`, `symbol`),
  ADD CONSTRAINT `CHANNEL_EVENT_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `EARTHQUAKE` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
