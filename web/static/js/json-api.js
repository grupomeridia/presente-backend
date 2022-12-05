fetch(`http://127.0.0.1:5000/historico/get_alunos`).then((data)=>{
    return data.json();
}).then((ObjectData)=>{
    let tbody = document.getElementById('tbody');
    tbody.innerHTML = '';

    for (let i = 0; i < ObjectData.length; i++){
        let tr = tbody.insertRow();
        

        let id = tr.insertCell();
        let name = tr.insertCell();
        let ra = tr.insertCell();
        let horario = tr.insertCell();
        

        id.innerText = ObjectData[i].ID;
        ra.innerText = ObjectData[i].RA;
        horario.innerText = ObjectData[i].horario;
        name.innerText = ObjectData[i].nome;
    }

    $('table#example').dataTable({
        "searching": true,
        "paging": true,
        "pageLength": 10,
    });
})