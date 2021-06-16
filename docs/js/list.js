window.onload = () => {
  const ulel = document.getElementById("kifus");
  for (const file of files) {
    const liel = document.createElement("li");
    const ael = document.createElement("a");
    const paths = file.split(".");
    ael.href=`./player.html?name=${paths[0]}&fmt=${paths[1]}`;
    ael.innerText=file;
    liel.appendChild(ael);
    ulel.appendChild(liel);
  }
}