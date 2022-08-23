function login(){
    login_div = document.getElementById("login")
    create_div = document.getElementById("create")
    if (login_div.classList.contains("off")){
        login_div.classList.remove("off")
        create_div.classList.add("off")
    }
    else{
        login_div.classList.add("off")
        create_div.classList.remove("off")
    }
   

   
}