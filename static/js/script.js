const profile = document.getElementById("profile");
let profil = true;
function openProfile() {
  profil = !profil;
  // if (profil) profile.style.top = "100%";
  // else profile.style.top = "-250%";
  if (profil) {
    profile.style.display = "none";
  } else {
    profile.style.display = "flex";
  }
}
