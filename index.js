function toggleMenu() {
    let menu = document.querySelector(".nav-links");

    if (menu.classList.contains("show")) {
        // Se já tem a classe, remove (fecha o menu)
        menu.classList.remove("show");
    } else {
        // Se não tem, adiciona (abre o menu)
        menu.classList.add("show");
    }
}
