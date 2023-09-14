import React, { useState, useEffect } from "react";
import api from "../../client/api";
import styles from "./style.module.css"; // Importe seus estilos aqui

import Navbar from "@/components/Navbar/navbar";
import Footer from "@/components/Footer/footer";

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

  return (
    <div>
      <Navbar />
      <section className={styles.page_content}>
        <section className={styles.search_and_user}>
          <div className={styles.admin_profile}>
            <span className={styles.greeting}>Hello admin</span>
            <i className="fa-solid fa-circle-user"></i>
          </div>
        </section>
        <section className={styles.grid}>
          <table className={styles.myTable} id="example">
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
                  <td>
                    {new Date(presenca.Horario).toLocaleTimeString()}
                  </td>
                  <td>{presenca.Chamada}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </section>
      <Footer />
    </div>
  );
}

export default Presenca;
