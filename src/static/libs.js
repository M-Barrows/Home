// Mobile menu toggle
  const mobileMenuButton = document.querySelector("#mobile-menu-button")
  const mobileMenu = document.querySelector("#mobile-menu")
// Profile menu toggle 
  const profileMenuButton = document.querySelector("#user-menu-button")
  const userMenu = document.querySelector("#user-menu")
// apps menu toggle 
  const appsMenuButton = document.querySelector("#apps-menu-button")
  const appsMenu = document.querySelector("#apps-menu")
  
  const mobileAppsMenuButton = document.querySelector("#mobile-apps-menu-button")
  const mobileAppsMenu = document.querySelector("#mobile-apps-menu")
  
mobileMenuButton.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden")
  })
  profileMenuButton.addEventListener("click", () => {
    userMenu.classList.toggle("hidden")
  })
  appsMenuButton.addEventListener("click", () => {
    appsMenu.classList.toggle("hidden")
  })
  mobileAppsMenuButton.addEventListener("click", () => {
    mobileAppsMenu.classList.toggle("hidden")
  })
