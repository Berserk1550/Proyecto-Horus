-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-10-2025 a las 16:55:40
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_parqueo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `convenios`
--

CREATE TABLE `convenios` (
  `tipo_convenio` enum('empresa','persona') NOT NULL DEFAULT 'persona',
  `parqueadero_nit` varchar(15) DEFAULT NULL,
  `nit` varchar(15) NOT NULL,
  `cedula` varchar(15) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `descuento_porcentaje` decimal(5,2) DEFAULT NULL,
  `tarifa_fija` decimal(10,2) DEFAULT NULL,
  `activo` enum('activa','inactiva') DEFAULT 'activa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `espacios`
--

CREATE TABLE `espacios` (
  `id_espacios` int(11) NOT NULL,
  `parqueadero_nit` varchar(15) DEFAULT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `tipo` enum('carro','moto','camioneta') DEFAULT NULL,
  `dimension` enum('pequeno','grande') DEFAULT 'pequeno',
  `ocupado` enum('disponible','ocupado') DEFAULT 'disponible'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parqueadero`
--

CREATE TABLE `parqueadero` (
  `nit` varchar(15) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(150) NOT NULL,
  `departamento` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(80) DEFAULT NULL,
  `fecha_registro` date DEFAULT curdate(),
  `estado` enum('activo','inactivo') DEFAULT 'activo',
  `capacidad_carros_pequenos` int(11) DEFAULT 0,
  `capacidad_carros_grandes` int(11) DEFAULT 0,
  `capacidad_motos` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `parqueadero`
--

INSERT INTO `parqueadero` (`nit`, `nombre`, `direccion`, `departamento`, `ciudad`, `telefono`, `correo`, `fecha_registro`, `estado`, `capacidad_carros_pequenos`, `capacidad_carros_grandes`, `capacidad_motos`) VALUES
('0001', 'Parkings Stark', 'Calle Malibu Point #10880', 'California', 'Malibu', '3120987654', 'stark@mail.com', '2025-10-23', 'activo', 5, 5, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros`
--

CREATE TABLE `registros` (
  `id_registros` int(11) NOT NULL,
  `parqueadero_nit` varchar(15) DEFAULT NULL,
  `usuario_cedula` varchar(15) DEFAULT NULL,
  `vehiculo_placa` varchar(7) DEFAULT NULL,
  `espacio_id` int(11) DEFAULT NULL,
  `fecha_ingreso` datetime DEFAULT NULL,
  `fecha_salida` datetime DEFAULT NULL,
  `tarifa_id` int(11) DEFAULT NULL,
  `convenio_nit` varchar(15) DEFAULT NULL,
  `convenio_cedula` varchar(15) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarifas`
--

CREATE TABLE `tarifas` (
  `id_tarifas` int(11) NOT NULL,
  `parqueadero_nit` varchar(15) DEFAULT NULL,
  `tipo_tarifa` enum('diurna','nocturna','convenio','por_hora','por_dia','jornada_diurna','jornada_nocturna') DEFAULT NULL,
  `tipo_vehiculo` enum('carro','moto','camioneta') DEFAULT NULL,
  `valor_primera_hora` decimal(7,2) DEFAULT NULL,
  `valor_hora_extra` decimal(7,2) DEFAULT NULL,
  `valor_jornada` decimal(10,2) DEFAULT NULL,
  `valor_dia_completo` decimal(10,2) DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `cedula` varchar(15) NOT NULL,
  `parqueadero_nit` varchar(15) DEFAULT NULL,
  `nombres` varchar(60) DEFAULT NULL,
  `apellidos` varchar(60) DEFAULT NULL,
  `correo` varchar(80) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `tel_emergencia` varchar(20) DEFAULT NULL,
  `contrasena` varchar(64) DEFAULT NULL,
  `rol` enum('admin','portero','cliente') DEFAULT NULL,
  `activo` enum('activo','inactivo') DEFAULT 'activo',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`cedula`, `parqueadero_nit`, `nombres`, `apellidos`, `correo`, `telefono`, `tel_emergencia`, `contrasena`, `rol`, `activo`, `fecha_registro`) VALUES
('1234567890', '0001', 'Emily', 'Stark', 'e@mail.com', '3120000000', '3111111111', '123', 'admin', 'activo', '2025-10-23 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `placa` varchar(7) NOT NULL,
  `parqueadero_nit` varchar(15) DEFAULT NULL,
  `tipo` enum('carro','moto','camioneta') DEFAULT NULL,
  `dimension` enum('pequeno','grande') DEFAULT 'pequeno',
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `convenios`
--
ALTER TABLE `convenios`
  ADD PRIMARY KEY (`nit`,`cedula`),
  ADD KEY `parqueadero_nit` (`parqueadero_nit`);

--
-- Indices de la tabla `espacios`
--
ALTER TABLE `espacios`
  ADD PRIMARY KEY (`id_espacios`),
  ADD KEY `parqueadero_nit` (`parqueadero_nit`);

--
-- Indices de la tabla `parqueadero`
--
ALTER TABLE `parqueadero`
  ADD PRIMARY KEY (`nit`);

--
-- Indices de la tabla `registros`
--
ALTER TABLE `registros`
  ADD PRIMARY KEY (`id_registros`),
  ADD KEY `parqueadero_nit` (`parqueadero_nit`),
  ADD KEY `usuario_cedula` (`usuario_cedula`),
  ADD KEY `vehiculo_placa` (`vehiculo_placa`),
  ADD KEY `espacio_id` (`espacio_id`),
  ADD KEY `tarifa_id` (`tarifa_id`),
  ADD KEY `convenio_nit` (`convenio_nit`,`convenio_cedula`);

--
-- Indices de la tabla `tarifas`
--
ALTER TABLE `tarifas`
  ADD PRIMARY KEY (`id_tarifas`),
  ADD KEY `parqueadero_nit` (`parqueadero_nit`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`cedula`),
  ADD KEY `parqueadero_nit` (`parqueadero_nit`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`placa`),
  ADD KEY `parqueadero_nit` (`parqueadero_nit`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `espacios`
--
ALTER TABLE `espacios`
  MODIFY `id_espacios` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registros`
--
ALTER TABLE `registros`
  MODIFY `id_registros` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tarifas`
--
ALTER TABLE `tarifas`
  MODIFY `id_tarifas` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `convenios`
--
ALTER TABLE `convenios`
  ADD CONSTRAINT `convenios_ibfk_1` FOREIGN KEY (`parqueadero_nit`) REFERENCES `parqueadero` (`nit`);

--
-- Filtros para la tabla `espacios`
--
ALTER TABLE `espacios`
  ADD CONSTRAINT `espacios_ibfk_1` FOREIGN KEY (`parqueadero_nit`) REFERENCES `parqueadero` (`nit`);

--
-- Filtros para la tabla `registros`
--
ALTER TABLE `registros`
  ADD CONSTRAINT `registros_ibfk_1` FOREIGN KEY (`parqueadero_nit`) REFERENCES `parqueadero` (`nit`),
  ADD CONSTRAINT `registros_ibfk_2` FOREIGN KEY (`usuario_cedula`) REFERENCES `usuarios` (`cedula`),
  ADD CONSTRAINT `registros_ibfk_3` FOREIGN KEY (`vehiculo_placa`) REFERENCES `vehiculos` (`placa`),
  ADD CONSTRAINT `registros_ibfk_4` FOREIGN KEY (`espacio_id`) REFERENCES `espacios` (`id_espacios`),
  ADD CONSTRAINT `registros_ibfk_5` FOREIGN KEY (`tarifa_id`) REFERENCES `tarifas` (`id_tarifas`),
  ADD CONSTRAINT `registros_ibfk_6` FOREIGN KEY (`convenio_nit`,`convenio_cedula`) REFERENCES `convenios` (`nit`, `cedula`);

--
-- Filtros para la tabla `tarifas`
--
ALTER TABLE `tarifas`
  ADD CONSTRAINT `tarifas_ibfk_1` FOREIGN KEY (`parqueadero_nit`) REFERENCES `parqueadero` (`nit`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`parqueadero_nit`) REFERENCES `parqueadero` (`nit`);

--
-- Filtros para la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `vehiculos_ibfk_1` FOREIGN KEY (`parqueadero_nit`) REFERENCES `parqueadero` (`nit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
