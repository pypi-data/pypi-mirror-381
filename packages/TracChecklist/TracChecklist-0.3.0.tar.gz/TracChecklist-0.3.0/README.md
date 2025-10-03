# TracChecklist

This plugin allows you to define checklists as a wiki page, and then embed
them in tickets as templates for recurring tasks. For example, if your workflow
for a bug ticket includes steps for fix/test/release, each of these can be defined
as a step and checked off as the assignee works on the ticket.

This prevents people from forgetting something (e.g. tag a new version), and
allows for ongoing process improvements by updating the checklist whenever gaps
in the existing process are discovered.

This plugin was developed and is maintained by [Outlyer](https://outlyer.space)


## Install

 A plugin can either be deployed globally, or only for a specific environment.
 Global deployment is done by installing the plugin:

    cd /path/to/plugin_source
    python setup.py install

The plugin is also available on PyPI and can be installed globally using pip:

    pip install TracChecklist

To deploy a plugin only to a specific Trac environment, copy the egg file into
the plugins directory of that environment:

    cd /path/to/plugin_source
    python setup.py bdist_egg
    cp dist/*.egg /path/to/project_environment/plugins


## Setup

Enable the plugin in your trac.ini file:

    [components]
    checklist.* = enabled

The plugin requires a new database table; update the environment to create it:

    $ trac-admin /path/to/env upgrade

The plugin uses static resources (CSS, JS).  If you mapped static resources so
they are served by the web server, the resources need to be deployed to the
location on the filesystem that is served by the web server. Execute the deploy
command, as is done during install and upgrade:

	$ trac-admin /path/to/env deploy /deploy/path

The plugin creates a "wiki:ChecklistTemplates" page as the root below which all
checklist definitions are located. If you move the page, update the entry in your
trac.ini file:

    [checklist]
    template_root = /path/to/ChecklistTemplates

 Restart the server once fully configured.


 ## Use

Create at least one checklist as a sub-page below the "Ticket Template" page
using the template provided in the "ChecklistTemplates" root page. You can also
create pages below non-existing parents, which will then be treated as category
headers. For example:

    wiki:ChecklistTemplates
    |- CatOne (not a page)
	   |- wiki:ChecklistTemplates/CatOne/Checklist One
	   |- wiki:ChecklistTemplates/CatOne/Checklist Two
    |- CatTwo (not a page)
	   |- wiki:ChecklistTemplates/CatTwo/Checklist Three
	   |- wiki:ChecklistTemplates/CatTwo/Checklist Four

Then use the dropdown menu at the top-right of any ticket description entry
box when in edit mode to select & insert a template. The preview will show the
checklist in your ticket.


## Revision Log

* 0.1 - Initial release to PyPI (build) & TracHacks (source)
