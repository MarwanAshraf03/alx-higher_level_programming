$("DIV#toggle_header").on("click", () => {
    if ($("header").hasClass("green")) {
        $("header").removeClass("green");
        $("header").addClass("red");
    }
    else {
        $("header").addClass("green");
        $("header").removeClass("red");
    }
})
