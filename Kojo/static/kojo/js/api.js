const api = {
  key: "752e22a992aa635abeceaadf584e933b",
  url: "https://api.openweathermap.org/data/2.5/weather",
};

let globalTemp = null;
const ciudad = document.getElementById("ciudad");
const fecha = document.getElementById("fecha");
const tempImg = document.getElementById("tempImg");
const temperatura = document.getElementById("temperatura");
const clima = document.getElementById("clima");
const rango = document.getElementById("rango");

async function search(query) {
  try {
    const response = await fetch(
      `${api.url}?q=${query}&appid=${api.key}&lang=es`
    );
    const data = await response.json();
    console.log(data);
    ciudad.innerHTML = `${data.name}, ${data.sys.country}`;
    fecha.innerHTML = new Date().toLocaleDateString();
    temperatura.innerHTML = `${toCelsius(data.main.temp)}°C`;
    localStorage.setItem("temperaturaP", toCelsius(data.main.temp));
    clima.innerHTML = data.weather[0].description;
    rango.innerHTML = `${toCelsius(data.main.temp_min)}°C/${toCelsius(
      data.main.temp_max
    )}°C`;
    updateImagenes(data);
  } catch (err) {
    console.log(err);
    alert("INGRESE UNA CIUDAD CORRECTA");
  }
}

function toCelsius(kelvin) {
  return Math.round(kelvin - 273.15);
}

function onSubmit(event) {
  event.preventDefault();
  search(searchBox.value);
}



function updateImagenes(data) {
  const temperatura = toCelsius(data.main.temp);
  let src = "imagen/temp-mid.png";
  if (temperatura > 26) {
    src = "imagen/temp-high.png";
  } else if (temperatura < 20) {
    src = "imagen/temp-low.png";
  }
  tempImg.src = src;
}

const searchForm = document.getElementById("search-form");
const searchBox = document.getElementById("searchBox");
searchForm.addEventListener("submit", onSubmit, true);
