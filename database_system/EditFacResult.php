<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="https://www.higheredjobs.com/images/AccountImages/4698_1.jpg">

	<?php
	//check if the user has come from the login or not//
	include('session.php');
	////////////////////////////////////////////////////
	?>
	
    <title>Result</title>

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
	<h1>Home Directory</h1>
      <div class="jumbotron">
        <p class="lead">
<?php $link = NEW MySQLi('localhost', 'development', 'leslie', 'development')
			or die(mysql_connect_error("Connection Failed"));
	
		session_start();
		$ID = $_SESSION['EditFacID'];
		
		if(($_POST['bnumber'] == NULL) and ($_POST['title'] == NULL) and ($_POST['firstname'] == NULL) and 
		($_POST['mi'] == NULL) and ($_POST['lastname'] == NULL) and ($_POST['email'] == NULL) and 
		($_POST['cpo'] == NULL) and (!isset($_POST['program'])) and (!isset($_POST['ethnicity'])) and 
		(!isset($_POST['gender'])) and (!isset($_POST['status']))){
			echo "No information entered. Nothing was changed.";
		}
		
		else{
			if($_POST['bnumber'] != NULL){
				$upd = $link->query("UPDATE faculty SET bnumber  = '".$_POST['bnumber']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Bnumber did not update <br />";
				}
				else{
					echo "Bnumber successfully updated! <br />";
				}
			}
			
			if($_POST['title'] != NULL){
				$upd = $link->query("UPDATE faculty SET title = '".$_POST['title']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Title did not update <br />";
				}
				else{
					echo "Title successfully updated! <br />";
				}
			}
			
			if($_POST['firstname'] != NULL){
				$upd = $link->query("UPDATE faculty SET firstname = '".$_POST['firstname']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: First Name did not update <br />";
				}
				else{
					echo "First Name successfully updated! <br />";
				}
			}
			
			if($_POST['mi'] != NULL){
				$upd = $link->query("UPDATE faculty SET mi = '".$_POST['mi']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Middle initial did not update <br />";
				}
				else{
					echo "Middle initial successfully updated! <br />";
				}
			}
			
			if($_POST['lastname'] != NULL){
				$upd = $link->query("UPDATE faculty SET lastname = '".$_POST['lastname']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Last Name did not update <br />";
				}
				else{
					echo "Last Name successfully updated! <br />";
				}
			}
			
			if($_POST['email'] != NULL){
				$upd = $link->query("UPDATE faculty SET email = '".$_POST['email']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Email did not update <br />";
				}
				else{
					echo "Email successfully updated! <br />";
				}
			}
			
			if($_POST['cpo'] != NULL){
				$upd = $link->query("UPDATE faculty SET cpo = '".$_POST['cpo']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: CPO did not update <br />";
				}
				else{
					echo "CPO successfully updated! <br />";
				}
			}
			
			if(isset($_POST['program'])){
				$upd = $link->query("UPDATE faculty SET program = '".$_POST['program']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Program did not update <br />";
				}
				else{
					echo "Program successfully updated! <br />";
				}
			}
			
			if(isset($_POST['ethnicity'])){
				$upd = $link->query("UPDATE faculty SET ethnicity = '".$_POST['ethnicity']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Ethnicity did not update <br />";
				}
				else{
					echo "Ethnicity successfully updated! <br />";
				}
			}
			
			if(isset($_POST['gender'])){
				$upd = $link->query("UPDATE faculty SET gender = '".$_POST['gender']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Gender did not update <br />";
				}
				else{
					echo "Gender successfully updated! <br />";
				}
			}
			
			if(isset($_POST['status'])){
				$upd = $link->query("UPDATE faculty SET status = '".$_POST['status']."' WHERE faculty.bnumber = '$ID'");
				if(!$upd){
					echo "ERROR: Status did not update <br />";
				}
				else{
					echo "Status successfully updated! <br />";
				}
			}
		}
		?>	
			
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
