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
<li role="presentation" class="active"><a href="#cur">Home</a></li>
<li role="presentation"><a href="#student">Student</a></li>
<li role="presentation"><a href="logout.php">Log Out</a></li>
</ul>
</nav>
<h3 class="text-primary">Berea College Curriculum Plan Library</h3>
</div>

<div class="jumbotron" id="cur">
<h2>Change Curriculum</h2>
<p class="lead">Change of Advisor/Major/Minor/Concentration</p>
<select class="btn btn-lg btn-success" name="form" onchange="location = this.options[this.selectedIndex].value;">
  <option value="header-search.php">Select...</option>
  <option value="idnumb.php">Add Or Change Major</option>
  <option value="somepage.php">Add Or Change Minor</option>
  <option value="somepage.php">Change Advisor</option>
  <option value="somepage.php">Change Primary Advisor</option>
</select>
</div><br>

<div class="jumbotron" id="student">
<h2>View Student Record</h2>
<p class="lead">View Student  Change of Advisor/Major/Minor/Concentration</p>
<p><a class="btn btn-lg btn-success" href="idnumber.php" role="button">View Now</a></p>
</div>

<div class="row marketing">
<div class="col-lg-6">
<h4>Subheading</h4>
<p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

<h4>Subheading</h4>
<p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

<h4>Subheading</h4>
<p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
</div>

<div class="col-lg-6">
<h4>Subheading</h4>
<p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

<h4>Subheading</h4>
<p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

<h4>Subheading</h4>
<p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
</div>
</div>

<footer class="footer">
<p>Copyright&copy; Berea College 2015</p>
</footer>

</div> <!-- /container -->


<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="boot/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
