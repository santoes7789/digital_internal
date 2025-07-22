let times = [];

function addTime(time) {
	times.push({ "date": Date.now(), "value": time })
	updateStats()
}


function updateStats() {

	const best = getBest();
	const ao5 = getAoX(5);
	const ao12 = getAoX(12);

	const bestText = best ? millisecondsToTime(best) : "--";
	const ao5Text = ao5 ? millisecondsToTime(ao5) : "--";
	const ao12Text = ao12 ? millisecondsToTime(ao12) : "--";

	document.getElementById("best-text").textContent = bestText;
	document.getElementById("ao5-text").textContent = ao5Text;
	document.getElementById("ao12-text").textContent = ao12Text;

	const table = document.getElementById("timer-table");
	// Insert a new row at the end of the table (-1 or omitted index)
	const newRow = table.insertRow(1);

	// Insert new cells into the new row
	const indexCell = newRow.insertCell(0); // Insert at index 0
	const timeCell = newRow.insertCell(1); //cell1 = new

	indexCell.textContent = times.length;
	timeCell.textContent = millisecondsToTime(times.at(-1)["value"]);

}



function getBest() {
	const timesOnlyArray = times.map(time => time["value"]);
	return Math.min(...timesOnlyArray);
}

function getAoX(x) {
	if (times.length < x) {
		return null;
	}
	const lastFive = times.slice(-x).map(time => time["value"]);
	lastFive.sort((a, b) => a - b);
	console.log(lastFive);

	let sum = 0;
	for (let i = 1; i < (x - 1); i++) {
		sum += lastFive[i];
	}
	return sum / (x - 2);
}


let startTime, updateInterval, timeoutId, timerState = "finished";
const waitTime = 500;

const timer = document.getElementById("timer");

document.addEventListener("keydown", function(event) {
	if (timerState == "finished" && event.code == "Space") {
		waitTimer();
	} else if (timerState == "active") {
		stopTimer();
	}
});

document.addEventListener("keyup", function(event) {
	if (timerState == "waiting") {
		resetTimer();
	} else if (timerState == "ready" && event.code == "Space") {
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
	const time = updateTimer() // Update final time
	addTime(time);
	clearInterval(updateInterval)

}

function updateTimer() {
	const timeInMilliseconds = Date.now() - startTime;
	timer.textContent = millisecondsToTime(timeInMilliseconds);
	return timeInMilliseconds;
}


function millisecondsToTime(milli) {
	const milliseconds = Math.floor(milli % 1000);
	const seconds = Math.floor(milli / 1000) % 60;
	const minutes = Math.floor(milli / 1000 / 60) % 60;
	// const hours = Math.floor(milliseconds / 1000 / 60 / 60);

	let str = "";
	if (minutes) {
		str += String(minutes) + ":";
	}
	str += String(seconds).padStart(2, "0") + "." + String(milliseconds).padStart(3, "0");
	return str;

}
