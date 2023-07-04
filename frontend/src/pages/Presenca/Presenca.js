import styles from "./Presenca.module.css";
import NavBar from "../../componets/layout/Navbar";
import Footer from "../../componets/layout/Footer";
import React, { useState, useEffect } from "react";
import api from "../../client/api";

function Presenca() {
  const [professores, setProfessores] = useState([]);
  const [projetos, setProjetos] = useState([]);
  const [projetoSelecionado, setProjetoSelecionado] = useState("");
  const [professor, setProfessor] = useState("");
  const [turmaSelecionada, setTurmaSelecionada] = useState("");
  const [turmas, setTurmas] = useState([]);
  const [chamadas, setChamadas] = useState([]);
  const [isActive, setIsActive] = useState(true);
  const [presencas, setPresencas] = useState([]);
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);

  useEffect(() => {
    const fetchPresencas = async () => {
      try {
        const response = await api.presenca.findByPresentes();
        console.log(response.data);
        setPresencas(response.data);
      } catch (error) {
        console.error("Erro ao buscar as presenças", error);
      }
    };

    fetchPresencas();
  }, []);

  console.log(presencas);

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
          <table id="example">
            <thead>
              <tr>
                <th>Nome</th>
                <th>Ra</th>
                <th>Horario</th>
                <th>N° da Chamada</th>
              </tr>
            </thead>
            <tbody>
              {presencas.map((presenca) => (
                <tr key={presenca.Id}>
                  <td>{presenca.Aluno_nome}</td>
                  <td>{presenca.Aluno_ra}</td>
                  <td>{presenca.Horario}</td>
                  <td>{presenca.Chamada}</td>
                </tr>
              ))}
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

export default Presenca;
