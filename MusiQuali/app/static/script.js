document.addEventListener('DOMContentLoaded', () => {
    const themeSauvegarde = localStorage.getItem('theme');
        if (themeSauvegarde === 'sombre') {
        activerModeSombre();
    }
});

const boutonMode = document.getElementById('bouton');
if (boutonMode) {
    boutonMode.addEventListener('click', chgt_mode);
}

function chgt_mode(event) {
    let bouton = event.target;
    
    if (bouton.classList.contains('mode-sombre')) {
        activerModeSombre();
        localStorage.setItem('theme', 'sombre');
    } 
    else {
        activerModeClair();
        localStorage.setItem('theme', 'clair');
    }
}

function activerModeSombre() {
    let bouton = document.getElementById('bouton');
    let body = document.querySelector('body');
    let nav = document.querySelector('.nav');
    let presentation = document.querySelector('.presentation');
    let equipe = document.querySelector('.equipe');
    let btnLogout = document.getElementById('logout');

    if(body) body.classList.add('sombre');
    if(nav) nav.classList.add('sombre');
    if(presentation) presentation.classList.add('sombre');
    if(equipe) equipe.classList.add('sombre');

    if (bouton) {
        bouton.classList.remove('mode-sombre');
        bouton.classList.add('mode-clair');
        bouton.value = "☀️";
    }

    if (btnLogout) {
        btnLogout.classList.remove('btn-logout');
        btnLogout.classList.add('btn-logout-sombre');
    }
}

function activerModeClair() {
    let bouton = document.getElementById('bouton');
    let body = document.querySelector('body');
    let nav = document.querySelector('.nav');
    let presentation = document.querySelector('.presentation');
    let equipe = document.querySelector('.equipe');
    let btnLogout = document.getElementById('logout');

    if(body) body.classList.remove('sombre');
    if(nav) nav.classList.remove('sombre');
    if(presentation) presentation.classList.remove('sombre');
    if(equipe) equipe.classList.remove('sombre');

    if (bouton) {
        bouton.classList.remove('mode-clair');
        bouton.classList.add('mode-sombre');
        bouton.value = "🌒";
    }

    if (btnLogout) {
        btnLogout.classList.remove('btn-logout-sombre');
        btnLogout.classList.add('btn-logout');
    }
}

const selectLangue = document.getElementById('select-langue');
if (selectLangue) {
    selectLangue.addEventListener('change', function() {
        const langue = this.value;
        window.location.search = '?lang=' + langue;
    });
}

function page_login(){
    document.location.href="http://localhost:8000/login";
}
const btnLogin = document.getElementById('login');
if (btnLogin) {
    console.log('login')
    btnLogin.addEventListener('click', page_login);
}

function page_index(){
    document.location.href="http://localhost:8000";
}
const btnIndex = document.getElementById('index');
if (btnIndex) {
    console.log('index')
    btnIndex.addEventListener('click', page_index);
}

