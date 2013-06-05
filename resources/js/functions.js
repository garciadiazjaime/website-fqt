var folder = ':8000/';
var server = get_server_path() + folder;

$(window).load(function() {
	var page = get_currentpage();
	console.log(page)
	var last_item = getLastItem(page)

	if(last_item.length && $('#' + last_item).length){
		if(page.indexOf('programas') !== -1)
			gotoTop(last_item, '', '450')
		else			
			gotoTop(last_item)				
	}else if(page.indexOf('ecocapsulas') !== -1)
	{
		console.log('here')
		gotoTop('ecocapsulas')
	}

	
	// CUSTOM FORM ELEMENTS
	$('.mySelectBoxClass').customSelect();
/*	$("input[type=file]").filestyle({ 
	     image: "static/media/grey.gif",
	     imageheight : 22,
	     imagewidth : 82,
	     width : 300
	 }); */
	
	$('#wrapper').animate({
		'opacity': '1'
	},  'slow', function(){
	});
		
	$('.goto_top').click(function(){ 
		var item = $(this).attr('href');
		id = getLastItem(item)			
		gotoTop(id, '', '-100')				
		window.history.pushState( id, id, item);
		return false;
	});

	// *********************** Slider simple - NOSOTROS y PROGRAMAS ***********************************

	$('.slideshow').cycle({
		fx: 'fade', // choose your transition type, ex: fade, scrollUp, shuffle, etc...	    
	});

	$('#slideshow_nosotros').bjqs({
	    height      : 320,
	    width       : 433,
	    responsive  : true
	  });
	
	/*
	$('.slideshow').bjqs({	    
	    responsive  : true
	  });
	
	
	
	$('#slideshow_reciclases').bjqs({
	    height      : 210,
	    width       : 433,
	    responsive  : true
	  });

	$('#slideshow_reciclases_jardin').bjqs({
	    height      : 185,
	    width       : 484,
	    responsive  : true
	  });

	$('#slideshow_proyecto_semilla').bjqs({
	    height      : 210,
	    width       : 433,
	    responsive  : true
	  });

	$('#slideshow_jovenes_transformando').bjqs({
	    height      : 210,
	    width       : 433,
	    responsive  : true
	  });

	$('#slideshow_laboratorio_vivo').bjqs({
	    height      : 210,
	    width       : 433,
	    responsive  : true
	  });
	*/

	$(".eco_fancybox").click(function(){
		$.fancybox({
			'padding'		: 0,
			'autoScale'		: false,
			'transitionIn'	: 'none',
			'transitionOut'	: 'none',
			'title'			: this.title,
			'width'			: '600',
			'height'		: '400',
			'href'			: this.href.replace(new RegExp("watch\\?v=", "i"), 'v/'),
			'type'			: 'swf',
			'swf'			: {
				'wmode'		: 'transparent',
				'allowfullscreen'	: 'true'
			}
		});
		return false
	})

	if($('.fancybox').length)
		$('.fancybox').fancybox({
			ajax : {
			    type	: "POST",
			    data	: 'mydata=test',
				
			},
			overlayColor: '#000000', 
			overlayOpacity:'.6',
			autoScale : false,
			width : 395
		})

	$('#transparencia_fancybox').fancybox(	{
			'left': itemLeft,
		})

	// *********************** ECOTIPS *********************************
	$('#ecotips_list li').click(function(){
			var thumb_id = $(this).attr('id');
			showDivEcotips(thumb_id);
			return false;
		}
	);

	$("form").submit(function() {
		console.log('here')
		return false;
	});

});

(function($) { 
         // slideTo function for nivo-slider
        $.slideTo = function(idx) {
            $('#slider').data('nivo:vars').currentSlide = idx - 1;
            $("#slider a.nivo-nextNav").trigger('click'); 
        }
  })(jQuery);



function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
}

function get_currentpage(){
	var loc = window.location;
	p = loc.href.substring(loc.href.indexOf(loc.host) + loc.host.length + folder.length );
	if(p == '') p = 'inicio';
	return p;
}

function gotoTop(id, speed , more){
	console.log(id)
	if(isNaN(speed))
		speed = 1250
	if(isNaN(more))
		more = 0

	if(id.length)
		$('html, body').animate({
			scrollTop: parseInt($('#'+id).offset().top -50 )
		}, speed);
}

function isFormReady() {
	var formChildren = $("form :input[type=text]"); // verificar inputs
	var flag = true;
	for (i = 0; i < (formChildren.length); i++) {
		if (formChildren[i].lang == 'es' && formChildren[i].value == '') {
				flag = false;
			$('#lab_'+formChildren[i].name).addClass('required');
		} else
			$('#lab_'+formChildren[i].name).removeClass('required');
	}

	var formChildren = $('select'); // selects
	for (i = 0; i < (formChildren.length); i++) {
		if ($(formChildren[i]).attr('lang') == 'es' && $(formChildren[i]).val() == 0) {
			if (flag) flag = false;
			$('#lab_'+formChildren[i].name).addClass('required');
		} else
			$('#lab_'+formChildren[i].name).removeClass('required');
	}

	var formChildren = $('textarea'); // textarea
	for (i = 0; i < (formChildren.length); i++) {
		if (formChildren[i].lang == 'es' && formChildren[i].value == '') {
			if (flag)
				flag = false;
			$('#lab_'+formChildren[i].name).addClass('required');
		} else
			$('#lab_'+formChildren[i].name).removeClass('required');
	}
	return flag;
}

function clearForm(){
	var formChildren = $("form :input[type=text]");
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).val('');
	}

	var formChildren = $("form :input[type=checkbox]");
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).attr('checked', false);
	}

	var formChildren = $('select'); // selects
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).val(0);
	}

	var formChildren = $('textarea'); // selects
	for (i = 0; i < (formChildren.length); i++) {
		$(formChildren[i]).val('');
	}
}

function getLastItem(cadena){
	var params = cadena.split('/');
	tmp = params.pop()
	if(!tmp.length)
		tmp = params.pop()
	return tmp;
}


function get_server_path(){
	var loc = window.location;
	return "http://" + loc.hostname;
}


function showDivEcotips(id)
{	
	if(id){	
		$('.ecotip_wrapper').hide();
    	$('.ecotip_wrapper').stop().animate({ opacity: 0 }, 300);
		$('#'+id+'_sld').show();	
    	$('#'+id+'_sld').stop().animate({ opacity: 1 }, 300);	
	}
}
