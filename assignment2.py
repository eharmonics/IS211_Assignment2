import urllib2
import csv
import argparse
import datetime
import logging

def downloadData(url):
    """Function to download the data from given url
        using urllib2.

    Parameters:
        url : str
            URL string
    Returns:
        The caller (object of urllib2)
    """
    return urllib2.urlopen(url)

def processData(infile):
    """Function to process the data of the given file
    and convert it into a dictionary and return it.

    Parameters:
        infile
            Object returned by downloadData()
            function.

    Returns:
            A dictionary having persons id as key and tuple
            of name and datetime object as its value.
        """
    processed_data = {}

    csv_reader = csv.reader(infile)

    next(csv_reader)
    for i, person in enumerate(csv_reader):
        try:
            p_id = int(person[0])
            p_name = person[1]
        p_birth_date = datetime.datetime.strptime(person[2], "%d/%m/%Y")
        processed_data[p_id] = (p_name, p_birth_date)

        except:
        error_msg = "Error processing line #{} for ID #{}.".format(i, p_id)
        logging.basicConfig(filename="error.log", level=logging.ERROR)
        logger = logging.getLogger("assignment2")
        logger.error(error_msg)

        return processed_data

def displayPerson(pid, dict_data):
    """Function to get name of birthday of the
    person having id equal to given pid parameter.

    Parameters:
        pid : int
            An integer that represents the id of the
            person for whom details should be returned.
        dict_data : dict
            Dictionary conataining data of all person
            returned by the processData() function.
    Prints:
        A string containing id along with person's name
        and birth date in the specified format:
        Person # is <name>  with a birthday of <date>.
    """

    if pid in dict_data:
        name = dict_data[pid][0]
        bdate = datetime.datetime.strftime(dict_data[pid][1], "%Y-%m-%d")
        print("Person #{} is {}  with a birthday of {}.".format(pid, name, bdate))
    else:
        print("No user found with that id.")

def main():
    """Driver function to use the defined
    functions to drive this program.
    """

    downloaded_data = None

    parser = argparse.ArgumentParser()
    parser.add_argument("https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv", required=True, help="Provide the csv file's URL.")
    args = parser.parse_args()

    try:
        downloaded_data = downloadData(args.url)

    except:
        print("Error occured while downloading the file !!!")

    process_dict = processData(downloaded_data)

    while True:
        pid = int(input("Enter ID to lookup: "))

        if pid <= 0:
            break

        else:
            displayPerson(pid, process_dict)


if __name__ == "__main__":
    main()