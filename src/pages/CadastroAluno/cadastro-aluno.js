import React , { useState } from 'react';
import styles from './cadastro-aluno.module.css';
import Footer from '../../componets/layout/Footer';
import Navbar from '../../componets/layout/Navbar';

function CadastroAluno() {
  const [aluno, setAluno] = useState('');
  const [ra, setRA] = useState('');
  const [curso, setCurso] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    const alunoData = {	
      aluno,
      ra,
      curso
    };

	console.log(alunoData);
  };
  


  return (
    <div>
      <Navbar />
      <section className="grid">
        <div className={styles.login_container}>
          <h1>Cadastro de Aluno</h1>
          <form onSubmit={handleSubmit}>
            <div className={styles.input_container}>
              <label htmlFor="aluno">Aluno:</label>
              <input
                type="text"
                name="aluno"
                id="aluno"
                autocomplete="off"
				placeholder="Nome do Aluno"
                value={aluno}
                onChange={(e) => setAluno(e.target.value)}
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
              <input
                type="text"
                name="curso"
                id="curso"
				autocomplete="off"
                placeholder="Curso do Aluno"
                value={curso}
                onChange={(e) => setCurso(e.target.value)}
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

export default CadastroAluno;
