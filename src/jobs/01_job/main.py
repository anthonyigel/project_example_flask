# Standard libraries
import pyspark.sql.functions as f
import sys

# 84.51 Libraries
from poirot import SparkManager

# EPP Library
from epp.file_utils import get_gitrepo_info, get_latest_file
from epp.config_utils import get_source_data_config, get_solution_config

# Get repo info and set sys.path to base dir of repo
repo_info=get_gitrepo_info()
sys.path.insert(0, repo_info["rootdir"])

# Repo modules
import resources.config as cfg
import spark_steps as sps
# import src.shared.shared_module as spm

# Set the execution environment to the first argument passed to the script or default to dev
try:
    __IPYTHON__
except:
    try:
        app_env = sys.argv[1]
    except:
        app_env = "dev"
else:
    app_env = "dev"
print(f"Environment: {app_env}")

# Get source data and solution output bucket locations
src_config = get_source_data_config()
sol_config = get_solution_config(repo_name=repo_info["reponame"], app_env=app_env, platform="gcp", output_config=cfg.output_config)

# Open spark session
manager = SparkManager(app_name=repo_info["reponame"])
spark = manager.spark
print(f"Spark version {spark.version}") 

# If running python file, execute the following code
if __name__ == '__main__':
    print("Starting spark execution")
    
    # Do Stuff
