$(document).ready(function () {
    $.ajax({
        url : '/get_dosen/',
        method : 'POST',
        success : function(response){
        $.each(response,function(index,value){
            $('#checkBoxDosen').append(`<div class="row mb-2">
            <div class="col-3">
                <div class="con-like">
                <input title="like" type="checkbox" class="like" id="dosen`+index+`" name="dosen`+index+`" style="display: hidden;" value="`+value+`">
                <div class="checkmark">
                    <svg viewBox="0 0 24 24" class="outline" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Zm-3.585,18.4a2.973,2.973,0,0,1-3.83,0C4.947,16.006,2,11.87,2,8.967a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,11,8.967a1,1,0,0,0,2,0,4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,22,8.967C22,11.87,19.053,16.006,13.915,20.313Z">
                    </path>
                    </svg>
                    <svg viewBox="0 0 24 24" class="filled" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Z">
                    </path>
                    </svg>
                    <svg class="celebrate" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
                    <polygon points="10,10 20,20" class="poly"></polygon>
                    <polygon points="10,50 20,50" class="poly"></polygon>
                    <polygon points="20,80 30,70" class="poly"></polygon>
                    <polygon points="90,10 80,20" class="poly"></polygon>
                    <polygon points="90,50 80,50" class="poly"></polygon>
                    <polygon points="80,80 70,70" class="poly"></polygon>
                    </svg>
                </div>
                </div>
            </div>
            <div class="col-9" style="margin-left: -1em; margin-top: -0.2em;">
                <label for="dosen`+index+`">`+value+`</label>
            </div>
            </div>`);
        })
        }
    });
    $.ajax({
        url : '/get_matkul/',
        method : 'POST',
        success : function(response){
        $.each(response,function(index,value){
            $('#checkBoxMatkul').append(`<div class="row">
            <div class="col-3">
                <div class="checkbox-wrapper-19">
                <input class="cbx-fav" id="matkul`+index+`" type="checkbox" value='`+value+`' name='matkul`+index+`''>
                <label class="check-box" for="matkul`+index+`">
                </label>
                </div>
            </div>
            <div class="col-9">
                <label for="matkul`+index+`">`+value+`</label>
            </div>
            </div>`);
        });
        }
    })

    const active = []

    $(document.body).on('click', '.cbx-matkul', function(e) {
        if ($(this).is(":checked")) {
            active.push(parseInt( $(this).val()))
        }
        else {
            var index = active.indexOf($(this).val())
    
            if (index != -1) {
                active.splice(index, 1)
            }
        }

        console.log(active)
    });

    $(".generateButton").click(function (e) {
        e.preventDefault();
        // let active = [];
        // $(".cbx-matkul:checked").each(function(){
        //     active.push($(this).val());
        // });
        let filter = {};
        let dosen = [];
        $('.like:checked').each(function(){
            dosen.push($(this).val());
        });
        filter['dosen'] = dosen;
        filter['minSKS'] = parseInt($('#minSKS').val());
        filter['maxSKS'] = parseInt($('#maxSKS').val());
        let matkul = [];
        $('.cbx-fav:checked').each(function(){
            matkul.push($(this).val());
        })
        filter['matkulFav'] = matkul;
        hariMasuk = [0,0,0,0,0,0]
        $('.inputHari:checked').each(function(){
            hariMasuk[$(this).val()] = 1;
        });
        filter['hariMasuk'] = hariMasuk;
        maksJam = [parseInt($('#jamSenin').val()),parseInt($('#jamSelasa').val()),parseInt($('#jamRabu').val()),parseInt($('#jamKamis').val()),parseInt($('#jamJumat').val()),parseInt($('#jamSabtu').val())]
        filter['maksJam'] = maksJam;
        $(".loadScreen").css("display", "block");
        $(".boxHasil").hide().fadeIn();
        
        console.log(active)
        console.log(filter)
        $.ajax({
            'url' : '/generate/',
            'method' : 'POST',
            'data' : JSON.stringify({
                "active" : active,
                "filter" : filter
            }),
            success : function(response){
                console.log(response);
                $(".loadScreen").show().fadeOut();
            }
        })
        
        
    });

        $("#senin").click(function () {
        if ($("#senin").is(":checked")) {
            $(".jamSenin").css("display", "block");
        } else {
            $(".jamSenin").css("display", "none");
        }
        })

        $("#selasa").click(function () {
        if ($("#selasa").is(":checked")) {
            $(".jamSelasa").css("display", "block");
        } else {
            $(".jamSelasa").css("display", "none");
        }
        })

        $("#rabu").click(function () {
        if ($("#rabu").is(":checked")) {
            $(".jamRabu").css("display", "block");
        } else {
            $(".jamRabu").css("display", "none");
        }
        })

        $("#kamis").click(function () {
        if ($("#kamis").is(":checked")) {
            $(".jamKamis").css("display", "block");
        } else {
            $(".jamKamis").css("display", "none");
        }
        })

        $("#jumat").click(function () {
        if ($("#jumat").is(":checked")) {
            $(".jamJumat").css("display", "block");
        } else {
            $(".jamJumat").css("display", "none");
        }
        })

        $("#sabtu").click(function () {
        if ($("#sabtu").is(":checked")) {
            $(".jamSabtu").css("display", "block");
        } else {
            $(".jamSabtu").css("display", "none");
        }
        })
        $.ajax({
            url : '/get/',
            type : 'POST',
            success: function(response){
                $.each(response['id'],function(key,value){
                    active.push(value);
                });
            }
        })
        $('#myTable').DataTable({
            responsive: true,
            ajax : {
            processing : true,
            serverSide : true,
            url : '/get/',
            dataSrc : "",
            type : 'POST'
            },
            columns : [
            {data : 'id'},
            {data : 'nama'},
            {data : 'dosen'},
            {data : 'paralel'},
            {data : 'sks'},
            {data : 'jadwal_kuliah_hari'},
            {data : 'jadwal_kuliah_jam'},
            {data : null,
            "render" : function(data,type,row){
                return `<div class="checkbox-wrapper-12">
                <div class="cbx">
                    <input class="cbx-matkul" id="cbx-`+row['id']+`" name="cbx-`+row['id']+`" type="checkbox" value='`+row['id']+`' checked>
                    <label for="cbx-`+row['id']+`"></label>
                    <svg width="15" height="14" viewBox="0 0 15 14" fill="none">
                    <path d="M2 8.36364L6.23077 12L13 2"></path>
                    </svg>
                </div>
        
                <svg xmlns="http://www.w3.org/2000/svg" version="1.1">
                    <defs>
                    <filter id="goo-12">
                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur"></feGaussianBlur>
                        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -7"
                        result="goo-12"></feColorMatrix>
                        <feBlend in="SourceGraphic" in2="goo-12"></feBlend>
                    </filter>
                    </defs>
                </svg>
                </div>`
            }},
            ]
        });
        $('#table1').DataTable({
            responsive: true
        });
        $('#tableUjian1').DataTable({
            responsive: true
        })
        var show = true;
        
    const location = document.getElementById("modalBody");
    activate();
});

function showCheckboxDosen() {
    var checkBoxDosen = document.getElementById("checkBoxDosen");

    if (show) {
    checkBoxDosen.style.display = "block";
    show = false;
    } else {
    checkBoxDosen.style.display = "none";
    show = true;
    }
}

function showCheckBoxHari() {
    var checkBoxHari = document.getElementById("checkBoxHari");

    if (show) {
    checkBoxHari.style.display = "block";
    show = false;
    } else {
    checkBoxHari.style.display = "none";
    show = true;
    }
}

function showCheckboxMatkul() {
    var checkboxMatkul = document.getElementById("checkBoxMatkul");

    if (show) {
    checkboxMatkul.style.display = "block";
    show = false;
    } else {
    checkboxMatkul.style.display = "none";
    show = true;
    }
}

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