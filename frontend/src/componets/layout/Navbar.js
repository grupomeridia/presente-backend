import { Link } from "react-router-dom";
import logo from "../img/logo-removebg.png";
import React from "react";
import styles from "../layout/Navbar.module.css";
import "./Mqrules.module.css";
function Navbar() {
  return (
    <header class={styles.page_header}>
      <nav>
        <a href="" class={styles.logo}>
          <img src={logo} alt="App Logo"></img>
        </a>
        <button
          class={styles.toggle_mob_menu}
          aria-expanded="false"
          aria-label="open menu"
        ></button>
        <ul class={styles.admin_menu}>
          <li class={styles.menu_heading}>
            <h3>Admin</h3>
          </li>
          <li>
            <Link to="/presenca">
              <i class="fa-solid fa-house"></i>
              <span>Home</span>
            </Link>
          </li>
          <li>
            <Link to="/cadastrar-turma">
              <i class="fa-solid fa-person-shelter"></i>
              <span>Cadastro de Turma</span>
            </Link>
          </li>
          <li>
            <Link to="/cadastrar">
              <i class="fa-solid fa-clipboard-user"></i>
              <span>Cadastro de Aluno</span>
            </Link>
          </li>
          <li>
            <Link to="/cadastrar-projeto">
              <i class="fa-solid fa-laptop"></i>
              <span>Cadastro de Projeto</span>
            </Link>
          </li>
          <li>
            <Link to="/cadastrar-professor">
              <i class="fa-solid fa-user-tie"></i>
              <span>Cadastro de Professor</span>
            </Link>
          </li>
          <li>
            <a href="/">
              <i class="fa-solid fa-chart-line"></i>
              <span>Marca Presença </span>
            </a>
          </li>
          {/* <li>
            <a href="">
              <i class="fa-regular fa-folder-open"></i>
              <span>Histórico</span>
            </a>
          </li> */}
          <li class={styles.menu_heading}>
            <h3>Settings</h3>
          </li>
          {/* <li>
            <a href="">
              <i class="fa-solid fa-sliders"></i>
              <span>Settings</span>
            </a>
          </li> */}
          <li>
            <Link to="/options">
              <i class="fa-solid fa-gear"></i>
              <span>Options</span>
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Navbar;
