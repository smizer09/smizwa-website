const navLinkEls = document.querySelectorAll('.nav__menu');
const sectionEls = document.querySelectorAll('.service section');

let currentSection = 'home';
window.addEventListener('scroll', () => {
	sectionEls.forEach(sectionEl => {
		if (window.scrollY >= (sectionEl.offsetTop - sectionEl.clientHeight / 4)){
			currentSection = sectionEl.id;
		}
	});

	navLinkEls.forEach(navLinkEl => {
		if (navLinkEl.href.includes(currentSection)) {
			document.querySelector('.active').classList.remove('active');
			navLinkEl.classList.add('active');

		}
	});
});