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

<!-- Display user in current session -->
<div class="log"><b>Welcome  <?php echo $login_session; ?>. You're logged in.</b></div>

<title>Berea College || Change Of Academic Discipline</title>

<!-- Bootstrap core CSS -->
<link href="boot/css/bootstrap.min.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="boot/css/jumbotron-narrow.css" rel="stylesheet">
<link href="boot/css/bootstrap.css" rel="stylesheet">
<link href="boot/css/tables.css" rel="stylesheet">

<!--Not being used-->
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
<h2>Change Major Form -- Please Fill Out All Sections</h2>
<?php
// Set variable for bnumber that was carried over multiple pages
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

// Table
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

// Run second query
$sql =  $myseli-> query ("SELECT majors.CHAIRMAN FROM majors");

// Run third query
$sqli =  $myseli-> query ("SELECT * FROM majors");

?>
<br><br>
<!-- Form -->
<form action= "backhome.php" method="post">
New Major:
<select name="option">
<?php while ($res = $sqli->fetch_array()){

echo "<option  value=".$res['MID'].">" .$res['MDESCRIPTION']." </option>";
}
?>

</select>

<br><br><br>
Primary Advisor:<input  class="tb5" type="text" name="padvisor" required>
<br><br><br>
Date:<input class="tb5" type="text" name="date" required>
<br><br><br>
<input class="tb5" type="hidden" name="bnumber" value="<?php echo $_POST['bnumber'];?>" required>
<input type="submit" value="SUBMIT" name="submit">
</form>

</div>
<footer class="footer">
<p>Copyright&copy; Berea College 2015</p>
</footer>

</div> <!-- /container -->


<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="boot/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
