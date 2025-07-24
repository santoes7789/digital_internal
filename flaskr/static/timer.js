let times = [];
let current_session = "3x3";
let is_authenticated = false;


fetch("/check-auth", {
	method: "GET",
	headers: {
		"Content-Type": "application/json",
	},
}).then(response => response.json())
	.then(data => {
		is_authenticated = data["authenticated"];
		if (is_authenticated) {
			console.log("User is authenticated")
			fetchData()
		}
	})

function fetchData() {
	fetch("/times", {
		method: "GET",
		headers: {
			"Content-Type": "application/json",
		},
	})
		.then(response => {
			if (response.status == 200) {
				return response.json()
			} else {
				return null;
			}
		}).then(data => {
			if (data) {
				times = data;
				updateStats()
			}
		})
		.catch(error => {
			console.error("Error:", error);
		})

}


function addTime(time) {
	const newTime = { "timestamp": Date.now(), "value": time, "session": current_session };
	times.push(newTime)

	if (is_authenticated) {
		fetch("/times", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(newTime)
		})
			.then(response => {
				if (response.status == 204) {
					console.log("Sucessfully sent new time to server")
				} else {
					console.log("Failed to send new time to server")
				}
			}).catch(error => {
				console.error("Error:", error);
			})

	}
	updateStats()
}

function deleteTime(time) {
	const index = times.indexOf(time);

	console.log(index);
	if (index == -1) return;

	times.splice(index, 1);
	if (is_authenticated) {
		fetch("/times", {
			method: "DELETE",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(time)
		})
			.then(response => {
				if (response.status == 204) {
					console.log("Sucessfully deleted time on server")
				} else {
					console.log("Failed to delete time on server")
				}
			}).catch(error => {
				console.error("Error:", error);
			})
	}
	updateStats()
}



const timeModal = document.getElementById("time-info-modal");
let current_time_selected;
const deleteTimeBtn = document.getElementById("delete-time-btn");
deleteTimeBtn.addEventListener("click", event => {
	deleteTime(current_time_selected);
})

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



	const table = document.getElementById("time-table-body");
	table.innerHTML = "";
	table.insertRow(0); // for the line between header and other

	for (let i = 0; i < times.length; i++) {
		// Insert a new row at the end of the table (-1 or omitted index)
		const newRow = table.insertRow(0);

		const time = millisecondsToTime(times.at(i)["value"]);

		newRow.setAttribute("type", "button");
		newRow.setAttribute("data-bs-toggle", "modal");
		newRow.setAttribute("data-bs-target", "#time-info-modal");

		// Insert new cells into the new row
		const indexCell = newRow.insertCell(0); // Insert at index 0
		const timeCell = newRow.insertCell(1);

		indexCell.textContent = i + 1;
		timeCell.textContent = time;

		newRow.addEventListener("click", event => {
			console.log("hello");

			// Update the modal's content.
			const modalTitle = timeModal.querySelector(".modal-title");
			const timeHeading = timeModal.querySelector(".time-heading");
			const dateText = timeModal.querySelector(".date-text");
			const timeText = timeModal.querySelector(".time-text");

			current_time_selected = times.at(i);

			modalTitle.textContent = "Solve No. " + (i + 1);
			timeHeading.textContent = time;

			date = new Date(times.at(i)["timestamp"]);
			dateText.textContent = date.toDateString();
			timeText.textContent = date.toTimeString().split(' ')[0];
		})
	}
}



function getBest() {
	const timesOnlyArray = times.map(time => time["value"]);
	return Math.min(...timesOnlyArray);
}

function getAoX(x) {
	if (times.length < x) {
		return null;
	}
	const lastX = times.slice(-x).map(time => time["value"]);
	lastX.sort((a, b) => a - b);

	let sum = 0;
	for (let i = 1; i < (x - 1); i++) {
		sum += lastX[i];
	}
	return sum / (x - 2);
}


let startTime, updateInterval, timeoutId, timerState = "finished";
const waitTime = 500;

const timer = document.getElementById("timer");
const timerBackground = document.getElementById("timer-background");
const timerFading = document.getElementById("fading-bg");

document.addEventListener("keydown", function(event) {
	if (timerState == "finished") {
		if (event.code == "Space") {
			waitTimer();
		} else if (event.shiftKey && event.code == "Backspace") {
			deleteTime(times.at(-1));
		}
	} else if (timerState == "active") {
		stopTimer();
	}
});

document.addEventListener("keyup", function(event) {
	if (timerState == "waiting") {
		resetTimer();
	} else if (timerState == "ready" && event.code == "Space") {
		startTimer();

	} else if (timerState == "stopped") {
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
	timer.textContent = "0.000";
	timerBackground.style.zIndex = 10;
	timerFading.classList.add("show");

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
	timerFading.classList.remove("show");
	timerFading.addEventListener("transitionend", () => {
		timerBackground.style.zIndex = 0;
	}, { once: true })
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
	str += String(seconds) + "." + String(milliseconds).padStart(3, "0");
	return str;

}
