import shutil
from pathlib import Path
import os
import subprocess

output_zip_filename = 'release'  # .zip will be appended

files_to_include_in_dist = [
    'settings.json',
    'imgs',
]
dist_dir = Path('dist')  # automatically created by pyinstaller

def build():
    # step 0: make sure requirements are installed
    os.system('pip install -r requirements.txt')

    # step 1: execute pyinstaller
    subprocess.call(('pyinstaller', 
                        '--icon=clocks.ico', 
                        '--distpath=./dist/', 
                        '--workpath=./build/',
                        '--onefile', './main.py',
                        '--name', 'Screen_Clicker'
                    ))

    # step 2: copy to dist dir
    for f in files_to_include_in_dist:
        try:
            if os.path.isdir(f):
                shutil.copytree(f, dist_dir / f)
            else:
                shutil.copy(f, dist_dir / f)
        except Exception as e:
            print(f'Failed to copy {f}: {e}')

    # step 3: zip it up
    shutil.make_archive(output_zip_filename, 'zip', dist_dir)

    print('\n\nDone\n\n')
    print('Safe to delete "./dist/" dir and "./build/" dir now')
    print('Exiting')

if __name__ == '__main__':
    build()