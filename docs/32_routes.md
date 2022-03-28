# Routes

This project template allows for dynamic configuring of routes and pages in your app. The code that makes this possible
is located in the `routes.py` file in the root of this repository. In that file, there is a
method `setup_routing(app: dash.Dash) -> List[PathUtil]` which has to be called on app startup. The method is
responsible for setting up routes, and importing the correct files within the pages directory.

## Creating pages

### Top level pages

Top level pages are pages which show up on the main navigation bar at the top of the screen. All you have to do to add
these, is create a folder within the pages directory. If you add in a `layout.py` file in this directory, the folder
will be considered a page. If you want subpages, you can't create this file.

`layout.py` should have a variable `layout` of the type `dash.html.Component`. e.g. `dash.html.P` for a `<p></p>`-tag

### Sub level pages

Let's say you want a collection of multiple pages in a single top level page. To realise this you can create the top level page like above, but don't create the `layout.py` file. Instead you create multiple subfolders, in which you WILL create the `layout.py` files.
When doing this, a sidebar will appear when clicking the top level folder name on the navigation bar.

## callbacks

In the folders you just created, you can also add a `callbacks.py` file. If this file is present, it will automatically be
loaded and the function `callbacks(app: dash.Dash)` will be called. This enables you to define your dash callbacks. If you want to work with stores, this is also the place to register them.
