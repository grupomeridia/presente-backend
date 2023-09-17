import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCog } from "@fortawesome/free-solid-svg-icons";
import style from "./cabecalho.module.css";

const Cabecalho = () => {
  return (
    <div className={style.cabecalho_center}>
      <div className={style.cabecalho}>
        <span className={style.headerTitle}>App Chamada</span>
        <FontAwesomeIcon icon={faCog} className={style.headerIcon} />
      </div>
    </div>
  );
};

export default Cabecalho;
