<!DOCTYPE html>
<html>
    <head>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    </head>
    <body>
        <form action="FormSubmit.php" method="post">
            <div>
                <label for="name">Enter a name:</label>
                <input type="text" name="name">
            </div>

            <div>
                <label for="occupation">Enter an occupation:</label>
                <input type="text" name="occupation">
            </div>

            <div>
                <input type="submit">
            </div>
        </form>
        <a href="EmbeddedTwitter.php">Click here to see a twitter feed in action</a>
    </body>
</html>
