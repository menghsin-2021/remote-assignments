const URL = 'http://13.230.176.178:4000/api/1.0/remote-w4-data'

function ajax(src, callback){
    let xhttp = new XMLHttpRequest();
    xhttp.open("get", src)
    xhttp.responseType = 'json';
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let data = xhttp.response
            callback(data)} else if (this.status != 200) {
            alert(this.status) // readyState != 4 的時候也會跳 alert
            return false
        }
    }
    // 將請求發送到伺服器
    xhttp.send();
}

function render(data){
    // document.createElement() and appendChild() methods are preferred
    const itemContent = document.querySelector(".item-content");
    let element = ['name', 'description', 'price']
    for (let i=0; i<data.length; i++){
        let tr = document.createElement("tr")
        let td;
        for (let j=0; j<element.length; j++){
                td = document.createElement('td');
                td.innerHTML = data[i][element[j]];
                tr.appendChild(td);
            }
        itemContent.appendChild(tr)
    }
}


ajax(URL, function(response){
    render(response)
})