// index.html's js
/*
This was the example url provided by newsapi.org
*/
var exampleurl = 'https://newsapi.org/v2/everything?' +
					'q=Apple&' +
					'from=2018-04-09&' +
					'sortBy=popularity&' +
					'apiKey=1473d5d8b9b54099940acc059d5cb4be';


function submitAPIRequest(){
	var url = 'https://newsapi.org/v2/everything?' +
				'q=' + $("input[name='Query'").val() + "&" +
				'from=2018-04-09&' + // Remove this line later
				'sortBy=' + $('select[name="SortBy"] :selected').val() + "&" +
				'apiKey=1473d5d8b9b54099940acc059d5cb4be';
	$.getJSON(url, function (data) {
		// Clear the content div
		$("#Content").html("");
		// data = the API's json response
		console.log(data);
		// Iterate through the articles
		var articles = data.articles;
		articles.forEach(function (element) {
			var htmlstring = "";
			htmlstring += "<div>Author: " + element.author + "</div>";
			htmlstring += "<div>Title: " + element.title + "</div>";
			htmlstring += "<div>URL: " + element.url + "</div>";
			htmlstring += "<hr/>";
			$("#Content").append(htmlstring);
		});
	});
}