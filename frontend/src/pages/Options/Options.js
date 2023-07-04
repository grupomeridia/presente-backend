import styles from "./Options.module.css";
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
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);

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

    const chamadaData = {
      ativo: true,
      projeto_id: projetoSelecionado,
      turma_id: turmaSelecionada,
      professor_id: professor,
    };

    api.chamada
      .create(chamadaData)
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

  const handleProjetoChange = (event) => {
    setProjetoSelecionado(event.target.value);
  };

  const handleProfessorChange = (event) => {
    setProfessor(event.target.value);
  };

  const handleTurmaChange = (event) => {
    setTurmaSelecionada(event.target.value);
  };

  const fetchChamadas = async () => {
    try {
      const response = await api.chamada.listAll();
      console.log(response.data);
      setChamadas(response.data);
    } catch (error) {
      console.error("Erro ao buscar as chamadas", error);
    }
  };

  const handleDeleteChamada = async (id) => {
    try {
      await api.chamada.delete(id);
      setChamadas((prevState) =>
        prevState.filter((chamada) => chamada.id !== id)
      );
      console.log(`Chamada com ID ${id} excluída com sucesso`);
    } catch (error) {
      console.error("Erro ao excluir chamada", error);
    }
  };

  useEffect(() => {
    fetchChamadas();
  }, []);

  useEffect(() => {
    const fetchProfessores = async () => {
      try {
        const response = await api.professor.listAll();
        console.log(response.data);
        setProfessores(response.data);
      } catch (error) {
        console.error("Erro ao buscar os professores", error);
      }
    };

    fetchProfessores();
  }, []);

  useEffect(() => {
    const fetchProjetos = async () => {
      try {
        const response = await api.projeto.listAll();
        console.log(response.data);
        setProjetos(response.data);
      } catch (error) {
        console.error("Erro ao buscar os projetos", error);
      }
    };


    fetchProjetos();
  }, []);

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

  const fecharChamada = async (chamadaId) => {
    try {
      const response = await api.chamada.delete(chamadaId);
      console.log(response.data);
      console.log(response.data.Id);
      console.log(chamadaId)
      setMessage("Chamada deletada com sucesso");
      setChamadas((prevState) =>
        prevState.filter((chamada) => chamada.Id !== chamadaId)

      )
    }

    //.then((response) => {        
    catch (error) {
      console.log(chamadaId)
      console.log("Erro ao deletar a chamada", error);
    };
  };
  const toggleActiveState = (chamadaId) => {
    setChamadas((prevState) =>
      prevState.map((chamada) =>
        chamada.Id === chamadaId ? { ...chamada, Ativo: !chamada.Ativo } : chamada
      )
    );

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
              <div className={`${styles.dropdownContainer} ${styles.center}`}>
                <label htmlFor="projeto">Projetos:</label>
                <select
                  id="projeto"
                  value={projetoSelecionado}
                  onChange={handleProjetoChange}
                >
                  <option value="">Selecione um projeto</option>
                  {projetos.map((projeto) => (
                    <option key={projeto.id} value={projeto.Id}>
                      {projeto.Nome}
                    </option>
                  ))}
                </select>
              </div>
              <div>
                <label htmlFor="professor">Professores:</label>
                <select 
                  id="professor"
                  value={professor}
                  onChange={handleProfessorChange}
                >
                  <option value="">Selecione um professor</option>
                  {professores.map((professor) => (
                    <option key={professor.id} value={professor.Id}>
                      {professor.Nome}
                    </option>
                  ))}
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
                  {turmas.map((turma) => (
                    <option key={turma.id} value={turma.Id}>
                      {turma.Nome}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            <button className={styles.botao} type="submit">
              Cadastrar Chamada
            </button>
            {message && (
            <div className={isSuccess ? "success-message" : "error-message"}>
              {message}
            </div>
          )}
          </section>
        </form>
        <section className={styles.grid}>
          <table id="example">
            <thead>
              <tr>
                <th>Projeto</th>
                <th>Professor</th>
                <th>Turma</th>
                <th>Ativo</th>
                <th>Açoes</th>
              </tr>
            </thead>
            <tbody>
              {chamadas.map((chamada) => (

                <tr >

                  <td>{getNomeProjeto(chamada.projeto_id)}</td>
                  <td>{getNomeProfessor(chamada.professor_id)}</td>
                  <td>{getNomeTurma(chamada.turma_id)}</td>
                  <td>{chamada.Ativo ? "Sim" : "Não"}</td>
                  <td>
                    <i
                      className={`fa-solid fa-user-xmark ${chamada.Ativo ? styles.active : ""
                        }`}
                        onClick={() => fecharChamada(chamada.Id)}
                    ></i>
                    <i className="fa-solid fa-user-pen"></i>
                  </td>
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

export default Options;
