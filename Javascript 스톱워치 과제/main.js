const msec = 00;
const sec = 00;

const msecText = document.getElementById('msec');
const secText = document.getElementById('sec');

const btnstart = document.getElementById('btnstart');
const btnstop = document.getElementById('btnstop');
const btnreset = document.getElementById('btnreset');

const record = document.getElementById('record-list');
const tb = document.getElementById('t-b');
const delete = document.querySelector('#idelete');
const all = document.querySelector('#all');

let Interval;

btnstart.addEventListener('click', () => {
  clearInterval(Interval);
  Interval = setInterval(startTime, 10);
});

function startTimer() {
  msec++;
  if (msec <= 9) {
    msecText.innerHTML = "0" + msec;
  }

  if (msec > 9) {
    msecText.innerHTML = msec;
  }

  if (msec > 99) {
    sec++;
    secText.innerHTML = "0" + sec;
    msec = 0;
    msecText.innerHTML = "0" + sec;
  }

  if (sec > 9) {
    secText.innerHTML = sec;

}}

btnstop.addEventListener('click', () => {
    clearInterval(Interval);
  });

btnreset.addEventListener('click', () => {
  clearInterval(Interval);
  alert('Timer Reset');
  msec = "00";
  sec = "00";
  msecText.innerHTML = msec;
  secText.innerHTML = sec;
  record.innerHTML = "";
});

function record() {
  var node = document.createElement('li');
  var record = tb.textContent;
  var textnode = document.createTextNode(record);
  node.appendChild(textnode);
  record.appendChild(node);
}

delete.onclick = function(){
    delete ();
}

all.onclick = function(){
    checkall();
}

function checkall(){
    var Box = document.querySelectorAll('#record-list .check');
    if(all.checked){
        for (var i in Box){
            Box[i].checked = true; 
        }
    }
    else{
        for (var i in Box){
            Box[i].checked = false; 
        }
    }
}

function deleted(){
    let list = document.getElementById('record-list');
    let checkbox = document.querySelectorAll('#record-list .check');

    for (var i in checkbox){
        if(checkbox[i].checked) list.removeChild(checkbox[i].parentNode.parentNode);
    }
}


