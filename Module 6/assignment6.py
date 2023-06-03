import csv

def read_csv(file_path):
    duplicates = set()
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if len(row) >= 2:
                column1 = row[0]
                column2 = row[1]
                print(f'ReleasedYear: {column1}\tMovieTitle: {column2}')
                data = (column1, column2)
                if data in duplicates:
                    print(f'This is a duplicate entry: {data}')
                else:
                    duplicates.add(data)
                    
def count_occurrences(file_path, search_word):
    count = 0
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header if present
        for row in reader:
            if len(row) >= 2:
                column2 = row[1]
                if search_word in column2:
                    count += 1
    return count


# Provide the path to your CSV file here
csv_file_path = "C:\\Users\\raghavan\\Downloads\\MoviesData.csv"
read_csv(csv_file_path)

search_word = "red"
occurrences = count_occurrences(csv_file_path, search_word)
print(f'The word "{search_word}" occurs {occurrences} times in MovieTitle column.')