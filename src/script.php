<?php 
  echo '<pre>';
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['sound']) ) {
  $cmd = "python /usr/local/bin/send.py " . $_POST['sound'];
  $last_line = shell_exec($cmd);
  echo ' </pre>
  <hr /> Last Line of output: ' . $last_line . '
  <hr /> Return Val';
}
foreach ($_POST as $param_name => $param_val) {
    echo "Param: $param_name; Value: $param_val<br />\n";
}
?>
