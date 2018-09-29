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
        <input type="text" placeholder="Full Name"/>
        <div class="input-icon"><i class="fa fa-user"></i></div>
      </div>
      <div class="input-group input-group-icon">
        <input type="password" placeholder="Password"/>
        <div class="input-icon"><i class="fa fa-key"></i></div>
      </div>
    </div>
    <div class="input-group">
        
        <label for="terms" id="create"><a href="signup.php">Create an Account??</a></label>
      </div>
     <a href="../make2.php"><button type="submit" name="submit_btn" id="submit"  class="btn btn-warning">Signin</button></a>
    </div>

  </form>
</div>
<?php
if (isset($_POST['submit_btn']))
    {  
       
       $output1 = shell_exec("python gensim2.py ");
       // $page = shell_exec("/tmp/my_script.php '".$my_url."' '".$my_refer."'");
       echo $output1;
    }
?>


  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

  

    <script  src="js/index.js"></script>




</body>

</html>
