-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 02-04-2023 a las 00:33:44
-- Versión del servidor: 10.5.16-MariaDB
-- Versión de PHP: 7.3.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `id20539402_db_tesis_alcros`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_alcohol_measure`
--

CREATE TABLE `tb_alcohol_measure` (
  `id_measure` smallint(5) UNSIGNED NOT NULL,
  `dni` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ing_alcohol` tinyint(1) NOT NULL,
  `alc_mgl` decimal(4,3) UNSIGNED NOT NULL,
  `alc_bac` decimal(4,3) UNSIGNED NOT NULL,
  `picture` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='alcohol_measures';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_loggin`
--

CREATE TABLE `tb_loggin` (
  `Username` varchar(50) COLLATE utf8_spanish_ci NOT NULL COMMENT 'user_email',
  `Password` varchar(50) COLLATE utf8_spanish_ci NOT NULL COMMENT 'user_password'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='loggin_user';

--
-- Volcado de datos para la tabla `tb_loggin`
--

INSERT INTO `tb_loggin` (`Username`, `Password`) VALUES
('lmerino@hotmail.com', '12345'),
('wilson_13_10@hotmail.com', '12345');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_user`
--

CREATE TABLE `tb_user` (
  `dni` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `name` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `lastname` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `phone_number` varchar(12) COLLATE utf8_spanish_ci DEFAULT NULL,
  `user_image` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='users_information';

--
-- Volcado de datos para la tabla `tb_user`
--

INSERT INTO `tb_user` (`dni`, `email`, `name`, `lastname`, `phone_number`, `user_image`) VALUES
('71234541', 'lmerino@hotmail.com', 'Luis', 'Merino Rojas', '917541331', NULL),
('74881892', 'wilson_13_10@hotmail.com', 'Wilson', 'Chavesta Gonzales', '954541221', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tb_alcohol_measure`
--
ALTER TABLE `tb_alcohol_measure`
  ADD PRIMARY KEY (`id_measure`),
  ADD KEY `dni` (`dni`);

--
-- Indices de la tabla `tb_loggin`
--
ALTER TABLE `tb_loggin`
  ADD PRIMARY KEY (`Username`);

--
-- Indices de la tabla `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`dni`),
  ADD KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tb_alcohol_measure`
--
ALTER TABLE `tb_alcohol_measure`
  MODIFY `id_measure` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tb_alcohol_measure`
--
ALTER TABLE `tb_alcohol_measure`
  ADD CONSTRAINT `tb_alcohol_measure_ibfk_1` FOREIGN KEY (`dni`) REFERENCES `tb_user` (`dni`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tb_user`
--
ALTER TABLE `tb_user`
  ADD CONSTRAINT `tb_user_ibfk_1` FOREIGN KEY (`email`) REFERENCES `tb_loggin` (`Username`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
