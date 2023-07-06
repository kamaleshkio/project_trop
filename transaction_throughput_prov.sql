-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 18, 2021 at 09:46 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `transaction_throughput_prov`
--
CREATE DATABASE IF NOT EXISTS `transaction_throughput_prov` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `transaction_throughput_prov`;

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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=106 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add user_reg1', 7, 'add_user_reg1'),
(20, 'Can change user_reg1', 7, 'change_user_reg1'),
(21, 'Can delete user_reg1', 7, 'delete_user_reg1'),
(22, 'Can add birth_details', 8, 'add_birth_details'),
(23, 'Can change birth_details', 8, 'change_birth_details'),
(24, 'Can delete birth_details', 8, 'delete_birth_details'),
(25, 'Can add birth_details', 9, 'add_birth_details'),
(26, 'Can change birth_details', 9, 'change_birth_details'),
(27, 'Can delete birth_details', 9, 'delete_birth_details'),
(28, 'Can add gov_login', 10, 'add_gov_login'),
(29, 'Can change gov_login', 10, 'change_gov_login'),
(30, 'Can delete gov_login', 10, 'delete_gov_login'),
(31, 'Can add bkey_request1', 9, 'add_bkey_request1'),
(32, 'Can change bkey_request1', 9, 'change_bkey_request1'),
(33, 'Can delete bkey_request1', 9, 'delete_bkey_request1'),
(34, 'Can add birth_certificate1', 11, 'add_birth_certificate1'),
(35, 'Can change birth_certificate1', 11, 'change_birth_certificate1'),
(36, 'Can delete birth_certificate1', 11, 'delete_birth_certificate1'),
(37, 'Can add community_details', 12, 'add_community_details'),
(38, 'Can change community_details', 12, 'change_community_details'),
(39, 'Can delete community_details', 12, 'delete_community_details'),
(40, 'Can add community_certificate1', 13, 'add_community_certificate1'),
(41, 'Can change community_certificate1', 13, 'change_community_certificate1'),
(42, 'Can delete community_certificate1', 13, 'delete_community_certificate1'),
(43, 'Can add school_details1', 14, 'add_school_details1'),
(44, 'Can change school_details1', 14, 'change_school_details1'),
(45, 'Can delete school_details1', 14, 'delete_school_details1'),
(46, 'Can add school_register1', 15, 'add_school_register1'),
(47, 'Can change school_register1', 15, 'change_school_register1'),
(48, 'Can delete school_register1', 15, 'delete_school_register1'),
(49, 'Can add transfer_certificate1', 16, 'add_transfer_certificate1'),
(50, 'Can change transfer_certificate1', 16, 'change_transfer_certificate1'),
(51, 'Can delete transfer_certificate1', 16, 'delete_transfer_certificate1'),
(52, 'Can add attendance_certificate1', 17, 'add_attendance_certificate1'),
(53, 'Can change attendance_certificate1', 17, 'change_attendance_certificate1'),
(54, 'Can delete attendance_certificate1', 17, 'delete_attendance_certificate1'),
(55, 'Can add attendance_details', 18, 'add_attendance_details'),
(56, 'Can change attendance_details', 18, 'change_attendance_details'),
(57, 'Can delete attendance_details', 18, 'delete_attendance_details'),
(58, 'Can add sports_certificate1', 19, 'add_sports_certificate1'),
(59, 'Can change sports_certificate1', 19, 'change_sports_certificate1'),
(60, 'Can delete sports_certificate1', 19, 'delete_sports_certificate1'),
(61, 'Can add sports_details', 20, 'add_sports_details'),
(62, 'Can change sports_details', 20, 'change_sports_details'),
(63, 'Can delete sports_details', 20, 'delete_sports_details'),
(64, 'Can add college_details1', 21, 'add_college_details1'),
(65, 'Can change college_details1', 21, 'change_college_details1'),
(66, 'Can delete college_details1', 21, 'delete_college_details1'),
(67, 'Can add college_register1', 22, 'add_college_register1'),
(68, 'Can change college_register1', 22, 'change_college_register1'),
(69, 'Can delete college_register1', 22, 'delete_college_register1'),
(70, 'Can add ctransfer_certificate1', 23, 'add_ctransfer_certificate1'),
(71, 'Can change ctransfer_certificate1', 23, 'change_ctransfer_certificate1'),
(72, 'Can delete ctransfer_certificate1', 23, 'delete_ctransfer_certificate1'),
(73, 'Can add degree_certificate11', 24, 'add_degree_certificate11'),
(74, 'Can change degree_certificate11', 24, 'change_degree_certificate11'),
(75, 'Can delete degree_certificate11', 24, 'delete_degree_certificate11'),
(76, 'Can add office_details', 25, 'add_office_details'),
(77, 'Can change office_details', 25, 'change_office_details'),
(78, 'Can delete office_details', 25, 'delete_office_details'),
(79, 'Can add office_register1', 26, 'add_office_register1'),
(80, 'Can change office_register1', 26, 'change_office_register1'),
(81, 'Can delete office_register1', 26, 'delete_office_register1'),
(82, 'Can add emppay_slip', 27, 'add_emppay_slip'),
(83, 'Can change emppay_slip', 27, 'change_emppay_slip'),
(84, 'Can delete emppay_slip', 27, 'delete_emppay_slip'),
(85, 'Can add salary_slip', 28, 'add_salary_slip'),
(86, 'Can change salary_slip', 28, 'change_salary_slip'),
(87, 'Can delete salary_slip', 28, 'delete_salary_slip'),
(88, 'Can add exp_certificate', 29, 'add_exp_certificate'),
(89, 'Can change exp_certificate', 29, 'change_exp_certificate'),
(90, 'Can delete exp_certificate', 29, 'delete_exp_certificate'),
(91, 'Can add experience1', 30, 'add_experience1'),
(92, 'Can change experience1', 30, 'change_experience1'),
(93, 'Can delete experience1', 30, 'delete_experience1'),
(94, 'Can add ration_card1', 31, 'add_ration_card1'),
(95, 'Can change ration_card1', 31, 'change_ration_card1'),
(96, 'Can delete ration_card1', 31, 'delete_ration_card1'),
(97, 'Can add ration_carddetails', 31, 'add_ration_carddetails'),
(98, 'Can change ration_carddetails', 31, 'change_ration_carddetails'),
(99, 'Can delete ration_carddetails', 31, 'delete_ration_carddetails'),
(100, 'Can add genration_card', 32, 'add_genration_card'),
(101, 'Can change genration_card', 32, 'change_genration_card'),
(102, 'Can delete genration_card', 32, 'delete_genration_card'),
(103, 'Can add school_birth1', 33, 'add_school_birth1'),
(104, 'Can change school_birth1', 33, 'change_school_birth1'),
(105, 'Can delete school_birth1', 33, 'delete_school_birth1');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
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
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `college_college_register1`
--

CREATE TABLE IF NOT EXISTS `college_college_register1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collegename` varchar(300) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `college_college_register1`
--

INSERT INTO `college_college_register1` (`id`, `collegename`, `email`, `mobile`, `password`) VALUES
(1, 'srm college', 'chennaisundayramya@gmail.com', 9867676767, 'srm'),
(2, 'info college', 'chennaisundayramya@gmail.com', 9878676767, 'info');

-- --------------------------------------------------------

--
-- Table structure for table `college_ctransfer_certificate1`
--

CREATE TABLE IF NOT EXISTS `college_ctransfer_certificate1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `dateof_birth` varchar(300) NOT NULL,
  `religion` varchar(300) NOT NULL,
  `caste` varchar(300) NOT NULL,
  `father_name` varchar(300) NOT NULL,
  `mother_name` varchar(300) NOT NULL,
  `address` varchar(300) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `cname` varchar(300) NOT NULL,
  `dateof_admission` varchar(300) NOT NULL,
  `degree` varchar(300) NOT NULL,
  `joining_year` varchar(300) NOT NULL,
  `degree_finishingyear` varchar(300) NOT NULL,
  `status` varchar(300) NOT NULL,
  `university` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `college_ctransfer_certificate1`
--

INSERT INTO `college_ctransfer_certificate1` (`id`, `uname`, `full_name`, `dateof_birth`, `religion`, `caste`, `father_name`, `mother_name`, `address`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `cname`, `dateof_admission`, `degree`, `joining_year`, `degree_finishingyear`, `status`, `university`, `certificate_file`) VALUES
(1, 'ramya', 'ramya ramachandran', '12-03-1992', 'hindu', 'yadava', 'ramachandran', 'mariammal', '15th street ashok nagar', '/media/ramya_collegetc_AccFp8u.pdf', '0', '327dac4981bb8eac8c50a2f2e861bd3684708cb72f632fe9b9ae067adec8c5b6', '2021-02-04 16:37:51.048026', 'srm college', '21-09-1995', 'BE CSE', '2012', '2017', 'course completed', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `college_degree_certificate11`
--

CREATE TABLE IF NOT EXISTS `college_degree_certificate11` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `dateof_birth` varchar(300) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `cname` varchar(300) NOT NULL,
  `dateof_admission` varchar(300) NOT NULL,
  `degree` varchar(300) NOT NULL,
  `joining_year` varchar(300) NOT NULL,
  `degree_finishingyear` varchar(300) NOT NULL,
  `status` varchar(300) NOT NULL,
  `university` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `college_degree_certificate11`
--

INSERT INTO `college_degree_certificate11` (`id`, `uname`, `full_name`, `dateof_birth`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `cname`, `dateof_admission`, `degree`, `joining_year`, `degree_finishingyear`, `status`, `university`, `certificate_file`) VALUES
(1, 'ramya', 'ramya ramachandran', '12-03-1992', '/media/ramya_degreecertificate.pdf', '0', 'fc5ca7141a80882c60473fba86c1f0397a3c253d865b476e3f184a2dcbc2f26c', '2021-02-04 17:56:27.101768', 'srm college', '21-09-1995', 'BE CSE', '2012', '2017', 'course completed', 'Anna University', '');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(22, 'college', 'college_register1'),
(23, 'college', 'ctransfer_certificate1'),
(24, 'college', 'degree_certificate11'),
(5, 'contenttypes', 'contenttype'),
(11, 'government', 'birth_certificate1'),
(9, 'government', 'bkey_request1'),
(13, 'government', 'community_certificate1'),
(32, 'government', 'genration_card'),
(10, 'government', 'gov_login'),
(8, 'hospital', 'birth_details'),
(27, 'office', 'emppay_slip'),
(30, 'office', 'experience1'),
(29, 'office', 'exp_certificate'),
(26, 'office', 'office_register1'),
(28, 'office', 'salary_slip'),
(17, 'school', 'attendance_certificate1'),
(18, 'school', 'attendance_details'),
(33, 'school', 'school_birth1'),
(15, 'school', 'school_register1'),
(19, 'school', 'sports_certificate1'),
(20, 'school', 'sports_details'),
(16, 'school', 'transfer_certificate1'),
(6, 'sessions', 'session'),
(21, 'user', 'college_details1'),
(12, 'user', 'community_details'),
(25, 'user', 'office_details'),
(31, 'user', 'ration_carddetails'),
(14, 'user', 'school_details1'),
(7, 'user', 'user_reg1');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=54 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-01-18 10:53:51.671219'),
(2, 'auth', '0001_initial', '2021-01-18 10:54:19.469809'),
(3, 'admin', '0001_initial', '2021-01-18 10:54:24.035070'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-18 10:54:24.110075'),
(5, 'contenttypes', '0002_remove_content_type_name', '2021-01-18 10:54:27.671278'),
(6, 'auth', '0002_alter_permission_name_max_length', '2021-01-18 10:54:29.461381'),
(7, 'auth', '0003_alter_user_email_max_length', '2021-01-18 10:54:31.134476'),
(8, 'auth', '0004_alter_user_username_opts', '2021-01-18 10:54:31.208481'),
(9, 'auth', '0005_alter_user_last_login_null', '2021-01-18 10:54:32.634562'),
(10, 'auth', '0006_require_contenttypes_0002', '2021-01-18 10:54:32.716567'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2021-01-18 10:54:32.792571'),
(12, 'auth', '0008_alter_user_username_max_length', '2021-01-18 10:54:35.305715'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2021-01-18 10:54:36.678794'),
(14, 'sessions', '0001_initial', '2021-01-18 10:54:37.757855'),
(15, 'user', '0001_initial', '2021-01-18 10:54:38.771913'),
(16, 'hospital', '0001_initial', '2021-01-20 08:49:02.698179'),
(17, 'hospital', '0002_auto_20210120_1421', '2021-01-20 08:51:49.171701'),
(18, 'government', '0001_initial', '2021-01-20 14:46:13.856293'),
(19, 'government', '0002_auto_20210120_2024', '2021-01-20 14:54:39.058189'),
(20, 'government', '0003_bkey_request1_key1', '2021-01-21 10:42:37.044417'),
(21, 'government', '0004_birth_certificate1', '2021-01-22 15:20:52.498883'),
(22, 'government', '0005_auto_20210122_2100', '2021-01-22 15:30:50.303076'),
(23, 'government', '0006_auto_20210123_1337', '2021-01-23 08:08:34.153605'),
(24, 'user', '0002_community_details', '2021-01-23 11:12:55.219262'),
(25, 'government', '0007_community_certificate1', '2021-01-23 12:52:37.668439'),
(26, 'user', '0003_school_details1', '2021-01-25 10:25:48.987530'),
(27, 'user', '0004_school_details1_school_name', '2021-01-25 13:01:31.597896'),
(28, 'school', '0001_initial', '2021-01-25 13:18:20.321592'),
(29, 'school', '0002_transfer_certificate1', '2021-01-25 15:37:03.781667'),
(30, 'school', '0003_attendance_certificate1_attendance_details', '2021-01-28 06:58:49.011505'),
(31, 'school', '0004_sports_certificate1_sports_details', '2021-02-03 13:23:25.686173'),
(32, 'user', '0005_college_details1', '2021-02-04 07:20:38.494446'),
(33, 'college', '0001_initial', '2021-02-04 07:38:36.378097'),
(34, 'college', '0002_ctransfer_certificate1', '2021-02-04 10:50:45.979395'),
(35, 'user', '0006_college_details1_status', '2021-02-04 10:50:48.217523'),
(36, 'college', '0003_auto_20210204_1636', '2021-02-04 11:06:43.298151'),
(37, 'college', '0004_auto_20210204_1745', '2021-02-04 12:16:07.751344'),
(38, 'user', '0007_college_details1_university', '2021-02-04 12:16:09.605450'),
(39, 'office', '0001_initial', '2021-02-04 13:00:19.945040'),
(40, 'user', '0008_office_details', '2021-02-04 13:00:21.361121'),
(41, 'office', '0002_emppay_slip_salary_slip', '2021-02-04 14:16:25.357167'),
(42, 'office', '0003_exp_certificate_experience1', '2021-02-05 05:57:32.663686'),
(43, 'user', '0009_ration_card1', '2021-02-05 07:13:26.687162'),
(44, 'user', '0010_auto_20210205_1256', '2021-02-05 07:27:07.147089'),
(45, 'government', '0008_genration_card', '2021-02-05 08:11:06.835071'),
(46, 'government', '0009_auto_20210206_1522', '2021-02-06 09:54:16.130814'),
(47, 'government', '0010_auto_20210206_1524', '2021-02-06 09:54:19.656420'),
(48, 'government', '0011_auto_20210206_1929', '2021-02-06 14:00:08.130438'),
(49, 'college', '0005_auto_20210206_2012', '2021-02-06 14:42:49.314543'),
(50, 'office', '0004_auto_20210206_2012', '2021-02-06 14:42:53.136550'),
(51, 'school', '0005_auto_20210206_2012', '2021-02-06 14:42:59.407761'),
(52, 'school', '0006_school_birth1', '2021-02-08 10:32:31.457832'),
(53, 'government', '0012_auto_20210208_1852', '2021-02-08 13:22:18.967610');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7vtgagwerq0zr2g347q9dnvqcoaegypc', 'YjM2MWUzODhiYjQwNjkyY2E0NTkzOGEyYzQ0MzUyOWIwNzc3OTRkZjp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhYmlyYW1pIiwic2Nob29saWQiOjIsInNjaG9vbG5hbWUiOiJzaG4gc2Nob29sIiwic2VtYWlsIjoiY2hlbm5haXN1bmRheS5jczAxODhAZ21haWwuY29tIiwicGVyc29uX2lkMSI6OSwicGVyc29uX25hbWUxIjoiYWJpcmFtaSIsInN0dWRlbnRfbmFtZSI6ImFiaXJhbWkiLCJjbmFtZSI6ImJpcnRoX2NlcnRpZmljYXRlIiwiY29sbGVnZWlkIjoyLCJjb2xsZWdlbmFtZSI6ImluZm8gY29sbGVnZSIsImNlbWFpbCI6ImNoZW5uYWlzdW5kYXlyYW15YUBnbWFpbC5jb20iLCJvZmZpY2VpZCI6Miwib2ZmaWNlbmFtZSI6ImNoZW5uYWlzdW5kYXkiLCJvZmZpY2VlbWFpbCI6ImNoZW5uYWlzdW5kYXlyYW15YUBnbWFpbC5jb20iLCJ1bmlkIjozfQ==', '2021-02-23 11:00:31.862113'),
('fm9gyhvmm5c7zhvapz371dmwa5k77l3w', 'MzVkMDhhZjU5ZDBlMGNkOTUwYjg3Y2MxMzc5ZWNmM2JhZmQ0YzFlZTp7InVzZXJpZCI6MSwidXNlcm5hbWUiOiJyYW15YSIsInNjaG9vbGlkIjoxLCJzY2hvb2xuYW1lIjoiYWJjIHNjaG9vbCIsInNlbWFpbCI6ImNoZW5uYWlzdW5kYXlyYW15YUBnbWFpbC5jb20iLCJ1bmlkIjozfQ==', '2021-02-11 07:00:06.183919'),
('lu3lvc1csumvvam6lq53yz38au43msfq', 'NDI4MDI4ZmIyOWRhYmM2ZWQxNzU2NDQ1ZGRhOGMzNjZlOTM5ZjE3NDp7InNjaG9vbGlkIjoxLCJzY2hvb2xuYW1lIjoiYWJjIHNjaG9vbCIsInNlbWFpbCI6ImNoZW5uYWlzdW5kYXlyYW15YUBnbWFpbC5jb20iLCJ1c2VyaWQiOjEsInVzZXJuYW1lIjoicmFteWEiLCJjb2xsZWdlaWQiOjEsImNvbGxlZ2VuYW1lIjoic3JtIGNvbGxlZ2UiLCJjZW1haWwiOiJjaGVubmFpc3VuZGF5cmFteWFAZ21haWwuY29tIiwidW5pZCI6MSwib2ZmaWNlaWQiOjEsIm9mZmljZW5hbWUiOiJjc3MgcHJpdmF0ZSBsaW1pdGVkIiwib2ZmaWNlZW1haWwiOiJjaGVubmFpc3VuZGF5cmFteWFAZ21haWwuY29tIn0=', '2021-02-19 07:27:54.231782'),
('ycxoheq9sw3qp8dki6eawps5ps5bahax', 'NTRhOTY5N2NjN2I4MTgxM2JhMjQ2NGMyY2JjYjgyZDdiMjZiZjBiODp7InVzZXJpZCI6MSwidXNlcm5hbWUiOiJyYW15YSIsImZpbGVfcGF0aDEiOiIiLCJmcGF0aDEiOiIiLCJwZXJzb25faWQxIjoyLCJwZXJzb25fbmFtZTEiOiJiaHV2YW5hIn0=', '2021-02-20 14:01:03.137227'),
('zj57mt1c24t34x63zcauechj4sueajvy', 'YTFhMjAzMjQ3YWMwYjU3MzM4OGZiMzI4Mzc1NmQzOWM0MjcyNzI0Nzp7InVzZXJpZCI6MSwicGVyc29uX2lkMSI6MSwicGVyc29uX25hbWUxIjoicmFteWEiLCJ1c2VybmFtZSI6InJhbXlhIiwic2Nob29saWQiOjEsInNjaG9vbG5hbWUiOiJhYmMgc2Nob29sIiwic2VtYWlsIjoiY2hlbm5haXN1bmRheXJhbXlhQGdtYWlsLmNvbSIsInVuaWQiOjJ9', '2021-02-08 15:47:43.718269');

-- --------------------------------------------------------

--
-- Table structure for table `government_birth_certificate1`
--

CREATE TABLE IF NOT EXISTS `government_birth_certificate1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `birth_place` varchar(300) NOT NULL,
  `dateof_birth` varchar(300) NOT NULL,
  `father_name` varchar(300) NOT NULL,
  `mother_name` varchar(300) NOT NULL,
  `address` varchar(300) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `government_birth_certificate1`
--

INSERT INTO `government_birth_certificate1` (`id`, `uname`, `gender`, `birth_place`, `dateof_birth`, `father_name`, `mother_name`, `address`, `file_path`, `atimestamp`, `newhash1`, `phash1`, `certificate_file`) VALUES
(2, 'ramya', 'female', 'saravana hospital', '12-03-1992', 'ramachandran', 'mariammal', '11,north street,sattur', '/media/ramya_birthcertificate_FWSlQCd.pdf', '2021-01-23 13:42:51.699336', '52738002620d95ee0430ca78f5f20bb3f55a79f5701410cf927a1e8a0ccd54da', '0', '');

-- --------------------------------------------------------

--
-- Table structure for table `government_bkey_request1`
--

CREATE TABLE IF NOT EXISTS `government_bkey_request1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `requestor` varchar(300) NOT NULL,
  `person_name` varchar(200) NOT NULL,
  `email` varchar(300) NOT NULL,
  `status1` varchar(300) NOT NULL,
  `key1` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- Table structure for table `government_community_certificate1`
--

CREATE TABLE IF NOT EXISTS `government_community_certificate1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `dateof_birth` varchar(300) NOT NULL,
  `religion` varchar(300) NOT NULL,
  `caste` varchar(300) NOT NULL,
  `father_name` varchar(300) NOT NULL,
  `mother_name` varchar(300) NOT NULL,
  `address` varchar(300) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `government_community_certificate1`
--

INSERT INTO `government_community_certificate1` (`id`, `uname`, `full_name`, `dateof_birth`, `religion`, `caste`, `father_name`, `mother_name`, `address`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `certificate_file`) VALUES
(2, 'ramya', 'ramya ramachandran', '19-04-1992', 'hindu', 'yadava', 'ramachandran', 'mariammal', '11,north street,sattur', '/media/ramya_communitycertificate_nXjrl92.pdf', '0', '38c302ccfa4bfeed5e127019e16898ece2ef75290bae0625f6fdd56e0b3f7f06', '2021-02-06 19:30:39.953040', '');

-- --------------------------------------------------------

--
-- Table structure for table `government_genration_card`
--

CREATE TABLE IF NOT EXISTS `government_genration_card` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `dateof_birth` varchar(300) NOT NULL,
  `address` varchar(300) NOT NULL,
  `age` varchar(300) NOT NULL,
  `gender` varchar(300) NOT NULL,
  `member_count` varchar(300) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `government_genration_card`
--

INSERT INTO `government_genration_card` (`id`, `uname`, `full_name`, `dateof_birth`, `address`, `age`, `gender`, `member_count`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `certificate_file`) VALUES
(2, 'ramya', 'ramya ramachandran', '12-03-1992', '15th street ashok nagar', '27', 'female', '3', '/media/ramya_rationcard_oqef0Ll.pdf', '0', '7e9ae702627ca95204e3113c4a40d1213ae7c6322a24adf505152e373c9583b2', '2021-02-06 19:41:01.533896', 'ramya_rationcard_tDzozsN.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `government_gov_login`
--

CREATE TABLE IF NOT EXISTS `government_gov_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(300) NOT NULL,
  `password` varchar(200) NOT NULL,
  `key1` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `government_gov_login`
--

INSERT INTO `government_gov_login` (`id`, `username`, `password`, `key1`) VALUES
(1, 'admin', 'admin', '52842');

-- --------------------------------------------------------

--
-- Table structure for table `hospital_birth_details`
--

CREATE TABLE IF NOT EXISTS `hospital_birth_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `birth_place` varchar(300) NOT NULL,
  `dateof_birth` varchar(300) NOT NULL,
  `father_name` varchar(200) NOT NULL,
  `mother_name` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `hospital_birth_details`
--

INSERT INTO `hospital_birth_details` (`id`, `uname`, `gender`, `birth_place`, `dateof_birth`, `father_name`, `mother_name`, `address`) VALUES
(1, 'ramya', 'female', 'saravana hospital', '12-03-1992', 'ramachandran', 'mariammal', '11,north street,sattur');

-- --------------------------------------------------------

--
-- Table structure for table `office_emppay_slip`
--

CREATE TABLE IF NOT EXISTS `office_emppay_slip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(300) NOT NULL,
  `uname` varchar(300) NOT NULL,
  `designation` varchar(300) NOT NULL,
  `month` varchar(300) NOT NULL,
  `year` varchar(300) NOT NULL,
  `basic_da` varchar(300) NOT NULL,
  `hra` varchar(300) NOT NULL,
  `conveyance` varchar(300) NOT NULL,
  `pf` varchar(300) NOT NULL,
  `esi` varchar(300) NOT NULL,
  `net_salary` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

-- --------------------------------------------------------

--
-- Table structure for table `office_experience1`
--

CREATE TABLE IF NOT EXISTS `office_experience1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(300) NOT NULL,
  `uname` varchar(300) NOT NULL,
  `designation` varchar(300) NOT NULL,
  `exp_year` varchar(300) NOT NULL,
  `starting_year` varchar(300) NOT NULL,
  `finishing_year` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `office_experience1`
--

INSERT INTO `office_experience1` (`id`, `company_name`, `uname`, `designation`, `exp_year`, `starting_year`, `finishing_year`) VALUES
(1, 'css private limited', 'ramya', 'junior engineer', '1 Year', 'January,2019', 'January 2020');

-- --------------------------------------------------------

--
-- Table structure for table `office_exp_certificate`
--

CREATE TABLE IF NOT EXISTS `office_exp_certificate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(300) NOT NULL,
  `uname` varchar(300) NOT NULL,
  `designation` varchar(300) NOT NULL,
  `exp_year` varchar(300) NOT NULL,
  `starting_year` varchar(300) NOT NULL,
  `finishing_year` varchar(300) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `office_exp_certificate`
--

INSERT INTO `office_exp_certificate` (`id`, `company_name`, `uname`, `designation`, `exp_year`, `starting_year`, `finishing_year`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `certificate_file`) VALUES
(1, 'css private limited', 'ramya', 'junior engineer', '1 Year', 'January,2019', 'January 2020', '/media/ramya_experiencecertificate.pdf', '0', '1a9bc4b5bfd14987961f93aa79f85da4c933c61028cb4ba252884af3dd68cdbb', '2021-02-05 11:32:20.055124', '');

-- --------------------------------------------------------

--
-- Table structure for table `office_office_register1`
--

CREATE TABLE IF NOT EXISTS `office_office_register1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `officename` varchar(300) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- Table structure for table `office_salary_slip`
--

CREATE TABLE IF NOT EXISTS `office_salary_slip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(300) NOT NULL,
  `uname` varchar(300) NOT NULL,
  `designation` varchar(300) NOT NULL,
  `month` varchar(300) NOT NULL,
  `year` varchar(300) NOT NULL,
  `basic_da` varchar(300) NOT NULL,
  `hra` varchar(300) NOT NULL,
  `conveyance` varchar(300) NOT NULL,
  `pf` varchar(300) NOT NULL,
  `esi` varchar(300) NOT NULL,
  `net_salary` varchar(300) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `office_salary_slip`
--

INSERT INTO `office_salary_slip` (`id`, `company_name`, `uname`, `designation`, `month`, `year`, `basic_da`, `hra`, `conveyance`, `pf`, `esi`, `net_salary`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `certificate_file`) VALUES
(1, 'css private limited', 'ramya', 'junior engineer', '09', '2020', '5000', '2000', '3000', '600', '400', '12000', '/media/ramya_salaryslip.pdf', '0', '647e0db713329961343b3cdb784e5963dabf933c9108a05e27b1bba544c98a8a', '2021-02-05 10:51:36.703373', '');

-- --------------------------------------------------------

--
-- Table structure for table `school_attendance_certificate1`
--

CREATE TABLE IF NOT EXISTS `school_attendance_certificate1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `sch_name` varchar(200) NOT NULL,
  `grade` varchar(200) NOT NULL,
  `day` varchar(200) NOT NULL,
  `month` varchar(200) NOT NULL,
  `year` varchar(200) NOT NULL,
  `file_path` varchar(200) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `school_attendance_certificate1`
--

INSERT INTO `school_attendance_certificate1` (`id`, `uname`, `sch_name`, `grade`, `day`, `month`, `year`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `certificate_file`) VALUES
(1, 'ramya', 'abc school', 'S', '03', '04', '1996', '/media/ramya_attendancecertificate.pdf', '0', 'e11755d431bf71160c7a8b59ea3af71af97ff681b5ca25a19c67b33409143d75', '2021-02-03 16:53:33.873825', '');

-- --------------------------------------------------------

--
-- Table structure for table `school_attendance_details`
--

CREATE TABLE IF NOT EXISTS `school_attendance_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `sch_name` varchar(200) NOT NULL,
  `grade` varchar(200) NOT NULL,
  `day` varchar(200) NOT NULL,
  `month` varchar(200) NOT NULL,
  `year` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `school_attendance_details`
--

INSERT INTO `school_attendance_details` (`id`, `uname`, `sch_name`, `grade`, `day`, `month`, `year`) VALUES
(5, 'ramya', 'abc school', 'S', '03', '04', '1996');

-- --------------------------------------------------------

--
-- Table structure for table `school_school_birth1`
--

CREATE TABLE IF NOT EXISTS `school_school_birth1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `requestor` varchar(300) NOT NULL,
  `studnet_name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `certificate_name` varchar(200) NOT NULL,
  `status1` varchar(200) NOT NULL,
  `key1` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=28 ;

-- --------------------------------------------------------

--
-- Table structure for table `school_school_register1`
--

CREATE TABLE IF NOT EXISTS `school_school_register1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schoolname` varchar(300) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- Table structure for table `school_sports_certificate1`
--

CREATE TABLE IF NOT EXISTS `school_sports_certificate1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `sch_name` varchar(200) NOT NULL,
  `sports_name` varchar(200) NOT NULL,
  `winning_place` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `file_path` varchar(200) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `school_sports_certificate1`
--

INSERT INTO `school_sports_certificate1` (`id`, `uname`, `sch_name`, `sports_name`, `winning_place`, `date`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `certificate_file`) VALUES
(1, 'ramya', 'abc school', 'volly ball', 'first', '09-05-2020', '/media/ramya_sportscertificate_TS8BsR8.pdf', '0', '987dd3b888d969221e60dbcf24ba8d59144b9a0b388ccf45d9c8338f0a83b839', '2021-02-03 19:04:21.193666', '');

-- --------------------------------------------------------

--
-- Table structure for table `school_sports_details`
--

CREATE TABLE IF NOT EXISTS `school_sports_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `sch_name` varchar(200) NOT NULL,
  `sports_name` varchar(200) NOT NULL,
  `winning_place` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `school_sports_details`
--

INSERT INTO `school_sports_details` (`id`, `uname`, `sch_name`, `sports_name`, `winning_place`, `date`) VALUES
(1, 'ramya', 'abc school', 'volly ball', 'first', '09-05-2020');

-- --------------------------------------------------------

--
-- Table structure for table `school_transfer_certificate1`
--

CREATE TABLE IF NOT EXISTS `school_transfer_certificate1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(300) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `dateof_birth` varchar(300) NOT NULL,
  `religion` varchar(300) NOT NULL,
  `caste` varchar(300) NOT NULL,
  `father_name` varchar(300) NOT NULL,
  `mother_name` varchar(300) NOT NULL,
  `address` varchar(300) NOT NULL,
  `file_path` varchar(200) NOT NULL,
  `phash1` varchar(300) NOT NULL,
  `newhash1` varchar(300) NOT NULL,
  `atimestamp` varchar(300) NOT NULL,
  `sname` varchar(300) NOT NULL,
  `dateof_admission` varchar(300) NOT NULL,
  `last_studiedclass` varchar(300) NOT NULL,
  `reason_leaving` varchar(300) NOT NULL,
  `issue_date` varchar(300) NOT NULL,
  `general_conduct` varchar(300) NOT NULL,
  `certificate_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `school_transfer_certificate1`
--

INSERT INTO `school_transfer_certificate1` (`id`, `uname`, `full_name`, `dateof_birth`, `religion`, `caste`, `father_name`, `mother_name`, `address`, `file_path`, `phash1`, `newhash1`, `atimestamp`, `sname`, `dateof_admission`, `last_studiedclass`, `reason_leaving`, `issue_date`, `general_conduct`, `certificate_file`) VALUES
(2, 'ramya', 'ramya ramachandran', '12-03-1992', 'hindu', 'yadava', 'ramachandran', 'mariammal', '11,north street,sattur', '/media/ramya_transfercertificate.pdf', '0', '72a83356f142a3070d0ee3077d005207f166ba84c97a563b1b065f057465a0ff', '2021-01-28 10:59:57.956586', 'abc school', '21-09-1995', '12', 'next study', '2-02-2012', 'good', '');

-- --------------------------------------------------------

--
-- Table structure for table `user_college_details1`
--

CREATE TABLE IF NOT EXISTS `user_college_details1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(300) NOT NULL,
  `uname` varchar(200) NOT NULL,
  `dateof_birth` varchar(200) NOT NULL,
  `address` varchar(300) NOT NULL,
  `religion` varchar(200) NOT NULL,
  `caste` varchar(200) NOT NULL,
  `father_name` varchar(200) NOT NULL,
  `mother_name` varchar(200) NOT NULL,
  `dateof_admission` varchar(200) NOT NULL,
  `degree` varchar(200) NOT NULL,
  `joining_year` varchar(200) NOT NULL,
  `degree_finishingyear` varchar(200) NOT NULL,
  `college_name` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `university` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `user_college_details1`
--

INSERT INTO `user_college_details1` (`id`, `fullname`, `uname`, `dateof_birth`, `address`, `religion`, `caste`, `father_name`, `mother_name`, `dateof_admission`, `degree`, `joining_year`, `degree_finishingyear`, `college_name`, `status`, `university`) VALUES
(1, 'ramya ramachandran', 'ramya', '12-03-1992', '15th street ashok nagar', 'hindu', 'yadava', 'ramachandran', 'mariammal', '21-09-1995', 'BE CSE', '2012', '2017', 'srm college', 'course completed', 'Anna University');

-- --------------------------------------------------------

--
-- Table structure for table `user_community_details`
--

CREATE TABLE IF NOT EXISTS `user_community_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(300) NOT NULL,
  `uname` varchar(200) NOT NULL,
  `dateof_birth` varchar(200) NOT NULL,
  `address` varchar(300) NOT NULL,
  `religion` varchar(200) NOT NULL,
  `caste` varchar(200) NOT NULL,
  `father_name` varchar(200) NOT NULL,
  `mother_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `user_community_details`
--

INSERT INTO `user_community_details` (`id`, `fullname`, `uname`, `dateof_birth`, `address`, `religion`, `caste`, `father_name`, `mother_name`) VALUES
(1, 'ramya ramachandran', 'ramya', '19-04-1992', '11,north street,sattur', 'hindu', 'yadava', 'ramachandran', 'mariammal');

-- --------------------------------------------------------

--
-- Table structure for table `user_office_details`
--

CREATE TABLE IF NOT EXISTS `user_office_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(300) NOT NULL,
  `uname` varchar(200) NOT NULL,
  `company_name` varchar(200) NOT NULL,
  `designation` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `user_office_details`
--

INSERT INTO `user_office_details` (`id`, `fullname`, `uname`, `company_name`, `designation`) VALUES
(1, 'ramya ramachandran', 'ramya', 'css private limited', 'junior engineer');

-- --------------------------------------------------------

--
-- Table structure for table `user_ration_carddetails`
--

CREATE TABLE IF NOT EXISTS `user_ration_carddetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(300) NOT NULL,
  `uname` varchar(200) NOT NULL,
  `dateof_birth` varchar(200) NOT NULL,
  `address` varchar(300) NOT NULL,
  `age` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `member_count` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `user_ration_carddetails`
--

INSERT INTO `user_ration_carddetails` (`id`, `fullname`, `uname`, `dateof_birth`, `address`, `age`, `gender`, `member_count`) VALUES
(1, 'ramya ramachandran', 'ramya', '12-03-1992', '15th street ashok nagar', '27', 'female', '3');

-- --------------------------------------------------------

--
-- Table structure for table `user_school_details1`
--

CREATE TABLE IF NOT EXISTS `user_school_details1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(300) NOT NULL,
  `uname` varchar(200) NOT NULL,
  `dateof_birth` varchar(200) NOT NULL,
  `address` varchar(300) NOT NULL,
  `religion` varchar(200) NOT NULL,
  `caste` varchar(200) NOT NULL,
  `father_name` varchar(200) NOT NULL,
  `mother_name` varchar(200) NOT NULL,
  `dateof_admission` varchar(200) NOT NULL,
  `last_studiedclass` varchar(200) NOT NULL,
  `reason_leaving` varchar(200) NOT NULL,
  `issue_date` varchar(200) NOT NULL,
  `general_conduct` varchar(200) NOT NULL,
  `school_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `user_school_details1`
--

INSERT INTO `user_school_details1` (`id`, `fullname`, `uname`, `dateof_birth`, `address`, `religion`, `caste`, `father_name`, `mother_name`, `dateof_admission`, `last_studiedclass`, `reason_leaving`, `issue_date`, `general_conduct`, `school_name`) VALUES
(3, 'ramya ramachandran', 'ramya', '12-03-1992', '11,north street,sattur', 'hindu', 'yadava', 'ramachandran', 'mariammal', '21-09-1995', '12', 'next study', '2-02-2012', 'good', 'abc school');

-- --------------------------------------------------------

--
-- Table structure for table `user_user_reg1`
--

CREATE TABLE IF NOT EXISTS `user_user_reg1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(300) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `uname` varchar(300) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `user_user_reg1`
--

INSERT INTO `user_user_reg1` (`id`, `fullname`, `email`, `mobile`, `uname`, `password`) VALUES
(1, 'ramya', 'ramya@gmail.com', 9878676767, 'ramya', 'ramya');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
