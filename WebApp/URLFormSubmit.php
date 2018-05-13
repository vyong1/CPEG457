<!DOCTYPE html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
        <script src="static\urlformsubmit.js"></script>
        <link rel="stylesheet" href="static\site.css" />
    </head>
    <body>
        <div class="content">
            <a href="index.php">
                <img src="static/Pinocchio.png" class="index-btn"> 
            </a>
            <?php
            // Clear the pipe
            $pipefile = fopen("pipe", "w") or die("Unable to open pipe");
            fclose($pipefile);

            // Write the $_POST data to the pipe
            $pipefile = fopen("pipe", "a") or die("Unable to open pipe");
            foreach($_POST as $key => $value)
            {
                fwrite($pipefile, $key .':'. $value . PHP_EOL);
            }
            fclose($pipefile);
            
            // Call appropriate python script to build up the file to the pipe
            // IMPORTANT! Replace python3 here with whatever you use for python
            //            (i.e. py, python, python3, py3, etc.)
            exec('py python/URLInputHandler.py');

            // Read the pipe file
            $pipefile = fopen("pipe", "r") or die("Unable to open pipe");
            echo fread($pipefile, filesize("pipe"));
            fclose($pipefile);
            ?>
        </div>
    </body>
</html>
