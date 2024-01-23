-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 23-01-2024 a las 16:29:44
-- Versión del servidor: 10.5.20-MariaDB
-- Versión de PHP: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
  `dni` varchar(10) NOT NULL,
  `ing_alcohol` tinyint(1) NOT NULL,
  `alc_mgl` decimal(4,3) UNSIGNED NOT NULL,
  `alc_bac` decimal(4,3) UNSIGNED NOT NULL,
  `picture` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='alcohol_measures';

--
-- Volcado de datos para la tabla `tb_alcohol_measure`
--

INSERT INTO `tb_alcohol_measure` (`id_measure`, `dni`, `ing_alcohol`, `alc_mgl`, `alc_bac`, `picture`, `date`) VALUES
(80, '00000005', 0, 0.000, 0.000, 'pruebaalc6432257d24d80.jpg', '2023-04-08 21:39:57'),
(81, '00000005', 0, 0.000, 0.000, 'pruebaalc643225b9bda57.jpg', '2023-04-08 21:40:57'),
(82, '00000005', 0, 0.000, 0.000, 'pruebaalc643225cc9bace.jpg', '2023-04-08 21:41:16'),
(83, '00000005', 0, 0.000, 0.000, 'pruebaalc64322609bb0d3.jpg', '2023-04-08 21:42:17'),
(84, '00000005', 0, 1.197, 0.251, 'pruebaalc64322679bf4dd.jpg', '2023-04-08 21:44:09'),
(85, '00000005', 0, 0.848, 0.178, 'pruebaalc643226b764696.jpg', '2023-04-08 21:45:11'),
(86, '00000005', 0, 0.740, 0.155, 'pruebaalc643226ee22768.jpg', '2023-04-08 21:46:06'),
(87, '00000005', 0, 0.509, 0.107, 'pruebaalc643227437f4a2.jpg', '2023-04-08 21:47:31'),
(88, '00000005', 1, 0.383, 0.080, 'pruebaalc6432279f5e3e0.jpg', '2023-04-08 21:49:03'),
(89, '00000005', 1, 0.288, 0.060, 'pruebaalc6432280731603.jpg', '2023-04-08 21:50:47'),
(90, '00000005', 1, 0.249, 0.052, 'pruebaalc6432285b10c98.jpg', '2023-04-08 21:52:11'),
(91, '00000005', 0, 0.208, 0.043, 'pruebaalc643228d3cc6c3.jpg', '2023-04-08 21:54:11'),
(92, '00000005', 0, 0.149, 0.031, 'pruebaalc6432296dca038.jpg', '2023-04-08 21:56:45'),
(93, '00000005', 0, 0.162, 0.034, 'pruebaalc6432298d636ff.jpg', '2023-04-08 21:57:17'),
(94, '00000005', 0, 0.178, 0.037, 'pruebaalc643229db18072.jpg', '2023-04-08 21:58:35'),
(95, '00000005', 0, 0.150, 0.031, 'pruebaalc64322a244955e.jpg', '2023-04-08 21:59:48'),
(96, '00000005', 0, 0.158, 0.033, 'pruebaalc64322a4f7cc52.jpg', '2023-04-08 22:00:31'),
(97, '00000005', 0, 0.125, 0.026, 'pruebaalc64322a9b100b8.jpg', '2023-04-08 22:01:47'),
(98, '00000005', 0, 0.110, 0.023, 'pruebaalc64322b5376913.jpg', '2023-04-08 22:04:51'),
(103, '00000005', 0, 0.000, 0.000, 'pruebaalc64b9b943c8ba0.jpg', '2023-07-20 17:46:27'),
(104, '00000005', 0, 0.000, 0.000, 'pruebaalc64b9bb7241ea8.jpg', '2023-07-20 17:55:46'),
(105, '00000005', 1, 0.000, 0.000, 'pruebaalc64b9bb8b20aeb.jpg', '2023-07-20 17:56:11'),
(106, '00000005', 0, 0.000, 0.000, 'pruebaalc64b9bc7ead3d1.jpg', '2023-07-20 18:00:14'),
(107, '00000005', 0, 0.000, 0.000, 'pruebaalc64b9bd0ca398f.jpg', '2023-07-20 18:02:36'),
(108, '00000005', 0, 0.000, 0.000, 'pruebaalc64b9bd2f2c634.jpg', '2023-07-20 18:03:11'),
(110, '00000005', 0, 0.000, 0.000, 'pruebaalc64cd8f097e507.jpg', '2023-08-04 18:51:37'),
(111, '00000005', 0, 0.000, 0.000, 'pruebaalc64cd90282a6f2.jpg', '2023-08-04 18:56:24'),
(112, '00000005', 0, 0.000, 0.000, 'pruebaalc64cd963622ced.jpg', '2023-08-04 19:22:14'),
(113, '00000005', 0, 0.000, 0.000, 'pruebaalc64cd964c7aebd.jpg', '2023-08-04 19:22:36'),
(130, '00000005', 0, 0.000, 0.000, 'pruebaalc64f934a64451a.jpg', '2023-09-06 21:25:42'),
(131, '00000005', 0, 0.000, 0.000, 'pruebaalc64f934b64fc89.jpg', '2023-09-06 21:25:58'),
(133, '00000005', 0, 0.000, 0.000, 'pruebaalc64f935113ef12.jpg', '2023-09-06 21:27:29'),
(134, '00000005', 0, 0.000, 0.000, 'pruebaalc64f935396a53b.jpg', '2023-09-06 21:28:09'),
(135, '00000005', 0, 0.000, 0.000, 'pruebaalc64f93558f120d.jpg', '2023-09-06 21:28:40'),
(136, '00000005', 0, 0.000, 0.000, 'pruebaalc64f935eb70f94.jpg', '2023-09-06 21:31:07'),
(137, '00000005', 0, 0.000, 0.000, 'pruebaalc64f9363b1ae45.jpg', '2023-09-06 21:32:27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_loggin`
--

CREATE TABLE `tb_loggin` (
  `Username` varchar(50) NOT NULL COMMENT 'user_email',
  `Password` varchar(50) NOT NULL COMMENT 'user_password'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='loggin_user';

--
-- Volcado de datos para la tabla `tb_loggin`
--

INSERT INTO `tb_loggin` (`Username`, `Password`) VALUES
('aoshita@hotmail.com', '12345'),
('jcardenas@gmail.com', '12345'),
('jchavesta@hotmail.com', '12345'),
('lmerino@hotmail.com', '12345'),
('sgonzales@hotmail.com', '12345'),
('wechavesta@hotmail.com', '12345'),
('wilson_13_10@hotmail.com', '12345');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_user`
--

CREATE TABLE `tb_user` (
  `dni` varchar(10) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `phone_number` varchar(12) DEFAULT NULL,
  `city` varchar(60) DEFAULT NULL COMMENT 'ciudad',
  `country` varchar(50) NOT NULL COMMENT 'país de residencia',
  `user_image` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='users_information';

--
-- Volcado de datos para la tabla `tb_user`
--

INSERT INTO `tb_user` (`dni`, `email`, `name`, `lastname`, `phone_number`, `city`, `country`, `user_image`) VALUES
('00000001', 'wechavesta@hotmail.com', 'Wilson Eduardo', 'Chavesta', '951211174', 'Lima', 'Perú', 'user643a569d48358.jpg'),
('00000002', 'sgonzales@hotmail.com', 'Sara', 'Gonzales', '954541113', 'Lima', 'Perú', 'user643a57578ebbf.jpg'),
('00000003', 'jcardenas@gmail.com', 'Jorge', 'Cardenas', '912111445', 'Lima', 'Perú', 'user643b426d840d0.jpg'),
('00000004', 'jchavesta@hotmail.com', 'Jackie', 'Chavesta', '912113746', 'Lima', 'Perú', 'user643b42c803849.jpg'),
('00000005', 'wilson_13_10@hotmail.com', 'Wilson', 'Chavesta Gonzales', '954541221', 'Lima', 'Perú', 'user1565934329801.jpg'),
('00000006', 'lmerino@hotmail.com', 'Luis', 'Merino Rojas', '917541331', 'Lima', 'Perú', 'user643a57578eer4.jpg'),
('00000007', 'aoshita@hotmail.com', 'Angel', 'Oshita', '945451175', 'Lima', 'Perú', 'user643a516544745.jpg');

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
  MODIFY `id_measure` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=147;

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
