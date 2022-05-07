AOS.init({
   duration: 800,
   easing: "slide",
});

(function ($) {
   "use strict";

   var fullHeight = function () {
      $(".js-fullheight").css("height", $(window).height());
      $(window).resize(function () {
         $(".js-fullheight").css("height", $(window).height());
      });
   };
   fullHeight();

   // loader
   var loader = function () {
      setTimeout(function () {
         if ($("#ftco-loader").length > 0) {
            $("#ftco-loader").removeClass("show");
         }
      }, 1);
   };
   loader();

   $("nav .dropdown").hover(
      function () {
         var $this = $(this);
         // 	 timer;
         // clearTimeout(timer);
         $this.addClass("show");
         $this.find("> a").attr("aria-expanded", true);
         // $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
         $this.find(".dropdown-menu").addClass("show");
      },
      function () {
         var $this = $(this);
         // timer;
         // timer = setTimeout(function(){
         $this.removeClass("show");
         $this.find("> a").attr("aria-expanded", false);
         // $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
         $this.find(".dropdown-menu").removeClass("show");
         // }, 100);
      }
   );

   $("#dropdown04").on("show.bs.dropdown", function () {
      console.log("show");
   });

   // scroll
   var scrollWindow = function () {
      $(window).scroll(function () {
         var $w = $(this),
            st = $w.scrollTop(),
            navbar = $(".ftco_navbar"),
            sd = $(".js-scroll-wrap");

         if (st > 150) {
            if (!navbar.hasClass("scrolled")) {
               navbar.addClass("scrolled");
            }
         }
         if (st < 150) {
            if (navbar.hasClass("scrolled")) {
               navbar.removeClass("scrolled sleep");
            }
         }
         if (st > 350) {
            if (!navbar.hasClass("awake")) {
               navbar.addClass("awake");
            }

            if (sd.length > 0) {
               sd.addClass("sleep");
            }
         }
         if (st < 350) {
            if (navbar.hasClass("awake")) {
               navbar.removeClass("awake");
               navbar.addClass("sleep");
            }
            if (sd.length > 0) {
               sd.removeClass("sleep");
            }
         }
      });
   };
   scrollWindow();

   var counter = function () {
      $("#section-counter").waypoint(
         function (direction) {
            if (direction === "down" && !$(this.element).hasClass("ftco-animated")) {
               var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(",");
               $(".number").each(function () {
                  var $this = $(this),
                     num = $this.data("number");
                  console.log(num);
                  $this.animateNumber(
                     {
                        number: num,
                        numberStep: comma_separator_number_step,
                     },
                     7000
                  );
               });
            }
         },
         { offset: "95%" }
      );
   };
   counter();

   // magnific popup
   $(".image-popup").magnificPopup({
      type: "image",
      closeOnContentClick: true,
      closeBtnInside: false,
      fixedContentPos: true,
      mainClass: "mfp-no-margins mfp-with-zoom", // class to remove default margin from left and right side
      gallery: {
         enabled: true,
         navigateByImgClick: true,
         preload: [0, 1], // Will preload 0 - before current, and 1 after the current image
      },
      image: {
         verticalFit: true,
      },
      zoom: {
         enabled: true,
         duration: 300, // don't foget to change the duration also in CSS
      },
   });
})(jQuery);
