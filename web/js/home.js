
const alunos = [
    {ra: 121312, aluno: 'Roberto'},
    {ra: 165322, aluno: 'Maria'},
    {ra: 142342, aluno: 'Joao'},
    {ra: 320392, aluno: 'Jose'},
    {ra: 832490, aluno: 'Andre'},

]



function tabela(data){
    var tbody = document.getElementById('tbody');
    tbody.innerText = '';

    for(var i=0;i<data.length;i++){
        var tr = tbody.insertRow();
        
        var td_aluno = tr.insertCell();
        var td_ra = tr.insertCell();
        var td_acoes = tr.insertCell();

        td_ra.innerText = data[i].ra;
        td_aluno.innerText = data[i].aluno;

        var marcarpresenca = document.createElement('img');
        var imgExcluir = document.createElement('img');
        var imgModInf = document.createElement('img');

        marcarpresenca.src = '../static/assets/marcarpresenca.svg';
        imgExcluir.src = '../static/assets/ExcluirAluno.svg';
        imgModInf.src = '../static/assets/modificarInformacao.svg';

        td_acoes.appendChild(marcarpresenca);
        td_acoes.appendChild(imgExcluir);
        td_acoes.appendChild(imgModInf);        
    } 
}

function filter(){
    var input, filter, tbody, tr, td, txtvalue;
    input = document.getElementById("filterName");
    filter = input.value.toUpperCase();
    tbody = document.getElementById("tbody");
    tr = tbody.getElementsByTagName("tr");

    for (var i=0; i<tr.length;i++){
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

function IniciarModal(){
    const modal = document.getElementById('modal-aparecer');  
    if(modal){
        modal.classList.add('mostrar');
        
        modal.addEventListener('click', (e) => {
        if(e.target.id == 'modal-aparecer' || e.target.className == 'button-close'){
            modal.classList.remove('mostrar')
        }
        });
    }

}


function MandarBE(){
    var inputra = document.getElementById('input-ra');
    var inputnome = document.getElementById('input-nome'); 

    var aluno = {ra: inputra.value, aluno: inputnome.value};
    //retornar ao Back-end
}
