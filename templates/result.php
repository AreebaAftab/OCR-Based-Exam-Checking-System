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
#table{
          border-bottom:3px solid #39F;
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
							<li><a href="#services_bg" class="hvr-underline-from-center scroll">Result</a></li>
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
      <h2 style="color:orange">Descriptive Section:</h2>
    </div>
     <div class="col-sm-6" >
    </div>
 </div>
    <br><br>
    <div class="row">
    <div class="col-sm-3" ></div>
    <div class="col-sm-6" >
     
   
 <form method='post' >
<label>Select Paper:</label>
<input type="text" palceholder="Enter Rollno" name="rollno"/>
<span class="glyphicon glyphicon-search" aria-hidden="true"></span>
<button  style="background-color:orange;margin-left:100px"  class="btn btn-warning navbar-btn">
     <a href="result2.php">Show</a>
  </button>
    </div>
    <div class="col-sm-3" >

    </div>
 </div>

 <div class="row">
    <div class="col-sm-3" ></div>
    <div class="col-sm-6" >
    <br><img src="images/img.png"  id="data" style="visibility: hidden;" />
    </div>
    <div class="col-sm-3" ></div>
 </div>
 </form>



<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "checker";
$conn = new mysqli($servername, $username, $password, $dbname);

  if(isset($_POST['Show']))
  {   $rollno=$_POST["rollno"];
    echo "<script> alert($rollno=)</script>";
    echo "<script>document.getElementById('data').src='images/img.png' </script>";

    $s="select std.std_rollnum,question.paper_name,std.obt_marks_of_ques,std.total_marks FROM std,question  where std.paper_id=question.paper_id AND std.std_rollnum ='$rollno'";
  $resource=mysqli_query($conn,$s);
  $count=mysqli_num_rows($resource);
  // echo "<div class='container'><table >";
  // echo "<div class='row' id='heading'>";
  // echo "<div class='col-md-2' id='head1'>Roll No</div>";
  // echo "<div class='col-md-2' id='head2'>Paper Name</div>";
  // echo "<div class='col-md-2' id='head3'>Obtain Marks</div>";
  // echo "<div class='col-md-2' id='head3'>Total Marks</div>";

  echo "</div>";
  //  echo "<div class='container' ><table rules='all'>";
  // echo "<tr>";
  // echo "<th>Date</th>";
  // echo "<th>Item</th>";
  // echo "</tr>";
  while($row=mysqli_fetch_row($resource))
  {
    // echo "</br>";
    // // echo "<tr>";
    // // echo "<td> ".$row[1]."</td>";
    // // echo "<td> ".$row[2]."</td>";    
    // // echo "</tr>";
    // echo "<div class='row' id ='table'>";
    // echo "<div class='col-xs-2' id='content1'> ".$row[0]."</div>";
    // echo "<div class='col-xs-2' id='content2'>".$row[1]."</div>";
    // echo "<div class='col-xs-2' id='content2'>".$row[2]."</div>";
    // echo "<div class='col-xs-2' id='content2'>".$row[3]."</div>";

    // echo "</div>";
  }
  echo "</table></div>";
  }


?>

</div>



<script type="text/javascript">
  function showhide(){
    var x=document.getElementById("data");
    if(x.style.display==="none")
    {
      x.style.display="block";
    }
    else{
      x.style.display="none";
    }
  }
</script>










  

// <!-- js -->

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