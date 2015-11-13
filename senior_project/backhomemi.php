<?php
error_reporting(0);

if(isset($_POST['submit'])){

$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

$bnumber= $_POST['bnumber'];
$pminor = $_POST['option'];
$padvisor = $_POST['padvisor'];
$date = $_POST['date'];

$sql =  $myseli-> query ("SELECT students.SID FROM students WHERE BNUMBER = '$bnumber'");

$result = mysqli_num_rows($sql);

//If we hit a row, put all the data in an array
if ($result !=0){
	while ($column = mysqli_fetch_assoc($sql)) {

	//Set varibale names for data from the database
	$SID = $column['SID'];
	}
	}

$sql1 =  $myseli-> query ("SELECT minors.MiID FROM minors WHERE MiID = '$pminor'");


$result1 = mysqli_num_rows($sql1);

//If we hit a row, put all the data in an array
if ($result1 !=0){
	while ($column1 = mysqli_fetch_assoc($sql1)) {

	//Set varibale names for data from the database
	$MiID = $column1['MiID'];

	}

	}

$sqol = $myseli-> query ("INSERT INTO studentminor (SID, MiID, ADVISOR, DAT) VALUES ('$SID', '$MiID', '$padvisor', '$date')");

echo ("Congratulations!! Your change minor form has been sent");

header("Refresh: 5; url= home.php");

}

?>
