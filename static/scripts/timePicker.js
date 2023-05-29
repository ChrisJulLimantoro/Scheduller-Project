$(document).ready(function () {
    const location = document.getElementById("modalBody");

    function activate() {
        document.head.insertAdjacentHTML("beforeend", `
        <style>
            .time-picker {
            position: absolute;
            display: inline-block;
            padding: 10px;
            background: #198754;
            border-radius: 6px;
            }
    
            .time-picker__select {
            -webkit-appearance: none;
            -moz-appearance: none;
            appearance: none;
            outline: none;
            text-align: center;
            border: 1px solid #dddddd;
            border-radius: 6px;
            padding: 6px 10px;
            background: #ffffff;
            cursor: pointer;
            font-family: 'Heebo', sans-serif;
            }
        </style>
        `);
    
        document.querySelectorAll(".time-pickable").forEach(timePickable => {
        let activePicker = null;
    
        timePickable.addEventListener("focus", () => {
            if (activePicker) return;
    
            activePicker = show(timePickable);
    
            const onClickAway = ({ target }) => {
            if (
                target === activePicker
                || target === timePickable
                || activePicker.contains(target)
            ) {
                return;
            }
    
            document.removeEventListener("mousedown", onClickAway);
            location.removeChild(activePicker);
            activePicker = null;
            };
    
            document.addEventListener("mousedown", onClickAway);
        });
        });
    }
    
    function show(timePickable) {    
        const picker = buildPicker(timePickable);
        const { bottom: top, left } = timePickable.getBoundingClientRect();
    
        picker.style.top = `${top}px`;
        picker.style.left = `${left}px`;
    
        location.appendChild(picker);
    
        return picker;
    }
    
    function buildPicker(timePickable) {
        const picker = document.createElement("div");
        const hourOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24].map(numberToOption);
        const minuteOptions = [0, 30].map(numberToOption);
    
        picker.classList.add("time-picker");
        picker.innerHTML = `
        <select class="time-picker__select">
            ${hourOptions.join("")}
        </select>
        :
        <select class="time-picker__select">
            ${minuteOptions.join("")}
        </select>
        `;
    
        const selects = getSelectsFromPicker(picker);
    
        selects.hour.addEventListener("change", () => timePickable.value = getTimeStringFromPicker(picker));
        selects.minute.addEventListener("change", () => timePickable.value = getTimeStringFromPicker(picker));
        // selects.meridiem.addEventListener("change", () => timePickable.value = getTimeStringFromPicker(picker));
    
        if (timePickable.value) {
        const { hour, minute } = getTimePartsFromPickable(timePickable);
    
        selects.hour.value = hour;
        selects.minute.value = minute;
        // selects.meridiem.value = meridiem;
        }
    
        return picker;
    }
    
    function getTimePartsFromPickable(timePickable) {
        const pattern = /^(\d+):(\d+)/;
        const [hour, minute] = Array.from(timePickable.value.match(pattern)).splice(1);
    
        return {
        hour,
        minute,
        };
    }
    
    function getSelectsFromPicker(timePicker) {
        const [hour, minute] = timePicker.querySelectorAll(".time-picker__select");
    
        return {
        hour,
        minute,
        };
    }
    
    function getTimeStringFromPicker(timePicker) {
        const selects = getSelectsFromPicker(timePicker);
    
        return `${selects.hour.value}:${selects.minute.value}`;
    }
    
    function numberToOption(number) {
        const padded = number.toString().padStart(2, "0");
    
        return `<option value="${padded}">${padded}</option>`;
    }
    activate();
});