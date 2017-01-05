function refreshCam() {
    var camImg = document.getElementById("camera");
	camImg.src="cam.jpg?t="+new Date().getTime();
}
function refreshLatest() {
	var latestImg = document.getElementById("latest");
	latestImg.src="latest.jpg?t="+new Date().getTime();
	
    var xhr = new XMLHttpRequest();
	xhr.open('GET', '/data', true);
    xhr.onload = function() {
	    console.log('HERE');
	    var status = xhr.status;
	    if (status == 200) {
	        var guesses = document.getElementById("guesses");
	        guesses.innerHTML = xhr.response	              
	    } 
	};
	xhr.send();
	
}

setInterval(refreshCam, 200);
setInterval(refreshLatest, 1001);
function call(name) {
    console.log(name);
    var xhr = new XMLHttpRequest();
    xhr.open('GET', name, true);
    xhr.send();
}

function setSpeed(left, right) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'setSpeed?left='+left+'&right='+right, true);
    xhr.send();
}

document.onkeyup = function(e) {
	call('stop');
}

document.onkeydown = function(e) {
    var key = e.keyCode ? e.keyCode : e.which;
	console.log(key);
	
    if (key == 37) { //Left
		call('l');
    } else if (key == 38) { //up
		call('b');
    } else if (key == 39) {//right
		call('r');
    } else if (key == 40) {// down
		call('f');
    } else if (key == 90) {//z
		call('stop');
    } else if (key == 32) { //space
		call('img_rec');
	}
}

if (window.DeviceMotionEvent != undefined) {
    window.ondevicemotion = function(e) {
		ax = event.accelerationIncludingGravity.x * 5;
		ay = event.accelerationIncludingGravity.y * 5;
		
		left = ax + ay;
		right = -ax + ay;
		
		
		setSpeed(left, right);
    }
}
