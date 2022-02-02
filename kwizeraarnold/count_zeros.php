<?php
function CountZeros($arr)
{
   $count = 0;
   foreach($arr as $ele)
   {
      if($ele == 0)
      {
	$count++;
      }
   } 
   return $count; 
}
?>