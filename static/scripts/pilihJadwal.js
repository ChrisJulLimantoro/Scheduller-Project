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
                <input id="matkul`+index+`" type="checkbox" value='`+value+`' name='matkul`+index+`''>
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


    $(".generateButton").click(function (e) {
        e.preventDefault();
        let active = [];
        $(".cbx-matkul:checked").each(function(){
            active.push($(this).val());
        });
        let filter = {};
        let dosen = [];
        $('.like:checked').each(function(){
            dosen.push($(this).val());
        });
        filter['dosen'] = dosen;
        filter['minSKS'] = $('#minSKS').val();
        filter['maxSKS'] = $('#maxSKS').val();
        filter['']
        $(".loadScreen").css("display", "block");
        $(".loadScreen").show().delay(2000).fadeOut();
        $(".boxHasil").hide().delay(2000).fadeIn();
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
                    <input class="cbx-matkul" id="cbx-`+row['id']+`" name="cbx-`+row['id']+`" type="checkbox" value='`+row['id']+`'>
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
    })