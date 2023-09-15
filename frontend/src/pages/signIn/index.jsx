// pages/SignIn.js
import { useState } from 'react';
import { useRouter } from 'next/router';
import styles from './style.module.css';
import logo from '../../img/logo-removebg.png'
import Image from "next/image";
import { motion } from 'framer-motion';

const SignIn = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const router = useRouter();

  const handleShowClick = () => setShowPassword(!showPassword);

  return (
    <div className={styles.container}>
      <div className={styles.card}>
      <div className={styles.avatar_center}>
            <Image src={logo} className={styles.avatar}/>
        <h1 className={styles.title}>Bem Vindo</h1>
        </div>
        <form className={styles.form}>
          <div className={styles.inputGroup}>
            <label className={styles.label}>Email:</label>
            <input 
              type="email" 
              className={styles.input} 
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className={styles.inputGroup}>
            <label className={styles.label}>Password:</label>
            <input 
              type={showPassword ? 'text' : 'password'} 
              className={styles.input} 
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button type="button" className={styles.showButton} onClick={handleShowClick}>
              {showPassword ? 'Hide' : 'Show'}
            </button>
          </div>
          <motion.button 
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 1.1 }}
        onClick={() => router.push('home')}
        className={styles.loginButton}
      >
        Acessar
      </motion.button>
          <p className={styles.helperText}>Forgot password?</p>
        </form>
      </div>
    </div>
  );
};

export default SignIn;
