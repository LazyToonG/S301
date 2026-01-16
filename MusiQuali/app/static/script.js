const boutonMode = document.getElementById('bouton');
if (boutonMode) {
    boutonMode.addEventListener('click', chgt_mode);
}

document.getElementById('bouton').addEventListener('click',chgt_mode)

function chgt_mode(event){

    let bouton=event.target;
    let btnLogout = document.getElementById('logout');
    let presentation = document.querySelector('.presentation');
    let equipe = document.querySelector('.equipe');
    let nav = document.querySelector('.nav');
    let fin_nav = document.getElementById('fin_nav');
    let body = document.querySelector('body');

    if (bouton.classList.contains('mode-sombre')){ // passe du clair au sombre
        bouton.classList.remove('mode-sombre');
        bouton.classList.add('mode-clair');
        bouton.value="☀️"

        if(body) {body.classList.add('sombre')};
        if(nav) {nav.classList.add('sombre')};
        if(fin_nav) {fin_nav.classList.add('sombre')};
        if (presentation) {presentation.classList.add('sombre')};
        if (equipe) {equipe.classList.add('sombre')};
        if (btnLogout) {
            btnLogout.classList.remove('btn-logout');
            btnLogout.classList.add('btn-logout-sombre');
        }
    }
    else if (bouton.classList.contains('mode-clair')){ // passe du sombre au clair
        bouton.classList.remove('mode-clair');
        bouton.classList.add('mode-sombre');
        bouton.value="🌒"

        if(body) {body.classList.remove('sombre')};
        if(nav) {nav.classList.remove('sombre')};
        if (presentation) {presentation.classList.remove('sombre')};
        if (equipe) {equipe.classList.remove('sombre')};
        if (btnLogout) {
            btnLogout.classList.remove('btn-logout-sombre');
            btnLogout.classList.add('btn-logout');
        }

        document.querySelector('body').classList.remove('sombre');
        document.querySelector('.nav').classList.remove('sombre');
        document.querySelector('.presentation').classList.remove('sombre');
        document.querySelector('.equipe').classList.remove('sombre');
        document.getElementById('logout').classList.remove('btn-logout-sombre');
        document.getElementById('logout').classList.add('btn-logout');
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
    btnLogin.addEventListener('click', page_login);
}


