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

<!-- PHP -->
<?php include('session.php');?>
<div class="log"><b>Welcome  <?php echo $login_session; ?>. You're logged in.</b></div>

<title>Berea College || Curriculum Library</title>

<!-- Bootstrap core CSS -->
<link href="boot/css/bootstrap.min.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="boot/css/jumbotron-narrow.css" rel="stylesheet">
<link href="boot/css/bootstrap.css" rel="stylesheet">

<!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
<!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
<script src="boot/js/ie-emulation-modes-warning.js"></script>

<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
</head>

<body>

<div class="container">
<div class="header clearfix">
<nav>
<ul class="nav nav-pills pull-right">
<li role="presentation" class="active"><a href="home.php">Home</a></li>
<li role="presentation"><a href="idnumber.php">Student</a></li>
<li role="presentation"><a href="logout.php">Log Out</a></li>
</ul>
</nav>
<h3 class="text-primary">Berea College Curriculum Plan Library</h3>
</div>

<div class="jumbotron" id="cur">
<h2>Change Minor Form -- Please Fill Out All Sections</h2>
<?php
$bnumber = $_POST['bnumber'];
error_reporting(0);
//Connect to database
$myseli = NEW MySQLi('localhost', 'root', '', 'test') or die(mysql_error('Could not establish connection'));

//Run query
$result = $myseli-> query("SELECT * FROM students WHERE BNUMBER='$bnumber'") or die ("Could not connect to database");

if ($result-> num_rows != 0){
echo "<table border=5>
<tr>
<th>Firstname</th>
<th>Lastname</th>
<th>Student ID Number</th>
<th>Present Major</th>
</tr>";
while($row = $result-> fetch_assoc()){

$name = $row['FIRSTNAME'];
$lname = $row['LASTNAME'];
$dbnumber = $row['BNUMBER'];
$major = $row['MID'];

echo
	"<tr>
			<td>$name</td>
			<td>$lname</td>
			<td>$dbnumber</td>
			<td>$major</td>
		  </tr>";



}

echo"</table>";

}

$sql =  $myseli-> query ("SELECT minors.CHAIRMAN FROM minors");

$sqli =  $myseli-> query ("SELECT * FROM minors");

?>
<br><br>
<form action= "backhome.php" method="post">
New Minor:
<select name="option">
		<?php while ($res = $sqli->fetch_array()){

			echo "<option  value=".$res['MiID'].">" .$res['DESCRIPTION']." </option>";
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
