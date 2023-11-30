<template>
  <article id="contact" class="contact-section">
    <section>
      <div>
        <h1 class="title">Fale <br />Comigo</h1>
        <h2 class="subtitle">
          Vamos falar sobre o seu projeto e construir algo juntos.
        </h2>
      </div>
    </section>
    <section class="row">
      <div class="column">
        <p class="subtitle">
          Estou ansioso para colaborar em projetos desafiadores e inovadores.
        </p>
        <p class="title">
          Se busca um parceiro confiável para impulsionar iniciativas ou
          fortalecer sua equipe, estou pronto para a ação.
        </p>
        <p class="subtitle">
          Sinta-se à vontade para entrar em contato hoje mesmo e juntos
          alcançaremos grandes objetivos.
        </p>
      </div>
      <div class="row">
        <a href="https://www.linkedin.com/in/brunominelli"
          ><img src="/assets/icon-linkedin.svg"
        /></a>
        <a href="https://github.com/brunominelli"
          ><img src="/assets/icon-github.svg"
        /></a>
        <a
          aria-label="Chat on WhatsApp"
          href="https://wa.me/5519989769066?text=Oi, Bruno, tudo bom? Gostaria de fazer uma proposta para você."
          ><img alt="Chat on WhatsApp" src="/assets/icon-whatsapp.svg" />
        </a>
      </div>
    </section>
  </article>
</template>

<script>
export default {
  name: "Contact",
  template: "<ContactSectionPage />",
};
</script>
