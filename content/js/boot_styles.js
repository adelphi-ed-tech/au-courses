
function safeName(name) {
    // replace non-alphanumeric characters with underscores
    let safe = name.replace(/[^a-z0-9]/gi, '_').toLowerCase();
    // replace multiple underscores with a single one
    safe = safe.replace(/_+/g, '_');
    // remove leading and trailing underscores
    
    let i = 0;
    while (document.getElementById(safe)) {
        safe = safe + i;
        i++;
    }
    return safe;
}


function addBootstrapStyles() {
    const headers = document.querySelectorAll("h1:not(.PageTitle), h2");
    const addLink = (header)=> {

        let link = document.createElement("a");
        let id = header.id;
        if (!id || id === "") {
            id = safeName(header.textContent);
            header.id = id;
        }
        link.href = "#" + header.id ;

        let icon = document.createElement("i");
        icon.classList.add("bi");
        icon.classList.add("bi-link-45deg");
        icon.classList.add("text-primary");
        icon.classList.add("text-decoration-none");
        // link.classList.add("fs-4");
        
        link.appendChild(icon);
        header.insertAdjacentElement("beforeend", link);

    }
    headers.forEach(addLink);
    
    const tables = document.querySelectorAll("table");
    const fmtTable = (table) => {
        table.classList.add("table");
        table.classList.add("table-striped");
        table.classList.add("table-hover");
    }

    tables.forEach(fmtTable);
}