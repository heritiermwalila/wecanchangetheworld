jQuery(document).ready(function($){

    $('.mobile-menu-handler').on('click', function(){
        $('.menu-container').slideToggle()
    })

    //slick
    $('.tagline-container').slick({
      adaptiveHeight:true,
      autoplay:true,
      arrows:false,
      useCSS:true
    });

//
//    $('#change-makers').slick({
//      adaptiveHeight:true,
//      autoplay:true,
//      arrows:false,
//      useCSS:false,
//    })

    var date = new Date()
    var fullYear = date.getFullYear()

    var footer = document.querySelector('.footer-credit')
    footer.innerHTML = '<p><span> &copy; ' + fullYear + ' Copyright' + ' All right reserved </span></p> Website Designed by '
    + '<a href="https://www.quirky30.co.za/" target="_blank"> Quirky Innovations </a>'

    window.addEventListener('scroll', scrollFun)

    var menu = document.getElementById('main-menu-container')
    var sticky = menu.offsetTop
    function scrollFun(){
        if(window.pageYOffset > sticky){
            menu.classList.add('fixed-menu')
        }else{
            menu.classList.remove('fixed-menu')
        }
    }
})

$(function() {
  var $slideshow = $('#change-makers');
  var ImagePauses = 86400000;

  // Init
  $slideshow.slick({
    initialSlide: 0,
    autoplay: true,
    autoplaySpeed: ImagePauses,
    useCSS:false,
  });

  // Sliding settings
  $slideshow.on('afterChange', function(event, slick, currentSlide) {

    // Update autoplay speed according to slide index
    $slideshow.slick('slickSetOption', 'autoplaySpeed', ImagePauses[currentSlide], true);
  });

});