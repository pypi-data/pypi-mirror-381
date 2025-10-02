import os
import json
from pathlib import Path
from .common import __itemList__
from shutil import copy2, copytree


def load_json(filename: Path | str, encoding: str = "utf-8") -> dict:
    """
    Loads dictionary from the file specified by filename
    :param filename: Absolute or relative path to the file
    :param encoding: "utf-8" is a default, but you can use None, 'cp1250' or others
    :return: returns dictionary class
    """
    if isinstance(filename, Path):
        filename = str(filename.resolve())
    if not(isinstance(filename, str)):
        raise Exception(f'Argument "filename" must be an instance of str or Path. But it is an instance of {str(type(filename))} which is not allowed.')
    with open(filename, "r", encoding=encoding) as file:
        result = json.load(file)
    try:
        # if result is instance of list
        # replaces list with object containing itemList
        # ["item1", "item2] is replace by {"itemList": ["item1", "item2]}
        if isinstance(result, list):
            result = dict({__itemList__: result})
        # result is dict
        else:
            result = dict(result)
        return result
    except:
        raise Exception(f'Cannot convert json file "{filename}" to dictionary object.')


def save_json(filename: Path | str, value, encoding: str = "utf-8", formatted: bool = True) -> None:
    """
    Saves dictionary to the file specified by filename
    :param value: dictionary object
    :param filename: Absolute or relative path to the file
    :param encoding: "utf-8" is a default, but you can use None, 'cp1250' or others
    :param formatted: If True the json will be saved as formatted text
    :return:
    """
    if not isinstance(value, (dict, list)):
        raise Exception(f'Cannot save "value" to json file. Argument "value" must be an instance of dict or list. But it is an instance '
                        f'of {str(type(value))} which is not allowed.')
    if isinstance(filename, Path):
        filename = str(filename.resolve())
    if not(isinstance(filename, str)):
        raise Exception(f'Argument "filename" must be an instance of str or Path. But it is an instance of {str(type(filename))} which is not allowed.')
    create_folder_structure(os.path.dirname(filename))
    with open(filename, "w", encoding=encoding, newline="\n") as file:
        if formatted:
            json.dump(value, file, indent=4, ensure_ascii=False)
        else:
            json.dump(value, file, ensure_ascii=False)


def load_textfile(filename: Path | str, encoding: str = "utf-8") -> str:
    """
    Loads text file and returns string
    :param filename: Absolute or relative path to the file
    :param encoding: "utf-8" is a default, but you can use None, 'cp1250' or others
    :return: Returns text loaded from the file
    """
    if isinstance(filename, Path):
        filename = str(filename.resolve())
    if not(isinstance(filename, str)):
        raise Exception(f'Argument "filename" must be an instance of str or Path. But it is an instance of {str(type(filename))} which is not allowed.')
    with open(filename, "r", encoding=encoding) as file:
        return file.read()


def save_textfile(filename: Path | str, value: str, encoding: str = "utf-8") -> None:
    """
    Ulozi text do souboru
    :param value:
    :param filename:
    :param encoding:
    :return:
    """
    if not isinstance(value, str):
        raise Exception(f'Cannot save "value" to json file. Argument "value" must be an instance of dict. But it is an instance of {str(type(value))} which is not allowed.')
    if isinstance(filename, Path):
        filename = str(filename.resolve())
    if not(isinstance(filename, str)):
        raise Exception(f'Argument "filename" must be an instance of str or Path. But it is an instance of {str(type(filename))} which is not allowed.')
    create_folder_structure(os.path.dirname(filename))
    with open(filename, "w", encoding=encoding, newline="\n") as file:
        file.write(value)


def load_binary(filename: Path | str) -> bytes:
    """
    Loads binary file and returns bytes
    :param filename: Absolute or relative path to the file
    :return: Returns bytes loaded from the file
    """
    with open(filename, "rb") as binary_file:
        return binary_file.read()


def save_binary(filename: Path | str, value: bytes,):
    """
    Saves binary data to a file
    :param filename: Absolute or relative path to the file
    :param value: Bytes to be saved
    """
    create_folder_structure(os.path.dirname(filename))
    with open(filename, "wb") as binary_file:
        binary_file.write(value)


def create_folder_structure(directory: Path | str) -> None:
    """
    Creates folder structure if it does not exist
    :param directory: Absolute or relative path to the directory
    """
    if isinstance(directory, str):
        directory = Path(directory)
    if not(isinstance(directory, Path)):
        raise Exception(f'Argument "directory" must be an instance of str or Path. But it is an instance of {str(type(directory))} which is not allowed.')
    if not directory.exists():
        directory.mkdir(parents=True)


def copy_folder(src: Path | str, dst: Path | str, symlinks=False, ignore=None):
    """
    Copy entire folder
    :param src:
    :param dst:
    :param symlinks:
    :param ignore:
    :return:
    """
    src = src if src is str else str(src)
    dst = dst if dst is str else str(dst)
    create_folder_structure(Path(dst))
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            copy2(s, d)


def copy_file(source_filename: str, destination_filename_or_directory: str) -> None:
    """
    Copy file. Creates folder structure if necessary. Overwrite file if it already exists.
    :param source_filename:
    :param destination_filename_or_directory:
    :return:
    """
    destination_path = Path(os.path.dirname(destination_filename_or_directory))
    create_folder_structure(destination_path)
    copy2(source_filename, destination_filename_or_directory)


def test_if_two_text_files_are_equal(filename1: Path | str, filename2: Path | str, encoding: str = "utf-8") -> bool:
    """
    Test if two text files are equal
    :param filename1:
    :param filename2:
    :param encoding:
    :return:
    """
    if isinstance(filename1, Path):
        filename1 = str(filename1.resolve())
    if not(isinstance(filename1, str)):
        raise Exception(f'Argument "filename" must be an instance of str or Path. But it is an instance of {str(type(filename1))} which is not allowed.')
    if isinstance(filename2, Path):
        filename2 = str(filename2.resolve())
    if not(isinstance(filename2, str)):
        raise Exception(f'Argument "filename" must be an instance of str or Path. But it is an instance of {str(type(filename2))} which is not allowed.')
    if not os.path.exists(filename1):
        return False
    if not os.path.exists(filename2):
        return False
    s1 = load_textfile(filename=filename1, encoding=encoding)
    s2 = load_textfile(filename=filename2, encoding=encoding)
    return s1 == s2


def search_folder(path: str, recursive: bool = True, list_of_extensions: list[str] | None = None,
                  filename_must_not_start_with: str | None = None, 
                  filename_must_start_with: str | None = None) -> tuple[list[str], list[str]]:
    """
    Search folder. Returns list of all files and list of all folders
    :param path:
    :param recursive:
    :param list_of_extensions:
    :return: vrati seznam souboru a seznam slozek
    :param filename_must_not_start_with:
    :param filename_must_start_with:
    """
    # ziska seznam vsech souboru a podadresaru v aktualni slozce
    list_of_files = []
    try:
        list_of_files = os.listdir(path)
    except PermissionError:
        pass
    all_files = []
    all_folders = []
    # pokud neni seznam pripon prazdny, tak jej prevede do lowercase a zabezpeci, ze pripona obsahuje tecku
    if list_of_extensions is not None:
        list_of_extensions = [(extension.lower() if extension.startswith(".") else f".{extension.lower()}") for extension in list_of_extensions]
    # projde vsechny nalezene soubory a podadresare
    for filename in list_of_files:
        # ziska uplny nazev cesty
        full_path = os.path.join(path, filename)
        # pokud se jedna o slozku, prida ji do seznamu slozek
        if os.path.isdir(full_path):
            all_folders.append(full_path)
            # pokud se ma prohledavat rekurzivne, tak slozku prohleda
            if recursive:
                recursive_files, recursive_folders = search_folder(full_path, recursive, list_of_extensions, filename_must_not_start_with, filename_must_start_with)
                all_files += recursive_files
                all_folders += recursive_folders
        # pokud se jedna o soubor tak jej prida do seznamu
        else:
            filename, extension = os.path.splitext(full_path)
            basename = os.path.basename(full_path)
            if ((list_of_extensions is None) or (extension.lower() in list_of_extensions)) and \
                    ((filename_must_not_start_with is None) or (basename.startswith(filename_must_not_start_with) is False)) and \
                    ((filename_must_start_with is None) or (basename.startswith(filename_must_start_with) is True)):
                all_files.append(full_path)
    # vrati vysledek
    return all_files, all_folders


def clear_folder(path: str, recursive: bool = True, list_of_extensions: list[str] | None = None,
                 filename_must_not_start_with: str | None = None) -> None:
    """
    Removes everything inside a folder including subfolders and files if the recursive parameter is set to true
    but the main folder will not be deleted. Only files and eventually subfolders will be deleted.
    :param path: path of the main folder which will be cleared
    :param recursive: indicator if subfolders needs to be deleted as well
    :param list_of_extensions: list of extensions of file which will be deleted. If list of extensions is None then all files will be deleted
    :param filename_must_not_start_with: If filename starts with specific prefix then it will not be deleted
    :return:
    """
    if os.path.exists(path):
        files, directories = search_folder(path, recursive=recursive, list_of_extensions=list_of_extensions, filename_must_not_start_with=filename_must_not_start_with)
        for file in files:
            os.remove(file)
        if recursive:
            for directory in reversed(directories):
                os.rmdir(directory)


def delete_folder(path: str) -> None:
    """
    Deletes entire folder including subfolders and files
    :param path:
    :return:
    """
    if os.path.exists(path):
        clear_folder(path)
        os.rmdir(path)


def delete_file(filename: str) -> None:
    """
    Deletes file
    :param filename:
    :return:
    """
    os.remove(filename)
