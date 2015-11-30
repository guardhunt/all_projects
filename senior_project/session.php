<?php

error_reporting(0);

$connect = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

// Starting Session
session_start();

// Storing Session
$user_check = $_SESSION['login_user'];

// SQL Query To Fetch Complete Information Of User
$ses_sql = $connect-> query("SELECT * FROM users WHERE USERNAME='$user_check'");

$row = mysqli_fetch_assoc($ses_sql);

$login_session = $row['FIRST_NAME'];

if(!isset($login_session)){
		mysqli_close($connect); // Closing Connection

		header('Location: index.php'); // Redirecting To Home Page
		}
?>
