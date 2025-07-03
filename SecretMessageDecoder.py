# Imports
import requests
from bs4 import BeautifulSoup

# Map object, for our convenience
class map:
    def __init__(self, table):
        # Form an array that contains
        # each row of values
        table_data = []
        for row in table.find_all("tr"):
            row_data = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
            table_data.append(row_data)

        # Determine which columns represent which type of data
        # Assume the name for each column is in the top row
        field_name_index = 0
        x_index = -1
        y_index = -1
        char_index = -1
        for index, field_name in enumerate(table_data[field_name_index]):
            if field_name == "x-coordinate":
                x_index = index
            elif field_name == "y-coordinate":
                y_index = index
            else:
                char_index = index

        # Finally, create an organized two-dimensional array, where
        # the first dimension has all of the rows and
        # the second dimension has the columns for each row.
        # This way, we have a proper map to display the code with.
        field_data_start_index = 1
        table_data_length = len(table_data)
        table_array = []
        table_array_length = 0
        for index in range(field_data_start_index, table_data_length):
            current_data = table_data[index]
            current_y = int(current_data[y_index])
            current_x = int(current_data[x_index])

            # Increase the height of the map whenever
            # the current Y coordinate exceeds the height
            while current_y + 1 > table_array_length:
                table_array.append([])
                table_array_length += 1
            
            # Do the same with width. Note that the
            # width is specific to each row rather than
            # all rows.
            while current_x + 1> len(table_array[current_y]):
                table_array[current_y].append(" ")

            table_array[current_y][current_x] = current_data[char_index]
        
        # Set the final result as our map object's data.
        self.map = table_array

        # Reverse the order of the array's rows, since the Y coordinates are treated
        # as GOING UP when increasing in value, rather than the usual going down.
        self.map.reverse()

    # Create a string representing the map and print it to the console
    def show_map(self):
        str = ""

        for row in self.map:
            for data in row:
                str += data
            str += "\n"

        print(str)

# main routine function
def main_routine():
    # Special thanks to this thread on Solution Fall for
    # help with writing this code: https://solutionfall.com/question/how-can-table-data-from-a-public-google-doc-be-parsed-using-python/
    url = input("Please provide the URL of the document you wish to read, or type \"quit\" to end the operation: ")

    if url == "quit":
        return True

    # Send an HTTP GET request to retrieve the content of the Google Doc
    # If the request fails, provide a message indicating such
    try:
        response = requests.get(url)
    except ValueError as e:
        print("Please ensure the URL you provided was correct and functional.\nFull error message: %s" % (e))
        return False

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table element in the Google Doc
    table = soup.find("table")

    if table:
        map(table).show_map()
        return False
    else:
        print("No table was found. Please ensure that the URL you provided was correct and functional.")
        return False

end_routine = False
while end_routine == False:
    end_routine = main_routine()