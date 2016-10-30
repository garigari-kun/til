import unicodecsv

enrollments = []
f = open('enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)
for row in reader:
    enrollments.append(row)
f.close()



def read_csv(file_name):
    with opne(file_name, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
