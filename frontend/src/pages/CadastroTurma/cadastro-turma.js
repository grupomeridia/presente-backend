import React, { useState } from "react";
import styles from "./cadastro-turma.module.css";
import Footer from "../../componets/layout/Footer";
import Navbar from "../../componets/layout/Navbar";
import api from "../../client/api";

function CadastroTurma() {
  const [ativo, setAtivo] = useState(true);
  const [nome, setNome] = useState("");
  const [ano, setAno] = useState("");
  const [semestre, setSemestre] = useState("");
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);

  const handleSubmit = (event) => {
    event.preventDefault();

    const turmaData = {
      nome,
      ativo,
      semestre,
      ano
    };
    console.log(turmaData);

    api.turma
      .create(turmaData)
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
  return (
    <div>
      <Navbar />
      <section className="grid">
        <div className={styles.login_container}>
          <h1>Cadastro de Turma</h1>
          {message && (
            <div className={isSuccess ? "success-message" : "error-message"}>
              {message}
            </div>
          )}
          <form onSubmit={handleSubmit}>
            <div className={styles.input_container}>
              <label htmlFor="nome">Turma:</label>
              <input
                type="text"
                name="turma"
                id="turma"
                autocomplete="off"
                placeholder="Identificador da turma"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
              />
            </div>
            <div className={styles.input_container}>
              <label htmlFor="ra">Ano:</label>
              <input
                type="number"
                name="ano"
                id="ano"
                autocomplete="off"
                placeholder="Ano"
                value={ano}
                onChange={(e) => setAno(e.target.value)}
              />
            </div>
            <div className={styles.input_container}>
              <label htmlFor="semestre">Semestre:</label>
              <select id="DropSemestre" value={semestre} onChange={(e) => setSemestre(e.target.value)}>
                <option value="" disabled selected>
                  Selecione o Semestre
                </option>
                <option value="1">Primeiro Semestre</option>
                <option value="2">Segundo Semestre</option>
                <option value="3">Terceiro Semestre</option>
                <option value="4">Quarto Semestre</option>
                <option value="5">Quinto Semestre</option>
                <option value="6">Sexto Semestre</option>
                <option value="7">Sétimo Semestre</option>
                <option value="8">Oitavo Semestre</option>
              </select>
            </div>
            <button className={styles.btn_login} type="submit">
              Cadastrar
            </button>
          </form>
        </div>
      </section>
      <Footer />
    </div>
  );
}

export default CadastroTurma;
