Installation
============

NuTS installation
-----------------

NuTS is available via pip and can be installed using:

.. code-block:: bash

    $ python3 -m pip install too-nuts

Otherwise you can install NuTS directly from source:

.. code-block:: bash

    $ git clone https://gitlab.com/jem-euso/euso-spb2/too/too-nuts.git
    $ cd too-nuts
    $ pip install .

We recommend making an editable installation with the additional `-e` option in the install.

Listeners installation
----------------------

TNS
~~~

The TNS listening module downloads an updated database from TNS at a predefined cadence (typically 1h and we do not recommend downloading at a too high cadence). To be able to use this service, the user has to create a user account on the TNS webpage (see https://www.wis-tns.org/content/tns-getting-started) and replace the following fields in the configuration file.

.. code-block:: bash

    [settings.TNS]
    user_id = <user_id>
    user_name = <user_name>

The other arguments in the \verb|[settings.TNS]| tag can be used to specify the output format and download frequency.

GCN
~~~

GCN sends out real-time alerts via its GCN-Kafka network. First, the user has to register to receive the GCN notices (see https://gcn.nasa.gov/quickstart) and replace the following fields in the configuration file

.. code-block:: bash

    [settings.GCN]
    client_id = <client_id>
    client_secret = <client_secret>

The GCN alerts are received by the GCN listener module, which extracts the primary information from the alert and creates an event following the data format used in NuTS. There are different alert-type formats for different instruments and different processing stages. We developed a template scheme for many of these alerts, and will expand and complete this list for the next NuTS release. A list of all the supported alerts can be found in the software source directory, in the file \verb|GCN_alerts.csv|. In the same file, the user can toggle the parsing on or off for any of these alerts using a boolean, depending on the unique requirements of the experiment.

Other alerts
~~~~~~~~~~~~

For all other alerts, for instance alerts displayed in ATels, there has been no dedicated pipeline developed yet. However, they can easily be added manually into a csv. The name of this cvs file (by default ``OtherTransients.csv'') should be provided in the configuration file

.. code-block:: bash

    [files.database]
    other = "OtherTransients.csv"

This csv must contain the keys required by the data format used in NuTS and can be used as part of the database.
