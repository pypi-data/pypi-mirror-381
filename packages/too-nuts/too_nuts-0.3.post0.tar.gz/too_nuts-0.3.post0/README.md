# Welcome to NuTS, the Neutrino Target Scheduler.

The NuTS software is a Python package developed as part of a general effort: nuSpaceSim (https://heasarc.gsfc.nasa.gov/docs/nuSpaceSim/), an end-to-end simulation chain dedicated to the observation from high atmosphere or space of very to ultra-high energy particles producing extensive air showers. NuTS is build as a modular tool, and is comprised of:
- the **listener module**, which collects alerts from alert systems to build a comprehensive database of energetic transient sources,
- the **observability module**, which convolves this database with the properties of the detection system (observation period, trajectory, field of view, and other observability requirements) to produce a list of observable sources,
- the **scheduler module**, which prioritizes observations, using constraints from detection method and informed choices from models, to determine a specific schedule for a given observation period.

For more information on NuTS:
- **Documentation**: https://jem-euso.gitlab.io/euso-spb2/too/too-nuts/
- **Paper**: https://arxiv.org/abs/2500.00000
- **Source code**: https://gitlab.com/jem-euso/euso-spb2/too/nuts.git

## Regular installation

Install using pip:
```
pip install too-nuts
```

## Install from source
Download the git repository:
```
git clone https://gitlab.com/jem-euso/euso-spb2/too/too-nuts.git
```
Change into the repository
```
pip install too-nuts
```
and install the repository using pip (for regular and editable install)
```
pip install .
pip install -e .
```
This should install all dependencies needed to run the code as well

## Install from source
Download the git repository:
```
git clone https://gitlab.com/jem-euso/euso-spb2/too/too-nuts.git
```
Change into the repository
```
git clone https://gitlab.com/jem-euso/euso-spb2/too/too-nuts.git
cd too-nuts
pip install .
```

### Build documentation from source
To build the documentation once the package is installed
```
pip install -r docs/requirements
mkdir docs_b
sphinx-build -b html docs docs_b
```

## Command line Interface
The CLI for the Neutrino Target Scheduler is based on clicker and works as follows
```bash
nuts --help               
	Usage: nuts [OPTIONS] COMMAND [ARGS]...

	Options:
	--help  Show this message and exit.

	Commands:
	gui          Run the GUI.
	init         Initialize the NUTS directory structure.
	listen       Run the specified alert listener.
	make-config  Create a new config file.
	run          Run the NUTS pipeline.
	single       Build a single source event.
```

### Make-config

The `make-config` option generates a config file with the correct path to the installed version of `nuts`
```bash
nuts make-config --help  
    Usage: nuts make-config [OPTIONS] CONFIG_PATH  

     Function to copy the config file from the default location to the user  
     defines location. :Author: Claire Guepin :Last edit by: Tobias Heibges  
     (theibges@mines.edu) :Date: 2024-02-14  

     Args:     config_path (str): path for the new config file  

    Options:  
     --help  Show this message and exit.
```

This is used as follows:
```bash
nuts make-config <config-file-name.toml>
```

We recommend to remove all the parameters that you do not want to edit. The input values that are not provided will be filled with the default values. However, some parameters are not created by default in the configuration file. Specifically, figure names are not initialized (and thus figures are not created). To modify these parameters, open the .toml configuration file and add them in the file. The default figure names are the following:

```toml
[output.plots.detector]  
detector_location_mollweide = "Detector_location_mollweide"  
detector_location_hammer = "Detector_map_hammer"  
detector_location_aeqd = "Detector_map_aeqd"  

[output.plots.source_skymaps]  
skymap_none = "Sky_observable"  
skymap_all = "Sources_all"  
skymap_obs = "Sources_observable"  
skymap_sched = "Sources_scheduled"  
skymap_comp = "Sources_comp"  

[output.plots.source_trajectories]  
source_trajectories_full_sky = "Traj_all"  
source_trajectories_zoom = "Traj_fov"  
source_trajectories_comp_full_sky = "Traj_Scheduled_all"  
source_trajectories_comp_zoom = "Traj_Scheduled_fov"  

[output.plots.flight]  
tobs_sources = "Flight_tobs_sources"  
tobs_priorities = "Flight_tobs_priorities"  
```

### Listen to Alerts

The `listen` option is dedicated to the listeners for GCN and TNS
```bash
nuts listen --help        
    Usage: nuts listen [OPTIONS] CONFIG_PATH  

     Run listeners to collect alerts from GCN and TNS. :Author: Tobias Heibges  
     (theibges@mines.edu) :Last edit by: Tobias Heibges (theibges@mines.edu)  
     :Date: 2024-03-11  

     Args:     config_path (str): Path to the configuration file     listener  
     (str): Listener name GCN or TNS     log_level (str): logging level  
     log_dir (str): Directory to save log files  

    Options:  
     -l, --listener [GCN|TNS]  
     -log, --log-dir TEXT      Directory to save log files  
     -ll, --log-level TEXT     Log level  
     --help                    Show this message and exit.
```

The `--log-dir` and `--log-level` are not mandatory inputs. An example could be
```bash
nuts listen -l GCN -log logs
```

The user is required to subscribe to TNS and GCN alerts by creating an account on these platforms, and indicate the associated credentials in the configuration file. More information is provided in the documentation.

### Run NuTS

The `run` option is the main command used to trigger the scheduler
An example of usage could be
```bash
nuts run <config-file-name.toml> -o all
```
to prepare the database, calculate a possible observation window, find observable sources and build a schedule.

Run currently allows for the following options:
- `obs_window`: calculates the next possible observation window(s) for the input date given in the configuration file
- `combine_db`: prepares the database by combining the different database files
- `clean_db`: prepares the database by excluding outdated sources and adding the priority ranking for the sources
- `prep_db`: `combine_db` and `clean_db|
- `observability`: calculates the observable sources for a given database
- `observations`: `prep_db` and `observability`
- `schedule`: calculates a schedule for a list of known observable sources
- `obs_sched`: `observability` and `schedule`
- `gw`: runs observability for poorly localized (GW) sources
- `pointing_obs`: computes FOV cuts for a known pointing of the detector
- `visuals`: produces visualizations of the results
- `all`: `prep_db`, `obs_sched` and `visuals`
- `obs_windows_all`: computes all successive observation windows for a given flight time and trajectory
- `flight`: computes all observabilities, schedules and visuals for a given flight time and trajectory

## Graphical user interface

The GUI allows the user to perform most of the actions allowed by the CLI. To start this interface, use the command line
```bash
nuts gui
```
The GUI provides a documentation, allows to generate and edit a configuration file, listen to alert systems, add sources to the database, run NuTS to determine observable source and compute an observation schedule, schedule a single source, visualize the results. The ToO user interface was developed using the open-source Python framework Streamlit.

## Alert Dataformat

Information in one event:
- event_type: str   ("GRB", "TDE", ...)
- event_id: str     ("GRB123456", ...)
- publisher: str    ("Fermi, Swift, TNS, ...")
- publisher_id: str ("ATels123456")
- coordinates: astropy.SkyCoord (ra, dec)
- detection_time: astropy.time.Time  ("2022-11-11T11:11:11")
- params: dict      (any parameters that might be interesting for the event)

## Gitlab basics

### Download the source

1. Move to the directory you want to have the git repository in

**ssh download**

- Set up an ssh key on you machine and gitlab for example by following this guide:
    https://www.tutorialspoint.com/gitlab/gitlab_ssh_key_setup.html
- Download the repository
```
git clone git@gitlab.com:jem-euso/euso-spb2/too/too-nuts.git
```

**HTTPS download**

- Download the repository
```
git clone https://gitlab.com/jem-euso/euso-spb2/too/too-nuts.git
```

### How to contribute

1. Create an issue to announce what you are working on
2. Within the issue click on the small arrow next to create merge request and create a branch. If you want to branch off from a branch other than main you need to input this into the source branch field. You can leave the automatically generated branch name as is to make the connection to the issue clear.
3. Find the branch you want to work on on your machine (you might need to run `git fetch` to update)
```
git branch -a
```
(exit with :q)
4. Move to your branch
```
git checkout <branch_name>
```
5. Pull changes from repository
```
git pull
```
or
```
git fetch
```
6. Check you are on the correct branch
```
git branch
```
The branch you are on has a * in front of it
7. Note: You can change everything you see. No need to make new directories with code backups or copy code

Happy coding!

### How to upload

1. After you have one section of code completed add them to the version control
```
git add <file_name>
```
or if you want to add everything you changed
```
git add .
```
2. Commit your changes
```
git commit -m "<commit_message>"
```
add a short message that describes what you did in this commit

3. Upload your changes to gitlab
```
git push
```

### Closing an issue
When you think the issue you have been working on has been resolved create a merge request
for that issue and make sure to add Tobias Heibges as reviewer
