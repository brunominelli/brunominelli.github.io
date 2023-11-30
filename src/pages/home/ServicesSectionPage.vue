<template>
  <article id="services" class="services-section">
    <section>
      <div class="column">
        <h1 class="title">Serviços</h1>
        <h2 class="subtitle">
          O que eu posso fazer por você e por seu negócio?
        </h2>
      </div>
    </section>
    <section class="row">
      <p class="card primary-card">Consultoria em tecnologia</p>
      <p class="card secondary-card">Desenvolvimento de aplicações web</p>
      <p class="card tertiary-card">Desenvolvimento de aplicações mobile</p>
      <p class="card tertiary-card">Gamificação</p>
      <p class="card primary-card">Sites institucionais</p>
      <p class="card secondary-card">Landing pages e Hotsites</p>
    </section>
  </article>
</template>

<script>
export default {
  name: "Services",
  template: "<ServicesSectionPage />",
};
</script>
