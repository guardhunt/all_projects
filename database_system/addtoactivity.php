<?php $link = NEW MySQLi('localhost', 'development', 'leslie', 'development')
or die(mysql_connect_error("Connection Failed"));
?>

<!DOCTYPE html>


<?php
	//check if the user has come from the login or not//
	include('session.php');
	////////////////////////////////////////////////////
	?>


<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="https://www.higheredjobs.com/images/AccountImages/4698_1.jpg">

    <title>Faculty Tracking</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="bootstrap/css/jumbotron-narrow.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="bootstrap/js/ie-emulation-modes-warning.js"></script>

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
            <li role="presentation" class="active"><a href="homestyles.php">Home</a></li>
			<li role="presentation" class="active"><a href="logout.php">Log Out</a></li>
            <!--<li role="presentation"><a href="#">About</a></li>-->
            <!--<li role="presentation"><a href="#">Contact</a></li>-->
          </ul>
        </nav>
        <h3 class=""><strong>Faculty Development</strong></h3>
      </div>
<CENTER>
	<h1>Manage Faculty Attendance</h1>
      <div class="jumbotron">
        <p class="lead">
				<?php
		error_reporting(0);
//==============================================================================================================================================//
//
//==============================================================================================================================================//
		
		$aq = $link -> query ("SELECT * FROM Activities_t ORDER BY Date DESC");	
		?><!--end php and start the form for the drop down-->
		<form action = "manageattendence.php" method = "post">

		<h4>Choose an Activity to add or delete Faculty from:</h4> <select name="aid" required>
		<option value="" selected = "selected" disabled = "disabled">Choose the Attended Activity</option>
		<?php
		while($row = $aq -> fetch_array()){
			$dcon = DateTime::createFromFormat('Y-m-d', $row['Date']);
			$date = $dcon->format('m/d/y');
			echo "<option value='" . $row['ID'] . "'>" .$date.": ".$row['Title'] . "</option>";
		}
		?>
		</select><br /><br />
		<input class="btn-group btn-primary btn-sm" type = "Submit">
		</form>

      </div>
</CENTER>

      <footer class="footer">
        <p>&copy; Computer Science 330 Faculty Development Team Fall 2015</p>
      </footer>

    </div> <!-- /container -->


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>

