<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <?php
        $cmd = 'py python/HtmlBuilder.py "' . $_POST['name'] . '"';
        exec($cmd);

        // Read the pipe file
        $pipefile = fopen("pipe", "r") or die("Unable to open pipe");
        echo fread($pipefile, filesize("pipe"));
        fclose($pipefile)
        ?>
        <a href="index.php">Click here to go back to index.php<a/>
    </body>
</html>
