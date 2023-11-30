<template>
  <main>
    <HeaderComponent />
    <WelcomeSectionPage />
    <AboutSectionPage />
    <ServicesSectionPage />
    <ExperienceSectionPage />
    <ContactSectionPage />
  </main>
</template>

<script>
import HeaderComponent from "../../components/HeaderComponent.vue";
import WelcomeSectionPage from "./WelcomeSectionPage.vue";
import AboutSectionPage from "./AboutSectionPage.vue";
import ServicesSectionPage from "./ServicesSectionPage.vue";
import ExperienceSectionPage from "./ExperienceSectionPage.vue";
import ContactSectionPage from "./ContactSectionPage.vue";

export default {
  name: "HomePage",
  template: "<HomePage />",
  components: {
    HeaderComponent,
    WelcomeSectionPage,
    AboutSectionPage,
    ServicesSectionPage,
    ExperienceSectionPage,
    ContactSectionPage,
  },
};
</script>
