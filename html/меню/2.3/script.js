document.addEventListener('DOMContentLoaded', function () {
    const showMenuButton = document.getElementById('showMenu');
    const menu = document.getElementById('menu');
    const overlay = document.getElementById('overlay');
    const closePopupButton = document.getElementById('closePopup');
    const categories = document.querySelectorAll('.category');
    const categoryItems = document.querySelectorAll('.categoryItem');

    showMenuButton.addEventListener('click', function () {
        menu.classList.toggle('hidden');
    });

    overlay.addEventListener('click', function () {
        overlay.classList.add('hidden');
    });

    closePopupButton.addEventListener('click', function () {
        overlay.classList.add('hidden');
    });

    categories.forEach(function (category) {
        category.addEventListener('click', function () {
            const categoryToShow = this.dataset.category;
            categoryItems.forEach(function (item) {
                item.classList.remove('active');
            });
            document.querySelector(`.${categoryToShow}`).classList.add('active');
        });
    });

    const detailsButtons = document.querySelectorAll('.details');
    detailsButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const menuItem = this.parentElement;
            const title = menuItem.querySelector('h3').innerText;
            const content = menuItem.querySelectorAll('p:not([class])').innerText;

            const popupTitle = document.getElementById('popupTitle');
            const popupContent = document.getElementById('popupContent');

            popupTitle.innerText = title;
            popupContent.innerText = content;

            overlay.classList.remove('hidden');
        });
    });
});
