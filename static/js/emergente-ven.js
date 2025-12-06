    // emergente-ven.js
    document.addEventListener("DOMContentLoaded", function () {
    const btnIngreso = document.getElementById("btn_ingreso");
    const btnEgreso  = document.getElementById("btn_egreso");   // SIN guion bajo en la variable
    const modal      = document.getElementById("ventana_proceso");
    const cerrarBtn  = document.querySelector("#ventana_proceso .cerrar");

    const formIngreso = document.getElementById("form_ingreso");
    const formEgreso  = document.getElementById("form_egreso");

    // Validaciones defensivas
    if (!btnIngreso || !btnEgreso || !modal || !cerrarBtn || !formIngreso || !formEgreso) {
        console.error("Faltan elementos en el DOM. Revisa IDs: btn_ingreso, btn_egreso, ventana_proceso, .cerrar, form_ingreso, form_egreso.");
        return;
    }

    // Abrir modal con formulario de Egreso
    btnEgreso.addEventListener("click", function () {
        modal.style.display = "flex";
        formIngreso.style.display = "none";
        formEgreso.style.display  = "block";
    });

    

    // Cerrar modal con la X
    cerrarBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    
    });

