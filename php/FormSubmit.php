<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <?php
        $cmd = 'py python/HtmlBuilder.py "' . $_POST['name'] . '"';
        
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
        exec('py python/HtmlBuilder.py');

        // Read the pipe file
        $pipefile = fopen("pipe", "r") or die("Unable to open pipe");
        echo fread($pipefile, filesize("pipe"));
        fclose($pipefile);
        ?>
        <a href="index.php">Click here to go back to index.php</a>
    </body>
</html>
