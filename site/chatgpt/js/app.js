// Simulation d'état des lecteurs
const lecteurs = [
    { nom: "Lecteur 1", etat: "UP", activite: "Il y a 2 min" },
    { nom: "Lecteur 2", etat: "KO", activite: "Il y a 10 min" },
    { nom: "Lecteur 3", etat: "UP", activite: "En cours" }
];

const tableBody = document.getElementById("lecteurs-table-body");

lecteurs.forEach(l => {
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${l.nom}</td>
        <td style="color:${l.etat === "UP" ? "green" : "red"}; font-weight:bold;">
            ${l.etat}
        </td>
        <td>${l.activite}</td>
    `;
    tableBody.appendChild(row);
});

// Journal des diffusions
const logs = [
    "Musique : Playlist Matin",
    "Publicité : Offre été",
    "Message urgent : Évacuation zone B"
];

const logList = document.getElementById("log-list");
logs.forEach(msg => {
    const li = document.createElement("li");
    li.textContent = msg;
    logList.appendChild(li);
});
