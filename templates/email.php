<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>Email</title>

</head>

<?php

    mail('coletterice11@gmail.com', $_POST['subject'], $_POST['message'], $_POST['email']);

?>

<p>Your email has been sent.</p>

<body>

</body>

</html>