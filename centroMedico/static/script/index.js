$(document).ready(function () {  

    $("#loginForm").submit(function (e) { 
        e.preventDefault();

        let userEmail = $("#userEmail").val();
        let userPassword = $("#userPassword").val();

        if (userEmail === "paciente@gmail.com" && userPassword === "paciente") {
            alert("Bienvenido paciente, ingresando a tu perfil...");
            window.location.replace("../../templates/paciente/paciente.html");
        } 
        
        console.log($(userEmail));
        console.log($(userPassword));
    
      });



    
});
   