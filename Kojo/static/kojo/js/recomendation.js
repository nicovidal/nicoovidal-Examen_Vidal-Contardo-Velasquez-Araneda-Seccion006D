let texto = document.getElementById("textoR");
let botonR = document.getElementById("recomendation");

let texto1 =
    "la recomendaciones para esta temperatura baja son:se recomienda planter lechugas , ya que son aptas para climas bajos,En términos de actividad, las plantas sienten un estrés hídrico debido a las bajas temperaturas similar al de la temporada calor: el flujo de agua dentro de las plantas se reduce afectando la movilidad de los nutrientes, ocurre el cierre estomático y la planta puede llegar a presentar síntomas parecidos a la sequía,Plantas resistentes al frío: lavanda, col ornamental, durillo, hiedra, rododendro…";
let texto2 = "la recomendaciones para esta temperatura media son:las plantas mas adaptables para estas temperaturas medias son las siguientes El bambu, la flor Jasmin, eucalyptus, margarita";
let texto3 = "la recomendaciones para esta temperatura  alta son:Flores resistentes al calor: verbena, caléndula, petunia, geranio y boca de dragón. La belleza de las flores es innegable. Lástima que no se pueda disfrutar de su aroma y colorido durante todo el año.";
let text4="la recomendacion para las temperaturas extremas bajas es no plantar nada ya que hace demasiado frio."

let tempe = document.getElementById("temperatura");

function recomendation() {
    let temp = localStorage.getItem("temperaturaP");
    console.log(typeof temp);
    if (!temp) {
        console.log(temp);
        document.getElementById("textoR").innerHTML = "INGRESE UNA CIUDAD!";
        return;
    }
    temp = parseFloat(temp);
    if (temp >= 0 && temp <= 10) {
        document.getElementById("textoR").innerHTML = texto1;
    } else if (temp >= 11 && temp <= 24) {
        document.getElementById("textoR").innerHTML = texto2;
    } else if (temp >= 25) {
        document.getElementById("textoR").innerHTML = texto3;
    }else if(temp < 0){
        document.getElementById("textoR").innerHTML = text4;
    }
}

function limpiar() {
    document.getElementById("ciudad").innerHTML = "Ciudad ";
    document.getElementById("fecha").innerHTML = new Date().toLocaleDateString();
    document.getElementById("temperatura").innerHTML = "°C";
    document.getElementById("clima").innerHTML = "estado";
    document.getElementById("rango").innerHTML = "minimo/maximo";
}