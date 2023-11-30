<template>
  <article id="about" class="about-section">
    <section class="column">
      <img src="/assets/logo-bruno-minelli.svg" alt="" />
      <h1 class="title">Bruno Minelli</h1>
      <h2 class="subtitle">
        Desenvolvedor Fullstack | Tecnologia da Informação | Apaixonado por
        Jogos e Tecnologia
      </h2>
    </section>
    <section class="row">
      <div class="card">
        <p class="primary-card">
          Sou apaixonado por jogos e tecnologia com mais de dez anos de
          experiência no setor de Tecnologia da Informação.
        </p>
        <img src="/assets/icon-joystick.svg" alt="" />
      </div>
      <div class="card">
        <p class="tertiary-card">
          Atuo com desenvolvimento de sistemas web e mobile e minha comunicação
          assertiva me permite alinhar expectativas e superar desafios.
        </p>
        <img src="/assets/icon-devices.svg" alt="" />
      </div>
    </section>
  </article>
</template>

<script>
export default {
  name: "About",
  template: "<AboutSectionPage />",
};
</script>
