document.querySelectorAll('.update-stock').forEach(button => {
    button.addEventListener('click', function() {
        let mangaId = this.getAttribute('data-manga-id');
        let action = this.getAttribute('data-action');
        
        let stockSpan = document.getElementById(`stock-${mangaId}`);
        let hiddenStockInput = document.getElementById(`hidden-stock-${mangaId}`);
        let currentStock = parseInt(stockSpan.textContent);
        
        if (action === 'increase') {
            stockSpan.textContent = currentStock + 1;
            hiddenStockInput.value = currentStock + 1;  
        } else if (action === 'decrease' && currentStock > 0) {
            stockSpan.textContent = currentStock - 1;
            hiddenStockInput.value = currentStock - 1;  
        }
    });
});

document.querySelectorAll('form[id^="update-manga-form-"]').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault(); 
        
        const mangaId = this.dataset.mangaId;
        const formData = new FormData(this); 
        const url = this.action; 

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value 
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors de la requête : ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                document.getElementById(`stock-${form.dataset.mangaId}`).textContent = data.new_stock;
                alert(`${data.title} mis à jour avec succès ! \n New price: ${data.new_price}€ | New stock: ${data.new_stock}`);
            } else {
                alert('Erreur : ' + data.error);
            }
        })
        .catch(error => {
            console.error('Erreur AJAX :', error);
            alert('Une erreur est survenue.');
        });
    });
});