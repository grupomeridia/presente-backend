const lista = [
    {Aluno:'Roberto Vinicius Passos Moreira de Lima', cursos:'Eng. de Software', Ra:54414854},
    {Aluno:'Guilherme de Narde',cursos:'Eng de Software', Ra:15234523},
    {Aluno:'Donizete dos Santos',cursos:'Eng de Software', Ra:12345234},
    {Aluno:'Matheus Guilherme Almeida',cursos:'Eng de Software', Ra:12345434},
    {Aluno:'Andre Chang',cursos:'Eng de Software', Ra:14253455},
    {Aluno:'Jose Roberto Pinheiro',cursos:'Eng de Software', Ra:12345234},
    {Aluno:'Maria Eduarda',cursos:'Eng de Software', Ra:12312342},
    {Aluno:'Matheus Henrique Almeida',cursos:'Eng de Software', Ra:14253455},
    {Aluno:'João Pedro Cavalcante',cursos:'Analise e Desenvolvimento', Ra:12345234},
    {Aluno:'Matheus Ricardo',cursos:'Analise e Desenvolvimento', Ra:12312342},
    {Aluno:'Laura Cesario',cursos:'Eng de Software', Ra:14253455},
    {Aluno:'Heitor Lorenzo Silva',cursos:'Analise e Desenvolvimento', Ra:39423942},
    {Aluno:'Gustavo Lima de Souza',cursos:'Eng de Software', Ra:45351234},
    {Aluno:'Erick Rafael Nascimento',cursos:'Eng de Software', Ra:58943782},
    {Aluno:'Rafael Silva Cunha',cursos:'Analise e Desenvolvimento', Ra:54908943},
    {Aluno:'Thiago Emanuel Souza',cursos:'Eng de Software', Ra:32480938},
    {Aluno:'Arthur Ricardo Perreira',cursos:'Eng de Software', Ra:70148923},
    {Aluno:'Daniel Pinheiro Junior',cursos:'Eng de Software', Ra:58587298},
    {Aluno:'Gabriella Barros de Souza',cursos:'Analise e Desenvolvimento', Ra:75841090},
    {Aluno:'Gabrielle Saraiva Pinheiro',cursos:'Analise e Desenvolvimento', Ra:78415748},
    {Aluno:'Maria Clara de Oliveira',cursos:'Eng de Software', Ra:56738901},
    {Aluno:'Paulo Henrique Pinhero',cursos:'Eng de Software', Ra:90970651},
    {Aluno:'Davi Miguel Dos Santos',cursos:'Analise e Desenvolvimento', Ra:56784301},
    {Aluno:'Maria Alice de Nascimento',cursos:'Eng de Software', Ra:44412451},
    {Aluno:'Sara de Oliveira',cursos:'Analise e Desenvolvimento', Ra:69399211},
    {Aluno:'Raquel de Florensa',cursos:'Analise e Desenvolvimento', Ra:76854922},
    {Aluno:'Ana Carolina Cavalcante',cursos:'Eng de Software', Ra:65772222},
    {Aluno:'Rodrigo Lucas David',cursos:'Analise e Desenvolvimento', Ra:67843622},
    {Aluno:'Cecília de Meireles',cursos:'Analise e Desenvolvimento', Ra:33482921},
    {Aluno:'Nathalia da Costa',cursos:'Eng de Software', Ra:87652566},
]


function tabela(data){
    let tbody = document.getElementById('tbody');
    tbody.innerText = '';



    for(let i=0; i<data.length; i++){
        let tr = tbody.insertRow();

        let td_aluno = tr.insertCell();
        let td_ra = tr.insertCell();
        let td_cursos = tr.insertCell();
        let td_acoes = tr.insertCell();

        td_aluno.innerText = data[i].Aluno;
        td_ra.innerText = data[i].Ra;
        td_cursos.innerText = data[i].cursos;




        let marcarpresenca = document.createElement('img');
        let imgExcluir = document.createElement('img');
        let modificarInfo = document.createElement('img');

        marcarpresenca.src = '../assets/img/marcarpresenca.svg';
        imgExcluir.src = '../assets/img/ExcluirAluno.svg';
        modificarInfo.src = '../assets/img/modificarInformacao.svg';

        td_acoes.appendChild(marcarpresenca);
        td_acoes.appendChild(imgExcluir);
        td_acoes.appendChild(modificarInfo);


    }

    

    $('table#example').dataTable({
        "searching": true,
        "paging": true,
        "pageLength": 10,
    });


    

}

function filtrar(){
    let td, txtvalue;
    let input = document.getElementById("filterName");
    let filter = input.value.toUpperCase();
    let tbody = document.getElementById("tbody");
    let tr = tbody.getElementsByTagName("tr");

    for (let i=0; i<tr.length;i++){
        td = tr[i].getElementsByTagName('td')[0];
        if(td){
            txtvalue = td.textContent || td.innerText;
            if(txtvalue.toUpperCase().indexOf(filter) > -1){
                tr[i].style.display = '';
            } else {
                tr[i].style.display = 'none';
            }
        }
    }
}


