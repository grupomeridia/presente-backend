import React, { useState } from "react";
import styles from "./cadastro-projeto.module.css";
import Footer from "../../componets/layout/Footer";
import Navbar from "../../componets/layout/Navbar";
import api from "../../client/api";

function CadastroProjeto() {
  const [ativo, setAtivo] = useState(true);
  const [nome, setNome] = useState("");
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);

  const handleSubmit = (event) => {
    event.preventDefault();

    const projetoData = {
      nome,
      ativo
    };
    console.log(projetoData);

    api.projeto
      .create(projetoData)
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
          <h1>Cadastro de Projeto</h1>
          {message && (
            <div className={isSuccess ? "success-message" : "error-message"}>
              {message}
            </div>
          )}
          <form onSubmit={handleSubmit}>
            <div className={styles.input_container}>
              <label htmlFor="nome">Projeto:</label>
              <input
                type="text"
                name="projeto"
                id="projeto"
                autocomplete="off"
                placeholder="Identificador do Projeto"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
              />
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

export default CadastroProjeto;
