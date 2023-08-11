function exportToCSV() {
  var filename = 'Participantes.csv';  // Reemplaza con el nombre de archivo CSV que deseas descargar

  var table = document.querySelector('.mi-tabla');  // Reemplaza '.mi-tabla' con el selector correcto de tu tabla
  var headers = table.querySelectorAll('th');
  var rows = table.querySelectorAll('tbody tr');

  var csvContent = [];

  // Agregar encabezados al contenido CSV
  var headerRow = [];
  headers.forEach(function(header) {
    headerRow.push(header.textContent);
  });
  csvContent.push(headerRow.join(','));

  // Agregar filas al contenido CSV
  rows.forEach(function(row) {
    var rowData = [];
    var cells = row.querySelectorAll('td');
    cells.forEach(function(cell) {
      rowData.push(cell.textContent);
    });
    csvContent.push(rowData.join(','));
  });

  var fileContent = csvContent.join('\n');

  var link = document.createElement('a');
  link.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(fileContent);
  link.download = filename;
  link.click();
}
function exportToExcel() {
  var filename = 'Participantes.xlsx';
  var table = document.querySelector('.mi-tabla');

  // Crea un objeto Workbook de xlsx
  var wb = XLSX.utils.table_to_book(table);

  // Genera el archivo Excel
  var wbout = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });

  // Crea un Blob a partir del array de bytes
  var blob = new Blob([wbout], { type: 'application/octet-stream' });

  // Crea un enlace y lo descarga
  var link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = filename;
  link.click();
}



//PDF
document.addEventListener("DOMContentLoaded", () => {
  const $boton = document.querySelector("#btnCrearPDF");
  $boton.addEventListener("click", () => {
    const $elementoParaConvertir = document.querySelector(".mi-tabla");

    // Obtener las filas de la tabla
    const filas = $elementoParaConvertir.querySelectorAll("tbody tr");

    // Crear una nueva tabla solo con las columnas deseadas
    const nuevaTabla = document.createElement("table");
    nuevaTabla.classList.add("mi-tabla");

    // Crear el encabezado de la tabla
    const encabezado = document.createElement("thead");
    const encabezadoFila = document.createElement("tr");
    const columnasDeseadas = ["Matricula", "Universidad", "Nombre", "Apellido Paterno", "Apellido Materno","Grado", "Carrera", "Curp", "Disciplina", "Rama", "Fecha de Ingreso", "Ciclo Escolar", "Sexo", "NSS"];

    columnasDeseadas.forEach(columna => {
      const encabezadoColumna = document.createElement("th");
      encabezadoColumna.textContent = columna;
      encabezadoFila.appendChild(encabezadoColumna);
    });

    encabezado.appendChild(encabezadoFila);
    nuevaTabla.appendChild(encabezado);

    // Copiar las filas deseadas a la nueva tabla
    const cuerpo = document.createElement("tbody");

    filas.forEach(fila => {
      const nuevaFila = document.createElement("tr");
      const columnas = fila.querySelectorAll("td");

      columnasDeseadas.forEach((_, index) => {
        const columnaDeseada = document.createElement("td");
        columnaDeseada.innerHTML = columnas[index].innerHTML;
        nuevaFila.appendChild(columnaDeseada);
      });

      cuerpo.appendChild(nuevaFila);
    });

    nuevaTabla.appendChild(cuerpo);

    // Ocultar las columnas innecesarias en la tabla original
    const columnasOcultas = $elementoParaConvertir.querySelectorAll("th:not(:first-child):not(:nth-child(2)):not(:nth-child(3)):not(:nth-child(4)):not(:nth-child(5)):not(:nth-child(6)):not(:nth-child(7)):not(:nth-child(8)), td:not(:first-child):not(:nth-child(2)):not(:nth-child(3)):not(:nth-child(4)):not(:nth-child(5)):not(:nth-child(6)):not(:nth-child(7)):not(:nth-child(8))");
    columnasOcultas.forEach(columna => {
      columna.style.display = "none";
    });

    // Generar el PDF
    html2pdf()
      .set({
        margin: 1,
        filename: 'Participantes.pdf',
        html2canvas: {
          scale: 3,
          letterRendering: true,
        },
        jsPDF: {
          unit: "in",
          format: "b3",
          orientation: 'portrait'
        }
      })
      .from(nuevaTabla)
      .save()
      .catch(err => console.log(err))
      .finally(() => {
        // Restaurar la visibilidad de las columnas ocultas
        columnasOcultas.forEach(columna => {
          columna.style.display = "";
        });
        console.log("Guardado!!");
      });
  });
});



