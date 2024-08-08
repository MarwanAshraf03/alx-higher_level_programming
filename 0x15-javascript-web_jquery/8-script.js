$.ajax({
    type: "GET",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    success: (data) => {
        $.each(data.results, (i, datum) => {
            $("ul#list_movies").append("<li>"+datum.title+"</i>");
        });
    }
});
