import React, { useState, useEffect } from "react";
import api from "@/client/api";
import styles from "./style.module.css";
import Navbar from "@/components/Navbar/navbar";
import Footer from "@/components/Footer/Footer";
import Cabecalho from "@/components/Cabecalho/cabecalho";

function presencaAluno(){
  const [professor, setProfessor] = useState([]);
  const [curso, setCusco] = useState([]);
  const [projeto, setProjeto] = useState([]);
  const [presencas, setPresencas] = useState([]);
  const [alunos, setAlunos] = useState([]);
  const [ativo, setAtivo] = useState(false);
  const [alunoRa, setAlunoRa] = useState("");
  const [turma, setTurma] = useState("");
  const [chamada, setChamada] = useState("");
  const [tipoPresenca, setTipoPresenca] = useState("");
  const [horario, setHorario] = useState("");
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);

    const handleSubmit = async (event) => {
        event.preventDefault();
    
        const presencaData = {
          ativo: true,
          AlunoRa: alunoRa,
          turma,
          projeto,
          chamada,
          professor,
          tipoPresenca : "NORMAL",
          horario: new Date().toLocaleString(),
        };
        console.log(presencaData)
    
          api.presenca
            .create(presencaData)
            .then((response) => {
              console.log(response.data);
              setMessage(response.data);
              setIsSuccess(true);
            })
            .catch((error) => {
              console.log(error);
              setMessage(error);
              setIsSuccess(false);
            });
            
      };




    return(
        <div>
       <Cabecalho/>
       <Navbar/>
        <section className={styles.page_content}>
          <section className={styles.inner_content}>
          <div className={styles.chamada}>
            <div>
              <h1>Presenças abertas</h1>
            </div>
            <table className={styles.tabela}>
                  {/* <thead>
                    <tr>
                      <th>Professor</th>
                      <th>Curso</th>
                      <th>Projeto</th>
                      <th>Data</th>
                      <th></th>
                    </tr>
                  </thead> */}
                  <tbody>
                 {/* {itens.map((itens) =>(
                  <tr key={itens.id}>
                    <td>{itens.professor}</td>
                    <td>{itens.curso}</td>
                    <td>{itens.projeto}</td>
                    <td>{itens.data}</td>
                    <td><button onClick={handleSubmit}>Marcar Presenca</button></td>
                  </tr>
                 ))} */}
                 <tr>
                  <td>Willian</td>
                  <td>Eng.Soft</td>
                  <td>Chamada</td>
                  <td>11/09</td>
                  <td><button className={styles.botao} onClick={handleSubmit}>Realiza Chamada</button></td>
                 </tr>
                  </tbody>
            </table>
                
            </div>
            <div className={styles.historico}>
              <div>
                <h1>Ultimas presenças</h1>
              </div>
                <table className={styles.tabela}>
                  <thead>
                    <tr>
                      <th>Professor</th>
                      <th>Curso</th>
                      <th>Projeto</th>
                      <th>Data</th>
                    </tr>
                  </thead>
                  <tbody>
                 {/* {itens.map((itens) =>(
                  <tr key={itens.id}>
                    <td>{itens.professor}</td>
                    <td>{itens.curso}</td>
                    <td>{itens.projeto}</td>
                    <td>{itens.data}</td>
                  </tr>
                 ))} */}
                 <tr>
                  <td>Willian</td>
                  <td>Eng.Soft</td>
                  <td>Chamada</td>
                  <td>11/09 20:59</td>
                 </tr>
                 <tr>
                  <td>Willian</td>
                  <td>Eng.Soft</td>
                  <td>Chamada</td>
                  <td>11/09 20:59</td>
                 </tr>
                  </tbody>
                </table>
            </div>
          </section>
        </section>
        <Footer/>
      </div>
    );

}

export default presencaAluno;