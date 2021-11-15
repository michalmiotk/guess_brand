function getOption() {
    let selectedValue = document.getElementById('greet').value;
    console.log(selectedValue);
    console.log("a powinno" + '{{ true_brand }}')
    let s= document.getElementById("result_text");
    if(selectedValue == '{{ true_brand }}'){
        console.log("zwyciestwo");
        s.innerHTML = 'good answer';
    }else{
        s.innerHTML = 'bad answer';
    }
}
