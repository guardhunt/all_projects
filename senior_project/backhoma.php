<?php
error_reporting(0);

if(isset($_POST['submit'])){

$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

$bnumber= $_POST['bnumber'];
$AIDD = $_POST['option'];

$sql =  $myseli-> query ("SELECT students.SID FROM students WHERE BNUMBER = '$bnumber'");

$result = mysqli_num_rows($sql);

//If we hit a row, put all the data in an array
if ($result !=0){
	while ($column = mysqli_fetch_assoc($sql)) {

	//Set varibale names for data from the database
	$SID = $column['SID'];
	}
	}

$sql1 =  $myseli-> query ("SELECT advisors.AID FROM advisors WHERE AID = '$AIDD'");


$result1 = mysqli_num_rows($sql1);

//If we hit a row, put all the data in an array
if ($result1 !=0){
	while ($column1 = mysqli_fetch_assoc($sql1)) {

	//Set varibale names for data from the database
	$AID = $column1['AID'];

	}

	}

$sqol = $myseli-> query ("UPDATE studentadvisor SET AID = '$AID' WHERE SID = '$SID'");

echo ("Congratulations!! Your change of adviros form has been sent.");

header("Refresh: 5; url= home.php");

}

?>
