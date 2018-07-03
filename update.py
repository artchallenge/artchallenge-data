import os
import json
import subprocess
import config
import shutil

shutil.rmtree(config.data_dir, ignore_errors=True)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.check_call(['git', 'clone', '--depth=1', config.data_respository, config.temp_data_respository_path])
os.rename(os.path.join(config.temp_data_respository_path, config.data_respository_dir), config.data_dir)
shutil.rmtree(config.temp_data_respository_path)