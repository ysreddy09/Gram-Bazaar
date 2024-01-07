        let slideIndex = 0;

        function showSlides() {
            const slides = document.querySelectorAll('.slides img');
            for (let i = 0; i < slides.length; i++) {
                slides[i].style.display = 'none';
            }
            slideIndex++;
            if (slideIndex > slides.length) {
                slideIndex = 1;
            }
            slides[slideIndex - 1].style.display = 'block';
        }

        function prevSlide() {
            const slides = document.querySelectorAll('.slides img');
            slideIndex--;
            if (slideIndex < 1) {
                slideIndex = slides.length;
            }
            showSlides();
        }

        function nextSlide() {
            const slides = document.querySelectorAll('.slides img');
            slideIndex++;
            if (slideIndex > slides.length) {
                slideIndex = 1;
            }
            showSlides();
        }

        setInterval(showSlides, 3000); // Change slide every 3 seconds
