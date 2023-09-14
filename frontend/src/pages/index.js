import React, { useState, useEffect } from "react";
import api from "@/client/api";
import styles from "./style.module.css";
import Navbar from "@/components/Navbar/navbar";
import Footer from "@/components/Footer/Footer";
import Cabecalho from "@/components/Cabecalho/cabecalho";

function Home() {
  const [alunos, setAlunos] = useState([]);
  const [ativo, setAtivo] = useState(false);
  const [alunoRa, setAlunoRa] = useState("");
  const [turma, setTurma] = useState("");
  const [projeto, setProjeto] = useState("");
  const [chamada, setChamada] = useState("");
  const [professor, setProfessor] = useState("");
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
    // console.log(presencaData)

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

  useEffect(() => {
    const fetchChamada = async () => {
      try {
        const response = await api.chamada.listAll();
        console.log(response.data);
        if (response.data.length > 0) {
          const [primeiraChamada] = response.data;
          setTurma(primeiraChamada.turma);
          setProjeto(primeiraChamada.Projeto);
          setChamada(primeiraChamada.Id);
          setProfessor(primeiraChamada.Professor);
          setTipoPresenca(primeiraChamada.tipoPresenca);
          setHorario(primeiraChamada.horario);
        }
      } catch (error) {
        console.log(error);
      }
    };
    fetchChamada();
  }, []);

  return (
    <div>
      <div className={styles.headerContainer}>
      <Navbar />
      <div className={styles.userInfoAndHeader}>
        <Cabecalho />
      <section className={styles.page_content}>
        {/* <section className={styles.search_and_user}>
          <div className={styles.admin_profile}>
            <span className={styles.greeting}>Hello admin</span>
            <i className="fa-solid fa-circle-user"></i>
          </div>
        </section> */}
        <section className={styles.grid}>
          <div className = {styles.form_wrapper}>
            <h1>Marcar Presença</h1>
            <form onSubmit={handleSubmit} className={styles.form}>
              <label htmlFor="alunoRa" className={styles.label}>
                RA do Aluno:
              </label>
              <input
                type="text"
                name="alunoRa"
                id="alunoRa"
                value={alunoRa}
                onChange={(e) => setAlunoRa(e.target.value)}
                className={styles.input}
              />
              <br />
              <button type="submit" className={styles.button}>
                Marcar Presença
              </button>
              {message && (
            <div className={isSuccess ? "success-message" : "error-message"}>
              {message}
            </div>
          )}
            </form>
          </div>
        </section>
      </section>
      </div>
    </div>
    </div>
  );
}

export default Home;
