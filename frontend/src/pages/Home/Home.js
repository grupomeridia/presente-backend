import styles from "./Home.module.css";
import NavBar from "../../componets/layout/Navbar";
import Footer from "../../componets/layout/Footer";
import React, { useState, useEffect } from "react";
import api from "../../client/api";
import { Link } from "react-router-dom";

function Home() {
  const [alunos, setAlunos] = useState([]);

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
          <section class={styles.grid}>
            <table id="example">
              <thead>
                <tr>
                  <th>Aluno</th>
                  <th>Ra</th>
                  <th>Cursos</th>
                  <th>Turma</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody id="tbody">
                {alunos.map((aluno) => (
                  <tr key={aluno.Id}>
                    <td>{aluno.Nome}</td>
                    <td>{aluno.RA}</td>
                    <td>{aluno.Curso}</td>
                    <td>{aluno.Turma}</td>
                    <td>
                      <Link to = '/editar-aluno/' ><i class="fa-solid fa-user-pen"></i></Link>
                      <i class="fa-solid fa-user-xmark"></i>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
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

export default Home;
