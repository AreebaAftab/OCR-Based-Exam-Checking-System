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


</head>
<body style="background-color: #e3e3e3">
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
							<li><a href="make.php" >Make</a></li>
							<li><a href="#about" class="hvr-underline-from-center scroll">Check</a></li>
							<li><a href="result.php" >Result</a></li>
							<li><a href="sign-up-form/signin.php">Logout</a></li>
						</ul>
					</div>
					<div class="clearfix"> </div>	
				</nav>
				<div class="search">
							<input class="search_box" type="checkbox" id="search_box">
							<label class="icon-search" for="search_box"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></label>
							<div class="search_form">
								<form action="#" method="post">
									<input type="search" name="Search" placeholder="Search..." required="">

									<input type="submit" value="Send">
								</form>
							</div>
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
    <div class="col-sm-6" >
      
      <?php
$mcq_paper="";
if(isset($_POST['mcq_paper'])){
  $mcq_paper=$_POST['mcq_paper'];
}
      ?>
 <form method='post' action='check.php' enctype='multipart/form-data'>

  <select name="mcq_paper" id="mcq_paper"  class="btn btn-warning dropdown-toggle" style="background-color:orange;color:white;margin-left: 90px ">
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

    
<img src="images/d2.jpg" style="visibility:hidden" style="margin-left:19px" width="160px" height:90px>
    </div>
    <div class="col-sm-3" ></div>
 </div>
 <div class="row">

    <div class="col-sm-3" ><input type='file' name='mcqstd_file' id="mcqstd_file" style="background-color:orange;margin-left:10px;visibility:hidden"  class="btn btn-warning navbar-btn"></div>
    <div class="col-sm-6" >
    <button type="submit" id="files" onclick="document.getElementById('mcqstd_file').click(); return false"
     name="upload_std_mcq" style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Browse Student Mcq
  </button>
     
   <input type="text" style="margin-left:-1px" id="mcqstd_path" name="mcqstd_path" >
   <button type="submit" name='submit' style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Upload </button>
    
    </div>
    <div class="col-sm-3" ></div>
 </div>
 </form>
 <div class="row">
   

 <form method='post' action='check.php' enctype='multipart/form-data'>
 <input type="text" name="tempo" id="tempo" style="visibility:hidden"/>
 
    <div class="col-sm-3" ><input type='file' name='mcqtea_file' id="mcqtea_file" style="background-color:orange;margin-left:10px;visibility:hidden"  class="btn btn-warning navbar-btn"></div>
    <div class="col-sm-6" >
    <button type="submit" id="files" onclick="document.getElementById('mcqtea_file').click(); return false"
     name="upload_tea_mcq" style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Browse Teacher Mcq
  </button>
    <input type="text" style="margin-left:-1px" id="mcqtea_path" name="mcqtea_path" >
   <button type="submit" name='submit' style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Upload </button>

   
    </div>
    <div class="col-sm-3" >
      <input type="text" name="papertempo" id="papertempo" style="visibility:hidden"/>

    </div>
 </div>
 
 <div class="row">
	<div class="col-sm-2" ></div>
	<div class="col-sm-2" ></div>
	<div class="col-sm-2" >
	<button type="submit"  name="mcq_check" style="width:350px;height:50px;background-color:orange;margin-left:-75px" class="btn btn-warning navbar-btn">Start Checking</button>
    </div>
    <div class="col-sm-4" ></div>
</div>
</form>

<hr><br><br>
<div class="row">
    <div class="col-sm-6" >
      <h2 style="color:orange">Descriptive Section:</h2>
    </div>
     <div class="col-sm-6" >
    </div>
 </div>
    <br><br>
    <div class="row">
    <div class="col-sm-3" ></div>
    <div class="col-sm-6" >
    
      <?php
$th_paper="";
if(isset($_POST['th_paper'])){
  $th_paper=$_POST['th_paper'];
}
      ?>
 <form method='post' action='check.php' enctype='multipart/form-data'>

  <select name="th_paper" id="th_paper"  class="btn btn-warning dropdown-toggle" style="background-color:orange;color:white;margin-left: 90px ">
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

<img src="images/d2.jpg" style="visibility:hidden"  style="margin-left:19px" width="160px" height:90px>
    </div>
    <div class="col-sm-3" ></div>
 </div>

 <div class="row">
    <div class="col-sm-3" ><input type='file' name='thstd_file' id="thstd_file" style="background-color:orange;margin-left:10px;visibility:hidden"  class="btn btn-warning navbar-btn"></div>
    <div class="col-sm-6" >
    <button type="submit" id="files" onclick="document.getElementById('thstd_file').click(); return false"
     name="upload_std_th" style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Browse Student Paper
  </button>
     
   <input type="text" style="margin-left:-1px" id="thstd_path" name="thstd_path">
   <button type="submit" name='submit' style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Upload </button>
    
    </div>
    <div class="col-sm-3" ></div>
 </div>
 </form>
 <div class="row">
 <form method='post' action='check.php' enctype='multipart/form-data'>
  <input type="text" name="thtempo" id="thtempo" style="visibility:hidden"/>
  
    <div class="col-sm-3" ><input type='file' name='thtea_file' id="thtea_file" style="background-color:orange;margin-left:10px;visibility:hidden"  class="btn btn-warning navbar-btn"></div>
    <div class="col-sm-6" >
    <button type="submit" id="files" onclick="document.getElementById('thtea_file').click(); return false"
     name="upload_tea_th" style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Browse Teacher Paper
  </button>
    <input type="text" style="margin-left:-1px" id="thtea_path" name="thtea_path">
   <button type="submit" name='submit' style="background-color:orange;margin-left:10px"  class="btn btn-warning navbar-btn">Upload </button>
   
    </div>
    <div class="col-sm-3" ><input type="text" name="thpapertempo" id="thpapertempo" style="visibility:hidden"/>
</div>
 </div>
 
 <div class="row">
	<div class="col-sm-2" ></div>
	<div class="col-sm-2" ></div>
	<div class="col-sm-2" >
	<button type="submit" name="th_check" style="width:350px;height:50px;background-color:orange;margin-left:-75px" class="btn btn-warning navbar-btn">Start Checking</button>
    </div>
    <div class="col-sm-4" ></div>
</div>
</form>
<?php
$arr=array();
$i=0;
$thtea_name="";
$thtea_temp_name="";
$thstd_name="";
$thstd_temp_name="";
$thtea_path_field="";
$mcqtea_name="";
$mcqtea_temp_name="";
$mcqstd_name="";
$mcqstd_temp_name="";
$mcqtea_path_field="";
$temp_value="";

if($_FILES){

	$mcqstd_name        = $_FILES['mcqstd_file']['name'];  
    $mcqstd_temp_name  = $_FILES['mcqstd_file']['tmp_name']; 
    $mcqpaper = $_POST['mcq_paper'];

    if(isset($mcqstd_name)){
        if(!empty( $mcqstd_name)){      
            $location = 'studentmcq/';      
            if(move_uploaded_file($mcqstd_temp_name, $location.$mcqstd_name)){
                echo 'File uploaded successfully';
                echo "filename: studentmcq/".$mcqstd_name;
                
                echo "<script>document.getElementById('mcqstd_path').value='$mcqstd_name' </script>";
                echo "<script>document.getElementById('tempo').value='$mcqstd_name' </script>";
                echo "<script>document.getElementById('papertempo').value='$mcqpaper' </script>";
                
                  
                
            }
        }       
    }  else {
        echo 'You should select a file to upload !!';
    }
}
$temp_value="<script>document.getElementById('tempo').value</script>";

if($_FILES){
	
  $temp_value=$_POST["tempo"];
  $paper_value=$_POST["papertempo"];

	$mcqtea_name        = $_FILES['mcqtea_file']['name'];  
    $mcqtea_temp_name  = $_FILES['mcqtea_file']['tmp_name']; 
    if(isset($GLOBALS['mcqtea_name'])){
        if(!empty( $GLOBALS['mcqtea_name']))
        {      
            $location = 'teachermcq/';      
            if(move_uploaded_file($GLOBALS['mcqtea_temp_name'], $location.$GLOBALS['mcqtea_name']))
            {   
                echo 'File uploaded successfully</br>';
                
                echo "filename: teachermcq/".$GLOBALS['mcqtea_name'];
                echo "<script>document.getElementById('mcqtea_path').value='$mcqtea_name'</script>";
                echo "<script>document.getElementById('tempo').value='$temp_value'</script>";
                echo "<script>document.getElementById('papertempo').value='$paper_value'+'mcq'</script>";

                 
                
                
                // echo("value of i",$i);
                // $GLOBALS['arr[$i]']=$mcqtea_name;
                // echo "teacher: ".$GLOBALS['arr[$i]'];
                // $i++;
            }
        }       
    }  
    else {
        echo 'You should select a file to upload !!';
    }


}

if (isset($_POST['mcq_check']))
    {  $myfield2=$_POST["mcqtea_path"];
       $std_value=$_POST["tempo"];
       $paper_value=$_POST["papertempo"];
       
       
       echo "inside mcq_check btn";
        $output1 = shell_exec("python argument.py $std_value $myfield2 $paper_value");

       // $output1 = shell_exec("python argument.py $std_value $myfield2");
       // $page = shell_exec("/tmp/my_script.php '".$my_url."' '".$my_refer."'");
       echo $output1;
    }

if($_FILES){

	$thstd_name        = $_FILES['thstd_file']['name'];  
    $thstd_temp_name  = $_FILES['thstd_file']['tmp_name']; 
        $thpaper = $_POST['th_paper'];

    if(isset($thstd_name)){
        if(!empty( $thstd_name)){      
            $location = 'students/';      
            if(move_uploaded_file($thstd_temp_name, $location.$thstd_name)){
                echo 'File uploaded successfully';
                echo "filename: students/".$thstd_name;
                
                echo "<script>document.getElementById('thstd_path').value='$thstd_name' </script>";
                echo "<script>document.getElementById('thtempo').value='$thstd_name' </script>";
                echo "<script>document.getElementById('thpapertempo').value='$thpaper' </script>";

                
                  
                
            }
        }       
    }  else {
        echo 'You should select a file to upload !!';
    }
}
$temp_value="<script>document.getElementById('tempo').value</script>";

if($_FILES){
	
    $temp_value=$_POST["thtempo"];
      $thpaper_value=$_POST["thpapertempo"];

	$thtea_name        = $_FILES['thtea_file']['name'];  
    $thtea_temp_name  = $_FILES['thtea_file']['tmp_name']; 
    if(isset($GLOBALS['thtea_name'])){
        if(!empty( $GLOBALS['thtea_name']))
        {      
            $location = 'teacher/';      
            if(move_uploaded_file($GLOBALS['thtea_temp_name'], $location.$GLOBALS['thtea_name']))
            {   
                echo 'File uploaded successfully</br>';
                
                echo "filename: teacher/".$GLOBALS['thtea_name'];
                echo "<script>document.getElementById('thtea_path').value='$thtea_name'</script>";
                echo "<script>document.getElementById('thtempo').value='$temp_value'</script>";
                echo "<script>document.getElementById('thpapertempo').value='$thpaper_value'</script>";


                 
                
                
                // echo("value of i",$i);
                // $GLOBALS['arr[$i]']=$mcqtea_name;
                // echo "teacher: ".$GLOBALS['arr[$i]'];
                // $i++;
            }
        }       
    }  
    else {
        echo 'You should select a file to upload !!';
    }


}

if (isset($_POST['th_check']))
    {  $myfield1=$_POST["thtea_path"];
       $std_value=$_POST["thtempo"];
       $thpaper_value=$_POST["thpapertempo"];
       
       $output1 = shell_exec("python gensimfile.py  $std_value $myfield1 $thpaper_value");
       // $page = shell_exec("/tmp/my_script.php '".$my_url."' '".$my_refer."'");
       echo $output1;
    }
?>


  

<!-- js -->

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
<!-- Countdown-Timer-JavaScript -->
			<script src="js/simplyCountdown.js"></script>
			<script>
				var d = new Date(new Date().getTime() + 48 * 120 * 120 * 2000);

				// default example
				simplyCountdown('.simply-countdown-one', {
					year: d.getFullYear(),
					month: d.getMonth() + 1,
					day: d.getDate()
				});

				// inline example
				simplyCountdown('.simply-countdown-inline', {
					year: d.getFullYear(),
					month: d.getMonth() + 1,
					day: d.getDate(),
					inline: true
				});

				//jQuery example
				$('#simply-countdown-losange').simplyCountdown({
					year: d.getFullYear(),
					month: d.getMonth() + 1,
					day: d.getDate(),
					enableUtc: false
				});
			</script>
		<!-- //Countdown-Timer-JavaScript -->
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