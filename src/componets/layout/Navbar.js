import logo from '../img/logo-removebg.png';
import styles from '../layout/Navbar.module.css';

function Navbar () {
    return (
        <header class={styles.page_header}>
            <nav>
            <a href="" class={styles.logo}>
                <img src={logo} alt="App Logo"></img>
            </a>
            <button class={styles.toggle_mob_menu} aria-expanded="false" aria-label="open menu">
            </button>
            <ul class={styles.admin_menu}>
                <li class={styles.menu_heading}>
                <h3>Admin</h3>
                </li>
                <li>
                <a href="">
                    <i class="fa-solid fa-house"></i>
                    <span>Home</span>
                </a>
                </li>
                <li>
                <a href="">
                    <i class="fa-solid fa-clipboard-user"></i>
                    <span>Cadastro de Aluno</span>
                </a>
                </li>
                <li>
                <a href="">
                    <i class="fa-solid fa-chart-line"></i>
                    <span>Dashboard </span>
                </a>
                </li>
                <li>
                    <a href="">
                        <i class="fa-regular fa-folder-open"></i>
                    <span>Histórico</span>
                    </a>
                </li>
                <li class={styles.menu_heading}>
                <h3>Settings</h3>
                </li>
                <li>
                <a href="">
                    <i class="fa-solid fa-sliders"></i>
                    <span>Settings</span>
                </a>
                </li>
                <li>
                <a href="">
                    <i class="fa-solid fa-gear"></i>
                    <span>Options</span>
                </a>
                </li>
            </ul>
            </nav>
	</header>
    );
}

export default Navbar;