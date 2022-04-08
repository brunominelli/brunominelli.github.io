import{ Component } from 'react';
import { Link } from 'react-router-dom';
import { images } from '../data/images';
import styles from '../styles/Home.module.css';

class HomeIntro extends Component {
  render() {
    return (
      <article className={styles.container}>
        <section className={styles.container_grey}>
          <div className={styles.container_block}>
            <h1>
              Olá,<br />eu sou <strong>Bruno Minelli</strong>
            </h1>
            <h2>Desenvolvedor Web</h2>
            <nav className={styles.container_button}>
              <Link to="/contact" className={`${styles.btn} ${styles.btn_white}`}>Contato</Link>
              <Link to="/projects" className={`${styles.btn} ${styles.btn_purple}`}>Projetos</Link>
            </nav>
          </div>
          <figure className={styles.container_block}>
            <img src={ images.laptop.src } alt={ images.laptop.alt } className={styles.container_image}/>
          </figure>
        </section>
      </article>
    );
  }
}

export default HomeIntro;
