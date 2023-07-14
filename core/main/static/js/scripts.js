var swiper = new Swiper(".mySwiper", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoplay: {
      delay: 3000,
      disableOnInteraction: false
    },
    loop : true,
});

function menuFunc(e) {
  let sidebar = document.querySelector('.sidebar_close')
    if (e.target.id == 'burger_menu' || e.target.parentNode.id == 'burger_menu') {
      sidebar.classList.add('sidebar')
      setTimeout(() => {
        sidebar.style.width = '280px'
        sidebar.style.padding = '50px 30px 30px 30px'
        
      }, 50);
      overlay.style.display = 'block';
    }
    else {
      sidebar.style.width = '0'
      sidebar.style.padding = '0'
      overlay.style.display = 'none';
      setTimeout(() => {
        sidebar.classList.remove('sidebar')
      }, 300);
    }
}

var swiper2 = new Swiper(".mySwiper2", {
  slidesPerView: 3,
  spaceBetween : 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  loop : true,
  autoplay: {
    delay: 2000,
    disableOnInteraction: false
  },
  breakpoints: {
    1000 : {
      slidesPerView : 3
    },

    800 : {
      slidesPerView : 2
    },

    200 : {
      slidesPerView : 1
    }
  }
});

var swiper = new Swiper(".mySwiper3", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  loop: true,
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
  speed: 1500
});

let dropdown_type = true

function dropdown() {
  let dropdown = document.querySelector('.dropdown')
  let arrow = document.querySelector('.fa-solid fa-arrow-down')
  if (dropdown_type) {
    dropdown.style.display = 'block'
    setTimeout(() => {
      dropdown.style.opacity = 1
    }, 10);
    dropdown_type = false
  }
  else {
    dropdown.style.opacity = 0
    setTimeout(() => {
      dropdown.styled.display = 'none'
    }, 300);
    dropdown_type = true
  }
}

var navLinks = document.querySelectorAll('.list a');
var nav_menu_links = document.querySelectorAll('.sidebar_close ul a')
var dropdown_links = document.querySelectorAll('.dropdown a')

for (var i = 0; i < navLinks.length; i++) {
  var link = navLinks[i];
  var menu_links = nav_menu_links[i]
  var dropdown_link = dropdown_links[i]
  if (link.href === window.location.href) {
      link.classList.add('page_link')
  }
  
  if (menu_links.href === window.location.href) {
      menu_links.classList.add('page_link')
  }
  if (dropdown_link.href === window.location.href) {
    dropdown_link.classList.add('page_link')
  }
}