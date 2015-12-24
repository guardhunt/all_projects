<?php

error_reporting(0);

// Connect to database
$connect = NEW MySQLi('localhost', 'development', 'leslie', 'development') or die(mysql_error('Could not establish connection'));

// Starting Session
session_start();

// Storing Session
$user_check = $_SESSION['login_user'];

// SQL Query To Fetch Complete Information Of User
$ses_sql = $connect-> query("SELECT * FROM USERS WHERE USERNAME='$user_check'");

$row = mysqli_fetch_assoc($ses_sql);

 // Grab user's firstname
$login_session = $row['FIRSTNAME'];

if(!isset($login_session)){
		mysqli_close($connect); // Closing Connection
		
		header('Location: index.php'); // Redirecting To Home Page
		}
?>
