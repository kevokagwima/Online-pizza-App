const login = document.querySelector(".login");
const profile = document.querySelector(".profile");

login.addEventListener("click", () => {
  profile.classList.toggle("show-profile");
});
