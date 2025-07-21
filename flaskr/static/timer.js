let startTime, updateInterval, timeoutId;
let timerState = "finished";
const waitTime = 500;

// Stopped, waiting, ready, active, finished 
timer = document.getElementById("timer");
document.addEventListener("keydown", function(event) {
	if (timerState == "finished") {
		waitTimer();
	} else if (timerState == "active") {
		stopTimer();
	}
});

document.addEventListener("keyup", function(event) {
	if (timerState == "waiting") {
		resetTimer();
	} else if (timerState == "ready") {
		startTimer();

	} else if (timerState == "active" || timerState == "stopped") {
		resetTimer();
	}
});

function waitTimer() {
	timerState = "waiting"
	timer.style.color = "red";
	timeoutId = setTimeout(readyTimer, waitTime);
}

function readyTimer() {
	timerState = "ready";
	timer.style.color = "green";
	timer.textContent = "00.000";
}

function startTimer() {
	timerState = "active";
	timer.style.color = "black";

	startTime = Date.now();
	updateInterval = setInterval(updateTimer, 10);
}

function resetTimer() {
	timerState = "finished";
	timer.style.color = "black";
	clearTimeout(timeoutId);
	clearInterval(updateInterval)
}

function stopTimer() {
	timerState = "stopped";
	updateTimer() //Update final time
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
