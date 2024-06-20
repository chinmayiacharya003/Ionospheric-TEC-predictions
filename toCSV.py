import csv


def convert_txt_to_csv(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r') as txt_file, open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the header
        header = ["YEAR", "DOY", "HR", "Kp index", "R (Sunspot No.)", "Dst-index, nT", "ap_index, nT", "f10.7_index"]
        csv_writer.writerow(header)
        
        for line in txt_file:
            # Split line by multiple spaces
            columns = line.split()
            
            # Write the data row
            csv_writer.writerow(columns)
    print("Done")

txt_file_path = 'Data/all_data.txt'
csv_file_path = 'Data/all_data.csv'
convert_txt_to_csv(txt_file_path, csv_file_path)    