
function addBootstrapStyles() {
    const headers = document.getElementsByTagName("h2");
    const addLink = (header)=> {

        let link = document.createElement("a");
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
    for (let header of headers) {
      console.log("adding header link to " + header.id);
      addLink(header);
    }
    
    let tables = document.getElementsByTagName("table");
    for (let table of tables) {
      table.classList.add("table");
      table.classList.add("table-striped");
      table.classList.add("table-hover");
    }
}