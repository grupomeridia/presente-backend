import styles from "./Options.module.css";
import NavBar from "../../componets/layout/Navbar";
import Footer from "../../componets/layout/Footer";
import React, { useState, useEffect } from "react";
import api from "../../client/api";

function Options() {
  const [alunos, setAlunos] = useState([]);
  const [chamadaAtiva, setChamadaAtiva] = useState(false);
  const [projetoSelecionado, setProjetoSelecionado] = useState("");
  const [professorSelecionado, setProfessorSelecionado] = useState("");
  const [turmaSelecionada, setTurmaSelecionada] = useState("");

  const handleProjetoChange = (event) => {
    setProjetoSelecionado(event.target.value);
  };

  const handleProfessorChange = (event) => {
    setProfessorSelecionado(event.target.value);
  };

  const handleTurmaChange = (event) => {
    setTurmaSelecionada(event.target.value);
  };

  const handleClick = () => {
    setChamadaAtiva(!chamadaAtiva);
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
      <body onload="tabela(lista)">
        <section class={styles.page_content}>
          <section class={styles.search_and_user}>
            <div class={styles.admin_profile}>
              <span class={styles.greeting}>Hello admin</span>
              <i class="fa-solid fa-circle-user"></i>
            </div>
          </section>
          <section className={styles.grid}>
            <div className={styles.center}>
        <div className={styles.dropdownContainer}>
          <label htmlFor="projeto">Projetos:</label>
          <select
            id="projeto"
            value={projetoSelecionado}
            onChange={handleProjetoChange}
          >
            <option value="">Selecione um projeto</option>

          </select>
        </div>
        <div className={styles.dropdownContainer}>
          <label htmlFor="professor">Professores:</label>
          <select
            id="professor"
            value={professorSelecionado}
            onChange={handleProfessorChange}
          >
            <option value="">Selecione um professor</option>

          </select>
        </div>
        <div className={styles.dropdownContainer}>
          <label htmlFor="turma">Turma:</label>
          <select
            id="turma"
            value={turmaSelecionada}
            onChange={handleTurmaChange}
          >
            <option value="">Selecione uma turma</option>
            
          </select>
          </div>
        </div>
        <button
          className={chamadaAtiva ? `${styles.pararChamada}` : `${styles.iniciarChamada}`}
          onClick={handleClick}
        >
          {chamadaAtiva ? "Parar chamada" : "Iniciar chamada"}
        </button>
      </section>
          </section>
        <script
          src="https://kit.fontawesome.com/a146d88807.js"
          crossorigin="anonymous"
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

export default Options;
