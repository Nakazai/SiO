<!DOCTYPE html>
<html>
<head>
<title>server log files</title>
<style>  
textarea{
        width:90%;
        height:25rem;
        background-color:#99FFCC;
        border:1px solid #008800;
	
}
table, th, td {
    border: 1px solid black;

}
td {
   padding-left: 95px;

}


</style>


</head>
<body>
<h1>nginx og gunicorn logfiler </h1>

</style>
<?php
echo "Servertid og dato er: <br> <strong>".date('Y-m-d H:i:s')."</strong>";

echo "<br><br>Tilgjengelig diskplass <br>";

$bytes = disk_free_space("."); 
    $si_prefix = array( 'B', 'KB', 'MB', 'GB', 'TB', 'EB', 'ZB', 'YB' );
    $base = 1024;
    $class = min((int)log($bytes , $base) , count($si_prefix) - 1);
    echo '<strong>' . $bytes . '  B<br/>';
    echo sprintf('%1.2f' , $bytes / pow($base,$class)) . ' ' . $si_prefix[$class] . '</strong>';

echo "<br><br>Serverens RAM i mb<br>";  
exec("free -mtl | grep 'Mem' | grep -oP 'Mem:\K.*'", $output);
  //print_r($output);
echo "<table>
<th>total - used - free - shared - buff/cache - available</th>";
foreach ($output as $showOutput) {
        echo "<tr><td>";
        echo $showOutput."<br>";
        echo "</tr></td>";
}
echo "</table>";




$gunicorn = file_get_contents("/webapps/sio/logs/gunicorn_supervisor.log");
$access = file_get_contents("/webapps/sio/logs/nginx-access.log");
$error = file_get_contents("/webapps/sio/logs/nginx-error.log");
echo "<h2>Gunicorn log</h2>";
echo "<textarea readonly>".$gunicorn."</textarea>";
echo "<h2> Nginx access log </h2>";
echo "<textarea readonly>".$access."</textarea>";
echo "<h2> Nginx error log </h2>"; 
echo  "<textarea readonly>".$error."</textarea>";
"<br>";


?>
</body>
</html>
