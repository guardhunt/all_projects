<?php
session_start();
error_reporting(0);

if (isset($_POST['submit'])) {

		$username=$_POST['username'];
		$password=$_POST['password'];

		$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

		$sql =  $myseli-> query ("SELECT * FROM users WHERE USERNAME= '$username' AND PASSWORD= '$password'");

		$result = mysqli_num_rows($sql);

		//If we hit a row, put all the data in an array
		if ($result !=0){
			while ($column = mysqli_fetch_assoc($sql)) {

					//Set varibale names for data from the database
					$dbuser = $column['USERNAME'];
					$dbpassword = $column['PASSWORD'];
				}
			}

		//Compare these varibales to what the user entered
		if ($username === $dbuser and $password === $dbpassword) {

			$_SESSION['login_user']=$username;

			header("location: home.php");

			} else {
				$error = ("Username or Password is invalid");

				header("location: index.php");
				}



}

?>
