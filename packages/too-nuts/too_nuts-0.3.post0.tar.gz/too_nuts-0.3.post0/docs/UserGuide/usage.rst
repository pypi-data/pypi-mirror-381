Usage
=====

Command line Interface
----------------------

The CLI for the Neutrino Target Scheduler is based on clicker and works as follows

.. code-block:: bash

    $ nuts --help
        Usage: nuts [OPTIONS] COMMAND [ARGS]...

        Options:
         --help  Show this message and exit.

        Commands:
         gui          Run the GUI.
         init         Initialize the directory structure needed for NuTS.
         listen       Run listeners to collect alerts from GCN and TNS.
         make-config  Generate a new config file
         run          Run NuTS on a given database
         single       Run NuTS on a single source.

Initialize
~~~~~~~~~~

The `init` command is used to set up the directory structure for NuTS. This includes creating the necessary folders and configuration files used for the source database. NuTS by default includes a short list of hand selected source candidates.

.. code-block:: bash

    $ nuts init --help
        Usage: nuts init [OPTIONS] [PATH]

        Options:
        --help  Show this message and exit.

This is used as follows:

.. code-block:: bash

    $ nuts init /path/to/your/Database

Make-config
~~~~~~~~~~~

The `make-config` command can be used to generate a config file with the correct path to the installed version of `nuts`

.. code-block:: bash

    $ nuts make-config --help
        Usage: nuts make-config [OPTIONS] CONFIG_PATH

         Generate a new config file with the correct path after running nuts init

         Args:   config_path (str): path for the new config file

        Options:
         --help  Show this message and exit.


This is used as follows:

.. code-block:: bash

    $ nuts make-config <config-file-name.toml>

We recommend to remove all the parameters that you do not want to edit. The input values that are not provided will be filled with the default values. However, some parameters are not created by default in the configuration file. Specifically, figure names are not initialized (and thus figures are not created). To modify these parameters, open the .toml configuration file and add them in the file. The default figure names are the following:

| [output.plots.detector]
| detector_location_mollweide = "Detector_location_mollweide"
| detector_location_hammer = "Detector_map_hammer"
| detector_location_aeqd = "Detector_map_aeqd"

| [output.plots.source_skymaps]
| skymap_none = "Sky_observable"
| skymap_all = "Sources_all"
| skymap_obs = "Sources_observable"
| skymap_sched = "Sources_scheduled"
| skymap_comp = "Sources_comp"

| [output.plots.source_trajectories]
| source_trajectories_full_sky = "Traj_all"
| source_trajectories_zoom = "Traj_fov"
| source_trajectories_comp_full_sky = "Traj_Scheduled_all"
| source_trajectories_comp_zoom = "Traj_Scheduled_fov"

| [output.plots.flight]
| tobs_sources = "Flight_tobs_sources"
| tobs_priorities = "Flight_tobs_priorities"

Listen
~~~~~~

The `listen` option is dedicated to the listeners for GCN and TNS

.. code-block:: bash

    nuts listen --help
        Usage: nuts listen [OPTIONS] CONFIG_PATH

         Run listeners to collect alerts from GCN and TNS.

        Args:
         config_path (str): Path to the configuration file
         listener  (str): Listener name GCN or TNS
         log_level (str): logging level
         log_dir (str): Directory to save log files

        Options:
         -l, --listener [GCN|TNS]
         -log, --log-dir TEXT      Directory to save log files
         -ll, --log-level TEXT     Log level
         --help                    Show this message and exit.


The `--log-dir` and `--log-level` are not mandatory inputs. An example could be

.. code-block:: bash

    nuts listen -l GCN -log logs

The user is required to subscribe to TNS and GCN alerts by creating an account on these platforms, and indicate the associated credentials in the configuration file. More information is provided in the documentation.

Run
~~~

The `run` is the main command used to trigger the scheduler
An example of usage could be

.. code-block:: bash

    nuts run <config-file-name.toml> -o all

to prepare the database, calculate a possible observation window, find observable sources and build a schedule.

Run currently allows for the following options:

* `obs_window`: calculates the next possible observation window(s) for the input date given in the configuration file
* `combine_db`: prepares the database by combining the different database files
* `clean_db`: prepares the database by excluding outdated sources and adding the priority ranking for the sources
* `prep_db`: `combine_db` and `clean_db|
* `observability`: calculates the observable sources for a given database
* `observations`: `prep_db` and `observability`
* `schedule`: calculates a schedule for a list of known observable sources
* `obs_sched`: `observability` and `schedule`
* `gw`: runs observability for poorly localized (GW) sources
* `pointing_obs`: computes FOV cuts for a known pointing of the detector
* `visuals`: produces visualizations of the results
* `all`: `prep_db`, `obs_sched` and `visuals`
* `obs_windows_all`: computes all successive observation windows for a given flight time and trajectory
* `flight`: computes all observabilities, schedules and visuals for a given flight time and trajectory

Graphical user interface
------------------------

The GUI allows the user to perform most of the actions allowed by the CLI. To start this interface, use the command line

.. code-block:: bash

    nuts gui

The GUI provides a documentation, allows to generate and edit a configuration file, listen to alert systems, add sources to the database, run NuTS to determine observable source and compute an observation schedule, schedule a single source, visualize the results. The ToO user interface was developed using the open-source Python framework Streamlit.
