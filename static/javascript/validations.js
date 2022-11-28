
// name validation
function validatename(){
    let x=document.getElementById("name").value
    let y=document.getElementById("nameerror")

    if(y){
        if(x==""){
            document.getElementById("nameerror").innerHTML="* Name cannot be empty"
        }

        else if(x.length<3 || x.length>25){
            document.getElementById("nameerror").innerHTML="* Should be in range"
        }
        else
        document.getElementById("nameerror").innerHTML=""

    }

    
}

// email validation
function Validateemail(){
    let id_email=document.getElementById("email").value
    let email_error=document.getElementById("emailerror")
    let pattern_email= /^\w+([\,.]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/g;

    if(email_error){
        if(id_email==""){
            document.getElementById("emailerror").innerHTML="* This field can't be empty"
            email_id.focus()
            return false

        }
        else if(!pattern_email.test(id_email)){
            document.getElementById("emailerror").innerHTML="Not in a valid format"
            email_id.focus()
            return false

        }
        else{
            document.getElementById("emailerror").innerHTML=""
        }
    }
}

// address validation
function validateaddress(){
    let address_id=document.getElementById("address").value
    let address_error=document.getElementById("addresserror")
    let pattern_address= /^\w+([\,.]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/g;

    if(address_error){
        if(address_id==""){
            document.getElementById("addresserror").innerHTML="* This field can't be empty"
        }
    }
}

// phone number validation
function validatephone(){
    let phone_no=document.getElementById("phone").value
    let phone_error=document.getElementById("phoneerror")

    if(phone_error){

        if(phone_no==" "){
            document.getElementById("phoneerror").innerHTML="* This field can't be empty"
        }
        else if(isNaN(phone_no)){
            
                document.getElementById("phoneerror").innerHTML="* Enter numbers only"
            
               
                return false
        }
        else if(phone_no.length!=10){
            document.getElementById("phoneerror").innerHTML="*Enter 10 digits only"

            phone_no.focus()
            return false
        }
        else{
            document.getElementById("phoneerror").innerHTML=""

            return true
        }
    }
}

function usnumber(){
    let n=document.getElementById("phone").value
            if(n.length==3|| n.length==7){
                document.getElementById("phone").value=n+"-"
            }

}

// age validation
function validateage(){
    let dateob = document.getElementById("dob").value
    let date_error = document.getElementById("ageerror")

    let current_date = new Date();
    var arr = dateob.split("-");
    var dobyear = arr[0];
    console.log(dobyear)
    var year = current_date.getFullYear()
    dateob = year-dobyear
    if( dateob< 18){
        console.log("error")
        document.getElementById("ageerror").innerHTML="* Age should be above 18 years"
        return false
    }
    else{
        document.getElementById("ageerror").innerHTML=""
    }
}

