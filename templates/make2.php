<!--
Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE html>
<html lang="en">
<head>
<title>Exam Checking Service</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
h2{
	text-decoration: underline;
}
textarea::-webkit-input-placeholder {
color: #0bf;
}
::-webkit-input-placeholder { /* Chrome/Opera/Safari */
  color: pink;
}
::-moz-placeholder { /* Firefox 19+ */
  color: pink;
}
:-ms-input-placeholder { /* IE 10+ */
  color: pink;
}
:-moz-placeholder { /* Firefox 18- */
  color: pink;
}
</style>
<!-- <meta name="keywords" content="Rapid Fodder Responsive web template, Bootstrap Web Templates, Flat Web Templates, Android Compatible web template, 
	SmartPhone Compatible web template, free WebDesigns for Nokia, Samsung, LG, Sony Ericsson, Motorola web design" /> -->
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- Custom Theme files -->

<link href="css/bootstrap.css" type="text/css" rel="stylesheet" media="all">
<link href="css/style.css" type="text/css" rel="stylesheet" media="all">  
<link rel="stylesheet" href="css/swipebox.css">
<!-- //Custom Theme files -->
<!-- font-awesome icons -->
<link href="css/font-awesome.css" rel="stylesheet"> 
<!-- //font-awesome icons -->

<!-- web-fonts -->
<link href='//fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>
<link href="//fonts.googleapis.com/css?family=Lora:400,400i,700,700i" rel="stylesheet">
<!-- //web-fonts -->
<!-- <script type="text/javascript">
var capnum = 0;
function add(){
     capnum=capnum+1;
      document.getElementById('display').innerHTML = capnum;
}</script> -->
<script type="text/javascript">
		var a=1;
		function increase(){
			var textBox=document.getElementById("text");
			textBox.value=a;
			a++;
		}

	</script>

</head>
<body style="background-color: #e3e3e3">
<?php session_start();?>
<!-- banner -->
	
	<!-- header -->
 <div class="header" style="background-image:url('images/navbg3.png')">
			<div class="container">	
				<nav class="navbar navbar-default">
					<div class="navbar-header">
						<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<h1><a  href="index.html"><span>E</span>XAM<span>C</span>HECKER</a></h1>
					</div>
					<!-- navbar-header -->
					<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
						<ul class="nav navbar-nav navbar-right">
							<li><a href="index.html" class="hvr-underline-from-center active">Make</a></li>
							<li><a href="check.php" >Check</a></li>
							<li><a href="#services_bg" class="hvr-underline-from-center scroll">Result</a></li>
							<li><a href="sign-up-form/signin.php">Logout</a></li>
						</ul>
					</div>
					<div class="clearfix"> </div>	
				</nav>
				<div class="search">
        
							<input class="search_box" type="checkbox" id="search_box"><br/>
							<label class="icon-search" for="search_box" style="color:white;font-size:15px;margin-top:4px">
                <?php 
     session_start();
     $uname=$_SESSION["USERNAME"];
     $pass=$_SESSION["Password"];
   echo "Username:      ".$uname;?> </label>
   
							<!-- <div class="search_form">
								<form  method="post">
									<input type="search" name="Search" placeholder="Search..." required="">

									<input type="submit" name="Send">
								</form>
							</div> -->
						</div>

			</div> 
		</div> 
		<br><br><br>
		<div class="container"  style="background-color: white;border-radius: 5px">
		
		
<div class="row">
    <div class="col-sm-6" >
      <h2 style="color:orange">Objective Section:</h2>
    </div>
     <div class="col-sm-6" >
    </div>
    </div>
    <br><br>
    
<div class="row">
	
    <div class="col-sm-3" ></div>
    <div class="col-sm-3" >
    	<form method="post" action="make2.php">
      Name:
      <?php
$mcq_paper="";
if(isset($_POST['mcq_paper'])){
	$mcq_paper=$_POST['mcq_paper'];
}
      ?>


      <select name="mcq_paper" id="mcq_paper"  class="btn btn-warning dropdown-toggle" style="background-color:orange;color:white">
  <option name="myoption1" value="Select your paper"  style="background-color:white;color:grey"
  <?php if($mcq_paper == 'Select your paper'): echo "selected='selected'"; endif; ?>>Select Your Paper</option>
  <option name="myoption1" value="computer" style="background-color:white;color:grey"
  <?php if($mcq_paper == 'computer'): echo "selected='selected'"; endif; ?>>Computer</option>
  <option name="myoption2" value="english" style="background-color:white;color:grey"
    <?php if($mcq_paper == 'english'): echo "selected='selected'"; endif; ?>>English</option>
>English</option>
  <option name="myoption3" value="science" style="background-color:white;color:grey"
    <?php if($mcq_paper == 'science'): echo "selected='selected'"; endif; ?>>Science</option>
>Science</option>
 </select>
    </div>
    <div class="col-sm-3" >Total Marks: 
    <input type="text"  name="mcq_tmarks" id="mcq_tmarks"
    value="<?php if(isset($_POST['mcq_tmarks'])){echo $_POST['mcq_tmarks'];} ?>"></div>
    <div class="col-sm-3" ><input type="text" id="click_value" value="false" style="visibility:hidden" name="click_value"/></div>
</div>
<br>
<div class="row">
	<div class="col-sm-3" ></div>
	<div class="col-sm-6" >
	Enter Question: <textarea name="mcq_ques" cols="76" rows="3" id="mcq_ques" placeholder="Enter Question"></textarea>
	</div>
	<div class="col-sm-3" ></div>

</div>
<br>
<div class="row">
	<div class="col-sm-3" ></div>
	<div class="col-sm-2" >
	Marks:  <input type="text" name="mcq_marks" id="mcq_marks">
    </div>
    <div class="col-sm-2"><button type="submit" name="mcq_next" style="background-color:orange" class="btn btn-warning navbar-btn">Next Question</button></div>
	<div class="col-sm-2"><button type="submit"   name="mcq_finish" style="background-color:orange" class="btn btn-warning navbar-btn">Finish Question</button></div>
    <div class="col-sm-3" ></div>
</div>
<br>
<div class="row">
	<div class="col-sm-4" ></div>
	<div class="col-sm-5" >
	<button type="submit" name="mcq_preview" style="width:350px;height:50px;background-color:orange" class="btn btn-warning navbar-btn">Save & Preview</button>
    </div>
    </form>
    <div class="col-sm-4" ></div>
</div>

<hr >

<br><br>

<div class="row">
    <div class="col-sm-6" >
      <h2 style="color:orange">Descriptive Section:</h2>
    </div>
     <div class="col-sm-6" >
    </div>
    </div>
    <br><br>
    <form method="post" action="make2.php">
<div class="row">
	 
    <div class="col-sm-3" ></div>
    <div class="col-sm-3" >
      Name:
     
      <?php
$th_paper="";
if(isset($_POST['th_paper'])){
	$th_paper=$_POST['th_paper'];
}
      ?>

      <select name="th_paper" id="th_paper"  class="btn btn-warning dropdown-toggle" style="background-color:orange;color:white">
  <option name="myoption1" value="Select your paper"  style="background-color:white;color:grey"
  <?php if($th_paper == 'Select your paper'): echo "selected='selected'"; endif; ?>>Select Your Paper</option>
  <option name="myoption1" value="computer" style="background-color:white;color:grey"
  <?php if($th_paper == 'computer'): echo "selected='selected'"; endif; ?>>Computer</option>
  <option name="myoption2" value="english" style="background-color:white;color:grey"
    <?php if($th_paper == 'english'): echo "selected='selected'"; endif; ?>>English</option>
>English</option>
  <option name="myoption3" value="science" style="background-color:white;color:grey"
    <?php if($th_paper == 'science'): echo "selected='selected'"; endif; ?>>Science</option>
>Science</option>
 </select>
    </div>
    <div class="col-sm-3" >Total Marks: 
    <input type="text"  name="th_tmarks" id="th_tmarks"
    value="<?php if(isset($_POST['th_tmarks'])){echo $_POST['th_tmarks'];} ?>"></div>
    <div class="col-sm-3" ><div class="col-sm-3" ><input type="text" style="visibility:hidden" id="thclick_value" value="false" name="thclick_value"/></div>
</div></div>
    <br>
    <div class="row">
	<div class="col-sm-3" ></div>
	<div class="col-sm-6" >
	Enter Question: <textarea name="th_ques" cols="76" rows="3" id="th_ques" placeholder="Enter Question"></textarea>
	</div>
	<div class="col-sm-3" ></div>

</div>
<br>
<div class="row">
	<div class="col-sm-3" ></div>
	<div class="col-sm-2" >
	Marks:  <input type="text" name="th_marks" id="th_marks">
    </div>
    
    <div class="col-sm-2"><button type="submit" name="th_next" style="background-color:orange" class="btn btn-warning navbar-btn">Next Question</button></div>

	<div class="col-sm-2"><button type="submit"   name="th_finish" style="background-color:orange" class="btn btn-warning navbar-btn">Finish Question</button></div>
    <div class="col-sm-3" ></div>
</div>
<br>
<div class="row">
	<div class="col-sm-4" ></div>
	<div class="col-sm-5" >
	<button type="submit" name="th_preview" style="width:350px;height:50px;background-color:orange" class="btn btn-warning navbar-btn">Save & Preview</button>
	 
    </div>
    </form>
    <div class="col-sm-4" ></div>
   
</div>

<!-- //header -->
		<!-- banner-text -->

		
<?php 
global $mcqfinish_btn;
$mcqfinish_btn="false";
$thfinish_btn="false";
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);

if(isset($_POST['mcq_next']))
{
	$mcqnext_btn="true";
	$_SESSION['mcou'] = ((isset($_SESSION['mcou'])) ? $_SESSION['mcou'] : 0);
     $_SESSION['mcou']++;
     echo $_SESSION['mcou'];
     $mcqpaper=$_POST["mcq_paper"].'mcq';
	$mcqtmarks=$_POST["mcq_tmarks"];
    $mcqques=$_POST["mcq_ques"];
    $mcqmarks=$_POST["mcq_marks"];
  $sql = "INSERT INTO question (q_id,paper_name, total_marks, q_name,marks_of_q)
VALUES ('".$_SESSION['mcou']."','".$mcqpaper."','".$mcqtmarks."','".$mcqques."','".$mcqmarks."')";
if ($conn->query($sql) === TRUE) {
    echo "<script> alert(' inserted')</script>";
    
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
         echo "<script> alert(' inserted' $sql.'and'.$conn->error)</script>";
}


$conn->close();
}

$mcq_paper="";
if(isset($_POST['Send'])){
 echo $_SESSION["USERNAME"];
}
     

//
//
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);

if(isset($_POST["mcq_finish"]))
{
	
	$mcqfinish_btn="true";
echo "finish click: ".$mcqfinish_btn;
$uname=$_SESSION["USERNAME"];
echo $uname;
	$_SESSION['mcou'] = ((isset($_SESSION['mcou'])) ? $_SESSION['mcou'] : 0);
     $_SESSION['mcou']++;
     echo $_SESSION['mcou'];
    $mcqpaper=$_POST["mcq_paper"].'mcq';
	$mcqtmarks=$_POST["mcq_tmarks"];
    $mcqques=$_POST["mcq_ques"];
    $mcqmarks=$_POST["mcq_marks"];
    $finishclick="true";
    echo "<script>document.getElementById('click_value').value='$finishclick' </script>";
     $sel = mysqli_query($conn,"select userid from userinfo where name= '$uname'");
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
    
    $userid=$row[0];
    
    echo "Userid:".$userid;

  }


  //  $sql1 = "INSERT INTO paper (paper_name) VALUES ('".$mcqpaper."')";
    $sql1 = mysqli_query($conn,"INSERT INTO paper (paper_name,userid) VALUES ('".$mcqpaper."','".$userid."')");
    
    $result = mysqli_query($conn,"SELECT * FROM paper");
    $num_rows = mysqli_num_rows($result);
    
   echo("no of rows in period:".$num_rows);
    $sel = mysqli_query($conn,"SELECT paper_id,paper_name FROM paper LIMIT".$num_rows);
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
  	
  	$selectmcqpaperidf=$row[0];
  	$selectmcqpaperf=$row[1];
  	echo "paperid:".$selectmcqpaperidf;

  }
     $sql2 = mysqli_query($conn,"INSERT INTO question (q_id,paper_name, total_marks, q_name,marks_of_q)
 VALUES ('".$_SESSION['mcou']."','".$mcqpaper."','".$mcqtmarks."','".$mcqques."','".$mcqmarks."')");
    $sql3 = mysqli_query($conn,"UPDATE question SET paper_id= '$selectmcqpaperidf' where paper_name= '$mcqpaper'");


$conn->close();
}

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);

if(isset($_POST['mcq_preview']))
	{   $finishclick=$_POST["click_value"];
$uname=$_SESSION["USERNAME"];

        echo "preview click1: ".$finishclick;

	if($finishclick=="false")
	{ 

     $mcqpaper=$_POST["mcq_paper"].'mcq';

	   
	
	
		$mcqpaper=$_POST["mcq_paper"].'mcq';
    $sel = mysqli_query($conn,"select userid from userinfo where name= '$uname'");
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
    
    $userid=$row[0];
    
    echo "Userid:".$userid;

  }

  
$sql1 = mysqli_query($conn,"INSERT INTO paper (paper_name,userid) VALUES ('".$mcqpaper."','".$userid."')");
    
    $result = mysqli_query($conn,"SELECT * FROM paper");
    $num_rows = mysqli_num_rows($result);
    
   echo("no of rows in period:".$num_rows);
    $sel = mysqli_query($conn,"SELECT paper_id,paper_name FROM paper LIMIT".$num_rows);
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
  	
  	$selectmcqpaperidf=$row[0];
  	$selectmcqpaperf=$row[1];
  	echo "paperid:".$selectmcqpaperidf;

  }
      $sql3 = mysqli_query($conn,"UPDATE question SET paper_id= '$selectmcqpaperidf' where paper_name= '$mcqpaper'");

if (  $mcqfinish_btn="false" ) {
    echo "<script> window.onload = function() {
     clearform();
 }; </script>";

} else {
    echo "Error: " . $sql2 . "<br>" . $conn->error;
         echo "<script> alert(' inserted' $sql2.'and'.$conn->error)</script>";
}
     }

$conn->close();
}
?>
<!-- DESCRIPTIVE SECTION: -->
<?php

$thfinish_btn="false";
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);

if(isset($_POST['th_next']))
{   
	$thnext_btn=true;
	$_SESSION['tcou'] = ((isset($_SESSION['tcou'])) ? $_SESSION['tcou'] : 0);
     $_SESSION['tcou']++;
     echo $_SESSION['tcou'];
    $thpaper=$_POST["th_paper"];
	$thtmarks=$_POST["th_tmarks"];
    $thques=$_POST["th_ques"];
    $thmarks=$_POST["th_marks"];
  $sql = "INSERT INTO question (q_id,paper_name, total_marks, q_name,marks_of_q)
VALUES ('".$_SESSION['tcou']."','".$thpaper."','".$thtmarks."','".$thques."','".$thmarks."')";
if ($conn->query($sql) === TRUE) {
    echo "<script> alert(' inserted')</script>";
    
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
         echo "<script> alert(' inserted' $sql.'and'.$conn->error)</script>";
}


$conn->close();
}

//
//
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);

if(isset($_POST["th_finish"]))
{
	global $thfinish_btn;
	$thfinish_btn="true";
echo "finish click: ".$thfinish_btn;
$uname=$_SESSION["USERNAME"];
	$_SESSION['tcou'] = ((isset($_SESSION['tcou'])) ? $_SESSION['tcou'] : 0);
     $_SESSION['tcou']++;
     echo $_SESSION['tcou'];
    $thpaper=$_POST["th_paper"];
	$thtmarks=$_POST["th_tmarks"];
    $thques=$_POST["th_ques"];
    $thmarks=$_POST["th_marks"];
    $thfinishclick="true";
    echo "<script>document.getElementById('thclick_value').value='$thfinishclick' </script>";

  //  $sql1 = "INSERT INTO paper (paper_name) VALUES ('".$mcqpaper."')";
$sel = mysqli_query($conn,"select userid from userinfo where name= '$uname'");
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
    
    $userid=$row[0];
    
    echo "Userid:".$userid;

  }

    $sql1 = mysqli_query($conn,"INSERT INTO paper (paper_name,userid) VALUES ('".$thpaper."','".$userid."')");
    
    $result = mysqli_query($conn,"SELECT * FROM paper");
    $num_rows = mysqli_num_rows($result);
    
   echo("no of rows in period:".$num_rows);
    $sel = mysqli_query($conn,"SELECT paper_id,paper_name FROM paper LIMIT".$num_rows);
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
  	
  	$selectthpaperidf=$row[0];
  	$selectthpaperf=$row[1];
  	echo "paperid:".$selectthpaperidf;

  }
     $sql2 = mysqli_query($conn,"INSERT INTO question (q_id,paper_name, total_marks, q_name,marks_of_q)
 VALUES ('".$_SESSION['tcou']."','".$thpaper."','".$thtmarks."','".$thques."','".$thmarks."')");
    $sql3 = mysqli_query($conn,"UPDATE question SET paper_id= '$selectthpaperidf' where paper_name= '$thpaper'");


$conn->close();
}

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);
if(isset($_POST['th_preview']))
	{   $thfinishclick=$_POST["thclick_value"];
$uname=$_SESSION["USERNAME"];
        echo "finish preview click1: ".$thfinishclick;

	if($thfinishclick=="false")
	{ 
	
		$thpaper=$_POST["th_paper"];
    $sel = mysqli_query($conn,"select userid from userinfo where name= '$uname'");
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
    
    $userid=$row[0];
    
    echo "Userid:".$userid;

  }

$sql1 = mysqli_query($conn,"INSERT INTO paper (paper_name,userid) VALUES ('".$thpaper."','".$userid."')");
    
    $result = mysqli_query($conn,"SELECT * FROM paper");
    $num_rows = mysqli_num_rows($result);
    
   echo("no of rows in period:".$num_rows);
    $sel = mysqli_query($conn,"SELECT paper_id,paper_name FROM paper LIMIT".$num_rows);
    $resource=mysqli_query($conn,$sel);
  $count=mysqli_num_rows($sel);
  while($row=mysqli_fetch_row($sel))
  {
  	
  	$selectthpaperidf=$row[0];
  	$selectthpaperf=$row[1];
  	echo "paperid:".$selectthpaperidf;

  }
      $sql3 = mysqli_query($conn,"UPDATE question SET paper_id= '$selectthpaperidf' where paper_name= '$thpaper'");

if (  $thfinish_btn!="true" ) {
    echo "<script> window.onload = function() {
     clearthform();
 }; </script>";

} else {
    echo "Error: " . $sql2 . "<br>" . $conn->error;
         echo "<script> alert(' inserted' $sql2.'and'.$conn->error)</script>";
}
     }

$conn->close();
}

?>	



<!-- js -->
<script type="text/javascript">
	function clearform()
{
	 // $('#mcq_paper option:eq(1)');
	 //  $('#mcq_paper option:contains("Select Your Paper)');
var $select = $('#mcq_paper');
$select.val("Select Your Paper");
if ($select.val() == null) {
  $select.val("Select your paper");
}


    document.getElementById("mcq_paper").value="Select your paper" ;//don't forget to set the textbox id
    document.getElementById("mcq_tmarks").value="";
    document.getElementById("mcq_ques").value="";
    document.getElementById("mcq_marks").value="";
    
}
function clearthform()
{
	 // $('#mcq_paper option:eq(1)');
	 //  $('#mcq_paper option:contains("Select Your Paper)');
var $select = $('#th_paper');
$select.val("Select Your Paper");
if ($select.val() == null) {
  $select.val("Select your paper");
}


    document.getElementById("th_paper").value="Select your paper" ;//don't forget to set the textbox id
    document.getElementById("th_tmarks").value="";
    document.getElementById("th_ques").value="";
    document.getElementById("th_marks").value="";
    
}

</script>

<script src="js/jquery-2.2.3.min.js"></script> 
<script type="text/javascript">
	$(".dropdown-menu").on('click', 'li a', function(){
        $(this).parent().parent().siblings(".btn:first-child").html($(this).text()+' <span class="caret"></span>');
        $(this).parent().parent().siblings(".btn:first-child").val($(this).text());
    });
</script>
<!-- //js -->
<!--banner-Slider-->
						<script src="js/responsiveslides.min.js"></script>
							<script>
								// You can also use "$(window).load(function() {"
								$(function () {
								  // Slideshow 4
								  $("#slider3").responsiveSlides({
									auto: true,
									pager:true,
									nav:false,
									speed:500,
									namespace: "callbacks",
									before: function () {
									  $('.events').append("<li>before event fired.</li>");
									},
									after: function () {
									  $('.events').append("<li>after event fired.</li>");
									}
								  });
							
								});
							 </script>
								<!-- Calendar -->
						<link rel="stylesheet" href="css/jquery-ui.css" />
						<script src="js/jquery-ui.js"></script>
						<script>
								$(function() {
									$( "#datepicker" ).datepicker();
								});
						</script>
						<!-- //Calendar -->  
<!--//banner-Slider-->
<!-- swipe box js -->
	<script src="js/jquery.adipoli.min.js" type="text/javascript"></script>
	<script type="text/javascript"> 
		$(function(){ 
			$('.row2').adipoli({
				'startEffect' : 'overlay',
				'hoverEffect' : 'sliceDown'
			}); 
		});
		
	</script>
	<script src="js/jquery.swipebox.min.js"></script> 
	<script type="text/javascript">
			jQuery(function($) {
				$(".swipebox").swipebox();
			});
	</script>
	<!-- //swipe box js -->
	<!-- smooth-scrolling-of-move-up -->
	<script type="text/javascript">
		$(document).ready(function() {
			/*
			var defaults = {
				containerID: 'toTop', // fading element id
				containerHoverID: 'toTopHover', // fading element hover id
				scrollSpeed: 1200,
				easingType: 'linear' 
			};
			*/
			
			$().UItoTop({ easingType: 'easeOutQuart' });
			
		});
	</script>
<!-- mcqmcountdown-Timer-JavaScript -->
			<script src="js/simplymcqmcountdown.js"></script>
			<script>
				var d = new Date(new Date().getTime() + 48 * 120 * 120 * 2000);

				// default example
				simplymcqmcountdown('.simply-mcqmcountdown-one', {
					year: d.getFullYear(),
					month: d.getMonth() + 1,
					day: d.getDate()
				});

				// inline example
				simplymcqmcountdown('.simply-mcqmcountdown-inline', {
					year: d.getFullYear(),
					month: d.getMonth() + 1,
					day: d.getDate(),
					inline: true
				});

				//jQuery example
				$('#simply-mcqmcountdown-losange').simplymcqmcountdown({
					year: d.getFullYear(),
					month: d.getMonth() + 1,
					day: d.getDate(),
					enableUtc: false
				});
			</script>
		<!-- //mcqmcountdown-Timer-JavaScript -->
<!-- start-smooth-scrolling -->
<script type="text/javascript" src="js/move-top.js"></script>
<script type="text/javascript" src="js/easing.js"></script>	
<script type="text/javascript">
		jQuery(document).ready(function($) {
			$(".scroll").click(function(event){		
				event.preventDefault();
		
		$('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
			});
		});
</script>
<!-- //end-smooth-scrolling -->	
    <script src="js/bootstrap.js"></script>

	
</body>
</html>