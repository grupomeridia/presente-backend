import React, { useState, useEffect } from "react";
import api from "../../client/api";
import { Link } from "react-router-dom";
import styles from "./Home.module.css";
import NavBar from "../../componets/layout/Navbar";
import Footer from "../../componets/layout/Footer";

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

    try {
      api.presenca
        .create(presencaData)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    } catch (error) {
      console.error("Erro ao marcar presença", error);
    }
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
      <NavBar />
      <section className={styles.page_content}>
        <section className={styles.search_and_user}>
          <div className={styles.admin_profile}>
            <span className={styles.greeting}>Hello admin</span>
            <i className="fa-solid fa-circle-user"></i>
          </div>
        </section>
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
            </form>
          </div>
        </section>
      </section>
      <Footer />
    </div>
  );
}

export default Home;
