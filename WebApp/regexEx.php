<?php
// Read the pipe file for the raw text
$pipefile = fopen("pipe", "r") or die("Unable to open pipe");
$rawText = fread($pipefile, filesize("pipe"));
fclose($pipefile);
// Read the pipe2 file for the reg exp
$pipefile = fopen("pipe2", "r") or die("Unable to open pipe");
$exp = fread($pipefile, filesize("pipe"));
fclose($pipefile);

$exp = '/' . $exp . '/mi';

$matches = [];

preg_match_all($exp, $rawText, $matches);
print_r($matches);


// Write the $_POST data to the pipe
// $pipefile = fopen("pipe", "w") or die("Unable to open pipe");
// foreach($_POST as $key => $value)
// {
//     fwrite($pipefile, $key .':'. $value . PHP_EOL);
// }
// fclose($pipefile);

?>