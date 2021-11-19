function getOption() {
    let selectedValue = document.getElementById('greet').value;
    let s= document.getElementById("result_text");
    if(selectedValue == '{{ true_brand }}'){
        s.innerHTML = 'good answer';
    }else{
        s.innerHTML = 'bad answer';
    }
}
