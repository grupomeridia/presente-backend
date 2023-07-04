import React, { useState, useEffect } from "react";
import styles from "./editar-aluno.module.css";
import Footer from "../../componets/layout/Footer";
import Navbar from "../../componets/layout/Navbar";
import api from "../../client/api";

function EditarAluno() {
  const [ativo, setAtivo] = useState(true);
  const [nome, setNome] = useState("");
  const [ra, setRA] = useState("");
  const [curso, setCurso] = useState("");
  const [turma, setTurma] = useState("");
  const [ano, setAno] = useState("");
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);
  const [aluno, setAluno] = useState("");
  const [turmas, setTurmas] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();

    const alunoData = {
      aluno,
      ativo,
      nome,
      ra,
      curso,
      turma,
    };
    console.log(alunoData);

    api.aluno
      .update(alunoData)
      
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
  const fetchTurmas = async () => {
    try {
      const response = await api.turma.listAll();
      console.log(response.data);
      setTurmas(response.data);
    } catch (error) {
      console.error("Erro ao buscar as turmas", error);
    }
  };

  fetchTurmas();
}, []);

  return (
    <div>
      <Navbar />
      <section className="grid">
        <div className={styles.login_container}>
          <h1>Editar Aluno</h1>
          {message && (
            <div className={isSuccess ? "success-message" : "error-message"}>
              {message}
            </div>
          )}
          <form onSubmit={handleSubmit}>
            <div className={styles.input_container}>
              <label htmlFor="nome">Aluno:</label>
              <input
                type="text"
                name="nome"
                id="nome"
                autocomplete="off"
                placeholder="Nome do Aluno"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
              />
            </div>
            <div className={styles.input_container}>
              <label htmlFor="ra">RA:</label>
              <input
                type="text"
                name="ra"
                id="ra"
                autocomplete="off"
                placeholder="RA do Aluno"
                value={ra}
                onChange={(e) => setRA(e.target.value)}
              />
            </div>
            <div className={styles.input_container}>
              <label htmlFor="curso">Curso:</label>
              <select
                id="DropCurso"
                value={curso}
                onChange={(e) => setCurso(e.target.value)}
              >
                <option value="" disabled selected>
                  Selecione um curso
                </option>
                <option value="ENGENHARIA_DE_SOFTWARE">
                  Engenharia de Software
                </option>
                <option value="ANALISE_E_DESENVOLVIMENTO_DE_SISTEMAS">
                  Análise e Desenvolvimento de Sistemas
                </option>
              </select>
            </div>
            <div className={styles.input_container}>
              <label htmlFor="Dropturma">Turma:</label>
              <select
                id="Dropturma"
                value={turma}
                onChange={(e) => setTurma(e.target.value)}
              >
                <option value="" disabled>
                  Selecione uma turma
                </option>
                {turmas.map((turmas) => (
                  <option key={turmas.Id} value={turmas.Id}>
                    {turmas.Nome}
                  </option>
                ))}
              </select>
            </div>
            <button className={styles.btn_login} type="submit">
              Editar
            </button>
          </form>
        </div>
      </section>
      <Footer />
    </div>
  );
}

export default EditarAluno;
