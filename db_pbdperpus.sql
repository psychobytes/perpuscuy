-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 11, 2023 at 02:53 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_pbdperpus`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(2) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `alamat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nama`, `nik`, `alamat`) VALUES
(1, 'admin', '123', 'Arasaka');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `id_buku` int(7) NOT NULL,
  `judul` varchar(30) NOT NULL,
  `kategori` varchar(15) NOT NULL,
  `stok` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`id_buku`, `judul`, `kategori`, `stok`) VALUES
(1, '1001 cara menjadi anime', 'tutorial ', 2),
(3, 'cara mendapat pacar anime', 'kehidupan', 2),
(5, 'aku ingin jadi anime', 'kejiwaan', 2);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `id_member` int(5) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `profesi` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`id_member`, `nama`, `nik`, `alamat`, `profesi`) VALUES
(123, 'raja meksiko', '1231231', 'meksiko', 'bandar kokain'),
(132, 'udin vatok the snake', '4311123', 'vatok', 'kang vatok pro');

-- --------------------------------------------------------

--
-- Table structure for table `pegawai`
--

CREATE TABLE `pegawai` (
  `id_pegawai` int(2) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `jabatan` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pegawai`
--

INSERT INTO `pegawai` (`id_pegawai`, `nama`, `nik`, `alamat`, `jabatan`) VALUES
(1, 'Dante', '123231', 'Redgrave City', 'Son of Sparda'),
(2, 'Vergil', '123456', 'Redgrave City', 'Son of Sparda');

-- --------------------------------------------------------

--
-- Table structure for table `pengunjung`
--

CREATE TABLE `pengunjung` (
  `id_pengunjung` int(6) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `tanggal` date NOT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengunjung`
--

INSERT INTO `pengunjung` (`id_pengunjung`, `nama`, `alamat`, `tanggal`, `status`) VALUES
(1, 'Kim Jong Un', 'Korea Utara', '0000-00-00', '666'),
(2, 'Adolf Hitler', 'Jerman', '0000-00-00', '69'),
(3, 'Stalin', 'USSR', '0000-00-00', '1337'),
(4, 'Dominic Toretto', 'Family', '0000-00-00', '7'),
(5, 'Dominic Toretto', 'Family', '0000-00-00', '7'),
(6, 'Vergil', 'Motivated', '0000-00-00', '123'),
(7, 'Vergil', 'Motivated', '0000-00-00', '123'),
(8, 'Vergil', 'Motivated', '0000-00-00', '123'),
(9, 'Vergil', 'Motivated', '0000-00-00', '123'),
(10, 'Dante', 'Redgrave City', '0000-00-00', '666'),
(11, 'Dante', 'Redgrave City', '0000-00-00', '123'),
(12, 'Dante', 'Redgrave City', '0000-00-00', '123'),
(13, 'Dante', 'Redgrave City', '0000-00-00', '123'),
(14, 'Dante', 'Redgrave City', '0000-00-00', '123'),
(15, 'Adolf Hitler', '111', '0000-00-00', '222'),
(16, 'Adolf Hitler', 'Jalan Basuki Rahmat, Gunung Alam, Arga Makmur', '0000-00-00', '222'),
(17, 'Paul Walker', 'Heaven', '2023-06-30', '123'),
(18, 'Kim Jong Un', 'Korea Utara', '2023-06-27', '123'),
(19, 'Adolf Hitler', 'Jerman', '2023-06-27', '123'),
(20, 'Adolf Hitler', 'Jerman', '2023-06-27', '123'),
(21, 'Paul Walker', 'Heaven', '2023-06-27', '123'),
(22, 'Adolf Hitler', 'German', '2023-06-29', '0'),
(23, 'Adolf Hitler', 'x', '2023-06-27', '0'),
(24, 'Kim Jong Un', 'x', '2023-06-30', '0'),
(25, 'Kim Jong Un', 'aaa', '2023-06-28', 'Bukan Memb'),
(26, 'jono', 'xx', '2023-06-24', 'Member'),
(27, 'Hirohito', 'Japan', '2023-06-29', 'Member'),
(28, 'Adolf Hitler', 'x', '2023-06-28', 'Bukan Memb'),
(29, 'Sigma', 'mars', '2023-07-10', 'Bukan Memb'),
(30, 'Sugma', 'planet disnut', '2023-07-10', 'Bukan Memb'),
(31, 'alvin', 'jakarta', '2023-07-11', 'Bukan Memb');

-- --------------------------------------------------------

--
-- Table structure for table `pinjam`
--

CREATE TABLE `pinjam` (
  `id_pinjam` int(7) NOT NULL,
  `member` int(5) NOT NULL,
  `buku` int(7) NOT NULL,
  `tanggal_pinjam` date NOT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pinjam`
--

INSERT INTO `pinjam` (`id_pinjam`, `member`, `buku`, `tanggal_pinjam`, `status`) VALUES
(2, 123, 3, '2023-06-26', NULL),
(3, 123, 3, '2023-06-27', NULL),
(5, 132, 3, '2023-06-26', NULL),
(6, 132, 3, '2023-06-26', 'Kembalikan'),
(7, 123, 3, '2023-06-26', 'pinjam'),
(8, 123, 3, '2023-06-26', 'pinjam'),
(9, 123, 3, '2023-06-26', 'pinjam'),
(10, 123, 3, '2023-06-26', 'pinjam'),
(11, 123, 3, '2023-06-26', 'pinjam'),
(12, 123, 3, '2023-06-26', 'pinjam'),
(13, 123, 3, '2023-06-26', 'pinjam'),
(14, 123, 3, '2023-06-26', 'pinjam'),
(15, 123, 3, '2023-06-27', 'pinjam'),
(16, 123, 3, '2023-06-27', 'kembalikan'),
(17, 123, 3, '2023-06-28', 'kembalikan'),
(18, 123, 1, '2023-06-27', 'pinjam'),
(19, 123, 3, '2023-06-27', 'pinjam'),
(20, 123, 3, '2023-06-27', 'pinjam'),
(21, 123, 3, '2023-06-27', 'kembalikan'),
(22, 123, 3, '2023-06-27', 'kembalikan'),
(23, 123, 5, '2023-06-29', 'kembalikan'),
(24, 123, 3, '2023-06-28', 'kembalikan'),
(25, 123, 3, '2023-06-28', 'kembalikan'),
(26, 123, 3, '2023-06-21', 'pinjam'),
(27, 123, 3, '2023-06-27', 'kembalikan'),
(28, 123, 3, '2023-06-27', 'pinjam'),
(29, 123, 3, '2023-06-27', 'kembalikan'),
(30, 123, 3, '2023-06-28', 'kembalikan'),
(31, 123, 3, '2023-06-27', 'pinjam'),
(32, 123, 3, '2023-06-27', 'kembalikan'),
(33, 123, 3, '2023-06-28', 'pinjam'),
(34, 123, 3, '2023-06-27', 'pinjam'),
(35, 123, 3, '2023-06-14', 'kembalikan'),
(36, 123, 3, '2023-06-14', 'pinjam'),
(37, 123, 3, '2023-06-27', 'pinjam'),
(38, 123, 3, '2023-06-27', 'pinjam'),
(39, 123, 3, '2023-06-27', 'kembalikan'),
(40, 123, 3, '2023-06-28', 'pinjam'),
(41, 123, 3, '2023-06-28', 'pinjam'),
(42, 123, 3, '2023-06-30', 'kembalikan'),
(43, 123, 3, '2023-06-29', 'kembalikan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id_member`);

--
-- Indexes for table `pegawai`
--
ALTER TABLE `pegawai`
  ADD PRIMARY KEY (`id_pegawai`);

--
-- Indexes for table `pengunjung`
--
ALTER TABLE `pengunjung`
  ADD PRIMARY KEY (`id_pengunjung`);

--
-- Indexes for table `pinjam`
--
ALTER TABLE `pinjam`
  ADD PRIMARY KEY (`id_pinjam`),
  ADD KEY `member` (`member`),
  ADD KEY `buku` (`buku`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pengunjung`
--
ALTER TABLE `pengunjung`
  MODIFY `id_pengunjung` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `pinjam`
--
ALTER TABLE `pinjam`
  MODIFY `id_pinjam` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pinjam`
--
ALTER TABLE `pinjam`
  ADD CONSTRAINT `pinjam_ibfk_1` FOREIGN KEY (`member`) REFERENCES `member` (`id_member`),
  ADD CONSTRAINT `pinjam_ibfk_2` FOREIGN KEY (`buku`) REFERENCES `buku` (`id_buku`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
