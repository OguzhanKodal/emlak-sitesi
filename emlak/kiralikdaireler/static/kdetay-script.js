$(document).ready(function() {
    var carousel = $('.carousel');
    var modalImage = $('#modalImage');
  
    carousel.carousel({
      interval: 5000
    });
  
    $('.carousel-control-prev').click(function() {
      $(this).closest('.carousel').carousel('prev');
    });
  
    $('.carousel-control-next').click(function() {
      $(this).closest('.carousel').carousel('next');
    });
  
    $('.carousel-item img').click(function() {
      var src = $(this).attr('src');
      modalImage.attr('src', src);
      $('#imageModal').modal('show');
    });
  
    $('#imageModal').on('shown.bs.modal', function() {
      carousel.carousel('pause');
    });
  
    $('#imageModal').on('hidden.bs.modal', function() {
      carousel.carousel('cycle');
    });
  });


  // detay-script.js
document.addEventListener('DOMContentLoaded', function () {
    const favoriEkleBtn = document.getElementById('favoriEkle');
    favoriEkleBtn.addEventListener('click', function () {
        // Favori ekleme işlemini gerçekleştir (AJAX istekleri veya diğer işlemler)
        // ...

        // Modal'i kapat
        const modal = bootstrap.Modal.getInstance(favoriEkleBtn.closest('.modal'));
        modal.hide();

        // Başarı mesajı göster
        alert('İlan favorilere eklendi!');
    });
});
