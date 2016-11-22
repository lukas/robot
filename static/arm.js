function call(name) {
    console.log(name);
    var xhr = new XMLHttpRequest();
    xhr.open('GET', name, true);
    xhr.send();
}

function saveFields() {
    var data = {};
    data.max = [];
    data.min = [];
    for (i=0; i<5; i++) {
	data.min[i] = document.getElementById("tmin" + i).value;
	data.max[i] = document.getElementById("tmax" + i).value;
    }
    localStorage.setItem("myData", JSON.stringify(data));
}

function loadFields() {
    var data = localStorage.getItem("myData");
    var dataObject;
    if (data != null) {
	dataObject = JSON.parse(data);
	for (i=0; i<5; i++) {
	    document.getElementById("tmin" + i).value = dataObject.min[i]
	    document.getElementById("tmax" + i).value = dataObject.max[i]
	}
	    
    } else {
	for (i=0; i<5; i++) {
	    document.getElementById("tmin" + i).value = 0
	    document.getElementById("tmax" + i).value = 100
	}
    }
}

function slider(num, value) {
    console.log(num);
    tid = "t" + num;
    document.getElementById(tid).value = value;
    var xhr = new XMLHttpRequest();
    xhr.open('GET',  "slider?num="+num+"&value="+value);
    xhr.send();
}

function sliderInc(num) {
    sid = "s" + num;
    v = parseInt(document.getElementById(sid).value);
    document.getElementById(sid).value = v+1;
    slider(num,document.getElementById(sid).value);
}

function sliderDec(num) {
    sid = "s" + num;
    v = parseInt(document.getElementById(sid).value);
    document.getElementById(sid).value = v-1;
    slider(num,document.getElementById(sid).value);
}

function sliderReset(num) {
    sid = "s" + num;
    v = parseInt(document.getElementById(sid).value);
    document.getElementById(sid).value = 50;
    slider(num,document.getElementById(sid).value);
}

function randomizeTargets() {
    for (i=0; i<5; i++) {
	min = parseInt(document.getElementById("tmin" + i).value);
	max = parseInt(document.getElementById("tmax" + i).value);
	r = Math.floor(Math.random() * (max-min) + min)
	document.getElementById("target"+i).value = r
    }
}



document.onkeyup = function(e) {
    
}

document.onkeydown = function(e) {
    var key = e.keyCode ? e.keyCode : e.which;
    console.log(key);
    
    if (key == 81) { //q
	sliderDec(0);
    } else if (key == 69) {
	sliderInc(0);
    } else if (key == 87) {
	sliderReset(0);
    }
    else if (key == 65) { 
	sliderDec(1);
    } else if (key == 68) {
	sliderInc(1);
    } else if (key == 83) {
	sliderReset(1);
    }
    else if (key == 90) {
	sliderDec(2);
    } else if (key == 67) {
	sliderInc(2);
    } else if (key == 88) {
	sliderReset(2);
    }
    else if (key == 84) {
	sliderDec(3);
    } else if (key == 85) {
	sliderInc(3);
    } else if (key == 89) {
	sliderReset(3);
    }
    else if (key == 71) { 
	sliderDec(4);
    } else if (key == 74) {
	sliderInc(4);
    } else if (key == 72) {
	sliderReset(4);
    }
    else if (key == 80) {
	randomizeTargets();
    } else if (key == 77) {
	moveToTarget();
    }
}

function stepToTarget() {
    stepSize = 1;
    for (i=0; i<5; i++) {
	stopFlag = true;
	pos = parseInt(document.getElementById("s" + i).value);
	target = parseInt(document.getElementById("target" + i).value);
	if ( pos == target ) {
	    newPos = target;
	} else if ( Math.abs(pos-target) < stepSize) {
	    newPos = target;
	} else if ( pos < target ) {
	    stopFlag = false;
	    newPos = pos + stepSize;
	} else if ( pos > target ) {
	    stopFlag = false;
	    newPos = pos - stepSize;
	}
	document.getElementById("s" + i).value = newPos;
	slider(i,newPos);
	if (stopFlag) {
	    clearFlag(timer);
	}
    }
}



var timer;
function moveToTarget() {
    timer=setInterval(function() { stepToTarget(); }, 100);
    
}


window.onload = function() {
    loadFields();
}
