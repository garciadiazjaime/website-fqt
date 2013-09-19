var folder = '';
var server = get_server_path() + folder;

$(window).load(function() {
	var page = get_currentpage();
	var last_item = getLastItem(page)

	if(last_item.length && $('#' + last_item).length){
		if(page.indexOf('programas') !== -1)
		{
			gotoTop(last_item, '', '450')
			//console.log('here: ' + $('#'+last_item).top)
			//$.scrollTo('#'+last_item, 800);
		}		
		else			
			gotoTop(last_item)				
	}else if(page.indexOf('ecocapsulas') !== -1)
	{
		gotoTop('ecocapsulas')
	}

	
	// CUSTOM FORM ELEMENTS
	if($('.mySelectBoxClass').length)
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

	if($('.slideshow_right').length)
		$('.slideshow_right').cycle({
			fx: 'scrollRight', // choose your transition type, ex: fade, scrollUp, shuffle, etc...	    
		});

	if($('.slideshow_left').length)
		$('.slideshow_left').cycle({
			fx: 'scrollLeft', // choose your transition type, ex: fade, scrollUp, shuffle, etc...	    
		});

	if($('#slideshow_nosotros').length)
		$('#slideshow_nosotros').cycle({
			fx: 'fade', // choose your transition type, ex: fade, scrollUp, shuffle, etc...	    
		});
	/*
		$('#slideshow_nosotros').bjqs({
		    height      : 320,
		    width       : 433,
		    responsive  : true
		  });
	*/
	$('.block_programas a.prev').click(function(){
		console.log('pref')
		return false
	})

	$('.block_programas a.next').click(function(){
		console.log('next')
		return false
	})

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
			},
			overlayColor: '#000000', 
			overlayOpacity:'.6',
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
			width : 395,
			onComplete	: function() {
			    load_fancy_program()
			},
		})

	if($('#transparencia_fancybox').length)
		$('#transparencia_fancybox').fancybox(
			{
				autoScale : false,
				height: 400,
				overlayColor: '#000000', 
				overlayOpacity:'.6',
			    responsive  : false,
				width: 1045,
			}
		)
	
	
	

	// *********************** ECOTIPS *********************************
	$('#ecotips_list li').click(function(){
			var thumb_id = $(this).attr('id');
			showDivEcotips(thumb_id);
			return false;
		}
	);

	$("#forma_voluntarios").submit(function() {
		console.log('gere')
		flag = true
		if($('#name').val() == '')
		{
			$('#name').prev().addClass('required')
			flag = false
		}
		else
			$('#name').prev().removeClass('required')

		if($('#edad').val() == '')
		{
			$('#edad').prev().addClass('required')
			flag = false
		}
		else
			$('#edad').prev().removeClass('required')

		if($('#email').val() == '')
		{
			$('#email').prev().addClass('required')
			flag = false
		}
		else
			$('#email').prev().removeClass('required')

		if($('#ocupacion').val() == '')
		{
			$('#ocupacion').prev().addClass('required')
			flag = false
		}
		else
			$('#ocupacion').prev().removeClass('required')

		if($('#select_apoyo').val() == '')
		{
			$('#select_apoyo').prev().addClass('required')
			flag = false
		}
		else
			$('#select_apoyo').prev().removeClass('required')

		if(!flag)
			$('#msg').html('Favor de llenar los campos marcados')
		else
		{
			$('#msg').html('Enviando datos, por favor espera...')
		}
		return false;
	});

	
	if($('.logo_slideshow').length)
	{
		//each li 940
		$('.buttons a').click(function(){
			dir = $(this).attr('class')
			console.log(dir)		
			sign = (dir == 'next') ? '-':'+'
			ul = $(this).parent().next().children()
			howmany_children = ul.children().length
			limit_right = (howmany_children-1) * 850 * -1
			margin_left = $(ul).css('margin-left').replace('px', '')			
			can_right = margin_left > limit_right ? true : false
			can_left = margin_left < 0 ? true : false

			console.log(margin_left + " " + limit_right)
			console.log("can_right: " + can_right)
			console.log("can_left: " + can_left)
			

			if( (dir == 'next' && can_right)
				|| (dir == 'prev' && can_left)
					)
				$(ul).stop().animate(
			 		{
		            	marginLeft: sign + '=1000px'
		        	},
		        	600
		        )
		    return false			
		})

		$('.no_link').click(function(){
			return false
		})

		if($('#btn_donar').length)
			$('#btn_donar').click(function(){
				$('#form_donar').submit()
				return false
			})			
	}
		 
	if($('#gmap').length) load_gmap()

	if($('#form_contact').length) load_contact_form()
		

	/*
		$('.logo_slideshow').serialScroll({		
			items:'li',
			prev:'.screen_logos a.prev',
			next:'.screen_logos a.next',
			offset:-230, //when scrolling to photo, stop 230 before reaching it (from the left)
			start:1, //as we are centering it, start at the 2nd
			duration:1200,
			force:true,
			stop:true,
			lock:false,
			cycle:true, //don't pull back once you reach the end
			//easing:'easeOutQuart', //use this easing equation for a funny effect
			jump: true //click on the images to scroll to them			
		});
	*/
});

function load_contact_form()
{
	var lang = 0;
	var msg_fill_fields = new Array('Favor de llenar campos marcados en rojo', 'Plase fill all fields in red');
	var msg_valid_email = new Array('Favor de captura un email correcto.', 'Please put a valid email.');
	var msg_sending = new Array('Enviando mensaje, Favor espera...', 'Sending message, please waite...');
	var msg_success = new Array('Mensaje enviado correctamente, gracias.', 'Your message has been sent, thank you.');
	var msg_error = new Array('Lo sentimos el mensaje no se pudo enviar, favor de intetar mas tarde.', 'We are sorry, the message could not been sent, please try later.');
	$("#form_contact").submit(function() {		
		$('#message').html('')
		flag = true
		if($('#name').val() == '')
		{
			$('#name').prev().addClass('required');
			flag = false;
		}
		else
			$('#name').prev().removeClass('required');

		if($('#email').val() == '')
		{
			$('#email').prev().addClass('required');
			flag = false;
		}
		else
			$('#email').prev().removeClass('required');

		if($('#message').val() == '')
		{
			$('#message').prev().addClass('required');
			flag = false;
		}
		else
			$('#message').prev().removeClass('required');

		if(!flag)
			$('#msg').html('Favor de llenar los campos marcados');
		else
		{
			$('#msg').html('Enviando datos, por favor espera...');
			$.post("send_mail_form", $("#form_contact").serialize(), function(data){
				if(data == 'success')
				{
					$('#msg').text(msg_success[lang]); 
					clear_form('form_contact');
				}
				else if(data == 'empty_data') $('#msg').text(msg_fill_fields[lang]);
				else $('#msg').text(msg_error[lang]);
			})
		}
		return false;
	});
}

function load_gmap()
{
	$('#gmap').html('<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=+32.529906,-117.0395&amp;aq=&amp;sll=37.0625,-95.677068&amp;sspn=61.153041,129.550781&amp;ie=UTF8&amp;ll=32.529906,-117.0395&amp;spn=0.002031,0.003954&amp;t=m&amp;z=17&amp;output=embed"></iframe><p id="big_map"><a href="https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=en&amp;geocode=&amp;q=+32.529906,-117.0395&amp;aq=&amp;sll=37.0625,-95.677068&amp;sspn=61.153041,129.550781&amp;ie=UTF8&amp;ll=32.529906,-117.0395&amp;spn=0.002031,0.003954&amp;t=m&amp;z=14" target="_blank">Ver mapa más grande</a></p>')
}

function load_fancy_program()
{
	$('#forma_inscripcion').submit(function(){
		console.log('here')
		flag = true
		$('#msg_ins').text('')
		if($('#nombre').val() == '')
		{
			$('#nombre').prev().addClass('required')
			flag = false
		}
		else
			$('#nombre').prev().removeClass('required')

		if($('#email').val() == '')
		{
			$('#email').prev().addClass('required')
			flag = false
		}
		else
			$('#email').prev().removeClass('required')

		if($('#mensaje').val() == '')
		{
			$('#mensaje').prev().addClass('required')
			flag = false
		}
		else
			$('#mensaje').prev().removeClass('required')

		if(flag == false)
			$('#msg_ins').text('Favor de llenar los campos marcados')
		else
		{
			$('#msg_ins').text('...enviando datos')
			fields = $(this).serialize()
			$.post("programa_inscribite", $(this).serialize(), function(data){
				if(data == 'success')
				{
					$('#form_wrapper').html('<b>Mensaje enviado, gracias.</b>')
					$('#msg_ins').text(''); 
					clear_form('forma_inscripcion');
				}
				else $('#msg_ins').text('Lo sentimos, intentar m\xE1s tarde.');
			});
		}
		return false
	})
}
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
	console.log('gototop')
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

jQuery.fn.reset = function () {
  $(this).each (function() { this.reset(); });
}