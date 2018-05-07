<!DOCTYPE html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
        <script src="static\index.js"></script>
        <link rel="stylesheet" href="static\site.css" />
    </head>
    <body>
        <div class="content">
            <form action="URLFormSubmit.php" method="post">
                 <div class="form-group">
                    <label for="url_input">Article URL</label>
                    <input type="text" class="form-control" id="url_input" name="url_input" placeholder="Enter the Article URL">
                </div>

                <div>
                    <input type="submit">
                </div>
            </form>
        </div>
    </body>
</html>
