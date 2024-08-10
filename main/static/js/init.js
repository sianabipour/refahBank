/*
 * Lawyers - WP Theme
 *
 * Author: https://matchthemes.com
 *
 */
 
(function($) {
    "use strict";
	
	// home slider
	$('.home-slider').owlCarousel({
    items:1,
    loop:true,
	autoplay:true,
	autoplayTimeout:5000,
	animateOut: 'fadeOut',
	dots:false,
	nav:true,
	navText:''
});

	// testimonials slider
	$('.testimonials-slider').owlCarousel({
    items:1,
    loop:true,
	autoplay:true,
	autoplayTimeout:7000,
	animateOut: 'fadeOut',
	dots:true,
	nav:false,
	navText:''
});

//mobile menu
$('.nav-button').on('click', function(e){
	
	e.preventDefault();
	
    $('.mobile-menu-holder, .menu-mask').addClass('is-active');
	$('body').addClass('has-active-menu');

});

$('.exit-mobile, .menu-mask').on('click', function(e){
	
	e.preventDefault();

    $('.mobile-menu-holder, .menu-mask').removeClass('is-active');
	$('body').removeClass('has-active-menu');

});

$('.menu-mobile > li.menu-item-has-children > a').on('click', function(e){
			
			e.preventDefault();
			e.stopPropagation();
			
			if ( $(this).parent().hasClass('menu-open') )
			
			$(this).parent().removeClass('menu-open');
			
			else {
			
			$(this).parent().addClass('menu-open');
			
			}
																  
			});
	
	// end mobile menu
	
// menu edge screen turn left

$(".menu-nav li").on('mouseenter mouseleave', function (e) {
        if ($('ul', this).length) {
            var elm = $('.sub-menu', this);
            var off = elm.offset();
            var l = off.left;
            var w = elm.width();
            var docW = $(window).width();

            var isEntirelyVisible = (l + w <= docW);

            if (!isEntirelyVisible) {
                $(this).addClass('edge');
            } else {
                $(this).removeClass('edge');
            }
        }
    });		
	
$(window).on('load', function() {
	
	//masonry
   var portfolioItems = $('.layout-masonry');
   
   portfolioItems.isotope({
  itemSelector : '.blog-item-masonry',
  layoutMode : 'masonry',
 
	});
	
	// filter items when filter link is clicked
 $('.portfolio-filter a').on('click', function(){
 $('.portfolio-filter .current').removeClass('current');
 $(this).addClass('current');
		
  var selector = $(this).attr('data-filter');
  portfolioItems.isotope({ filter: selector });
  return false;
});


});	//window.load	

	//gallery

	$('.gal-img a, .blocks-gallery-item a').magnificPopup({
	type: 'image',
	gallery:{
		enabled:true
			}
	});
	
$('.faq-section').hide();

$('.faq-title').on('click', function(){

  if( $(this).next().is(':hidden') ) {
  
  $('.faq-title').removeClass('active').next().slideUp(); 
  $(this).toggleClass('active').next().slideDown();
  
  } else {
   $('.faq-title').removeClass('active').next().slideUp();
 }
  return false; 
 });
 
 $(window).on('scroll', function() {
  if ($(document).scrollTop() > 1 ) {
    $('#header-bar').addClass('nav-fixed-top');
	} else {
    $('#header-bar').removeClass('nav-fixed-top');
  }
  
  });

$(".scrollup").hide();
     $(window).on('scroll', function() {
         if ($(this).scrollTop() > 400) {
             $('.scrollup').fadeIn();
         } else {
             $('.scrollup').fadeOut();
         }
     });

$("a.scrolltop[href^='#']").on('click', function(e) {
   e.preventDefault();
   var hash = this.hash;
   $('html, body').stop().animate({scrollTop:0}, 1000, 'easeOutExpo');

});

//fluid width videos

$('.blog-post-single, .custom-page-template').fitVids({customSelector: "iframe[src^='https://w.soundcloud.com']"});

})(jQuery);