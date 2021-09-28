<?php


/**
 * Count the number of zeroes
 */
function CountZeros($array)
{
    $arraySize = count($array);

    //sort Array
    $sortedArray = sortArray(($array));

    //if first index is not 0, then 0 is not in sorted array
    if ($sortedArray[0] != 0) {
        return 0;
    }
    $key = 0;

    //get first index of search element
    $firstIndex = getFirstIndex($sortedArray, 0, $arraySize - 1, $key, $arraySize);

    if ($firstIndex == -1) {
        return 0;
    }
    //get last index of search element
    $lastIndex = getLastIndex($sortedArray, $firstIndex, $arraySize - 1, $key, $arraySize);

    return $lastIndex - $firstIndex + 1;
}


/**
 * Sort Array first in ascending order
 * using quicksort
 */
function sortArray(array $array)
{
    $arraySize = count($array);
    if ($arraySize <= 1) {
        return $array;
    } else {
        $pivot = $array[0];
        $leftArray = $rightArray = array();
        for ($i = 1; $i < $arraySize; $i++) {
            if ($array[$i] < $pivot) {
                $leftArray[] = $array[$i];
            } else {
                $rightArray[] = $array[$i];
            }
        }

        return array_merge(sortArray($leftArray), array($pivot), sortArray($rightArray));
    }
}

/**
 * Get the first index of the searched element
 */
function getFirstIndex($array, $lowestElement, $highestElement, $key, $arraySize)
{
    if ($highestElement >= $lowestElement) {

        $midElement = floor(($highestElement + $lowestElement) / 2);

        if (($midElement == 0 || $key > $array[$midElement - 1]) && $array[$midElement] == $key) {
            return $midElement;
        } elseif ($key > $array[$midElement]) {
            //key is greater than mid element
            return getFirstIndex($array, $midElement + 1, $highestElement, $key, $arraySize);
        } else {
            //key is less than mid element
            return getFirstIndex($array, $lowestElement, $midElement - 1, $key, $arraySize);
        }
    }
    return -1;
}

/**
 * Get the last index of the searched element
 */
function getLastIndex($array, $lowestElement, $highestElement, $key, $arraySize)
{
    if ($highestElement >= $lowestElement) {

        $midElement = floor(($highestElement + $lowestElement) / 2);

        if (($midElement == $arraySize - 1 || $key < $array[$midElement + 1]) && $array[$midElement] == $key) {
            return $midElement;
        } elseif ($key < $array[$midElement]) {
            return getLastIndex($array, $lowestElement, $midElement - 1, $key, $arraySize);
        } else {
            return getLastIndex($array, $midElement + 1, $highestElement, $key, $arraySize);
        }
    }
    return -1;
}

