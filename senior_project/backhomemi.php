<?php
// Turn off error reporting
error_reporting(0);

// Condition fot this code to run
if(isset($_POST['submit'])){

// Connect to databse
$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

// Set variables
$bnumber= $_POST['bnumber'];
$MiID = $_POST['option'];
$padvisor = $_POST['padvisor'];
$date = $_POST['date'];

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

// Run second query
$sql1 =  $myseli-> query ("SELECT minors.MiID FROM minors WHERE MiID = '$pminor'");


$result1 = mysqli_num_rows($sql1);

//If we hit a row, put all the data in an array
if ($result1 !=0){
while ($column1 = mysqli_fetch_assoc($sql1)) {

//Set varibale names for data from the database
$MiID = $column1['MiID'];

}

}

// Update database
$sqol = $myseli-> query ("UPDATE studentminor SET SID = '$SID', MiID = '$MiID', ADVISOR = '$padvisor', DAT = '$date' WHERE SID = '$SID'");

echo ("Congratulations!! Your change minor form has been sent.");
//Back to home page
header("Refresh: 5; url= home.php");

}

?>
