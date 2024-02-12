let currentIndex = 0;

function scrollStocks(direction) {
    const container = document.getElementById('stock-container');
    const stocks = container.querySelectorAll('.stock-item');
    
    if (direction === 'left' && currentIndex > 0) {
        currentIndex--;
    } else if (direction === 'right' && currentIndex < stocks.length - 1) {
        currentIndex++;
    }

    stocks.forEach((stock, index) => {
        if (index === currentIndex) {
            stock.style.display = 'block';
        } else {
            stock.style.display = 'none';
        }
    });
}
