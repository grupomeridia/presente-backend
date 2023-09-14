import React, { useState } from "react";
import styles from "./style.module.css";
import Navbar from "@/components/Navbar/navbar";
import Footer from "@/components/Footer/footer";
import api from "../../client/api";

function CadastroProfessor() {
  const [ativo, setAtivo] = useState(true);
  const [nome, setNome] = useState("");
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);

  const handleSubmit = (event) => {
    event.preventDefault();

    const professorData = {
      nome,
      ativo
    };
    console.log(professorData);

    api.professor
      .create(professorData)
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
          <h1>Cadastro do Professor</h1>
          {message && (
            <div className={isSuccess ? "success-message" : "error-message"}>
              {message}
            </div>
          )}
          <form onSubmit={handleSubmit}>
            <div className={styles.input_container}>
              <label htmlFor="nome">Professor:</label>
              <input
                type="text"
                name="professor"
                id="professor"
                autocomplete="off"
                placeholder="Nome do Professor"
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

export default CadastroProfessor;
