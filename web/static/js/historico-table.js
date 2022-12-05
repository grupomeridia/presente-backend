function tabela(consultaDados){
    let tbody = document.getElementById('tbody');
    tbody.innerText = '';



    for(let i=0; i<data.length; i++){
        let tr = tbody.insertRow();

        let td_id = tr.insertCell();
        let td_aluno = tr.insertCell();
        let td_ra = tr.insertCell();
        let td_horario = tr.insertCell();

        td_aluno.innerText = data[i].Aluno;
        td_ra.innerText = data[i].Ra;
        td_horario.innerText = data[i].horario;


    }

    

    $('table#example').dataTable({
        "searching": true,
        "paging": true,
        "pageLength": 10,
    });

}

