<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="UTF-8">
  <title>Sign Up Form</title>
  
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">

  <link rel='stylesheet prefetch' href='http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'>

      <link rel="stylesheet" href="css/style.css">

  
</head>

<body>

  
<div class="container">
  <form method="post">
    <div class="row">
      <h4>Login</h4>
      <div class="input-group input-group-icon">
        <input type="text" placeholder="Full Name" name="uname"/>
        <div class="input-icon"><i class="fa fa-user"></i></div>
      </div>
      <div class="input-group input-group-icon">
        <input type="password" placeholder="Password" name="pass"/>
        <div class="input-icon"><i class="fa fa-key"></i></div>
      </div>
    </div>
    <div class="input-group">
        
        <label for="terms" id="create"><a href="signup.php">Create an Account??</a></label>
      </div>
     <button type="submit" name="submit_btn" id="submit"  class="btn btn-warning">Signin</button>
    </div>

  </form>
</div>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);
if(isset($_POST["submit_btn"]))
{ $uname=$_POST["uname"];
  $pass=$_POST["pass"];
$sel = mysqli_query($conn,"select name,password from userinfo where name='$uname' and password='$pass' ");
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  $row= mysqli_fetch_array($sel);

if($row['name']=="mariyam" && $row['password']=="123")
{
  echo "<script>alert('Login succesfully')</script> ";
  header("location:../make2.php");
  
}

else{

  echo "<script>alert('Username or Password in incorrect')</script> ";
  
}
}

session_start();
$_SESSION['USERNAME']=$uname;
$_SESSION['Password']=$pass;

?>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

  

    <script  src="js/index.js"></script>




</body>

</html>
