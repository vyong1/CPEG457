// index.html's js
var url = 'https://newsapi.org/v2/everything?' +
					'q=Apple&' +
					'from=2018-04-09&' +
					'sortBy=popularity&' +
					'apiKey=1473d5d8b9b54099940acc059d5cb4be';

$.getJSON(url, function (data) {
		// data = the API's json response
		console.log(data);
		// Iterate through the articles
		var articles = data.articles;
		var htmlstring = "";
		articles.forEach(function (element) {
			htmlstring += "<p>";
			htmlstring += "<div>Author: " + element.author + "</div>";
			htmlstring += "<div>Title: " + element.title + "</div>";
			htmlstring += "</p>";
		});
		$("#Content").html(htmlstring);
	});