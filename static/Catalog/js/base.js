//Анимация в main
    document.addEventListener('DOMContentLoaded', function() {
        const slides = document.querySelectorAll('.slide');
        let currentSlide = 0;
        let slideInterval;

        function showSlide(n) {
            slides[currentSlide].classList.remove('active');
            currentSlide = (n + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
        }

        function nextSlide() {
            showSlide(currentSlide + 1);
        }

        function startSlideShow() {
            slideInterval = setInterval(nextSlide, 5000); // 5 секунд
        }

        // Инициализация
        slides.forEach((slide, index) => {
            slide.style.zIndex = -index; // Правильное наложение
            if (index === 0) slide.classList.add('active');
        });

        startSlideShow();
    });

//Модальное окно


// Получаем элементы
const modal = document.getElementById("modal");
const btn = document.getElementById("openModalBtn");
const span = document.getElementsByClassName("close")[0];

// Открываем модальное окно при клике на кнопку
btn.onclick = function() {
  modal.style.display = "block";
}

// Закрываем при клике на крестик
span.onclick = function() {
  modal.style.display = "none";
}

// Закрываем при клике вне окна
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
