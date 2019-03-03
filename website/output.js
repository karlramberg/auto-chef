var currentJson;

function yesPress() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/jsonyes", true);
    xhttp.send(currentJson);
    updatePage();
}

function maybePress() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/jsonmaybe", true);
    xhttp.send(currentJson);
    updatePage();
}

function noPress() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/jsonno", true);
    xhttp.send(currentJson);
    updatePage();
}
function updatePage() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
            var objs = JSON.parse(this.responseText);
            currentJson = this.responseText;

            var list = "";
            let collectionString = "";
            objs.forEach(function(i) {
                let count = 0;
                if(!(list.includes(i.name))) {
                    count = occurances(i, objs);
                    if(count == 1) {
                        list += `<li> ${i.name} </li>`;
                    } else {
                        list += `<li> ${count} ${i.name} </li>`;
                    }
                }
            });
            document.getElementById("ingredients").innerHTML = list;
        }
    };
    xhttp.open("GET", "/jsonget", true);
    xhttp.send();
}

function occurances(i, objs) {
    let count = 0;
    objs.forEach(function(a) {
        if (a.name == i.name) {
            count++
        }
    });
    return count;
}
