<!DOCTYPE html>
<center>

<html >
<head>

<title>Curriculum Plan Library</title>
<!-- <link rel="stylesheet" href="css/style.css"> -->

<!-- Header copyright @ http://demo.tutorialzine.com/2015/02/freebie-7-responsive-header-templates/, written by  Danny Markov -->
<link rel="stylesheet" href="css/header-search.css">
<link href='http://fonts.googleapis.com/css?family=Cookie' rel='stylesheet' type='text/css'>


<header class="header-search">

<div class="header-limiter">

<h1><a href="singin.php">Curriculum Plan Library</span></a></h1>
<a class="logout" href="logout.php">Log Out</a> 

</header>
</head>

</head>

<body>

<div class="container">

<div id="login-form">


<fieldset>
<div class="body">
<h3>Change Curriculum</h3>

<select name="form" onchange="location = this.options[this.selectedIndex].value;">

	<option value="header-search.php">Select...</option>
	<option value="student.php">Add Or Change Major</option>
	<option value="somepage.php">Add Or Change Minor</option>
	<option value="somepage.php">Change Advisor</option>
	<option value="somepage.php">Change Primary Advisor</option>

</select>

<br><br><br>
<h3>Student Curriculum</h3>
<form action="entern.php" method="post">
<button type="submit">View Student Record</button>
</form>

</fieldset>

</div> 

</div>
</div> 


</body>
</html>
</center>
