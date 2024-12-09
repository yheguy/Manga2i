document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".add-to-cart");

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const mangaId = this.dataset.id;

            fetch(`/add_to_cart/${mangaId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}",
                    "Content-Type": "application/json"
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message); // Affiche un message de confirmation
                } else {
                    alert("Erreur : " + data.message); // Affiche un message d'erreur
                }
            })
            .catch(error => {
                console.error("Erreur lors de l'ajout au panier :", error);
                alert("Une erreur est survenue.");
            });
        });
    });
});