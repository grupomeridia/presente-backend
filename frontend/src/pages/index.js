import { motion } from 'framer-motion';
import React from 'react';
import { useRouter } from 'next/router';
import style from './style.module.css'
import Image from "next/image";
import logo from '../img/logo-removebg.png'

const Welcome = () => {
  const router = useRouter();
  
  return (
    <motion.div 
      className={style.container} 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <motion.div
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        transition={{ duration: 0.5 }}
      >
        <Image src={logo}></Image>
      </motion.div>
      <h1>
"Sistema de chamada"

      </h1>
      <p>Faça login para começar!</p>
      <motion.button 
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        onClick={() => router.push('signIn')}
      >
        Acessar
      </motion.button>
    </motion.div>
  );
};

export default Welcome;
