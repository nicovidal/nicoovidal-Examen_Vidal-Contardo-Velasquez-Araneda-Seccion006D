const $formulario = document.getElementById("formulario");
const $inputs = document.querySelectorAll("#formulario input");

const expresiones = {
    usuario: /^[a-zA-Z0-9_.+-@]{4,16}$/,
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,
    password: /^.{4,12}$/,
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
};

const campos = {
    usuario: false,
    nombre: false,
    apellido: false,
    password: false,
    correo: false,
};

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "usuario":
            validarCampo(expresiones.usuario, e.target, "usuario");
            break;
        case "nombre":
            validarCampo(expresiones.nombre, e.target, "nombre");
            break;
        case "apellido":
            validarCampo(expresiones.apellido, e.target, "apellido");
            break;
        case "password":
            validarCampo(expresiones.password, e.target, "password");
            break;
        case "correo":
            validarCampo(expresiones.correo, e.target, "correo");
            break;


    }


};

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document
            .getElementById(`grupo__${campo}`)
            .classList.remove("formulario__grupo-incorrecto");
        document
            .getElementById(`grupo__${campo}`)
            .classList.add("formulario__grupo-correcto");
        document
            .querySelector(`#grupo__${campo} i`)
            .classList.remove("fa-times-circle");
        document
            .querySelector(`#grupo__${campo} i`)
            .classList.add("fa-check-circle");
        document
            .querySelector(`#grupo__${campo} .formulario__input-error`)
            .classList.remove("formulario__input-error-activo");
        campos[campo] = true;
        console.log("Funciona");


    } else {
        document
            .getElementById(`grupo__${campo}`)
            .classList.add("formulario__grupo-incorrecto");
        document
            .getElementById(`grupo__${campo}`)
            .classList.remove("formulario__grupo-correcto");
        document
            .querySelector(`#grupo__${campo} i`)
            .classList.add("fa-times-circle");
        document
            .querySelector(`#grupo__${campo} i`)
            .classList.remove("fa-check-circle");
        document
            .querySelector(`#grupo__${campo} .formulario__input-error`)
            .classList.add("formulario__input-error-activo");
        campos[campo] = false;
        console.log("Funciona");

    }

};

$inputs.forEach((input) => {
    input.addEventListener("keyup", validarFormulario);
    input.addEventListener("blur", validarFormulario);
});

$formulario.addEventListener("submit", (e) => {

    const $terminos = document.getElementById("terminos");
    if (
        campos.usuario  &&
        campos.nombre &&
        campos.apellido &&
        campos.password &&
        campos.correo &&
        $terminos.checked

    ) {
        // formulario.reset();
        document.getElementById("formulario__mensaje").style.display = null;
        document
            .getElementById("formulario__mensaje-exito")
            .classList.add("formulario__mensaje-exito-activo");
        setTimeout(() => {
            document
                .getElementById("formulario__mensaje-exito")
                .classList.remove("formulario__mensaje-exito-activo");

        }, 3000);

        document
            .querySelectorAll(".formulario__grupo--correcto")
            .forEach((icono) => {
                icono.classList.remove("formulario__grupo--correcto");

            });

        setTimeout(() => {
            location.reload();

        }, 5000);

    } else {
        document
            .getElementById("formulario__mensaje")
            .classList.add("formulario__mensaje-activo");
    }

});