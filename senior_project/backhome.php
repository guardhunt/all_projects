<?php
// Turn off error reporting
error_reporting(0);

// Condition for action
if(isset($_POST['submit'])){

// Connect to database
$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

// Set variables
$bnumber= $_POST['bnumber'];
$pmajor = $_POST['option'];
$padvisor = $_POST['padvisor'];
$date = $_POST['date'];

// Run query
$sql =  $myseli-> query ("SELECT * FROM students WHERE BNUMBER = '$bnumber'");

$result = mysqli_num_rows($sql);

//If we hit a row, put all the data in an array
if ($result !=0){
while ($column = mysqli_fetch_assoc($sql)) {

//Set varibale names for data from the database
$SID = $column['SID'];
}
}

// Run query
$sql1 =  $myseli-> query ("SELECT majors.MID FROM majors WHERE MID = '$pmajor'");


$result1 = mysqli_num_rows($sql1);

//If we hit a row, put all the data in an array
if ($result1 !=0){
while ($column1 = mysqli_fetch_assoc($sql1)) {

//Set varibale names for data from the database
$MID = $column1['MID'];

}

}

// Update table
$sqol = $myseli-> query ("UPDATE studentmajor SET SID = '$SID', MID = '$MID', ADVISOR = '$padvisor', DAT = '$date' WHERE SID = '$SID'");

echo ("Congratulations!! Your change major form has been sent.");

// Back to home page
header("Refresh: 5; url= home.php");

}

?>
