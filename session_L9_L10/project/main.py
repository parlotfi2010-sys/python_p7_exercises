#==================================
#==============Task 3==============
#==================================

import os
import math

def check_folder(folder_path) :
    '''
    Check whether the given path is an existing folder.

    Parameters
    ----------
    folder_path : str
        The path of the folder.

    Returns
    -------
    bool
        True if the folder exists, otherwise False.
    '''
    return os.path.isdir(folder_path)


def list_files(folder_path) :
    '''
    Get the names and sizes of files directly inside the folder.

    Parameters
    ----------
    folder_path : str
        The path of the folder.

    Returns
    -------
    list
        A list containing file names and sizes in bytes.
    '''
    files = []

    for name in os.listdir(folder_path) :
        file_path = os.path.join(folder_path, name)

        if os.path.isfile(file_path) :
            size_bytes = os.path.getsize(file_path)
            files.append((name, size_bytes))

    return files


def display_files(files) :
    '''
    Display the names of all files in the folder.

    Parameters
    ----------
    files : list
        A list containing file names and sizes in bytes.

    Returns
    -------
    None
    '''
    print('\nFile names : ')

    if len(files) == 0 :
        print('No files found.')
        return

    for name, size_bytes in files :
        print(name)


def count_files(files) :
    '''
    Count the number of files.

    Parameters
    ----------
    files : list
        A list containing file information.

    Returns
    -------
    int
        The total number of files.
    '''
    return len(files)


def calculate_file_sizes(files) :
    '''
    Calculate and display file sizes in KB.

    The size in KB is rounded up to the next integer
    using math.ceil().

    Parameters
    ----------
    files : list
        A list containing file names and sizes in bytes.

    Returns
    -------
    list
        A list containing file names and sizes in KB.
    '''
    file_sizes = []

    print('\nFile sizes :')

    for name, size_bytes in files :
        size_kb = size_bytes / 1024
        rounded_size = math.ceil(size_kb)

        file_sizes.append((name, size_bytes, size_kb))

        print(
            f'{name} : {size_kb:.2f} KB '
            f'(rounded up : {rounded_size} KB)'
        )

    return file_sizes


def calculate_total_size(file_sizes) :
    '''
    Calculate the total size of all files in KB.

    Parameters
    ----------
    file_sizes : list
        A list containing file names and sizes.

    Returns
    -------
    float
        The total size in KB.
    '''
    total_size = 0

    for name, size_bytes, size_kb in file_sizes :
        total_size += size_kb

    return total_size


def calculate_average_size(file_sizes) :
    '''
    Calculate the average file size in KB.

    Parameters
    ----------
    file_sizes : list
        A list containing file names and sizes.

    Returns
    -------
    float
        The average file size in KB.
    '''
    if len(file_sizes) == 0:
        return 0

    total_size = calculate_total_size(file_sizes)
    average_size = total_size / len(file_sizes)

    return average_size


def find_largest_file(files) :
    '''
    Find the largest file.

    Parameters
    ----------
    files : list
        A list containing file names and sizes in bytes.

    Returns
    -------
    tuple or None
        The largest file information, or None if no files exist.
    '''
    if len(files) == 0:
        return None

    largest_file = files[0]

    for file_info in files :
        if file_info[1] > largest_file[1] :
            largest_file = file_info

    return largest_file


def find_smallest_file(files) :
    '''
    Find the smallest file.

    Parameters
    ----------
    files : list
        A list containing file names and sizes in bytes.

    Returns
    -------
    tuple or None
        The smallest file information, or None if no files exist.
    '''
    if len(files) == 0 :
        return None

    smallest_file = files[0]

    for file_info in files :
        if file_info[1] < smallest_file[1] :
            smallest_file = file_info

    return smallest_file


def count_files_by_extension(files) :
    '''
    Count files according to their extensions.

    Parameters
    ----------
    files : list
        A list containing file names and sizes in bytes.

    Returns
    -------
    dict
        A dictionary containing extensions and file counts.
    '''
    extension_counts = {}

    for name, size_bytes in files :
        extension = os.path.splitext(name)[1].lower()

        if extension == '' :
            extension = '[no extension]'

        if extension in extension_counts :
            extension_counts[extension] += 1
        else :
            extension_counts[extension] = 1

    return extension_counts


def create_report(folder_path, files, file_sizes) :
    '''
    Create a text report and save it inside the reports folder.

    Parameters
    ----------
    folder_path : str
        The path of the analyzed folder.
    files : list
        A list containing file names and sizes in bytes.
    file_sizes : list
        A list containing file names and sizes in KB.

    Returns
    -------
    None
    '''
    os.makedirs('reports', exist_ok=True)

    report_path = os.path.join('reports', 'analysis_report.txt')

    total_files = count_files(files)
    total_size = calculate_total_size(file_sizes)
    average_size = calculate_average_size(file_sizes)
    extension_counts = count_files_by_extension(files)

    with open(report_path, 'w', encoding='utf-8') as report:
        report.write('Folder Analysis Report\n')
        report.write('=' * 30 + '\n')
        report.write(f'Analyzed folder: {folder_path}\n')
        report.write(f'Total files: {total_files}\n')
        report.write(f'Total size: {total_size:.2f} KB\n')
        report.write(f'Average file size: {average_size:.2f} KB\n')

        report.write('\nFile Details:\n')

        for name, size_bytes, size_kb in file_sizes :
            rounded_size = math.ceil(size_kb)

            report.write(f'{name} : {size_kb:.2f} KB '
                         f'(rounded up : {rounded_size} KB)\n')

        largest_file = find_largest_file(files)
        smallest_file = find_smallest_file(files)

        report.write('\nLargest and Smallest Files :\n')

        if largest_file is None:
            report.write('No files found.\n')
        else:
            largest_kb = largest_file[1] / 1024
            smallest_kb = smallest_file[1] / 1024

            report.write(
                f'Largest file : {largest_file[0]} '
                f'({largest_kb :.2f} KB)\n'
            )
            report.write(
                f'Smallest file : {smallest_file[0]} '
                f'({smallest_kb :.2f} KB)\n'
            )

        report.write('\nFiles by Extension :\n')

        if len(extension_counts) == 0 :
            report.write('No files found.\n')
        else :
            for extension, count in extension_counts.items() :
                report.write(f'{extension} : {count}\n')

    print(f'\nReport saved to : {report_path}')


def main() :
    '''
    Run the folder analysis program.
    '''
    folder_path = input('Enter folder path : ').strip()

    try:
        if not check_folder(folder_path) :
            print('Error : The folder does not exist.')
            return

        files = list_files(folder_path)

        display_files(files)

        total_files = count_files(files)
        print(f'\nTotal number of files : {total_files}')

        file_sizes = calculate_file_sizes(files)

        total_size = calculate_total_size(file_sizes)
        print(f'\nTotal size : {total_size:.2f} KB')

        average_size = calculate_average_size(file_sizes)
        print(f'Average file size : {average_size:.2f} KB')

        largest_file = find_largest_file(files)
        smallest_file = find_smallest_file(files)

        if largest_file is not None :
            largest_kb = largest_file[1] / 1024
            print(f'Largest file : {largest_file[0]} '
                  f'({largest_kb:.2f} KB)')

            smallest_kb = smallest_file[1] / 1024
            print(f'Smallest file : {smallest_file[0]} '
                  f'({smallest_kb:.2f} KB)')
        else :
            print('Cannot find the largest or smallest file.')

        extension_counts = count_files_by_extension(files)

        print('\nFiles by extension : ')

        if len(extension_counts) == 0 :
            print('No files found.')
        else:
            for extension, count in extension_counts.items() :
                print(f'{extension}: {count}')

        create_report(folder_path, files, file_sizes)

    except OSError as error :
        print(f'File system error : {error}')


if __name__ == '__main__' :
    main()
