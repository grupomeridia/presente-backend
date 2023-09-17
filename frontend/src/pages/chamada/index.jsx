import { Fundo } from "@/components/Fundo/fundo";
import styles from "./style.module.css";
import Navbar from "@/components/Navbar/navbar";
import Cabecalho from "@/components/Cabecalho/cabecalho";

export default function Chamada() {
  return (
    <>
      <Navbar />
      <Cabecalho />
      <Fundo>
        <div className={styles.form_center}>
          <div className={styles.form}>
            <h2 className={styles.titulo}>Abrir Chamada</h2>
            <label className={styles.label} htmlFor="turma"></label>
            <input
              className={styles.input}
              type="text"
              id="turma"
              list="turmas"
              placeholder="Turma"
            />
            <datalist id="turmas">
              <option value="Turma A" />
              <option value="Turma B" />
              <option value="Turma C" />
            </datalist>

            <label className={styles.label} htmlFor="periodo"></label>
            <input
              className={styles.input}
              type="text"
              id="periodo"
              list="periodos"
              placeholder="Periodo"
            />
            <datalist id="periodos">
              <option value="Manhã" />
              <option value="Tarde" />
              <option value="Noite" />
            </datalist>

            <label className={styles.label} htmlFor="projeto"></label>
            <input
              className={styles.input}
              type="text"
              id="projeto"
              list="projetos"
              placeholder="Projeto"
            />
            <datalist id="projetos">
              <option value="Projeto 1" />
              <option value="Projeto 2" />
              <option value="Projeto 3" />
            </datalist>
          </div>
          <button className={styles.botao}>ABRIR</button>
        </div>
      </Fundo>

      <Fundo>
        <div className={styles.container_chamadas}>
          <h2>Chamadas Abertas</h2>
          <table className={styles.table}>
            <thead>
              <tr>
                <th>Turma</th>
                <th>Periodo</th>
                <th>Projeto</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>eng.Software</td>
                <td>Pizzaria</td>
                <td>Noturno</td>
                <td>Fecha:22:00</td>
              </tr>
              <tr>
                <td>eng.Software</td>
                <td>Pizzaria</td>
                <td>Noturno</td>
                <td>Fecha:22:00</td>
              </tr>
              <tr>
                <td>eng.Software</td>
                <td>Pizzaria</td>
                <td>Noturno</td>
                <td>Fecha:22:00</td>
              </tr>
              <tr>
                <td>eng.Software</td>
                <td>Pizzaria</td>
                <td>Noturno</td>
                <td>Fecha:22:00</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Fundo>
    </>
  );
}
