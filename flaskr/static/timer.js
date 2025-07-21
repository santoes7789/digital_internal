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
	const timeInMilliseconds = Date.now() - startTime;
	const milliseconds = timeInMilliseconds % 1000;
	const seconds = Math.floor(timeInMilliseconds / 1000) % 60;
	const minutes = Math.floor(timeInMilliseconds / 1000 / 60) % 60;
	const hours = Math.floor(timeInMilliseconds / 1000 / 60 / 60);

	let display = "";
	if (minutes) {
		display += String(minutes) + ".";
	}
	display += String(seconds).padStart(2, "0") + "." + String(milliseconds).padStart(3, "0");
	timer.textContent = display;
}
