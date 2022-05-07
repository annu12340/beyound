AOS.init({
   duration: 800,
   easing: "slide",
});

(function ($) {
   "use strict";

   // loader
   var loader = function () {
      setTimeout(function () {
         if ($("#ftco-loader").length > 0) {
            $("#ftco-loader").removeClass("show");
         }
      }, 1);
   };
   loader();

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
