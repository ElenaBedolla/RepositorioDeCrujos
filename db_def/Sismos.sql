-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 10-04-2020 a las 08:52:18
-- Versión del servidor: 10.4.8-MariaDB
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Sismos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `CHANNEL`
--

CREATE TABLE `CHANNEL` (
  `symbol` char(3) NOT NULL,
  `station` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `CHANNEL_EVENT`
--

CREATE TABLE `CHANNEL_EVENT` (
  `station` varchar(10) NOT NULL,
  `channel` char(3) NOT NULL,
  `event_id` int(10) UNSIGNED NOT NULL,
  `sample_rate` int(10) UNSIGNED NOT NULL,
  `waveform` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `EARTHQUAKE`
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
-- Estructura de tabla para la tabla `STATION`
--

CREATE TABLE `STATION` (
  `symbol` varchar(10) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `elevation` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `CHANNEL`
--
ALTER TABLE `CHANNEL`
  ADD PRIMARY KEY (`symbol`,`station`),
  ADD KEY `station` (`station`);

--
-- Indices de la tabla `EARTHQUAKE`
--
ALTER TABLE `EARTHQUAKE`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `STATION`
--
ALTER TABLE `STATION`
  ADD PRIMARY KEY (`symbol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `EARTHQUAKE`
--
ALTER TABLE `EARTHQUAKE`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `CHANNEL`
--
ALTER TABLE `CHANNEL`
  ADD CONSTRAINT `CHANNEL_ibfk_1` FOREIGN KEY (`station`) REFERENCES `STATION` (`symbol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
