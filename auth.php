<?php

//Turn off error reorting for sucurity reason
error_reporting(0);

//Connect to the database
$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

//if user presses "submit", do the following
if(isset($_POST['submit'])){

	//set variable names for the value of email and password from the form
	$email= $_POST['email'];
	$password= $_POST['password'];

	//Run query and compare to varibales
	$sql =  $myseli-> query ("SELECT * FROM users WHERE EMAIL= '$email' and PASSWORD= '$password'");

	//Check to make sure we hit a row
	$result = mysqli_num_rows($sql);

//If we hit a row, put all the data in an array
if ($result !=0){
	while ($column = mysqli_fetch_assoc($sql)) {

	//Set varibale names for data from the database
	$dbemail = $column['EMAIL'];
	$dbpassword = $column['PASSWORD'];
	}
	}

//Compare these varibales to what the user entered
if ($email === $dbemail and $password === $dbpassword) {

	//If they're the same, redirect to page and start a session
	echo ("You have successfully logged in");
	session_start();
	//$_SESSION['sess_user'] = $email;
	header("location: testlog.php");

	//Else, echo this
	}else{
	echo ("Invalid username or password");

	}
}
?>


