
function addBootstrapStyles() {
    const headers = document.getElementsByTagName("h2");
    const addLink = (header)=> {

        let small = document.createElement("small");
        let link = document.createElement("a");
        link.classList.add("toc-link");
        link.href = "#" + header.id ;
        link.innerHTML = " 🔗 ";
        small.classList.add("text-muted");
        small.classList.add("text-decoration-none");
        small.appendChild(link);
        header.insertAdjacentElement("beforeend", small);

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