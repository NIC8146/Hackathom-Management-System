document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".card").forEach((card) => {
        card.addEventListener("click", function () {
            let url = this.getAttribute("data-url");
            window.location.replace(url);
        });
    });
});
