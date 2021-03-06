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

<!-- PHP sessions -->
<?php include('session.php');?>

<!-- Display the user of the session -->
<div class="log"><b>Welcome  <?php echo $login_session; ?>. You're logged in.</b></div>

<title>Berea College || Change Of Academic Discipline</title>

<!-- Bootstrap core CSS -->
<link href="boot/css/bootstrap.min.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="boot/css/jumbotron-narrow.css" rel="stylesheet">
<link href="boot/css/bootstrap.css" rel="stylesheet">

<!--not being used. It just comes with the template-->
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

<!-- Template class -->

<div class="jumbotron" id="cur">
<h2>Change Advisor Application</h2>
<form action="advisorstu.php" method="post">
Student B number
<br><br>
<input  type="text" name="bnumber" required>
<br><br><br>
<input type="submit" value="Continue" name="submit">

</form>
</div><br>

<footer class="footer">
<p>Copyright&copy; Berea College 2015</p>
</footer>

</div> <!-- /container -->

<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="boot/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
