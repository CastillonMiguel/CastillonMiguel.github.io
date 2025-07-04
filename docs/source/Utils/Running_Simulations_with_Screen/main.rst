Running Simulations with Screen
===============================

This guide explains how to run a Python-based simulation using a `conda` environment inside a detached `screen` session on a remote terminal.

Step-by-Step Instructions
-------------------------

1. **Start a Named Screen Session**

   Create a new screen session with a custom name:

   .. code-block:: bash

      screen -S mysession_simulation

2. **Activate Your Conda Environment**

   Once inside the screen session, activate the environment:

   .. code-block:: bash

      conda activate my-conda-env

3. **Run Your Simulation Script**

   Start your Python simulation:

   .. code-block:: bash

      python myscript.py

4. **Detach from the Screen Session**

   To leave the session running in the background:

   - Press: ``Ctrl + a``, then ``d``

   You will return to the main terminal while the script continues running.

Managing Screen Sessions
------------------------

- **List All Screen Sessions**

  .. code-block:: bash

     screen -ls

- **Reattach to a Running Session**

  If only one screen is active:

  .. code-block:: bash

     screen -r

  If multiple sessions exist, reattach using the session name or ID:

  .. code-block:: bash

     screen -r mysession_simulation
     screen -r 1234567.mysession_simulation

  To forcibly detach it from another terminal and reattach:

  .. code-block:: bash

     screen -D -r mysession_simulation

- **Terminate a Screen Session Remotely**

  From outside the session:

  .. code-block:: bash

     screen -S 1234567.mysession_simulation -X quit

  Or from inside the session:

  .. code-block:: bash

     exit

- **Exit the Terminal Session**

  Once everything is done:

  .. code-block:: bash

     exit

Tips
----

- Screen sessions are persistent; you can disconnect from the remote server and reattach later without interrupting your simulation.
- Always use meaningful names for screen sessions to stay organized during multiple simulation runs.