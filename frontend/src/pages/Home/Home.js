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
      tipoPresenca,
      horario,
    };

    try {
      const response = await api.post("/presenca", presencaData);
      console.log(response.data);
      // Tratar a resposta ou redirecionar para outra página
    } catch (error) {
      console.error("Erro ao marcar presença", error);
    }
  };

  useEffect(() => {
    const fetchAlunos = async () => {
      try {
        const response = await api.aluno.listAll();
        console.log(response.data);
        setAlunos(response.data);
      } catch (error) {
        console.error("Erro ao buscar os alunos", error);
      }
    };
    fetchAlunos();
  }, []);

  return (
    <div>
      <NavBar />
      <body onLoad="tabela(lista)">
        <section className={styles.page_content}>
          <section className={styles.search_and_user}>
            <div className={styles.admin_profile}>
              <span className={styles.greeting}>Hello admin</span>
              <i className="fa-solid fa-circle-user"></i>
            </div>
          </section>
          <section className={styles.grid}>
            <div>
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
        <script
          src="https://kit.fontawesome.com/a146d88807.js"
          crossOrigin="anonymous"
        ></script>
        <script src="//code.jquery.com/jquery-3.3.1.js"></script>
        <script src="//cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
        <script src="{{ url_for('static', filename='js/home-table.js') }}"></script>
        <script src="{{ url_for('static', filename='js/toggle-menu.js') }}"></script>
      </body>
      <Footer />
    </div>
  );
}

export default Home;
