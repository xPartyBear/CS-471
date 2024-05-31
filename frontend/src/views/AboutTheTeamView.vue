<template>
  <section class="team-member">
    <div v-for="(member, index) in teamMembers" :key="index" class="member-profile">
      <h2>{{ member.name }}</h2>
      <p>Email: {{ member.email }}</p>
      <div class="social-links">
        <a :href="member.github" target="_blank"><img src="../assets/github-icon.png" alt="GitHub" /></a>
        <a :href="member.linkedin" target="_blank"><img src="../assets/linkedin-icon.png" alt="LinkedIn"
        /></a>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutTheTeam',
  data() {
    return {
      teamMembers: [
        {
          name: 'Ethan Rowe',
          email: 'rowe8284@kettering.edu',
          github: 'https://github.com/derppancakes',
          linkedin: 'https://www.linkedin.com/in/ethanrowe'
        },
        {
          name: 'Michael Dekoski',
          email: 'deko6236@kettering.edu',
          github: 'https://www.github.com/xpartybear',
          linkedin: 'https://www.linkedin.com/in/michaeldekoski'
        },
        {
          name: 'William Nashif',
          email: 'nash4850@kettering.edu',
          github: 'https://www.github.com/wnashif',
          linkedin: 'https://www.linkedin.com/in/williamnashif'
        },
        {
          name: 'Lily Moran',
          email: 'mora3267@kettering.edu',
          github: 'https://www.github.com/lilym01',
          linkedin: 'https://www.linkedin.com/in/lilymoran'
        },
        {
          name: 'Heidi Gwinner',
          email: 'gwin3383@kettering.edu',
          github: 'https://www.github.com/hgwinner',
          linkedin: 'https://www.linkedin.com/in/heidigwinner'
        }
      ]
    }
  }
}
</script>

<style scoped>
.team-member {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 20px;
}

.member-profile {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  text-align: center;
  width: 300px;
}

.member-profile h2 {
  margin: 10px 0;
}

.member-profile p {
  margin: 5px 0;
}

.social-links {
  margin-top: 10px;
}

.social-links a {
  display: inline-block;
  margin-right: 10px;
}

.social-links img {
  width: 30px;
  height: 30px;
}
</style>
