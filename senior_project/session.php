<?php
// Turn off error reporting
error_reporting(0);

// Connect to database
$connect = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

// Starting Session
session_start();

// Storing Session
$user_check = $_SESSION['login_user'];

// SQL Query To fetch all information of user
$ses_sql = $connect-> query("SELECT * FROM users WHERE USERNAME='$user_check'");

$row = mysqli_fetch_assoc($ses_sql);

// Grab user's firstname
$login_session = $row['FIRST_NAME'];

// Condition for session
if(!isset($login_session)){
mysqli_close($connect); // Closing Connection

// redirect to index page is session was not set
header('Location: index.php'); // Redirecting To Home Page
}
?>
