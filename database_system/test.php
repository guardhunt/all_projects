<?php 
	
	$link = NEW MySQLi('localhost', 'development', 'leslie', 'development')
		or die(mysql_connect_error("Connection Failed"));
		
	$test = $link -> query("SELECT firstname FROM(SELECT * FROM faculty)");
	echo $test;
	
	while($row = $test->fetch_array()){
		echo $row['firstname'];
	}
?>