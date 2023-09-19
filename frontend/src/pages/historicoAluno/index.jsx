import React, { useState, useEffect } from "react";
import api from "@/client/api";
import styles from "./style.module.css";
import Navbar from "@/components/Navbar/navbar";
import Footer from "@/components/Footer/Footer";
import Cabecalho from "@/components/Cabecalho/cabecalho";
import { text } from "@fortawesome/fontawesome-svg-core";


function historicoAluno(){




    return(
        <div>
        <Cabecalho/>
        <Navbar/>
            <section className={styles.page_content}>
                <section className={styles.inner_content}>
                    <div className={styles.div_content}>
                        <div className={styles.dados}>                   
                            <div>
                                <h1>9</h1>
                                <p>Chamadas realizadas</p>
                            </div>
                            <div>
                                <h1>1</h1>
                                <p>Faltas</p>
                            </div>
                        </div>
                        <div className={styles.search_input}>
                        <div>
                            <input type="text"></input>
                            <div>buscar</div>
                        </div>
                        </div>
                    </div>
                    <div className={styles.div_table}>
                        <table className={styles.tabela}>
                            <thead>
                                <tr>
                                    <th>Nome</th>
                                    <th>Dia</th>
                                    <th>RA</th>
                                    <th>Projeto/Materia</th>
                                    <th>Professor</th>
                                    <th>Periodo</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Carlos</td>
                                    <td>22/06</td>
                                    <td>903497</td>
                                    <td>Pizaria</td>
                                    <td>Willian</td>
                                    <td>3° Periodo</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
            </section>
            <Footer/>
        </div>
    );
}

export default historicoAluno;