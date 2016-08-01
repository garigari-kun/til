import os

def rename_files():
    target_dir = r'/Users/macuser/Documents/webapp/til/src/prank'
    # Get file names from a folder
    file_list = os.listdir(target_dir)
    # print(file_list)
    saved_path = os.getcwd()
    # print(saved_path)
    os.chdir(target_dir)
    for file_name in file_list:
        os.rename(file_name, file_name.translate('0123456789'))
    os.chdir(saved_path)




if __name__ == '__main__':
    rename_files()
