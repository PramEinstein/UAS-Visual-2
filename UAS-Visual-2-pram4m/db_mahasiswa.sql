-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 20, 2025 at 01:58 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_mahasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `npm` varchar(10) NOT NULL,
  `nama_lengkap` varchar(100) NOT NULL,
  `nama_panggilan` varchar(100) NOT NULL,
  `telepon` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `kelas` varchar(50) NOT NULL,
  `matakuliah` varchar(50) NOT NULL,
  `lokasi_kampus` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`npm`, `nama_lengkap`, `nama_panggilan`, `telepon`, `email`, `kelas`, `matakuliah`, `lokasi_kampus`) VALUES
('2310010050', 'Jung Ahyeon', 'Ahyeon', '087788265156', 'ahyeon@gmail.com', '4C Reguler', 'Filsafat', 'Jl. Adyaksha Banjarmasin'),
('2310010100', 'Nina Marcela', 'Cela', '087788265153', 'nina_mar26@gmail.cpm', '2M Reguler', 'Bahasa', 'Jl. Adyaksha Banjarmasin'),
('2310010255', 'Max Verstappen', 'Max', '087788265155', 'max01@gmail.com', '6C Reguler', 'Web', 'Jl. Adyaksha Banjarmasin'),
('2310010447', 'Zanuar Pramudya Putra Utama Radriansyah', 'Pram Einstein', '087788265152', 'zanuar.ppur@gmail.com', '4M Reguler', 'Pemrograman Visual 2', 'Jl. Adyaksha Banjarmasin'),
('2310010500', 'Erling Haaland', 'Haaland', '087788265154', 'erling09@gmail.com', '6A Reguler', 'PBO', 'Jl. Adyaksha Banjarmasin');

-- --------------------------------------------------------

--
-- Table structure for table `nilai`
--

CREATE TABLE `nilai` (
  `id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `id_mahasiswa` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nilai_harian` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nilai_tugas` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nilai_uts` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nilai_uas` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `nilai`
--

INSERT INTO `nilai` (`id`, `id_mahasiswa`, `nilai_harian`, `nilai_tugas`, `nilai_uts`, `nilai_uas`) VALUES
('001', '2310010447', '100', '100', '100', '100'),
('002', '2310010440', '90', '90', '90', '90'),
('003', '2310010441', '85', '90', '80', '100'),
('004', '2310010100', '90', '90', '95', '80'),
('005', '2310010777', '80', '80', '75', '90'),
('006', '2310010325', '100', '75', '75', '90');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`npm`);

--
-- Indexes for table `nilai`
--
ALTER TABLE `nilai`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
