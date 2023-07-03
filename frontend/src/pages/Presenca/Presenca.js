import styles from "./Presenca.module.css";
import NavBar from "../../componets/layout/Navbar";
import Footer from "../../componets/layout/Footer";
import React, { useState, useEffect } from "react";
import api from "../../client/api";

function Options() {
  const [professores, setProfessores] = useState([]);
  const [projetos, setProjetos] = useState([]);
  const [projetoSelecionado, setProjetoSelecionado] = useState("");
  const [professor, setProfessor] = useState("");
  const [turmaSelecionada, setTurmaSelecionada] = useState("");
  const [turmas, setTurmas] = useState([]);
  const [chamadas, setChamadas] = useState([]);
  const [isActive, setIsActive] = useState(true);

  const getNomeProjeto = (projetoId) => {
    const projeto = projetos.find((p) => p.id === projetoId);
    return projeto ? projeto.Nome : "";
  };

  const getNomeProfessor = (professorId) => {
    const professor = professores.find((p) => p.id === professorId);
    return professor ? professor.Nome : "";
  };

  const getNomeTurma = (turmaId) => {
    const turma = turmas.find((p) => p.id === turmaId);
    return turma ? turma.Nome : "";
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const presencaData = {
      ra: true,
      nome_professor: projetoSelecionado,
      turma_id: turmaSelecionada,
      professor_id: professor,
    };
  };

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
        <form onSubmit={handleSubmit}>
          <section className={styles.grid}>
            <div className={styles.center}>
            </div>
            <button className={styles.botao} type="submit">
              Cadastrar Chamada
            </button>
          </section>
        </form>
        <section className={styles.grid}>
          <table id="example">
            <thead>
              <tr>
                <th>Nome</th>
                <th>Ra</th>
                <th>Horario</th>
              </tr>
            </thead>
            <tbody>

            </tbody>
          </table>
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
      <Footer />
    </div>
  );
}

export default Options;
