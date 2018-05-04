<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <?php
            // Read the pipe file
            $pipefile = fopen("python/pipe", "r") or die("Unable to open pipe");
            echo fread($pipefile, filesize("python/pipe"));
            fclose($pipefile)
        ?>
        
        <!-- Temporary -->
        <hr>
        <form action="FormSubmit.php" method="post">
            <input type="submit">
        </form>

    </body>
</html>
