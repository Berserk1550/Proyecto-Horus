document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("ventana_proceso");
  const cerrarBtn = document.querySelector("#ventana_proceso .cerrar");
  const tipoVehiculoInput = document.getElementById("tipo_vehiculo_input");
  const formOperacion = document.getElementById("form_operacion");

  // Iconos disparan modal
  document.getElementById("btn_carro").addEventListener("click", () => {
    tipoVehiculoInput.value = "carro";
    modal.style.display = "flex";
  });
  document.getElementById("btn_moto").addEventListener("click", () => {
    tipoVehiculoInput.value = "moto";
    modal.style.display = "flex";
  });

  // Cerrar modal
  cerrarBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Registrar ingreso
  document.getElementById("registrar_ingreso").addEventListener("click", async () => {
    const datos = new FormData(formOperacion);
    try {
      const response = await fetch("/operaciones/ingreso", { method: "POST", body: datos });
      const data = await response.json();
      console.log("Respuesta ingreso:", data);

      if (data.ok) {
        alert("Ingreso realizado con éxito 🚗🏍️");
      } else {
        alert("Error en ingreso: " + data.error);
      }
    } catch (err) {
      alert("Error de conexión al registrar ingreso");
    }
    formOperacion.reset();        // limpia el input SIEMPRE
    modal.style.display = "none"; // cierra el modal SIEMPRE
  });

  // Liberar salida
  document.getElementById("liberar_salida").addEventListener("click", async () => {
    const datos = new FormData(formOperacion);
    try {
      const response = await fetch("/operaciones/salida", { method: "POST", body: datos });
      const data = await response.json();
      console.log("Respuesta salida:", data);

      if (data.ok) {
        alert("Salida registrada con éxito ✅");
      } else {
        alert("Error en salida: " + data.error);
      }
    } catch (err) {
      alert("Error de conexión al registrar salida");
    }
    formOperacion.reset();        // limpia el input SIEMPRE
    modal.style.display = "none"; // cierra el modal SIEMPRE
  });
});
