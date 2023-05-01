import logo from '../img/logo-removebg.png';
import styles from './Footer.module.css';

function Footer (){
    return (
        <footer class={styles.page_footer}>
            <span>copyright by </span>
            <a href="#" target="_blank">
            <img width="45px" height="45px" src={logo} alt="Meridia Logo"></img>
            </a>
        </footer>
    );
};

export default Footer;