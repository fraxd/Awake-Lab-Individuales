$(document).ready(function () {
    $("#verVideo").click(function () {
        Fancybox.show([
            {
                src: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                type: "video",
                ratio: 16 / 10,
                width: 640,
                height: 360,
            },
        ]);
    });

    Fancybox.bind('[data-fancybox="single-image"]', {
        //
    });

    $("#verMapa").click(function () {
        Fancybox.show([
            {
                src: "https://www.google.com/maps/place/Coca+Cola+Logo/@-18.5285964,-70.2530801,15.92z",
                width: 800,
                height: 600,
            },
        ]);
    });
});