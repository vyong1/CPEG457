<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <?php
        exec('py python/HtmlBuilder.py');

        // Read the pipe file
        $pipefile = fopen("pipe", "r") or die("Unable to open pipe");
        echo fread($pipefile, filesize("pipe"));
        fclose($pipefile)
        ?>
    </body>
</html>
