let startTime, updateInterval, active = false, finished = true;
timer = document.getElementById("timer");
document.addEventListener("keydown", function(event) {
	if (active && !finished) {
		active = false
		stopTimer();
	}
	if (!active && finished && event.code == "Space") {
		readyTimer();
	}
});

document.addEventListener("keyup", function(event) {
	if (!active && finished) {
		startTimer();
	} else {
		startTime = null;
		finished = true;
	}

});

function readyTimer() {
	timer.style.color = "red";
}

function startTimer() {
	finished = false;
	active = true;
	timer.style.color = "black";
	startTime = Date.now();
	updateInterval = setInterval(updateTimer, 10);
}

function stopTimer() {
	active = false;
	updateTimer()
	clearInterval(updateInterval)
}

function updateTimer() {
	timer.textContent = Date.now() - startTime;
}
