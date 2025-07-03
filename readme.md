# How to run
Simply open the file using python by writing `py Secret Message Decoder.py` in the console and you will be prompted to provide a google document URL.

If the google document URL contains a table with the fields "x-coordinate", "y-coordinate" and "Character" at the top, the table's data will be processed and then it will print out the secret message hidden within the table data.

# Explanation
Using the "requests" and "BeautifulSoup" modules, this program prompts the user with a URL. If the URL has a table that is able to be processed, the program creates a raw data array of each row. Next, it determines which columns represent the X and Y coordinates, and then assumes the column that's neither is where the character data is. The indexes of these columns are stored for later.

Next, it creates a two-dimensional array where the first dimension contains each row, and the second dimension contains the character data for each column in said row. By setting up the array this way, the X and Y coordinates can be used to fetch the correct character data from the array.

Lastly, since the Data Annotation prompt assumes that positive Y coordinates go UP instead of DOWN (down is more common, typically), the array's rows are arranged in reverse order. The map is then printed to the console.

For the sake of convenience, this routine will loop indefinitely until the user types "quit" to end the program.