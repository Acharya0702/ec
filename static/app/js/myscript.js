$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function (data) {
            alert(data.message)
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})


$('.minus-wishlist').click(function () {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            prod_id: id
        },
        success: function (data) {
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})


// Extra Code

const navbar = document.querySelector(".navbar");
window.onscroll = () => {
    this.scrollY > 20 ? navbar.classList.add("sticky") : navbar.classList.remove("sticky");
}



// ==========================================================For Car================================================
var swiper1 = new Swiper(".slide-content1", {
    slidesPerView: 4,
    spaceBetween: 25,
    slidesPerGroup: 1,
    centerSlide: true,
    fade: true,
    grabCursor: true,
    loop: false,
    loopFillGroupWithBlank: true,
    navigation: {
        nextEl: ".swiper-nav-next-btn1",
        prevEl: ".swiper-nav-prev-btn1",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        400: {
            slidesPerView: 2,
        },
        800: {
            slidesPerView: 3,
        },
        1200: {
            slidesPerView: 4,
        },
    }
});
var swiper2 = new Swiper(".slide-content2", {
    slidesPerView: 4,
    spaceBetween: 25,
    slidesPerGroup: 1,
    centerSlide: true,
    fade: true,
    grabCursor: true,
    loop: false,
    loopFillGroupWithBlank: true,
    navigation: {
        nextEl: ".swiper-nav-next-btn2",
        prevEl: ".swiper-nav-prev-btn2",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        400: {
            slidesPerView: 2,
        },
        800: {
            slidesPerView: 3,
        },
        1200: {
            slidesPerView: 4,
        },
    }
});
var swiper3 = new Swiper(".slide-content3", {
    slidesPerView: 5,
    spaceBetween: 25,
    slidesPerGroup: 3,
    centerSlide: true,
    fade: true,
    grabCursor: true,
    loop: false,
    loopFillGroupWithBlank: true,
    navigation: {
        nextEl: ".swiper-nav-next-btn3",
        prevEl: ".swiper-nav-prev-btn3",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        200: {
            slidesPerView: 2,
        },
        400: {
            slidesPerView: 3,
        },
        600: {
            slidesPerView: 4,
        },
        800: {
            slidesPerView: 5,
        },
        1000: {
            slidesPerView: 6,
        },
        1200: {
            slidesPerView: 7,
        },
    }
});

var swiper4 = new Swiper(".slide-content4", {
    slidesPerView: 1,
    spaceBetween: 25,
    slidesPerGroup: 1,
    centerSlide: true,
    fade: true,
    grabCursor: true,
    loop: true,
    loopFillGroupWithBlank: true,
    navigation: {
        nextEl: ".swiper-nav-next-btn4",
        prevEl: ".swiper-nav-prev-btn4",
    },
});



// ==========================================================For Car Search================================================

var radio1 = document.getElementById("flexRadioDefault1");
var radio2 = document.getElementById("flexRadioDefault2");
var carselect1 = document.getElementById("myselect1");
var carselect2 = document.getElementById("myselect2");

if (radio1) {
    radio1.addEventListener("change", updateSelectOptions);
} else {
    console.error("The radio1 with ID 'flexRadioDefault1' was not found.");
}
if (radio2) {
    radio2.addEventListener("change", updateSelectOptions);
} else {
    console.error("The radio1 with ID 'flexRadioDefault2' was not found.");
}

// Function to update the select options
function updateSelectOptions() {
    // Clear existing options
    carselect1.innerHTML = "";
    carselect2.innerHTML = "";
    var selectedcar1 = document.querySelector('input[name="flexRadioDefault"]:checked');
    if (selectedcar1) {
        // Add new options based on the selected car
        var car = selectedcar1.value;
        if (carselect1) {
            carselect1.addEventListener("change", updateSecondSelectOptions);
        } else {
            console.error("The carselect1 with ID 'myselect1' was not found.");
        }
        if (car === "Budget") {
            addOption1("", "--Select Budget--");
            addOption1("1", "1-5 Lakh");
            addOption1("2", "5-10 Lakh");
            addOption1("3", "10-20 Lakh");
            addOption1("4", "20-30 Lakh");
            addOption1("5", "30-50 Lakh");
            addOption1("6", "Above 50 Lakh");
            addOption2("", "--Select Category--");
        } else if (car === "Brand") {
            addOption1("", "--Select Brand--");
            addOption1("TATA", "TATA");
            addOption1("Toyota", "Toyota");
            addOption1("Hyundai", "Hyundai");
            addOption1("Gundai", "Gundai");
            addOption1("Pundai", "Pundai");
            addOption2("", "--Select Model--");
        }
        function updateSecondSelectOptions() {
            carselect2.innerHTML = "";
            if (carselect1.value === 'TATA') {
                addOption2("TATA_SUV", "TATA_SUV");
                addOption2("TATA_Hatchback", "TATA_Hatchback");
                addOption2("TATA_Sedan", "TATA_Sedan");
                addOption2("Nexon", "Nexon");
                addOption2("TATA_Luxury", "TATA_Luxury");
            }
            else if (carselect1.value === 'Toyota') {
                addOption2("Toyota_SUV", "Toyota_SUV");
                addOption2("Toyota_Hatchback", "Toyota_Hatchback");
                addOption2("Toyota_Sedan", "Toyota_Sedan");
                addOption2("Toyota_MUV", "Toyota_MUV");
                addOption2("Toyota_Luxury", "Toyota_Luxury");
            }
            else if (carselect1.value === 'Hyundai') {
                addOption2("Hyundai_SUV", "Hyundai_SUV");
                addOption2("Hyundai_Hatchback", "Hyundai_Hatchback");
                addOption2("Exter", "Exter");
                addOption2("Hyundai_MUV", "Hyundai_MUV");
                addOption2("Hyundai_Luxury", "Hyundai_Luxury");
            }
            else if (carselect1.value === 'Gundai') {
                addOption2("Gundai_SUV", "Gundai_SUV");
                addOption2("Gundai_Hatchback", "Gundai_Hatchback");
                addOption2("Gundai_Sedan", "Gundai_Sedan");
                addOption2("Gundai_MUV", "Gundai_MUV");
                addOption2("Gundai_Luxury", "Gundai_Luxury");
            }
            else if (carselect1.value === 'Pundai') {
                addOption2("Pundai_SUV", "Pundai_SUV");
                addOption2("Pundai_Hatchback", "Pundai_Hatchback");
                addOption2("Pundai_Sedan", "Pundai_Sedan");
                addOption2("Pundai_MUV", "Pundai_MUV");
                addOption2("Pundai_Luxury", "Pundai_Luxury");
            }
            else {
                addOption2("SUV", "SUV");
                addOption2("Hatchback", "Hatchback");
                addOption2("Sedan", "Sedan");
                addOption2("MUV", "MUV");
                addOption2("Luxury", "Luxury");
            }
        }
    }
}

// Helper function to add options to the select element
function addOption1(value, text) {
    var option = document.createElement("option");
    option.value = value;
    option.textContent = text;
    carselect1.appendChild(option);
}
function addOption2(value, text) {
    var option = document.createElement("option");
    option.value = value;
    option.textContent = text;
    carselect2.appendChild(option);
}

// ===============================================For Car Search=========================================================
// ================================================Full Screen===========================================================
const fullscreenButton = document.getElementById("fullscreen");
if (fullscreenButton) {
    fullscreenButton.addEventListener('dblclick', () => {
        if (fullscreenButton.requestFullscreen) {
            fullscreenButton.requestFullscreen();
        } else if (fullscreenButton.mozRequestFullScreen) { // Firefox
            fullscreenButton.mozRequestFullScreen();
        } else if (fullscreenButton.webkitRequestFullscreen) { // Chrome, Safari, and Opera
            fullscreenButton.webkitRequestFullscreen();
        } else if (fullscreenButton.msRequestFullscreen) { // Internet Explorer
            fullscreenButton.msRequestFullscreen();
        }
    });
} else {
    console.error('The fullscreenbutton with id "fullscreen" was not found.');
}
// ================================================Full Screen===========================================================

