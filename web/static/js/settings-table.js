let SALAS = [
    
    {
        sala : 101,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 102,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 103,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 104,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 105,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 106,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 107,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 108,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 110,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 201,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 202,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 203,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 204,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 205,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 206,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 207,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 208,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 209,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 210,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 301,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 302,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 303,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 304,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala : 305,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    },
    {
        sala :306,
        disponibilidade : "DISPONIVEL",
        status: "ONLINE"
    }

    
      
]

let tbody = document.getElementById('tt');
tbody.innerText= ' ';

for (let i=0;i<SALAS.length;i++){
    let tr = tbody.insertRow();
    let td_sala = tr.insertCell();
    let td_disp = tr.insertCell();
    let td_status = tr.insertCell();

    td_sala.innerText = SALAS[i].sala;
    td_disp.innerText = SALAS[i].disponibilidade;
    td_status.innerText = SALAS[i].status;    

    document.getElementById("GroupSelect").innerHTML+="<option value='" + SALAS[i].sala +"'>"+ SALAS[i].sala +"</opntion>"; 

}

document.getElementById("GroupSelect").addEventListener("change",function(){
    let batata = document.getElementById("GroupSelect").value;
    
    for(var i = 0; i < linhas.length; i++){
        var linha_ = linhas[i];
       
        if (linha_.firstChild.innerHTML==batata){
           break;

        }
        
    }
    selLinha(linha_,false);
});

function alerta1(){
    alert("Reiniciando o leitor")
}
function alerta2(){
    alert("Desligando o leitor")
}

var tabela = document.getElementById("tabela-sec");
var linhas = tabela.getElementsByTagName("tr");

for(var i = 0; i < linhas.length; i++){
	var linha = linhas[i];
  linha.addEventListener("click", function(){
  	
		selLinha(this, false); 
                
	});
}
function selLinha(linha, multiplos){
    if(!multiplos){
        var linhas = linha.parentElement.getElementsByTagName("tr");
          for(var i = 0; i < linhas.length; i++){
             var linha_ = linhas[i];
             linha_.classList.remove("selecionado");    
          }
    }
    linha.classList.toggle("selecionado");
    console.log(linha.firstChild);
    var escolha = linha.firstChild.innerHTML;
    console.log(escolha);
    let tent = document.getElementById("GroupSelect");
    tentativa=tent.getElementsByTagName("option");
    for(let i=0;i<tentativa.length;i++){
        if(tentativa[i].innerHTML==escolha){
           tentativa[i].setAttribute("selected","selected");

            console.log(tentativa[i]);
        }
    }

}
