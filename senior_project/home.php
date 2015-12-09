<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
<meta name="description" content="">
<meta name="author" content="">
<link rel="icon" type="image/jpg" href="img/berea_logo.jpg" class="img-circle">

<!-- PHP session -->
<?php include('session.php');?>
<!-- display session user -->
<div class="log"><b>Welcome  <?php echo $login_session; ?>. You're logged in.</b></div>

<title>Berea College || Change Of Academic Discipline</title>

<!-- Bootstrap core CSS -->
<link href="boot/css/bootstrap.min.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="boot/css/jumbotron-narrow.css" rel="stylesheet">
<link href="boot/css/bootstrap.css" rel="stylesheet">

<!--Not being used-->
<script src="boot/js/ie-emulation-modes-warning.js"></script>

</head>

<body>

<div class="container">
<div class="header clearfix">
<nav>
  <!-- nav bar buttons -->
<ul class="nav nav-pills pull-right">
<li role="presentation" class="active"><a href="home.php">Home</a></li>
<li role="presentation" class="active"><a href="#student">Student</a></li>
<li role="presentation" class="active"><a href="logout.php">Log Out</a></li>
</ul>
</nav>
<h3 class="text-primary">Berea College Change Of Academic Discipline</h3>
</div>

<div class="jumbotron" id="cur">
<h2>Change Curriculum</h2>
<p class="lead">Change of Advisor/Major/Minor/Concentration</p>

<!-- Options to select from -->
<select class="btn btn-primary" name="form" onchange="location = this.options[this.selectedIndex].value;">
<option value="home.php">Select...</option>
<option value="major.php">Add Or Change Major</option>
<option value="minor.php">Add Or Change Minor</option>
<option value="advisor.php">Add Or Change Advisor</option>
</select>
</div><br>

<div class="jumbotron" id="student">
<h2>View Student Record</h2>
<p class="lead">View Student  Change of Advisor/Major/Minor/Concentration</p>
<p><a class="btn btn-primary" href="idnumber.php" role="button">View Now</a></p>
</div>

<footer class="footer">
<p>Copyright&copy; Berea College 2015</p>
</footer>

</div> <!-- /container -->


<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="boot/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
