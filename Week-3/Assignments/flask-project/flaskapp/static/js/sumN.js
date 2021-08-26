//針對每個 DOM 元素來做選取
const number_text = document.querySelector('#number')
const btn = document.querySelector('#btn')
//按鈕綁上監聽:
btn.addEventListener('click', () => getData());

function getData() {
    // // 針對 api 要寫入的格式，把 HTML　撈取回來的　value 寫成物件
    let number = number_text.value
    // 建構 XMLHttpRequest 物件專門用來和伺服器做連線
    let xhttp = new XMLHttpRequest();
    // open(method, url, async) 請求類型(GET, POST), URL(文件在伺服器上的位置), 是否同步處理請求(true為非同步)
    xhttp.open("get", "http://35.75.222.200/data?number="+number)
    //  上傳到伺服器上之後就不是 localhost port也不是5000 所以要改成能求到東西的網址
    // 每當 readyState 屬性更改時要呼叫的函式，為存有 XMLHttpRequest的狀態，從0到4發生變化，當readyState=4 代表請求已完成，回應就緒
    // 也可以用 xhttp.onload 用於偵測連線狀態
    xhttp.onreadystatechange = function() {
    // 如果連線成功就做以下動作
    if (this.readyState == 4 && this.status == 200) {
    // 設定要改變內容的位置
    let content = document.querySelector('#result');
    // XMLHttpRequest 物件有兩個屬性：responseText(輸出為DOM string) and responseXML(接收時要為XML檔案)
    content.innerHTML = this.responseText
      }
    };
    // 將請求發送到伺服器，string僅用於POST
    xhttp.send();
}


// 若網頁沒更新要按 ctrl + F5


//用 DOM parser 的方式 (感覺不好，最好應該是寫好取資料的 API，或直接把網頁內容放入)
//    let response = this.responseText
//    const parser = new DOMParser();
//    let doc = parser.parseFromString(response, "text/html")
//    content.textContent = doc.querySelector('#sum').textContent