'''
    SHARING DATA BETWEEN CALLBACKS
    One of the core Dash principles explained in the Getting Started Guide on Callbacks is that Dash Callbacks must never modify variables outside
        of their scope. It is not safe to modify any global variables. This chapter explains why and provides some alternative patterns for sharing
        state between callbacks.
    
    WHY SHARE STATE?
    In some apps, you may have multiple callbacks that depend on expensive data processing tasks like making database queries, running simulations, or downloading data.

    Rather than have each callback run the same expensive task, you can have one callback run the task and then share the results to the other callbacks.

    One way to achieve this is by having multiple outputs for one callback: the expensive task can be done once and immediately used in all the outputs. 
        For example, if some data needs to be queried from a database and then displayed in both a graph and a table, then you can have one callback that 
        calculates the data and creates both the graph and the table outputs.

    But sometimes having multiple outputs in one callback isn't a good solution. For example, suppose your Dash app allows a user to select a date and a 
        temperature unit (Fahrenheit or Celcius), and then displays the temperature for that day. You could have one callback that outputs the temperature
        by taking both the date and the temperature unit as inputs, but this means that if the user merely changes from Fahrenheit to Celcius then the
        weather data would have to be re-downloaded, which can be time consuming. Instead, it can be more efficient to have two callbacks: one callback that
        fetches the weather data, and another callback that outputs the temperature based on the downloaded data. This way, when only the unit is changed,
        the data does not have to be downloaded again. This is an example of sharing a variable, or state, between callbacks.

    DASH IS STATELESS
    Dash was designed to be a stateless framework.

    Stateless frameworks are more scalable and robust than stateful ones. Most websites that you visit are running on stateless servers.

    They are more scalable because it's trivial to add more compute power to the application. In order to scale the application to serve more users
        or run more computations, run more "copies" of the app in separate processes.

    In production, this can be done either with gunicorn's worker command:
        gunicorn app:server --workers 8
        or by running the app in multiple Docker containers or servers and load balancing between them.

    Stateless frameworks are more robust because even if one process fails, other processes can continue serving requests. In Dash Enterprise Kubernetes,
        these containers can run on separate servers or even separate regions, providing resiliency against server failure.

    With a stateless framework, user sessions are not mapped 1-1 with server processes. Each callback request can be executed on any of the available processes. 
        gunicorn will check which process isn't busy running a callback and send the new callback request to that process. This means that a few processes can
        balance the requests of 10s or 100s of concurrent users so long as those requests aren't happening at the exact same time (they usually don't!).

    WHY GLOBAL VARIABLES WILL BREAK YOUR APP
    Dash is designed to work in multi-user environments where multiple people view the application at the same time and have independent sessions.

    If your app uses and modifies a global variable, then one user's session could set the variable to some value which would affect the next user's session.

    Dash is also designed to be able to run with multiple workers so that callbacks can be executed in parallel.

    This is commonly done with gunicorn using syntax like
        $ gunicorn --workers 4 app:server
        (app refers to a file named app.py and server refers to a variable in that file named server: server = app.server).

    When Dash apps run across multiple workers, their memory is not shared. This means that if you modify a global variable in one callback, 
        that modification will not be applied to the other workers / processes.
'''