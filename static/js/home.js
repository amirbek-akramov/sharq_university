window.addEventListener("DOMContentLoaded", () => {
    // Reviewing elements on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show")
            }
        });
    });

    const hiddenElements = document.querySelectorAll(".hidden");

    hiddenElements.forEach((el) => observer.observe(el));
    // ##########################

    // Parallax effect on background
    let background_image = document.getElementById("background_image")

    window.addEventListener('scroll', function () {
        let value = window.scrollY;
        background_image.style.backgroundSize = 140 + value*0.07 + "%"
    })
    // ##########################
})