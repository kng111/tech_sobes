document.addEventListener('DOMContentLoaded', function () {
    const showMenuButton = document.getElementById('showMenu');
    const categoriesContainer = document.getElementById('categories');
    const menuContainer = document.getElementById('menu');
    const overlay = document.getElementById('overlay');
    const closePopupButton = document.getElementById('closePopup');

    showMenuButton.addEventListener('click', function () {
        categoriesContainer.innerHTML = ''; // Очищаем контейнер категорий
        menuContainer.innerHTML = ''; // Очищаем контейнер меню

        // Загрузка информации о категориях и меню из JSON
        fetch('menu.json')
            .then(response => response.json())
            .then(data => {
                // Создаем кнопки категорий
                data.categories.forEach(category => {
                    const categoryButton = document.createElement('button');
                    categoryButton.textContent = category.name;
                    categoryButton.addEventListener('click', function () {
                        // Фильтрация и отображение меню для выбранной категории
                        const categoryId = category.id;
                        menuContainer.innerHTML = ''; // Очищаем контейнер меню
                        data.menu[categoryId].forEach(item => {
                            const menuItem = createMenuItem(item);
                            menuContainer.appendChild(menuItem);
                        });
                        menuContainer.classList.remove('hidden');
                    });
                    categoriesContainer.appendChild(categoryButton);
                });

                // Функция для создания элемента меню
                function createMenuItem(item) {
                    const menuItem = document.createElement('div');
                    menuItem.classList.add('menuItem');
                    menuItem.id = item.id;
                    menuItem.innerHTML = `
                        <img src="${item.id}.jpg" alt="${item.name}">
                        <h3>${item.name}</h3>
                        <p>${item.description}</p>
                        <p>Калории: ${item.calories}</p>
                        <p>Состав: ${item.ingredients}</p>
                        <button class="details">Детали</button>
                    `;
                    menuItem.querySelector('.details').addEventListener('click', function () {
                        const title = item.name;
                        const content = `Состав: ${item.ingredients}<br>Калории: ${item.calories}`;
                        const popupTitle = document.getElementById('popupTitle');
                        const popupContent = document.getElementById('popupContent');
                        popupTitle.innerHTML = title;
                        popupContent.innerHTML = content;
                        overlay.classList.remove('hidden');
                    });
                    return menuItem;
                }
            })
            .catch(error => console.error('Ошибка загрузки меню:', error));
    });

    overlay.addEventListener('click', function () {
        overlay.classList.add('hidden');
    });

    closePopupButton.addEventListener('click', function () {
        overlay.classList.add('hidden');
    });
});
