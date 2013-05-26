-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 25, 2013 at 12:07 AM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `fqt`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=43 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add log entry', 7, 'add_logentry'),
(20, 'Can change log entry', 7, 'change_logentry'),
(21, 'Can delete log entry', 7, 'delete_logentry'),
(22, 'Can add program', 8, 'add_program'),
(23, 'Can change program', 8, 'change_program'),
(24, 'Can delete program', 8, 'delete_program'),
(25, 'Can add Imagen', 9, 'add_image'),
(26, 'Can change Imagen', 9, 'change_image'),
(27, 'Can delete Imagen', 9, 'delete_image'),
(28, 'Can add video_ category', 10, 'add_video_category'),
(29, 'Can change video_ category', 10, 'change_video_category'),
(30, 'Can delete video_ category', 10, 'delete_video_category'),
(31, 'Can add video', 11, 'add_video'),
(32, 'Can change video', 11, 'change_video'),
(33, 'Can delete video', 11, 'delete_video'),
(34, 'Can add download', 12, 'add_download'),
(35, 'Can change download', 12, 'change_download'),
(36, 'Can delete download', 12, 'delete_download'),
(37, 'Can add toner', 13, 'add_toner'),
(38, 'Can change toner', 13, 'change_toner'),
(39, 'Can delete toner', 13, 'delete_toner'),
(40, 'Can add logos', 14, 'add_logos'),
(41, 'Can change logos', 14, 'change_logos'),
(42, 'Can delete logos', 14, 'delete_logos');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', '', '', 'jaime@mintitmedia.com', 'pbkdf2_sha256$10000$8tUweWVSE6rl$P921LCJZG0p64mFvKyTJI6o+IHtrF5bE7e9Qux1PZeM=', 1, 1, 1, '2013-05-24 15:38:05', '2013-05-06 03:24:46');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2013-05-06 03:44:20', 1, 8, '1', 'Program object', 1, ''),
(2, '2013-05-06 03:45:31', 1, 8, '2', 'Program object', 1, ''),
(3, '2013-05-06 03:46:38', 1, 8, '3', 'Program object', 1, ''),
(4, '2013-05-06 03:47:42', 1, 8, '4', 'Program object', 1, ''),
(5, '2013-05-06 03:48:53', 1, 8, '5', 'Program object', 1, ''),
(6, '2013-05-06 03:51:06', 1, 8, '6', 'Program object', 1, ''),
(7, '2013-05-24 17:56:02', 1, 8, '1', 'Program object', 1, ''),
(8, '2013-05-24 17:56:31', 1, 8, '2', 'Program object', 1, ''),
(9, '2013-05-24 17:56:51', 1, 8, '3', 'Program object', 1, ''),
(10, '2013-05-24 17:57:18', 1, 8, '4', 'Program object', 1, ''),
(11, '2013-05-24 17:57:36', 1, 8, '5', 'Program object', 1, ''),
(12, '2013-05-24 17:58:20', 1, 8, '6', 'Program object', 1, ''),
(13, '2013-05-24 17:58:37', 1, 8, '1', 'Program object', 2, 'Changed has_contact_form.'),
(14, '2013-05-24 20:59:27', 1, 8, '1', 'Program object', 1, ''),
(15, '2013-05-24 21:10:27', 1, 8, '1', 'Program object', 1, ''),
(16, '2013-05-24 21:11:55', 1, 8, '2', 'Program object', 1, ''),
(17, '2013-05-24 21:12:20', 1, 8, '3', 'Program object', 1, ''),
(18, '2013-05-24 21:12:47', 1, 8, '4', 'Program object', 1, ''),
(19, '2013-05-24 21:13:21', 1, 8, '5', 'Program object', 1, ''),
(20, '2013-05-24 21:14:00', 1, 8, '6', 'Program object', 1, ''),
(21, '2013-05-24 21:16:18', 1, 8, '5', 'Program object', 2, 'Changed weight.'),
(22, '2013-05-24 21:16:58', 1, 8, '4', 'Program object', 2, 'Changed weight.'),
(23, '2013-05-24 21:17:17', 1, 8, '3', 'Program object', 2, 'Changed weight.'),
(24, '2013-05-24 21:32:42', 1, 8, '6', 'Program object', 2, 'Changed has_contact_form.');

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'log entry', 'admin', 'logentry'),
(8, 'program', 'programas', 'program'),
(9, 'Imagen', 'programas', 'image'),
(10, 'video_ category', 'youtube', 'video_category'),
(11, 'video', 'youtube', 'video'),
(12, 'download', 'downloads', 'download'),
(13, 'toner', 'inversiones', 'toner'),
(14, 'logos', 'inversiones', 'logos');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1365d5541b25e68b658c148765d391f6', 'YjdkYjA2OTVhYTFlNmI4MGYzZDhkNmI3ZGExZTk5YjZlMmJjZDMwMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-05-20 03:31:32'),
('a6cfdfba0f84cb3c88640ef27a515b4c', 'YjdkYjA2OTVhYTFlNmI4MGYzZDhkNmI3ZGExZTk5YjZlMmJjZDMwMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-06-07 15:38:05');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `downloads_download`
--

CREATE TABLE IF NOT EXISTS `downloads_download` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `source` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `reg_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `inversiones_logos`
--

CREATE TABLE IF NOT EXISTS `inversiones_logos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alt` varchar(140) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `weight` int(11) DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `category` varchar(140) NOT NULL,
  `reg_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `inversiones_toner`
--

CREATE TABLE IF NOT EXISTS `inversiones_toner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `counter` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `programas_image`
--

CREATE TABLE IF NOT EXISTS `programas_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alt` varchar(140) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `weight` int(11) DEFAULT NULL,
  `program_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `programas_image_7eef53e3` (`program_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `programas_image`
--

INSERT INTO `programas_image` (`id`, `alt`, `image`, `weight`, `program_id`) VALUES
(1, '', 'programas/lab_vivo_01_3.jpg', NULL, 1),
(2, '', 'programas/lab_vivo_02_3.jpg', NULL, 1),
(3, '', 'programas/lab_vivo_03_3.jpg', NULL, 1),
(4, '', 'programas/ecoagentes_01_2.jpg', NULL, 2),
(5, '', 'programas/proyect_semilla_01_2.jpg', NULL, 3),
(6, '', 'programas/proyect_semilla_02_3.jpg', NULL, 3),
(7, '', 'programas/proyect_semilla_03_3.jpg', NULL, 3),
(8, '', 'programas/reci_jardin_01_2.jpg', NULL, 4),
(9, '', 'programas/reci_jardin_02_2.jpg', NULL, 4),
(10, '', 'programas/reci_jardin_03_2.jpg', NULL, 4),
(11, '', 'programas/reciclases_01_2.jpg', NULL, 5),
(12, '', 'programas/reciclases_02_1.jpg', NULL, 5),
(13, '', 'programas/reciclases_03_1.jpg', NULL, 5),
(14, '', 'programas/jov_trans_01_2.jpg', NULL, 6),
(15, '', 'programas/jov_trans_02_2.jpg', NULL, 6);

-- --------------------------------------------------------

--
-- Table structure for table `programas_program`
--

CREATE TABLE IF NOT EXISTS `programas_program` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `description_left` longtext,
  `description_right` longtext,
  `weight` int(11) DEFAULT NULL,
  `has_contact_form` tinyint(1) NOT NULL,
  `contact_form_title` varchar(120) DEFAULT NULL,
  `reg_date` datetime NOT NULL,
  `where_gallery` varchar(140) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `programas_program`
--

INSERT INTO `programas_program` (`id`, `title`, `description_left`, `description_right`, `weight`, `has_contact_form`, `contact_form_title`, `reg_date`, `where_gallery`) VALUES
(1, 'Laboratorio Vivo', '<p>Consta de talleres pr&aacute;cticos que van guiando a ni&ntilde;as y ni&ntilde;os en la importancia de cultivar por si mismos, alimentos org&aacute;nicos.</p>\r\n<p>Se le llama Laboratorio Vivo, ya que el huerto se convierte en un lugar donde se experimenta directamente con la naturaleza, se observa, se interviene y adem&aacute;s se basa en el trabajo en equipo.</p>\r\n<p>Es considerado un programa transversal con la propuesta del Plan de estudios 2011, se rescatan tem&aacute;ticas de los diferentes campos de formaci&oacute;n, en los distintos niveles de educaci&oacute;n b&aacute;sica.</p>\r\n<p>Estos talleres son impartidos dentro de las instituciones educativas como escuelas p&uacute;blicas y casas hogar.</p>', '\r\n<h3>Objetivo General</h3>\r\n<p>Establecer un huerto de aprendizaje (un laboratorio vivo) dentro de instituciones educativas, con el fin de conectar directamente a los ni&ntilde;os y ni&ntilde;as con su entorno y con la producci&oacute;n de alimentos org&aacute;nicos, dando una herramienta de vida pr&aacute;ctica en su formaci&oacute;n.</p>\r\n<h3>Objetivos Espec&iacute;ficos</h3>\r\n<ul class="yellow_list">\r\n<li><span>Crear una conciencia social sobre el origen de nuestros alimentos, para reducir su huella ecol&oacute;gica.</span></li>\r\n<li><span>Vincular los conocimientos construidos en el campo de otras asignaturas curriculares del nivel b&aacute;sico con el huerto.</span></li>\r\n<li><span>Estimular las inteligencias m&uacute;ltiples que cada uno de los participantes poseen.</span></li>\r\n<li><span>Diversificar la dieta de los estudiantes dentro del programa de huerto escolar.</span></li>\r\n<li><span>Desarrollar habilidades pr&aacute;cticas para que el alumnos puedan reproducir estos conocimientos en su hogar o comunidad. </span></li>\r\n</ul>\r\n', NULL, 0, '', '2013-05-24 21:09:58', '1'),
(2, 'Ecoagentes', '\r\n<p>Programa enfocado a involucrar a ni&ntilde;os y j&oacute;venes en el cuidado del medio ambiente de forma proactiva utilizando una plataforma virtual dise&ntilde;ada para monitorear las reducciones de C02 a partir de las acciones de los participantes.</p>\r\n<p>Se promueve el trabajo en equipo y el liderazgo a fin de generar sinergias positivas y consolidar la forma de percibirse como agente de cambio. Adem&aacute;s de promover una cultura de la conservaci&oacute;n y cuidado del agua, de la energ&iacute;a el&eacute;ctrica, de las &aacute;reas verdes y la buena disposici&oacute;n de residuos org&aacute;nicos e inorg&aacute;nicos no t&oacute;xicos.</p>\r\n<p>Esto se logra a trav&eacute;s de talleres de educaci&oacute;n ambiental y una plataforma ambiental que permite el monitoreo y seguimiento.</p>\r\n', '', NULL, 0, '', '2013-05-24 21:10:27', '2'),
(3, 'Proyecto Semilla', '', '<p>El proyecto semilla es un programa din&aacute;mico de participaci&oacute;n y educaci&oacute;n, en el que ni&ntilde;os y j&oacute;venes de casas hogar aprenden la importancia de la conservaci&oacute;n del entorno y la apropiaci&oacute;n del espacio. Con actividades como forestaci&oacute;n, construcci&oacute;n de su propio huerto, realizaci&oacute;n de composta, asignaci&oacute;n de espacio para la separaci&oacute;n de residuos y con talleres de educaci&oacute;n ambiental Reciclases.</p>\r\n<p>Desde su arranque se ha impartido en dos etapas, la primera fue de enero a julio de 2011 en el que se invit&oacute; a 9 casas hogar donde se beneficiaron 250 ni&ntilde;os y en la segunda etapa de enero a julio de 2012 se continu&oacute; el programa con 8 casas hogar beneficiando a 200 ni&ntilde;os.</p>\r\n<p>Contamos con la colaboraci&oacute;n de estudiantes de la licenciatura en educaci&oacute;n, de la Universidad del Desarrollo Profesional (UNIDEP) campus Ensenada, quienes imparten los talleres.</p>', 1, 0, '', '2013-05-24 21:11:55', '1'),
(4, 'Reciclases en tu jardín', '\r\n<p><em>Son una evoluci&oacute;n de las Reciclases.</em></p>\r\n<p>Las escuelas interesadas en recibir &aacute;rboles para ser plantados en sus espacios comunes, se registran para entrar en el programa. Los estudiantes de estos espacios educativos participan en la actividad de forestaci&oacute;n de su propio centro educativo. Se invitan a los padres de familia a ser parte de esta actividad para poder fortalecer un sentido de pertenencia en su comunidad. A la fecha se han plantado 1,331 &aacute;rboles frutales y de sombra en escuelas y casas hogar de Tijuana y Ensenada.</p>\r\n', '', 1, 0, '', '2013-05-24 21:12:20', '2'),
(5, 'Reciclases', '<p>Talleres que promueven una cultura urbana proactiva, <em>enfocada al medio ambiente y desarrollo sustentable</em>, de forma din&aacute;mica y divertida. Se realizan en escuelas p&uacute;blicas de educaci&oacute;n b&aacute;sica y media superior, adem&aacute;s de eventos organizados por otras organizaciones civiles o por dependencias de gobierno de los tres niveles de gobierno, enfocadas a la educaci&oacute;n, medio ambiente, cultura, ciencia y tecnolog&iacute;a.</p>\r\n<p>Las actividades est&aacute;n dirigidas a ni&ntilde;os y j&oacute;venes. En Reciclases se les ense&ntilde;a a ni&ntilde;os y j&oacute;venes la importancia de cuidar el entono donde conviven con otras personas, a hacer uso correcto de los recursos, a respetar el espacio que comparten con otras personas y la necesidad de reducir, reutilizar y separar los residuos generados en la din&aacute;mica diaria.</p>', '<p>Las Reciclases se realizan gracias al apoyo y compromiso de j&oacute;venes universitarios que realizan servicio social o pr&aacute;cticas profesionales, los cuales son capacitados para convertirse en Talleristas de Reciclases, se les asigna una escuela y cumplen con el total de horas frente a grupo. De esta forma formamos a futuros maestros y se brinda la oportunidad de crear la necesidad, dentro de los espacios educativos, de incorporar la clase de cultura y educaci&oacute;n ambiental.</p>\r\n<p>A la fecha se han beneficiado a 66 preescolares, primarias y secundarias de Tijuana y Mexicali con la participaci&oacute;n de 172 talleristas y 25 voluntarios universitarios, beneficiando a 42,228 ni&ntilde;os y j&oacute;venes en escuelas y 12,890 en eventos especiales.</p>', 1, 1, 'Forma parte de nuestro equipo de talleristas', '2013-05-24 21:12:47', '1'),
(6, 'Jóvenes transformando', '', '<p>Programa integral donde los j&oacute;venes son un agente de cambio dentro de su comunidad. Se promueve la participaci&oacute;n ciudadana con actividades que fortalecen una cultura urbana proactiva y un sentido de pertenencia dentro de la comunidad.</p>', NULL, 1, '¿Te gustaría ser parte de los jóvenes que transforman su ciudad?', '2013-05-24 21:13:40', '1');

-- --------------------------------------------------------

--
-- Table structure for table `youtube_video`
--

CREATE TABLE IF NOT EXISTS `youtube_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `source` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `reg_date` datetime NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `youtube_video_42dc49bc` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `youtube_video_category`
--

CREATE TABLE IF NOT EXISTS `youtube_video_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `programas_image`
--
ALTER TABLE `programas_image`
  ADD CONSTRAINT `program_id_refs_id_9af5dc82` FOREIGN KEY (`program_id`) REFERENCES `programas_program` (`id`);

--
-- Constraints for table `youtube_video`
--
ALTER TABLE `youtube_video`
  ADD CONSTRAINT `category_id_refs_id_f1d7839d` FOREIGN KEY (`category_id`) REFERENCES `youtube_video_category` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
