$(function () {
    getdata();
    function getdata(flag=1){
        $.get("/movies/",{flag:flag},function (data) {
        let movies = data.movies;
        $("#list").empty();
        for (let i=0;i<movies.length;i++){
            let movie = movies[i];
            $("<li><img src="+"https://img.alicdn.com/bao/uploaded/"+movie.backgroundpicture+" /></li>").appendTo("#list")
        }
    })}

    $("#btn1").click(function () {

        getdata()
    });

    $("#btn2").click(function () {
        getdata(2)
    });




});