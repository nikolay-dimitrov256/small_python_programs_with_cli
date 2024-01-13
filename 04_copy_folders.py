import os


def create_code_folder():
    if os.path.exists('./CODE'):
        return None

    os.mkdir('./CODE')


def copy_empty_folders():
    resources = './RESOURCES'

    if not os.path.exists(resources):
        return None

    for folder in os.listdir(resources):
        current_path = f'./CODE/{folder}'

        if os.path.exists(current_path):
            continue

        os.mkdir(current_path)


create_code_folder()

copy_empty_folders()
