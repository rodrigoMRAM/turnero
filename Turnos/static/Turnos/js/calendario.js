// Obtener referencia al elemento contenedor del calendario
var calendarContainer = document.getElementById("calendar");

// Obtener referencia a los botones de navegación
var prevButton = document.getElementById("prevButton");
var nextButton = document.getElementById("nextButton");

// Definir el rango de años
var startYear = 2023;
var endYear = 2030;

// Variables para el año y mes actual
var currentYear = new Date().getFullYear();
var currentMonth = new Date().getMonth();

// Renderizar el calendario inicial
renderCalendar(currentYear, currentMonth);

// Agregar eventos click a los botones de navegación
prevButton.addEventListener("click", goToPreviousMonth);
nextButton.addEventListener("click", goToNextMonth);

// Función para renderizar el calendario
function renderCalendar(year, month) {
  // Crear una instancia de fecha para el primer día del mes
  var firstDay = new Date(year, month, 1);

  // Obtener el día de la semana del primer día (0-6, donde 0 es domingo)
  var firstDayOfWeek = firstDay.getDay();

  // Obtener el número de días en el mes
  var daysInMonth = new Date(year, month + 1, 0).getDate();

  // Crear la estructura del calendario
  var calendarHTML = '<table class="mitabla">';
  calendarHTML += '<caption>' + getMonthName(month) + ' ' + year + '</caption>';
  calendarHTML += '<tr><th>D</th><th>L</th><th>M</th><th>M</th><th>J</th><th>V</th><th>S</th></tr>';
  calendarHTML += '<tr>';

  // Agregar celdas vacías hasta el primer día de la semana
  for (var i = 0; i < firstDayOfWeek; i++) {
    calendarHTML += '<td></td>';
  }

  // Agregar celdas con los números de los días del mes
  var dayCount = 1;
  for (var j = firstDayOfWeek; j < 7; j++) {
    var date = getDateLink(year, month + 1, dayCount);
    calendarHTML += '<td><a href="' + date + '">' + getTwoDigitNumber(dayCount) + '</a></td>';
    dayCount++;
  }

  calendarHTML += '</tr>';

  // Agregar las filas restantes del calendario
  while (dayCount <= daysInMonth) {
    calendarHTML += '<tr>';
    for (var k = 0; k < 7 && dayCount <= daysInMonth; k++) {
      var date = getDateLink(year, month + 1, dayCount);
      calendarHTML += '<td><a href="' + date + '">' + getTwoDigitNumber(dayCount) + '</a></td>';
      dayCount++;
    }
    calendarHTML += '</tr>';
  }

  calendarHTML += '</table>';

  // Agregar el HTML generado al contenedor del calendario
  calendarContainer.innerHTML = calendarHTML;
}

// Función para obtener el nombre del mes
function getMonthName(month) {
  var monthNames = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
  ];
  return monthNames[month];
}

// Función para obtener el número de dos dígitos
function getTwoDigitNumber(number) {
  return number.toString().padStart(2, '0');
}

// Función para obtener el enlace de la fecha
function getDateLink(year, month, day) {
  var formattedMonth = getTwoDigitNumber(month);
  var formattedDay = getTwoDigitNumber(day);
  return "/recolectando/" + year + "-" + formattedMonth + "-" + formattedDay;
}

// Función para ir al mes anterior
function goToPreviousMonth() {
  currentMonth--;
  if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  }
  renderCalendar(currentYear, currentMonth);
}

// Función para ir al siguiente mes
function goToNextMonth() {
  currentMonth++;
  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }
  renderCalendar(currentYear, currentMonth);
}
