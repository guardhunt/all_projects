<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
<meta name="description" content="">
<meta name="author" content="">
<link rel="icon" type="image/jpg" href="img/berea_logo.jpg">

<!-- PHP session-->
<?php include('session.php');?>

<!-- Display the user of the session -->
<div class="log"><b>Welcome  <?php echo $login_session; ?>. You're logged in.</b></div>

<title>Berea College || Change Of Academic Discipline</title>

<!-- Bootstrap core CSS -->
<link href="boot/css/bootstrap.min.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="boot/css/jumbotron-narrow.css" rel="stylesheet">
<link href="boot/css/bootstrap.css" rel="stylesheet">
<link href="boot/css/tables.css" rel="stylesheet">


<!-- Not being used -->
<script src="boot/js/ie-emulation-modes-warning.js"></script>


</head>

<body>

<div class="container">
<div class="header clearfix">
<nav>
	<!-- Nav bar buttons -->
<ul class="nav nav-pills pull-right">
<li role="presentation" class="active"><a href="home.php">Home</a></li>
<li role="presentation" class="active"><a href="home.php">Student</a></li>
<li role="presentation" class="active"><a href="logout.php">Log Out</a></li>
</ul>
</nav>
<h3 class="text-primary">Berea College Change Of Academic Discipline</h3>
</div>

<div class="jumbotron" id="cur">
<h2>Change Of Advisor Form -- Please Fill Out All Sections</h2>
<?php
// Get bnumber from input
$bnumber = $_POST['bnumber'];

// Turn off error reporting
error_reporting(0);

//Connect to database
$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));


//Run query
$result = $myseli-> query("SELECT * FROM advisors, studentadvisor, studentminor, studentmajor,
				majors, minors, students  WHERE BNUMBER='$bnumber'
				AND studentmajor.SID = students.SID
				AND studentmajor.MID = majors.MID
				AND studentminor.SID = students.SID
				AND studentminor.MiID = minors.MiID
				AND studentadvisor.SID = students.SID
				AND studentadvisor.AID = advisors.AID") or die ("Could not connect to database");

// Create table

if ($result-> num_rows != 0){
echo "<table border=5 class= tables>
<tr>
<td>Firstname</td>
<td>Lastname</td>
<td>Student ID Number</td>
<td>Present Major</td>
<td>Present Minor</td>
<td>Advisor</td>
</tr>";
while($row = $result-> fetch_assoc()){

$name = $row['FIRSTNAME'];
$lname = $row['LASTNAME'];
$dbnumber = $row['BNUMBER'];
$major = $row['MDESCRIPTION'];
$minor = $row['MiDESCRIPTION'];
$adv = $row['NAME'];

// Display query result in table
echo
"<tr>
<td>$name</td>
<td>$lname</td>
<td>$dbnumber</td>
<td>$major</td>
<td>$minor</td>
<td>$adv</td>
</tr>";



}

echo"</table>";

}

// Drop down query
$sql =  $myseli-> query ("SELECT * FROM advisors");


?>

<!-- Form to get info -->

<br><br>
<form action= "backhoma.php" method="post">
New Advisor:
<select name="option">
<?php while ($res = $sql->fetch_array()){

echo "<option  value=".$res['AID'].">" .$res['NAME']." </option>";
}
?>

</select>
<br><br><br>

<!-- Carry Bnumber over multiple pages -->
<input class="tb5" type="hidden" name="bnumber" value="<?php echo $_POST['bnumber'];?>" required>

<input type="submit" value="SUBMIT" name="submit">
</form>

</div>
<footer class="footer">
<p>Copyright&copy; Berea College 2015</p>
</footer>

</div> <!-- /container -->


<!-- not being used -->
<script src="boot/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
