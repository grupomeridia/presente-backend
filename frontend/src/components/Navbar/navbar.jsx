import Link from "next/link";
import Image from "next/image";
import styles from "./navbar.module.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHistory,
  faUserCheck,
  faChalkboardTeacher,
  faBell,
  faTachometerAlt,
  faUserPlus,
} from "@fortawesome/free-solid-svg-icons";
import { useState, useEffect } from "react";
import Cabecalho from "../Cabecalho/cabecalho";
import { useRouter } from "next/router";

const Navbar = () => {
  const [activeItem, setActiveItem] = useState("");
  const [userType, setUserType] = useState("professor"); // Substitua por 'aluno' ou 'professor' conforme necessário
  const [userImage, setUserImage] = useState(""); // lembrar de colocar aqui a imagen dafault
  const router = useRouter();

  useEffect(() => {
    const fetchedImage = ""; //adiciona aqui o caminho pra pegar a imagen no backend
    setUserImage(fetchedImage);
  }, []);

  const getMenuItems = () => {
    if (userType === "aluno") {
      return [
        { name: "Histórico", icon: faHistory, link: "/historico" },
        { name: "Presença", icon: faUserCheck, link: "/presenca" },
      ];
    }

    if (userType === "professor") {
      return [
        { name: "Frequência", icon: faHistory, link: "/frequencia" },
        { name: "Chamada", icon: faUserCheck, link: "/chamada" },
        {
          name: "Presença",
          icon: faChalkboardTeacher,
          link: "/presenca-professor",
        },
        { name: "Lembretes", icon: faBell, link: "/lembretes-professor" },
      ];
    }

    if (userType === "admin") {
      return [
        { name: "Dashboard", icon: faTachometerAlt, link: "/dashboard" },
        { name: "Chamada", icon: faUserCheck, link: "/chamada-admin" },
        { name: "Cadastrar", icon: faUserPlus, link: "/cadastrar" },
        {
          name: "Presença",
          icon: faChalkboardTeacher,
          link: "/presenca-admin",
        },
        { name: "Alunos", icon: faUserPlus, link: "/alunos" },
        { name: "Lembretes", icon: faBell, link: "/lembretes-admin" },
      ];
    }
    return [];
  };

  return (
    <>
      <header className={styles.pageHeader}>
        <div className={styles.userInfo}>
          <Image
            className={styles.userImg}
            src={userImage}
            alt="User"
            width={50}
            height={50}
          />
          <div className={styles.userText}>
            <span className={styles.userName}>John Doe</span>
            <span className={styles.userCourse}>Computer Science</span>
          </div>
        </div>

        <nav className={styles.nav}>
          <ul className={styles.adminMenu}>
            {getMenuItems().map((item) => (
              <li key={item.name} onClick={() => setActiveItem(item.name)}>
                <Link href={item.link}>
                  <span
                    className={`${styles.iconTextContainer} ${
                      router.pathname === item.link ? styles.active : ""
                    }`}
                  >
                    <FontAwesomeIcon icon={item.icon} size="1x" />
                    {item.name}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      </header>
    </>
  );
};

export default Navbar;
