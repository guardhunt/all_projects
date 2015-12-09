<?php
// Turn off error reporting
error_reporting(0);

// Condition for action
if(isset($_POST['submit'])){

// Connect to database
$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

// Reset variable for bnumber
$bnumber= $_POST['bnumber'];

// Set variable for the option chosen form the previous page
$AIDD = $_POST['option'];

// Run query
$sql =  $myseli-> query ("SELECT students.SID FROM students WHERE BNUMBER = '$bnumber'");

$result = mysqli_num_rows($sql);

//If we hit a row, put all the data in an array
if ($result !=0){
while ($column = mysqli_fetch_assoc($sql)) {

//Set varibale names for data from the database
$SID = $column['SID'];
}
}

// Run query
$sql1 =  $myseli-> query ("SELECT advisors.AID FROM advisors WHERE AID = '$AIDD'");


$result1 = mysqli_num_rows($sql1);

//If we hit a row, put all the data in an array
if ($result1 !=0){
while ($column1 = mysqli_fetch_assoc($sql1)) {

//Set varibale names for data from the database
$AID = $column1['AID'];

}

}

// update table
$sqol = $myseli-> query ("UPDATE studentadvisor SET AID = '$AID' WHERE SID = '$SID'");

echo ("Congratulations!! Your change of adviros form has been sent.");
// Back to home page
header("Refresh: 5; url= home.php");

}

?>
