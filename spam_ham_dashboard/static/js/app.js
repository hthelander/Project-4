console.log("app.js")

function checkResult() {
    let message = d3.select("#message").property("value");
    console.log("** message **")
    console.log(message)

    d3.json("/api/classify/" + message).then(function (data) {
        console.log("data")
        console.log(data)

        document.getElementById("spam_or_ham").value = data["result"];
    })
}

d3.select("#submitButton").on("click", checkResult);
