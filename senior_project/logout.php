<?php
// Begin session
session_start();
if(session_destroy()) // Destroying All Sessions
{
  // Redirect to index page if session was destroyed
header("Location: index.php");
}
?>
