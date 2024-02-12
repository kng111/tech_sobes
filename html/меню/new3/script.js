function showDetails(name, description, calories) {
    const itemDetails = document.querySelector('.item-details');
    const overlay = document.getElementById('overlay'); 
    const itemName = itemDetails.querySelector('#item-name');
    const itemDescription = itemDetails.querySelector('#item-description');
    const itemCalories = itemDetails.querySelector('#item-calories');

    itemName.textContent = name;
    itemDescription.textContent = description;
    itemCalories.textContent = 'Калории: ' + calories;

    itemDetails.style.display = 'block';
    overlay.style.display = 'block'; 
    document.body.style.overflow = 'hidden'; 
}

function closeDetails() {
    const itemDetails = document.querySelector('.item-details');
    const overlay = document.getElementById('overlay'); 

    itemDetails.style.display = 'none';
    overlay.style.display = 'none'; 
    document.body.style.overflow = 'auto'; 
}

document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.item');
    const categoryButtons = document.querySelectorAll('.category-btn');
    const overlay = document.getElementById('overlay'); 

    categoryButtons.forEach(button => {
        button.addEventListener('click', function() {
            const category = this.dataset.category;

            menuItems.forEach(item => {
                if (category === 'all' || item.classList.contains(category)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            const name = this.querySelector('h2').textContent;
            const description = this.querySelector('p').textContent;
            const calories = this.querySelector('.price').textContent;

            showDetails(name, description, calories);
        });
    });

    const closeDetailsBtn = document.querySelector('.close-details');
    closeDetailsBtn.addEventListener('click', closeDetails);
});
