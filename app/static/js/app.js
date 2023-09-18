document.getElementById("search-button").addEventListener("click", searchMovies);

function searchMovies() {
    const title = document.getElementById("input-title").value;
    const imdb_id = document.getElementById("input-imdb_id").value;
    const year = document.getElementById("input-year").value;
    const r_type = document.getElementById("input-r_type").value;
    const plot = document.getElementById("input-plot").value;
    const codeData = {
        title: title,
        imdb_id: imdb_id,
        year: year,
        r_type: r_type,
        plot: plot
    };

    fetch('/search_movies', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(codeData)
        })
        .then(response => response.json())
        .then(result => {
            outputArea.innerText = result.output || result.error || 'No output';
        })
        .catch(error => {
            setResuoutputArea.innerText = 'Error: ' + error.message;
        });
}

function displayResults(results) {
    const list = document.getElementById("results-list");
    clearResultsList();

    results.forEach((movie) => {
        const listItem = document.createElement("li");
        listItem.innerText = `${movie.Title} (${movie.Year})`;
        list.appendChild(listItem);
    });
}

function clearResultsList() {
    document.getElementById("results-list").innerHTML = "";
}