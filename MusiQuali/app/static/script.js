document.getElementById('bouton').addEventListener('click',chgt_mode)
            function chgt_mode(){
                let bouton=event.target;
                console.log(bouton);
                if (bouton.className == 'mode_sombre'){
                    bouton.classList.remove('mode_sombre');
                    bouton.classList.add('mode_clair');
                    bouton.value="☀️"
                    document.querySelector('body').classList.add('sombre');
                    document.querySelector('.nav').classList.add('sombre');
                    document.querySelector('.presentation').classList.add('sombre');
                    document.querySelector('.equipe').classList.add('sombre');
                }
                else if (bouton.className == 'mode_clair'){
                    bouton.classList.remove('mode_clair');
                    bouton.classList.add('mode_sombre');
                    bouton.value="🌒"
                    document.querySelector('body').classList.remove('sombre');
                    document.querySelector('.nav').classList.remove('sombre');
                    document.querySelector('.presentation').classList.remove('sombre');
                    document.querySelector('.equipe').classList.remove('sombre');
                }
            };

const selectLangue = document.getElementById('select-langue');

if (selectLangue) {
    selectLangue.addEventListener('change', function() {
        // On récupère la valeur (fr ou en)
        const langue = this.value;
        
        // On recharge la page en ajoutant ?lang=en (ou fr) à la fin de l'URL
        window.location.search = '?lang=' + langue;
    });
}

document.getElementById('login').addEventListener('click',page_login)
function page_login(){
    document.location.href="http://localhost:8000/login";
}