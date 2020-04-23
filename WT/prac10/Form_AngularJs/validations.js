function ValidateForm(form) {
  var mailformat = /^[0-9]{2}[A-Za-z]{3}[0-9]{3}@nirmauni.ac.in$/;
  var phoneno = /^\d{10}$/;
  var letters = /^[A-Za-z ]+$/;
  var pcode = /^[0-9]{6}$/;
  var pass = /^.*(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!#$%&?@ "]).*$/;



  if(!( form.Firstname.value.match(letters)) || !( form.Lastname.value.match(letters))){
    alert('Name must have alphabet characters only');
    form.Firstname.focus();
    form.Lastname.focus();
    return false;
  }
  else if(!(form.Email.value.match(mailformat)))
  {
    alert("You have entered an invalid email address!");
    form.Email.focus();
    return false;
  }
  else if(!(form.Contact.value.match(phoneno))){
    alert("You have entered an invalid contact!");
    form.Contact.focus();
    return false;
  }
	else if ( !(form.pass1.value.match(pass))){
    alert("Password must be minimum of eight characters long consisting of a combination of uppercase letter, lowercase letter, and digits.!")
    form.pass1.focus();
    return false;
  }

  else if (form.pass1.value != form.pass2.value ) {
    alert("Passwords do not match!")
    form.pass1.focus();
    return false;
  }
  
  else {
    return true;
  }
  
}

