/*
JavaScript for the demo: Recreating the Nikebetterworld.com Parallax Demo
Demo: Recreating the Nikebetterworld.com Parallax Demo
Author: Ian Lunn
Author URL: http://www.ianlunn.co.uk/
Demo URL: http://www.ianlunn.co.uk/demos/recreate-nikebetterworld-parallax/
Tutorial URL: http://www.ianlunn.co.uk/blog/code-tutorials/recreate-nikebetterworld-parallax/

License: http://creativecommons.org/licenses/by-sa/3.0/ (Attribution Share Alike). Please attribute work to Ian Lunn simply by leaving these comments in the source code or if you'd prefer, place a link on your website to http://www.ianlunn.co.uk/.

Dual licensed under the MIT and GPL licenses:
http://www.opensource.org/licenses/mit-license.php
http://www.gnu.org/licenses/gpl.html
*/

$(document).ready(function() { //when the document is ready...


	//save selectors as variables to increase performance
	var $window = $(window);
	var $first = $('#first');
	var $first_bg = $("#first .bg");
	var $first_bg2 = $("#first .bg2");
	var $first_bg25 = $("#first .bg25");
	var $first_bg3 = $("#first .bg3");
	var $first_bg4 = $("#first .bg4");
	var $first_bg5 = $("#first .bg5");
	var $first_bg6 = $("#first .bg6");
	var $first_bgt = $("#first .bgt");
	var $second = $('#second');
	var $second_bg = $("#second .bg");
	var $second_bg2 = $("#second .bg2");
	var $second_bg3 = $("#second .bg3");
	var $second_bg4 = $("#second .bg4");
	var $second_bg5 = $("#second .bg5");
	var $second_bg6 = $("#second .bg6");
	var $second_bg7 = $("#second .bg7");
	var $second_bg8 = $("#second .bg8");
	var $second_bgt = $("#second .bgt");
	var $third = $('#third');
	var $third_bg = $("#third .bg");
	var $third_bg2 = $("#third .bg2");
	var $third_bg3 = $("#third .bg3");
	var $third_bg4 = $("#third .bg4");
	var $third_bg5 = $("#third .bg5");
	var $third_bg6 = $("#third .bg6");
	var $third_bg7 = $("#third .bg7");
	var $third_bgsand = $("#third .bg_sand_pattern");
	var $third_bgt = $("#third .bgt");
	var $personaje = $("#personaje");

	
	var windowHeight = $window.height(); //get the height of the window
	
	
	//apply the class "inview" to a section that is in the viewport
	$('#first, #second, #third').bind('inview', function (event, visible) {
			if (visible == true) {
				$(this).addClass("inview");
			} else {
				$(this).removeClass("inview");
			}
		});
	
			
	//function that places the navigation in the center of the window
	function RepositionNav(){
		var windowHeight = $window.height(); //get the height of the window
		var windowWidth = $window.width();
		var navHeight = $('#nav').height() / 2;
		var windowCenter = (windowHeight / 2); 
		var newtop = windowCenter - navHeight;
		$('#nav').css({"top": newtop}); //set the new top position of the navigation list
	}
	//Automatic scrolling
	$(".nosotros_scroll").click(function(){
		console.log("hola");								   
		$('html, body').animate({
			scrollTop: $("#first").offset().top -100
		}, 1000);									   
	});
	$(".programas_scroll").click(function(){
		console.log("hola");								   
		$('html, body').animate({
			scrollTop: $("#first").offset().top +720
		}, 1000);									   
	});
	$(".ecotips_scroll").click(function(){
		console.log("hola");								   
		$('html, body').animate({
			scrollTop: $("#second").offset().top +9
		}, 1000);									   
	});
	$(".transparencia_scroll").click(function(){
		console.log("hola");								   
		$('html, body').animate({
			scrollTop: $("#third").offset().top
		}, 1000);									   
	});
	//function that is called for every pixel the user scrolls. Determines the position of the background
	/*arguments: 
		x = horizontal position of background
		windowHeight = height of the viewport
		pos = position of the scrollbar
		adjuster = adjust the position of the background
		inertia = how fast the background moves in relation to scrolling
	*/
	function newPos(x, windowHeight, pos, adjuster, inertia){
		return x + "% " + (-((750 + pos) - adjuster) * inertia)  + "px";
	}
	
	//function to be called whenever the window is scrolled or resized
	function Move(){ 
		var pos = $window.scrollTop(); //position of the scrollbar
		pos = parseInt(pos, 10);

		//if the first section is in view...
		
		if($first.hasClass("inview")){
			//call the newPos function and change the background position 1200
			$first.css({'backgroundPosition': newPos(50, windowHeight, pos, 900, .2)});
			$first_bg.css({'backgroundPosition': newPos(50+pos*.01, windowHeight, pos, 900, -.2)});
			$first_bg2.css({'backgroundPosition': newPos(50, windowHeight, pos, 800, 1.7)});
			$first_bg25.css({'backgroundPosition': newPos(50+pos*.3, windowHeight, pos, 900, .6)});
			$first_bg3.css({'backgroundPosition': newPos(50, windowHeight, pos, 4000, .04)});
			if(pos<720){
				$first_bg4.css({'backgroundPosition': newPos(50, windowHeight, pos, 2442, .5)});
				$first_bg5.css({'backgroundPosition': newPos(50, windowHeight, pos, 1860, .8)});
				$first_bg6.css({'backgroundPosition': newPos(50, windowHeight, pos, 1604, 1.1)});
			}else{
				$first_bg4.css({'backgroundPosition': newPos(50, windowHeight, pos, 1960, 1)});
				$first_bg5.css({'backgroundPosition': newPos(50, windowHeight, pos, 1785, 1)});
				$first_bg6.css({'backgroundPosition': newPos(50, windowHeight, pos, 1620, 1)});
			}
			$first_bgt.css({'backgroundPosition': newPos(50, windowHeight, pos, 900, 0.05)});
			
		//	if(pos > 420){
		//		$first_bg3.css({'z-index': 1});
		//	}else{
				$first_bg3.css({'z-index': 5});
		//	}
			
		}
		
		//if the second section is in view...
		if($second.hasClass("inview")){
			//call the newPos function and change the background position 1990
			$second.css({'backgroundPosition': newPos(50, windowHeight, pos, 1700, 0.3)});
			$second_bg.css({'backgroundPosition': newPos(50+pos*.01, windowHeight, pos, 2150, -.2)});
			$second_bg2.css({'backgroundPosition': newPos(50, windowHeight, pos, 4000, .04)});
			if(pos<1408){
				$second_bg3.css({'backgroundPosition': newPos(50, windowHeight, pos, 3005, .5)});
				$second_bg4.css({'backgroundPosition': newPos(50, windowHeight, pos, 2546, .8)});
				$second_bg5.css({'backgroundPosition': newPos(50, windowHeight, pos, 2742, 1.1)});
				$second_bg6.css({'backgroundPosition': newPos(50, windowHeight, pos, 2705, 1.1)});
			}else{
				console.log(pos)
				$second_bg3.css({'backgroundPosition': newPos(50, windowHeight, pos, 2580, 1)});
				$second_bg4.css({'backgroundPosition': newPos(50, windowHeight, pos, 2470, 1)});
				$second_bg5.css({'backgroundPosition': newPos(50, windowHeight, pos, 2800, 1)});
				$second_bg6.css({'backgroundPosition': newPos(50, windowHeight, pos, 2760, 1)});
			}
			$second_bg7.css({'backgroundPosition': newPos(50, windowHeight, pos, 2600, .5)});
			$second_bg8.css({'backgroundPosition': newPos(50, windowHeight, pos, 2670, 1)});
			$second_bgt.css({'backgroundPosition': newPos(50, windowHeight, pos, 900, 0.05)});
		}

		//if the third section is in view...
		if($third.hasClass("inview")){
			$third.css({'backgroundPosition': newPos(50, windowHeight, pos, 2700, 0.3)});
			$third_bg7.css({'backgroundPosition': newPos(50, windowHeight, pos, 2840, 1)});
			//$third_bg.css({'backgroundPosition': newPos(50+pos*.01, windowHeight, pos, 2150, -.2)});
			$third_bg2.css({'backgroundPosition': newPos(50+.05*pos, windowHeight, pos, 0, 1)});
			if(pos<1980){
				$third_bg5.css({'backgroundPosition': newPos(50, windowHeight, pos, 7300, .045)});
			}else{
				$third_bg5.css({'backgroundPosition': newPos(50, windowHeight, pos, 2940, 1)});
			}
			if(pos<2090){
				$third_bg3.css({'backgroundPosition': newPos(50, windowHeight, pos, 2430, -.5)});
			}else{
				$third_bg3.css({'backgroundPosition': newPos(50, windowHeight, pos, 3040, 1)});
			}
			$third_bg6.css({'backgroundPosition': newPos(50, windowHeight, pos, 3100, 1)});
			$third_bgsand.css({'backgroundPosition': newPos(50, windowHeight, pos, 3100, 1)});

			$third_bgt.css({'backgroundPosition': newPos(50, windowHeight, pos, 900, 0.05)});
		}
		if(pos>1570){
			$personaje.css({'display': "none"});
		}
		else{
			$personaje.css({'display': "block"});
		}
	}
		
	RepositionNav(); //Reposition the Navigation to center it in the window when the script loads
	
	$window.resize(function(){ //if the user resizes the window...
		Move(); //move the background images in relation to the movement of the scrollbar
		RepositionNav(); //reposition the navigation list so it remains vertically central
	});		
	
	$window.bind('scroll', function(){ //when the user is scrolling...
		Move(); //move the background images in relation to the movement of the scrollbar
	});
	
});