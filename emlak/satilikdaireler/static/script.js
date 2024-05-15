document.addEventListener('DOMContentLoaded', function() {
    var sliders = document.getElementsByClassName('resim-slider');
    
    for (var i = 0; i < sliders.length; i++) {
        var resimler = sliders[i].getElementsByClassName('slider-resim');
        var index = 0;
        
        setInterval(function() {
            resimler[index].style.opacity = 0;
            index = (index + 1) % resimler.length;
            resimler[index].style.opacity = 1;
        }, 2000);
    }
});

