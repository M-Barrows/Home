// Mobile menu toggle
  const mobileMenuButton = document.querySelector("#mobile-menu-button")
  const mobileMenu = document.querySelector("#mobile-menu")
// Profile menu toggle 
  const profileMenuButton = document.querySelector("#user-menu-button")
  const userMenu = document.querySelector("#user-menu")
  
  mobileMenuButton.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden")
  })
  // TODO: Enable blur event but also allow clicking into modal for links
  // mobileMenuButton.addEventListener("blur", () => {
  //   mobileMenu.classList.add("hidden")
  // })
  profileMenuButton.addEventListener("click", () => {
    userMenu.classList.toggle("hidden")
  })
  // TODO: Enable blur event but also allow clicking into modal for links
  // profileMenuButton.addEventListener("blur", () => {
  //   userMenu.classList.add("hidden")
  // })