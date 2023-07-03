import styles from "./Options.module.css";
import NavBar from "../../componets/layout/Navbar";
import Footer from "../../componets/layout/Footer";
import React, { useState, useEffect } from "react";
import api from "../../client/api";

function Options() {
  const [professores, setProfesores] = useState([]);
  const [projetos, setProjetos] = useState([]);
  const [projeto, setProjeto] = useState("");
  const [professor, setProfesor] = useState("");
  const [turma, setTurma] = useState("");
  const [turmas, setTurmas] = useState([]);
  const [chamadaAtiva, setChamadaAtiva] = useState(false);
  const [chamadas, setChamadas] = useState([]);
  const [projetoSelecionado, setProjetoSelecionado] = useState("");
  const [professorSelecionado, setProfessorSelecionado] = useState("");
  const [turmaSelecionada, setTurmaSelecionada] = useState("");
  const [message, setMessage] = useState("");
  const [isSuccess, setIsSuccess] = useState(true);
  const [ativo,setAtivo] = useState(true);

  const handleSubmit = (event) => {
    event.preventDefault();

    const chamadaData = {
      projeto: projetoSelecionado,
      professor: professorSelecionado,
      turma: turmaSelecionada,
      ativo: true,
    };

    console.log(chamadaData);

    api.chamada
      .create(chamadaData)
      .then((response) => {
        console.log(response.data);
        setMessage("Chamada cadastrada com sucesso");
        setIsSuccess(true);
      })
      .catch((error) => {
        console.log(error);
        setMessage("Erro ao cadastrar a Chamada");
        setIsSuccess(false);
      });

  };

  // const handleClick = () => {
  //   setChamadaAtiva(!chamadaAtiva);
  // };

  const handleProjetoChange = (event) => {
    setProjetoSelecionado(event.target.value);
  };

  const handleProfessorChange = (event) => {
    setProfessorSelecionado(event.target.value);
  };

  const handleTurmaChange = (event) => {
    setTurmaSelecionada(event.target.value);
  };

  useEffect(() => {
    const fetchChamadas = async () => {
      try {
        const response = await api.chamada.listAll();
        console.log(response.data);
        setChamadas(response.data);
      } catch (error) {
        console.error("Erro ao buscar os chamadas", error);
      }
    };

    fetchChamadas();
  }, []);


  useEffect(() => {
    const fetchProfesores = async () => {
      try {
        const response = await api.professor.listAll();
        console.log(response.data);
        setProfesores(response.data);
      } catch (error) {
        console.error("Erro ao buscar os profesores", error);
      }
    };

    fetchProfesores();
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
        console.error("Erro ao buscar os projetos", error);
      }
    };

    fetchTurmas();
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
          <form onSubmit={handleSubmit}>
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
                    {projetos.map((projeto) => (
                      <option key={projeto.id} value={projeto.id}>
                        {projeto.Nome}
                      </option>
                    ))}
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
                    {professores.map((professor) => (
                      <option key={professor.id} value={professor.id}>
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
                      <option key={turma.id} value={turma.id}>
                        {turma.Nome}
                      </option>
                    ))}
                  </select>
                </div>
              </div>
              <button
                className={styles.botao}
                type="submit"
              >
                Cadastrar Chamada
              </button>
            </section>
          </form>
          <section class={styles.grid}>
            <table id="example">
              <thead>
                <tr>
                  <th>Projeto</th>
                  <th>Professor</th>
                  <th>Turma</th>
                  <th>Ativo</th>
                </tr>
              </thead>
              <tbody id="tbody">
                {chamadas.map((chamada) => (
                  <tr key={chamada.Id}>
                    <td>{chamada.Projeto}</td>
                    <td>{chamada.Professor}</td>
                    <td>{chamada.Turma}</td>
                    <td>
                      <i class="fa-solid fa-user-pen"></i>
                      <i class="fa-solid fa-user-xmark"></i>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
          <script
            src="https://kit.fontawesome.com/a146d88807.js"
            crossorigin="anonymous"
          ></script>
          <script src="//code.jquery.com/jquery-3.3.1.js"></script>
          <script src="//cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
          <script src="{{ url_for('static', filename='js/home-table.js') }}"></script>
          <script src="{{ url_for('static', filename='js/toggle-menu.js') }}"></script>
        </section>

      </body>
      <Footer />
    </div >

  );
}

export default Options;
