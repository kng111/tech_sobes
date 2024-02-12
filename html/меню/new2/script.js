document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.item');
    const categoryButtons = document.querySelectorAll('.category-btn');

    categoryButtons.forEach(button => {
        button.addEventListener('click', function() {
            const category = this.dataset.category;

            menuItems.forEach(item => {
                item.style.display = 'none';
            });

            menuItems.forEach(item => {
                if (category === 'all' || item.classList.contains(category)) {
                    item.style.display = 'block';
                }
            });
        });
    });
});
